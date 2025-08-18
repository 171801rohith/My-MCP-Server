import os
import shutil
from send2trash import send2trash
from AppOpener import open, close


def rename_to_episodes(full_path: str) -> str:
    os.startfile(full_path)
    episodes = os.listdir(full_path)
    for i, episode in enumerate(episodes, start=1):
        old_path = os.path.join(full_path, episode)
        file_name = f"E0{i}" if i <= 9 else f"E{i}"
        extension = episode[episode.index(".") :]
        new_path = os.path.join(full_path, file_name + extension)
        os.rename(old_path, new_path)

    return f"Successfully renamed to Episodes."


def delete_folder(path: str) -> str:
    shutil.rmtree(path)
    return f"Successfully deleted the folder."


def move_folder_trash(path: str) -> str:
    send2trash(path)
    return f"Successfully trashed the folder."


def open_app(app_name: str) -> str:
    try:
        open(app_name, match_closest=True, throw_error=True)
        return f"Successfully opened {app_name}."
    except Exception as e:
        print("Error:", e)
        return f"Failed to open {app_name}."


def close_app(app_name: str) -> str:
    try:
        close(app_name, match_closest=True, throw_error=True)
        return f"Successfully closed {app_name}."
    except Exception as e:
        print("Error:", e)
        return f"Failed to close {app_name}."
