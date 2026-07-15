import os
import glob
import re
import shutil
import urllib.parse

def main():
    docs_dir = "/home/broo/Documents/Porto/Curapic/docs"
    # Cari semua file md, termasuk di dalam subfolder (jika ada)
    md_files = glob.glob(os.path.join(docs_dir, "**/*.md"), recursive=True)
    
    count = 0
    for file_path in md_files:
        # Jangan proses jika nama foldernya sudah ada "versions/latest"
        if "versions/latest" in file_path:
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read(1024)
            
        match = re.search(r'^source_url:\s*"([^"]+)"', content, re.MULTILINE)
        if not match:
            continue
            
        url = match.group(1)
        
        parsed = urllib.parse.urlparse(url)
        path = parsed.path
        
        # Hilangkan akhiran .md dari path (karena kita akan menambahkannya lagi nanti)
        if path.endswith('.md'):
            path = path[:-3]
            
        rel_path = path.strip('/')
        
        if not rel_path:
            continue
            
        new_path = os.path.join(docs_dir, f"{rel_path}.md")
        
        if file_path != new_path:
            os.makedirs(os.path.dirname(new_path), exist_ok=True)
            shutil.move(file_path, new_path)
            count += 1
            print(f"Memindahkan: {os.path.basename(file_path)} -> {rel_path}.md")
            
    print(f"\nSelesai! {count} file berhasil dipindahkan ke struktur endpoint.")

if __name__ == "__main__":
    main()
