#!/usr/bin/env python3
"""
Web to Markdown Crawler for AI Input
-------------------------------------
Script untuk mengunduh halaman web dan mengubahnya menjadi file Markdown bersih
yang siap digunakan sebagai input untuk AI / LLMs (seperti Gemini, Claude, ChatGPT).

Fitur:
1. Deteksi otomatis Expo Docs: langsung mengunduh versi .md asli (tanpa HTML boilerplate).
2. Pembersihan HTML cerdas: menghapus iklan, sidebar, header, footer, navigasi.
3. Resolusi Link: mengubah link relatif menjadi link absolut.
4. Metadata/Frontmatter: menambahkan detail judul, sumber, deskripsi, dan tanggal crawl.
5. Fallback Tanpa Dependency: Menggunakan pustaka standar Python jika BeautifulSoup4 / html2text belum terinstall.
"""

import os
import sys
import re
import urllib.request
import urllib.parse
from datetime import datetime
from html.parser import HTMLParser
from typing import Any, Dict, List, Optional, Tuple

# Inisialisasi variabel modul bertipe data dinamis
has_requests: bool = False
has_bs4: bool = False
has_html2text: bool = False

requests: Optional[Any] = None
BeautifulSoup: Optional[Any] = None
html2text: Optional[Any] = None

# Mengimpor pustaka opsional jika terpasang
try:
    import requests as req
    requests = req
    has_requests = True
except ImportError:
    pass

try:
    from bs4 import BeautifulSoup as bs
    BeautifulSoup = bs
    has_bs4 = True
except ImportError:
    pass

try:
    import html2text as h2t
    html2text = h2t
    has_html2text = True
except ImportError:
    pass


