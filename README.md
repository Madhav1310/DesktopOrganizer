# DesktopOrganizer

As a coder who admittedly prefers to spend more time writing code than manually organizing files, I decided to create this automation tool to make my life a bit easier. 

This script is designed to clean and organize files on your desktop by automatically moving them into designated folders based on their file extensions. By default, the script targets the Desktop folder, but you can easily change it to organize files in any folder by changing a few variable names. 

```python
# Global Constants
DESKTOP_FOLDER = '/Users/madhavmittal/Desktop'

FULL_PATH_TO_DOCUMENTS_FOLDER = '/Users/madhavmittal/Desktop/documents'
FULL_PATH_TO_IMAGES_FOLDER = '/Users/madhavmittal/Desktop/images'
FULL_PATH_TO_VIDEOS_FOLDER = '/Users/madhavmittal/Desktop/videos'
FULL_PATH_TO_AUDIO_FOLDER = '/Users/madhavmittal/Desktop/audio'
FULL_PATH_TO_ARCHIVES_FOLDER = '/Users/madhavmittal/Desktop/archives'
FULL_PATH_TO_SCRIPTS_FOLDER = '/Users/madhavmittal/Desktop/scripts'
FULL_PATH_TO_APPS_FOLDER = '/Users/madhavmittal/Desktop/apps'
```

You may change the ```DESKTOP_FOLDER``` variable to your own source folder. I mainly use this for my desktop, since it gets cluttered very easily. Additionally, you may change the destination folders for each file type. 

<br>


https://github.com/user-attachments/assets/cfbcbcbe-8179-4d02-9a84-08a0e44fa10e

