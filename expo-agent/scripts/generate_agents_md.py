import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
docs_dir = os.path.join(script_dir, "../reference/docs")

def extract_meta(file_path):
    title, desc = os.path.basename(file_path), ""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read(2048)
        title_match = re.search(r'^title:\s*"?([^"\r\n]+)"?', content, re.MULTILINE)
        if title_match:
            title = title_match.group(1)
        desc_match = re.search(r'^description:\s*"?([^"\r\n]+)"?', content, re.MULTILINE)
        if desc_match:
            desc = desc_match.group(1)
    except:
        pass
    return title, desc

def get_folder_description(folder_name):
    descriptions = {
        'data-storage': 'Modules for local data storage (AsyncStorage, SQLite, SecureStore, etc).',
        'hardware': 'Device hardware capabilities (Battery, Haptics, Network, Cellular, etc).',
        'media': 'Media handling (Audio, Video, Camera, ImagePicker, etc).',
        'others': 'Miscellaneous uncategorized modules.',
        'router': 'Expo Router components and navigation.',
        'sensors': 'Device sensors (Accelerometer, Gyroscope, Location, etc).',
        'services': 'System services and integrations (Auth, Contacts, Calendar, Speech, etc).',
        'system': 'Core system behaviors (Filesystem, Updates, TaskManager, AppState, etc).',
        'ui': 'UI components and visual capabilities.',
        'jetpack-compose': 'Expo UI components using Android Jetpack Compose.',
        'swift-ui': 'Expo UI components using iOS SwiftUI.',
        'universal': 'Universal UI components for all platforms.',
        'drop-in-replacements': 'UI components designed as drop-in replacements for core elements.'
    }
    return descriptions.get(folder_name, 'Expo SDK modules.')

def generate_tree(startpath):
    tree_str = []
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        folder = os.path.basename(root)
        if level == 0:
            tree_str.append(f"📦 docs/")
        else:
            tree_str.append(f"{indent}📂 {folder}/")
            
        subindent = ' ' * 4 * (level + 1)
        md_count = sum(1 for f in files if f.endswith('.md') and f != 'AGENTS.md')
        if md_count > 0:
            tree_str.append(f"{subindent}📄 {md_count} markdown files (see AGENTS.md)")
            
    return "\n".join(tree_str)

def main():
    for root, dirs, files in os.walk(docs_dir):
        md_files = sorted([f for f in files if f.endswith('.md') and f != 'AGENTS.md'])
        subdirs = sorted(dirs)
        
        folder_name = os.path.basename(root)
        lines = []
        
        if root == docs_dir:
            lines.append("# Expo Docs - Navigation Guide")
            lines.append("\nThis directory contains the complete offline Expo SDK documentation.")
            lines.append("Use this guide to locate modules. Each sub-folder has its own `AGENTS.md` detailing its exact contents.\n")
            lines.append("## Directory Tree\n")
            lines.append("```text")
            lines.append(generate_tree(docs_dir))
            lines.append("```\n")
            lines.append("## Categories\n")
            for d in subdirs:
                lines.append(f"- **`{d}/`**: {get_folder_description(d)}")
        else:
            lines.append(f"# 📂 {folder_name}/")
            lines.append(f"\n{get_folder_description(folder_name)}\n")
            
            if subdirs:
                lines.append("## Sub-directories\n")
                for d in subdirs:
                    lines.append(f"- **`{d}/`**: {get_folder_description(d)}")
                lines.append("\n")
                
            if md_files:
                lines.append("## Available Modules\n")
                for f in md_files:
                    title, desc = extract_meta(os.path.join(root, f))
                    desc_text = f" - {desc}" if desc else ""
                    lines.append(f"- **`{f}`** ({title}){desc_text}")
                    
        # Tulis AGENTS.md
        with open(os.path.join(root, 'AGENTS.md'), 'w', encoding='utf-8') as f_out:
            f_out.write("\n".join(lines) + "\n")
            
    print("[+] Berhasil membuat AGENTS.md di root docs dan semua sub-foldernya!")

if __name__ == "__main__":
    main()
