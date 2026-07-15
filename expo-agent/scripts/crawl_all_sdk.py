import os
import sys
import re
import urllib.request
import time

# Import fungsi dari crawl_to_markdown
from crawl_to_markdown import crawl_page, save_markdown_file

def get_sdk_links():
    url = "https://docs.expo.dev/sitemap.xml"
    req = urllib.request.Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) WebCrawler/1.0'}
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            data = response.read().decode('utf-8')
            
        # Cari semua link yang menuju ke latest/sdk
        links = re.findall(r'<loc>(https://docs\.expo\.dev/versions/latest/sdk/[^<]*)</loc>', data)
        # Hapus duplikat
        return list(set(links))
    except Exception as e:
        print(f"Gagal mengambil sitemap: {e}")
        return []

categories = {
    'media': ['audio', 'camera', 'imagepicker', 'imagemanipulator', 'media-library-legacy', 'video', 'video-thumbnails', 'live-photo', 'captureRef'],
    'sensors': ['accelerometer', 'barometer', 'gyroscope', 'magnetometer', 'pedometer', 'sensors', 'devicemotion', 'location'],
    'hardware': ['battery', 'brightness', 'cellular', 'device', 'haptics', 'network', 'netinfo', 'fingerprint'],
    'ui': ['blur-view', 'gl-view', 'map-view', 'webview', 'safe-area-context', 'flash-list', 'font', 'glass-effect', 'screens', 'slider', 'splash-screen', 'svg', 'lottie', 'masked-view', 'pager-view', 'segmented-control', 'colorpicker', 'datetimepicker', 'date-time-picker', 'checkbox', 'dropdownmenu', 'loadingindicator', 'progress', 'radiobutton', 'searchbar', 'snackbar', 'switch', 'textinput', 'tooltip', 'skia', 'reanimated'],
    'system': ['application', 'background-fetch', 'background-task', 'clipboard', 'constants', 'crypto', 'filesystem', 'filesystem-legacy', 'intent-launcher', 'keep-awake', 'localization', 'task-manager', 'updates', 'app-integrity', 'build-properties', 'dev-client', 'dev-menu', 'manifests', 'expo', 'brownfield', 'server', 'symbols', 'widgets'],
    'services': ['apple-authentication', 'auth-session', 'contacts', 'contacts-legacy', 'mail-composer', 'print', 'sharing', 'sms', 'speech', 'notifications', 'local-authentication', 'calendar', 'calendar-legacy', 'document-picker', 'storereview', 'tracking-transparency', 'age-range'],
    'data-storage': ['async-storage', 'blob', 'sqlite', 'securestore', 'asset'],
    'router': ['router', 'link', 'stack', 'native-tabs', 'split-view', 'ui', 'color', 'experimental-stack']
}

def get_category(filename, url):
    name = filename.replace('.md', '').lower()
    
    # Deteksi URL khusus UI yang bersarang
    if 'ui/jetpack-compose' in url:
        return 'ui/jetpack-compose'
    if 'ui/swift-ui' in url:
        return 'ui/swift-ui'
    if 'ui/universal' in url:
        return 'ui/universal'
    if 'ui/drop-in-replacements' in url:
        return 'ui/drop-in-replacements'
        
    for cat, keywords in categories.items():
        if name in keywords:
            return cat
            
    if 'ui/' in url or 'swift-ui' in url or 'jetpack-compose' in url or 'universal' in url or 'drop-in-replacements' in url:
        return 'ui'
    elif 'router' in url:
        return 'router'
    return 'others'

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "../reference/docs")
    os.makedirs(output_dir, exist_ok=True)
    
    print("[*] Mengambil daftar URL dari sitemap Expo...")
    links = get_sdk_links()
    
    # Filter hanya yang benar-benar child dari sdk/ atau sdk sendiri
    sdk_links = [link for link in links if "/versions/latest/sdk/" in link]
    print(f"[*] Ditemukan {len(sdk_links)} halaman SDK Expo.")
    
    for url in sdk_links:
        clean_url = url.rstrip('/')
        page_name = clean_url.split('/')[-1]
        if page_name == "sdk":
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
