import os
import glob
import shutil

categories = {
    'media': [
        'audio', 'camera', 'imagepicker', 'imagemanipulator', 
        'media-library-legacy', 'video', 'video-thumbnails', 'live-photo',
        'captureRef'
    ],
    'sensors': [
        'accelerometer', 'barometer', 'gyroscope', 'magnetometer', 
        'pedometer', 'sensors', 'devicemotion', 'location'
    ],
    'hardware': [
        'battery', 'brightness', 'cellular', 'device', 'haptics', 
        'network', 'netinfo', 'fingerprint'
    ],
    'ui': [
        'blur-view', 'gl-view', 'map-view', 'webview', 'safe-area-context',
        'flash-list', 'font', 'glass-effect', 'screens', 'slider',
        'splash-screen', 'svg', 'lottie', 'masked-view', 'pager-view',
        'segmented-control', 'colorpicker', 'datetimepicker', 'date-time-picker',
        'checkbox', 'dropdownmenu', 'loadingindicator', 'progress', 'radiobutton',
        'searchbar', 'snackbar', 'switch', 'textinput', 'tooltip', 'skia', 'reanimated'
    ],
    'system': [
        'application', 'background-fetch', 'background-task', 'clipboard',
        'constants', 'crypto', 'filesystem', 'filesystem-legacy', 'intent-launcher',
        'keep-awake', 'localization', 'task-manager', 'updates', 'app-integrity',
        'build-properties', 'dev-client', 'dev-menu', 'manifests', 'expo',
        'brownfield', 'server', 'symbols', 'widgets'
    ],
    'services': [
        'apple-authentication', 'auth-session', 'contacts', 'contacts-legacy',
        'mail-composer', 'print', 'sharing', 'sms', 'speech', 
        'notifications', 'local-authentication', 'calendar', 'calendar-legacy',
        'document-picker', 'storereview', 'tracking-transparency', 'age-range'
    ],
    'data-storage': [
        'async-storage', 'blob', 'sqlite', 'securestore', 'asset'
    ],
    'router': [
        'router', 'link', 'stack', 'native-tabs', 'split-view', 'ui', 'color', 'experimental-stack'
    ]
}

def get_category(filename):
    name = filename.replace('.md', '').lower()
    for cat, keywords in categories.items():
        if name in keywords:
            return cat
            
    # Default category for UI-related subfolders from jetpack-compose / swift-ui / universal
    return None

def main():
    docs_dir = "/home/broo/Documents/Porto/Curapic/docs"
    # Find all md files
    md_files = glob.glob(os.path.join(docs_dir, "**/*.md"), recursive=True)
    
    count = 0
    for file_path in md_files:
        filename = os.path.basename(file_path)
        
        # skip if already in root (we don't want to mess up something that is already processed?) 
        # actually let's just move everything to docs/category/filename
        
        # Check if the file is in ui/ swift-ui, jetpack-compose, drop-in-replacements, etc
        rel_dir = os.path.dirname(file_path).replace(docs_dir, '').strip('/')
        
        cat = get_category(filename)
        
        if not cat:
            if 'ui/' in file_path or 'swift-ui' in file_path or 'jetpack-compose' in file_path or 'universal' in file_path or 'drop-in-replacements' in file_path:
                cat = 'ui'
            elif 'router' in file_path:
                cat = 'router'
            else:
                cat = 'others'
                
        new_dir = os.path.join(docs_dir, cat)
        os.makedirs(new_dir, exist_ok=True)
        
        new_path = os.path.join(new_dir, filename)
        
        # Handle conflict by appending number
        if os.path.exists(new_path) and new_path != file_path:
            base = filename.replace('.md', '')
            idx = 1
            while os.path.exists(new_path) and new_path != file_path:
                new_path = os.path.join(new_dir, f"{base}_{idx}.md")
                idx += 1
                
        if file_path != new_path:
            shutil.move(file_path, new_path)
            count += 1
            
    print(f"Selesai! {count} file berhasil dikelompokkan ke dalam kategori masing-masing.")

    # Bersihkan folder-folder kosong
    print("Membersihkan folder lama yang kosong...")
    for root, dirs, files in os.walk(docs_dir, topdown=False):
        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                os.rmdir(dir_path)
            except OSError:
                pass # Folder tidak kosong

if __name__ == "__main__":
    main()
