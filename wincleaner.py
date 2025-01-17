import os
import shutil
import tempfile
import winreg
from pathlib import Path

def clear_temp_files():
    temp_dir = tempfile.gettempdir()
    try:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                try:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                    print(f'Deleted file: {file_path}')
                except Exception as e:
                    print(f'Failed to delete file {file}: {e}')

            for dir in dirs:
                try:
                    dir_path = os.path.join(root, dir)
                    shutil.rmtree(dir_path)
                    print(f'Deleted directory: {dir_path}')
                except Exception as e:
                    print(f'Failed to delete directory {dir}: {e}')

    except Exception as e:
        print(f'Error while cleaning temp directory: {e}')


def clear_recycle_bin():
    try:
        # Windows Recycle Bin path
        recycle_bin = Path(os.getenv('SystemDrive') + '\\$Recycle.Bin')
        for user in recycle_bin.iterdir():
            if user.is_dir():
                shutil.rmtree(user, ignore_errors=True)
                print(f'Cleared recycle bin for: {user}')
    except Exception as e:
        print(f'Error while clearing recycle bin: {e}')


def clear_windows_update_cache():
    try:
        update_cache_path = Path(r'C:\Windows\SoftwareDistribution\Download')
        for item in update_cache_path.iterdir():
            if item.is_file():
                item.unlink()
                print(f'Deleted update cache file: {item}')
            elif item.is_dir():
                shutil.rmtree(item)
                print(f'Deleted update cache directory: {item}')
    except Exception as e:
        print(f'Error while clearing Windows update cache: {e}')


def clear_prefetch():
    try:
        prefetch_path = Path(r'C:\Windows\Prefetch')
        for item in prefetch_path.iterdir():
            if item.is_file():
                item.unlink()
                print(f'Deleted prefetch file: {item}')
    except Exception as e:
        print(f'Error while clearing prefetch files: {e}')


def main():
    print("Starting WinCleaner...")
    clear_temp_files()
    clear_recycle_bin()
    clear_windows_update_cache()
    clear_prefetch()
    print("Finished cleaning.")

if __name__ == "__main__":
    main()