class FallbackHTMLParser(HTMLParser):
    """
    Parser HTML sederhana menggunakan library standar Python (html.parser)
    sebagai cadangan jika BeautifulSoup dan html2text tidak terinstall.
    """
    def __init__(self, base_url: str) -> None:
        super().__init__()
        self.base_url: str = base_url
        self.markdown: List[str] = []
        self.tag_stack: List[str] = []
        
        # Tag yang isinya diabaikan karena merupakan bagian dari navigasi, iklan, dll.
        self.ignored_tags = {
            'script', 'style', 'nav', 'header', 'footer', 'aside', 
            'form', 'svg', 'noscript', 'iframe', 'button', 'select'
        }
        self.in_ignored_tag: bool = False
        
        self.in_pre: bool = False
        self.in_code: bool = False
        self.list_stack: List[List[Any]] = []  # Menyimpan jenis list ('ul' atau 'ol') dan nomor urut untuk 'ol'
        
        self.in_link: bool = False
        self.link_href: Optional[str] = None
        self.link_text: str = ""
        
        self.in_title: bool = False
        self.title_text: str = ""

        # Mapping parser handlers untuk mereduksi cognitive complexity
        self.tag_handlers_start = {
            'title': self._start_title,
            'pre': self._start_pre,
            'code': self._start_code,
            'ul': self._start_list,
            'ol': self._start_list,
            'li': self._start_li,
            'p': self._start_p,
            'a': self._start_a,
            'strong': self._start_strong,
            'b': self._start_strong,
            'em': self._start_em,
            'i': self._start_em,
            'img': self._start_img,
            'br': self._start_br,
        }

        self.tag_handlers_end = {
            'title': self._end_title,
            'pre': self._end_pre,
            'code': self._end_code,
            'ul': self._end_list,
            'ol': self._end_list,
            'a': self._end_a,
            'strong': self._end_strong,
            'b': self._end_strong,
            'em': self._end_em,
            'i': self._end_em,
            'h1': self._end_h,
            'h2': self._end_h,
            'h3': self._end_h,
            'h4': self._end_h,
            'h5': self._end_h,
            'h6': self._end_h,
            'p': self._end_p,
        }

    # Start Tag Helper Handlers
    def _start_title(self, tag: str, attrs: Dict[str, Optional[str]]) -> None:
        self.in_title = True
        
    def _start_pre(self, tag: str, attrs: Dict[str, Optional[str]]) -> None:
        self.in_pre = True
        self.markdown.append("\n\n```\n")
        
    def _start_code(self, tag: str, attrs: Dict[str, Optional[str]]) -> None:
        self.in_code = True
        if not self.in_pre:
            self.markdown.append("`")
            
    def _start_list(self, tag: str, attrs: Dict[str, Optional[str]]) -> None:
        self.list_stack.append([tag, 1])
        self.markdown.append("\n")
        
    def _start_li(self, tag: str, attrs: Dict[str, Optional[str]]) -> None:
        indent = "  " * (len(self.list_stack) - 1)
        if self.list_stack:
            list_type, count = self.list_stack[-1]
            if list_type == 'ol':
                self.markdown.append(f"{indent}{count}. ")
                self.list_stack[-1][1] = count + 1
            else:
                self.markdown.append(f"{indent}- ")
        else:
            self.markdown.append("- ")
            
    def _start_header(self, tag: str, attrs: Dict[str, Optional[str]]) -> None:
        level = int(tag[1])
        self.markdown.append(f"\n\n{'#' * level} ")
        
    def _start_p(self, tag: str, attrs: Dict[str, Optional[str]]) -> None:
        self.markdown.append("\n\n")
        
    def _start_a(self, tag: str, attrs: Dict[str, Optional[str]]) -> None:
        self.in_link = True
        href = attrs.get('href', '')
        if href:
            self.link_href = urllib.parse.urljoin(self.base_url, href)
        else:
            self.link_href = ""
        self.link_text = ""
        
    def _start_strong(self, tag: str, attrs: Dict[str, Optional[str]]) -> None:
        self.markdown.append("**")
        
    def _start_em(self, tag: str, attrs: Dict[str, Optional[str]]) -> None:
        self.markdown.append("*")
        
    def _start_img(self, tag: str, attrs: Dict[str, Optional[str]]) -> None:
        alt = attrs.get('alt', 'Gambar')
        src = attrs.get('src', '')
        if src:
            abs_src = urllib.parse.urljoin(self.base_url, src)
            self.markdown.append(f"\n![{alt}]({abs_src})\n")
            
    def _start_br(self, tag: str, attrs: Dict[str, Optional[str]]) -> None:
        self.markdown.append("\n")

    # End Tag Helper Handlers
    def _end_title(self, tag: str) -> None:
        self.in_title = False
        
    def _end_pre(self, tag: str) -> None:
        self.in_pre = False
        self.markdown.append("\n```\n")
        
    def _end_code(self, tag: str) -> None:
        self.in_code = False
        if not self.in_pre:
            self.markdown.append("`")
            
    def _end_list(self, tag: str) -> None:
        if self.list_stack:
            self.list_stack.pop()
        self.markdown.append("\n")
        
    def _end_a(self, tag: str) -> None:
        self.in_link = False
        if self.link_href:
            self.markdown.append(f"[{self.link_text.strip()}]({self.link_href})")
        else:
            self.markdown.append(self.link_text)
        self.link_href = None
        
    def _end_strong(self, tag: str) -> None:
        self.markdown.append("**")
        
    def _end_em(self, tag: str) -> None:
        self.markdown.append("*")
        
    def _end_h(self, tag: str) -> None:
        self.markdown.append("\n\n")
        
    def _end_p(self, tag: str) -> None:
        self.markdown.append("\n\n")

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        self.tag_stack.append(tag)
        
        # Cek jika tag termasuk yang diabaikan
        if tag in self.ignored_tags:
            self.in_ignored_tag = True
            return
            
        if self.in_ignored_tag:
            return
            
        attr_dict = dict(attrs)
        
        # Dispatch ke handler spesifik
        handler = self.tag_handlers_start.get(tag)
        if handler:
            handler(tag, attr_dict)
        elif tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self._start_header(tag, attr_dict)

    def handle_endtag(self, tag: str) -> None:
        if self.tag_stack:
            self.tag_stack.pop()
            
        if tag in self.ignored_tags:
            # Periksa apakah kita masih berada di dalam tag terabaikan lainnya
            self.in_ignored_tag = any(t in self.ignored_tags for t in self.tag_stack)
            return
            
        if self.in_ignored_tag:
            return
            
        handler = self.tag_handlers_end.get(tag)
        if handler:
            handler(tag)

    def handle_data(self, data: str) -> None:
        if self.in_ignored_tag:
            return
            
        if self.in_title:
            self.title_text += data
        elif self.in_link:
            self.link_text += data
        elif self.in_pre:
            self.markdown.append(data)
        else:
            # Bersihkan whitespace berlebih
            clean_data = re.sub(r'\s+', ' ', data)
            if clean_data and clean_data != ' ':
                self.markdown.append(clean_data)

    def get_markdown(self) -> str:
        text = "".join(self.markdown)
        # Menghapus duplikasi baris kosong berlebih
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()


