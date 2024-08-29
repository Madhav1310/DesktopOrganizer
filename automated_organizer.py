import os
import shutil

# Global Constants
DESKTOP_FOLDER = '/Users/madhavmittal/Desktop'

FULL_PATH_TO_DOCUMENTS_FOLDER = '/Users/madhavmittal/Desktop/documents'
FULL_PATH_TO_IMAGES_FOLDER = '/Users/madhavmittal/Desktop/images'
FULL_PATH_TO_VIDEOS_FOLDER = '/Users/madhavmittal/Desktop/videos'
FULL_PATH_TO_AUDIO_FOLDER = '/Users/madhavmittal/Desktop/audio'
FULL_PATH_TO_ARCHIVES_FOLDER = '/Users/madhavmittal/Desktop/archives'
FULL_PATH_TO_SCRIPTS_FOLDER = '/Users/madhavmittal/Desktop/scripts'
FULL_PATH_TO_APPS_FOLDER = '/Users/madhavmittal/Desktop/apps'

# File extensions grouped by type
FILE_EXTENSIONS = {
    'documents': ['.txt', '.doc', '.docx', '.pdf', '.xls', '.xlsx', '.ppt', '.pptx'],
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
    'audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma'],
    'archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'scripts': ['.py', '.js', '.html', '.css', '.java', '.cpp'],
    'apps': ['.app', '.dmg']
}

# Destination folders for each category
DESTINATION_FOLDERS = {
    'documents': FULL_PATH_TO_DOCUMENTS_FOLDER,
    'images': FULL_PATH_TO_IMAGES_FOLDER,
    'videos': FULL_PATH_TO_VIDEOS_FOLDER,
    'audio': FULL_PATH_TO_AUDIO_FOLDER,
    'archives': FULL_PATH_TO_ARCHIVES_FOLDER,
    'scripts': FULL_PATH_TO_SCRIPTS_FOLDER,
    'apps': FULL_PATH_TO_APPS_FOLDER
}

def scan_files(directory):
    """
    Scan the directory for files and extract their extensions.
    """
    files = os.listdir(directory)
    
    # Filter out unwanted system files 
    files = [file for file in files if file not in ['desktop.ini', 'downloads.ini']]
    files = [file for file in files if file.split('.')[-1] not in ['DS_Store', 'localized'] and '.' in file]
    
    # List full file names and their extensions
    full_file_names = [os.path.join(directory, file) for file in files]
    extensions = [os.path.splitext(file)[1] for file in files]
    
    return full_file_names, extensions

def get_destination_folder(extension):
    """
    Determine the destination folder based on the file extension.
    """
    for category, ext_list in FILE_EXTENSIONS.items():
        if extension in ext_list:
            return DESTINATION_FOLDERS.get(category)
    return None

def organize_files(full_file_names, extensions):
    """
    Organize files by moving them to designated folders based on their extensions.
    """
    for file_name, ext in zip(full_file_names, extensions):
        destination_folder = get_destination_folder(ext)

        if destination_folder:
            try:
                # Ensure destination folder exists
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                
                shutil.move(file_name, destination_folder)
            except FileNotFoundError as e:
                print(f"File not found error for {file_name}: {e}")
        else:
            print(f"No destination folder defined for extension '{ext}'. File not moved.")

def clean_folder(folder_path):
    """
    Clean the specified folder by organizing its files.
    """
    full_file_names, extensions = scan_files(folder_path)
    organize_files(full_file_names, extensions)

def main():
    """
    Main function to initiate desktop folder cleaning.
    """
    print("\nCleaning the Desktop folder...\n")
    clean_folder(DESKTOP_FOLDER)
    print("Desktop cleaning completed.\n")

if __name__ == "__main__":
    main()