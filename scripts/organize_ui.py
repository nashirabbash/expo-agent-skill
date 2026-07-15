import os
import glob
import re
import shutil

def main():
    docs_ui_dir = "/home/broo/Documents/Porto/Curapic/docs/ui"
    md_files = glob.glob(os.path.join(docs_ui_dir, "*.md"))
    
    count = 0
    for file_path in md_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read(1024)
            
        match = re.search(r'^source_url:\s*"([^"]+)"', content, re.MULTILINE)
        if not match:
            continue
            
        url = match.group(1)
        
        target_subfolder = None
        if 'ui/jetpack-compose' in url:
            target_subfolder = 'jetpack-compose'
        elif 'ui/swift-ui' in url:
            target_subfolder = 'swift-ui'
        elif 'ui/universal' in url:
            target_subfolder = 'universal'
        elif 'ui/drop-in-replacements' in url:
            target_subfolder = 'drop-in-replacements'
            
        if target_subfolder:
            new_dir = os.path.join(docs_ui_dir, target_subfolder)
            os.makedirs(new_dir, exist_ok=True)
            
            filename = os.path.basename(file_path)
            new_path = os.path.join(new_dir, filename)
            
            shutil.move(file_path, new_path)
            count += 1
            print(f"Memindahkan: {filename} -> {target_subfolder}/")
            
    print(f"\nSelesai! {count} file berhasil dipindahkan ke sub-folder UI.")

if __name__ == "__main__":
    main()