def install_dependencies() -> None:
    """Menginstal dependency menggunakan pip."""
    import subprocess
    print("[*] Menginstal library pendukung (requests, beautifulsoup4, html2text)...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "beautifulsoup4", "html2text"])
        print("[+] Instalasi berhasil! Silakan jalankan kembali script ini.")
        # Reload modules
        global has_requests, has_bs4, has_html2text, requests, BeautifulSoup, html2text
        import requests as req
        from bs4 import BeautifulSoup as bs
        import html2text as h2t
        requests = req
        BeautifulSoup = bs
        html2text = h2t
        has_requests = True
        has_bs4 = True
        has_html2text = True
    except Exception as e:
        print(f"[-] Gagal menginstal dependency secara otomatis: {e}")
        print("Silakan install secara manual dengan: pip install requests beautifulsoup4 html2text")
        sys.exit(1)


def clean_html_with_bs4(html_content: str, base_url: str) -> Tuple[Any, str, str]:
    """
    Membersihkan HTML menggunakan BeautifulSoup.
    Membuang elemen yang tidak penting dan memformat link relatif menjadi absolut.
    """
    if BeautifulSoup is None:
        return html_content, "Untitled Page", "BeautifulSoup is not available"

    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 1. Hapus elemen navigasi, iklan, script, styling, dll.
    selector_to_remove = [
        'script', 'style', 'nav', 'header', 'footer', 'aside', 
        'form', 'noscript', 'iframe', '.sidebar', '.menu', '.navigation', 
        '.ads', '.footer', '.header', 'button', 'select', 'svg'
    ]
    for selector in selector_to_remove:
        for element in soup.select(selector):
            element.decompose()
            
    # 2. Cari kontainer artikel utama jika ada (memperkecil cakupan boilerplate)
    main_content = None
    main_selectors = [
        'article', 'main', '[role="main"]', '#content', '#main', '.content', 
        '.main-content', '.prose', '.markdown-body', '#main-content'
    ]
    for selector in main_selectors:
        found = soup.select_one(selector)
        if found:
            main_content = found
            break
            
    if not main_content:
        main_content = soup.body if soup.body else soup

    # 3. Ubah semua URL relatif menjadi absolut
    for tag in main_content.find_all('a', href=True):
        href_val = tag.get('href')
        if href_val and isinstance(href_val, str):
            tag['href'] = urllib.parse.urljoin(base_url, href_val)
        
    for tag in main_content.find_all('img', src=True):
        src_val = tag.get('src')
        if src_val and isinstance(src_val, str):
            tag['src'] = urllib.parse.urljoin(base_url, src_val)
        
    # Ambil judul halaman
    title = soup.title.string.strip() if soup.title and soup.title.string else "Untitled Page"
    
    # Ambil deskripsi meta jika ada
    description = ""
    meta_desc = soup.find('meta', attrs={'name': 'description'}) or soup.find('meta', attrs={'property': 'og:description'})
    if meta_desc:
        desc_val = meta_desc.get('content')
        if desc_val and isinstance(desc_val, str):
            description = desc_val.strip()

    return main_content, title, description


def fetch_raw_expo_markdown(url: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Fungsi khusus untuk mendeteksi halaman dokumentasi Expo.
    Expo menyediakan file .md mentah secara resmi untuk konsumsi AI/LLM.
    Contoh: https://docs.expo.dev/versions/latest/sdk/ui/universal/ -> https://docs.expo.dev/versions/latest/sdk/ui/universal.md
    """
    parsed = urllib.parse.urlparse(url)
    if 'docs.expo.dev' not in parsed.netloc:
        return None, None
        
    # Buat url .md
    path = parsed.path
    if not path.endswith('.md'):
        # Buat path berakhir dengan .md
        if path.endswith('/'):
            path = path[:-1]
        path = path + ".md"
        
    md_url = urllib.parse.urlunparse((
        parsed.scheme,
        parsed.netloc,
        path,
        parsed.params,
        parsed.query,
        parsed.fragment
    ))
    
    print(f"[*] Mendeteksi Expo Docs. Mencoba mengunduh file Markdown resmi dari: {md_url}")
    try:
        req = urllib.request.Request(
            md_url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) WebToMarkdownCrawler/1.0'}
        )
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                raw_content = response.read().decode('utf-8')
                print("[+] Berhasil mengunduh Markdown resmi Expo!")
                return raw_content, md_url
    except Exception as e:
        print(f"[!] Gagal mengunduh Markdown resmi ({e}). Fallback ke HTML parsing.")
        
    return None, None


def convert_html_to_markdown_html2text(soup_element: Any) -> str:
    """Mengubah elemen BeautifulSoup menjadi Markdown menggunakan html2text."""
    if html2text is None:
        return str(soup_element)

    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.ignore_images = False
    converter.body_width = 0  # Jangan membungkus baris agar rapi sebagai input AI
    converter.mark_code = True
    converter.native_table_conversion = True
    
    # Hapus markup html2text yang kurang bersih
    markdown = converter.handle(str(soup_element))
    return markdown


def crawl_page(url: str) -> Tuple[str, str, str, str]:
    """Mengambil halaman web dan mengembalikan Markdown bersih serta metadatanya."""
    # 1. Cek jika Expo Docs
    expo_md, md_url = fetch_raw_expo_markdown(url)
    if expo_md and md_url:
        # Jika berhasil mengunduh Markdown resmi Expo,
        # kita tinggal membersihkan AgentInstructions jika ada, karena AI tidak butuh instruksi navigasi lokal tersebut
        cleaned_md = expo_md
        
        # Bersihkan tag <AgentInstructions> menggunakan pencarian string index agar terhindar dari regex backtracking
        start_tag = "<AgentInstructions>"
        end_tag = "</AgentInstructions>"
        while start_tag in cleaned_md and end_tag in cleaned_md:
            start_idx = cleaned_md.find(start_tag)
            end_idx = cleaned_md.find(end_tag) + len(end_tag)
            if start_idx < end_idx:
                cleaned_md = cleaned_md[:start_idx] + cleaned_md[end_idx:]
            else:
                break
        
        # Ekstrak judul dan deskripsi dari frontmatter jika ada (menggunakan range pembatas non-newline untuk menghindari backtracking)
        title = "Expo Docs Page"
        description = "Expo official documentation"
        title_match = re.search(r'^title:\s*([^\r\n]*)$', cleaned_md, re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip()
        desc_match = re.search(r'^description:\s*([^\r\n]*)$', cleaned_md, re.MULTILINE)
        if desc_match:
            description = desc_match.group(1).strip()
            
        return cleaned_md, title, description, md_url

    # 2. Fetch HTML Konten
    print(f"[*] Mengunduh halaman HTML dari: {url}")
    html_content = ""
    
    try:
        if has_requests and requests is not None:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            r = requests.get(url, headers=headers, timeout=15)
            r.raise_for_status()
            html_content = r.text
        else:
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            )
            with urllib.request.urlopen(req, timeout=15) as response:
                html_content = response.read().decode('utf-8')
    except Exception as e:
        print(f"[-] Gagal mengunduh halaman: {e}")
        sys.exit(1)

    # 3. Parsing & Konversi ke Markdown
    if has_bs4 and has_html2text:
        print("[*] Menggunakan BeautifulSoup4 dan html2text untuk konversi...")
        clean_element, title, description = clean_html_with_bs4(html_content, url)
        markdown_body = convert_html_to_markdown_html2text(clean_element)
    else:
        print("[!] BeautifulSoup4 / html2text tidak ditemukan.")
        print("[*] Menggunakan HTML Parser standar (Fallback)...")
        parser = FallbackHTMLParser(url)
        parser.feed(html_content)
        markdown_body = parser.get_markdown()
        title = parser.title_text.strip() or "Web Page"
        description = "Parsed using standard Python library"

    return markdown_body, title, description, url


def save_markdown_file(markdown_body: str, title: str, description: str, source_url: str, output_path: Optional[str] = None) -> str:
    """Menyimpan konten markdown ke file dengan frontmatter metadata lengkap."""
    # Bersihkan nama file dari karakter ilegal jika output_path tidak ditentukan
    if not output_path:
        clean_title = re.sub(r'[^\w\s-]', '', title).strip().lower()
        clean_title = re.sub(r'[-\s]+', '_', clean_title)
        output_path = f"{clean_title or 'output'}.md"

    # Menyusun Frontmatter agar siap digunakan AI
    frontmatter = f"""---
title: "{title}"
description: "{description}"
source_url: "{source_url}"
scraped_at: "{datetime.now().isoformat()}"
---

"""
    # Gabungkan frontmatter dan body
    final_content = frontmatter + markdown_body
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"[+] Berhasil disimpan ke: {os.path.abspath(output_path)}")
        return output_path
    except Exception as e:
        print(f"[-] Gagal menulis ke file: {e}")
        sys.exit(1)


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(
        description="Web to Markdown Crawler untuk AI Input",
        usage="%(prog)s [--url URL] | [URL] [--output FILE] | [--install]"
    )
    
    # Positional arguments untuk backward compatibility
    parser.add_argument("pos_url", nargs="?", help=argparse.SUPPRESS)
    parser.add_argument("pos_output", nargs="?", help=argparse.SUPPRESS)
    
    # Optional arguments
    parser.add_argument("--url", dest="url", help="URL halaman web yang akan di-crawl")
    parser.add_argument("--output", "-o", dest="output", help="File output (opsional)")
    parser.add_argument("--install", action="store_true", help="Menginstal library pendukung")
    
    args, unknown = parser.parse_known_args()
    
    if args.install:
        install_dependencies()
        sys.exit(0)
        
    final_url = args.url or args.pos_url
    
    # Cek literal --http:// atau --https:// (berjaga-jaga jika dipanggil seperti --https://...)
    if not final_url:
        for unk in unknown:
            if unk.startswith("--http"):
                final_url = unk[2:]
                break
                
    if not final_url:
        parser.print_help()
        print("\nContoh penggunaan:")
        print("  python3 crawl_to_markdown.py --url https://docs.expo.dev/versions/latest/sdk/ui/universal/")
        sys.exit(1)
        
    output_file = args.output or args.pos_output

    # Tampilkan status dependency
    print("--- Status Pustaka ---")
    print(f"requests: {'TERINSTALL' if has_requests else 'TIDAK TERINSTALL'}")
    print(f"beautifulsoup4: {'TERINSTALL' if has_bs4 else 'TIDAK TERINSTALL'}")
    print(f"html2text: {'TERINSTALL' if has_html2text else 'TIDAK TERINSTALL'}")
    if not (has_bs4 and has_html2text):
        print("Tip: Jalankan `python3 crawl_to_markdown.py --install` untuk kualitas konversi terbaik.")
    print("----------------------\n")

    markdown_body, title, description, crawled_url = crawl_page(final_url)
    save_markdown_file(markdown_body, title, description, crawled_url, output_file)


if __name__ == "__main__":
    main()
