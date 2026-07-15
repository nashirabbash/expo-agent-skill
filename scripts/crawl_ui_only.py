import os
import sys
import time
from crawl_all_sdk import get_sdk_links, get_category
from crawl_to_markdown import crawl_page, save_markdown_file

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "../reference/docs")
    
    print("[*] Mengambil daftar URL dari sitemap Expo...")
    links = get_sdk_links()
    
    # Filter HANYA yang ada di ui/universal/
    sdk_links = [link for link in links if "/versions/latest/sdk/ui/universal/" in link]
    print(f"[*] Ditemukan {len(sdk_links)} halaman UI Universal Expo.")
    
    for url in sdk_links:
        clean_url = url.rstrip('/')
        page_name = clean_url.split('/')[-1]
        if page_name == "universal":
            page_name = "index"
            
        cat = get_category(page_name, url)
        
        cat_dir = os.path.join(output_dir, cat)
        os.makedirs(cat_dir, exist_ok=True)
        
        output_file = os.path.join(cat_dir, f"{page_name}.md")
        
        print(f"\n[>] Memproses: {url}")
        try:
            markdown_body, title, description, crawled_url = crawl_page(url)
            save_markdown_file(markdown_body, title, description, crawled_url, output_file)
            time.sleep(0.5)
        except Exception as e:
            print(f"[-] Gagal memproses {url}: {e}")

if __name__ == "__main__":
    main()
