from paperbox.utils import get_config
from typing import List
import shutil
import os

config = get_config()


def get_all_markdown_file_names() -> List[str]:
    """Get all markdown file names tree search."""
    return [
        os.path.join(root, file)
        for root, _, files in os.walk(config["dirs"]["markdown"])
        for file in files
        if file.endswith(".md")
    ]


def add_markdown_folder(folder_name: str) -> None:
    """Add a markdown folder."""
    os.makedirs(os.path.join(config["dirs"]["markdown"], folder_name), exist_ok=True)


def delete_markdown_folder(folder_name: str) -> None:
    """Delete a markdown folder."""
    shutil.rmtree(
        os.path.join(config["dirs"]["markdown"], folder_name), ignore_errors=True
    )


def add_markdown_file(file_name: str) -> None:
    """Add a markdown file."""
    open(os.path.join(config["dirs"]["markdown"], file_name), "a").close()


def delete_markdown_file(file_name: str) -> None:
    """Delete a markdown file."""
    os.remove(os.path.join(config["dirs"]["markdown"], file_name))


def rename_markdown_file(old_file_name: str, new_file_name: str) -> None:
    """Rename a markdown file."""
    os.rename(
        os.path.join(config["dirs"]["markdown"], old_file_name),
        os.path.join(config["dirs"]["markdown"], new_file_name),
    )


def move_markdown_file(old_file_name: str, new_file_name: str) -> None:
    """Move a markdown file."""
    shutil.move(
        os.path.join(config["dirs"]["markdown"], old_file_name),
        os.path.join(config["dirs"]["markdown"], new_file_name),
    )


def copy_markdown_file(old_file_name: str, new_file_name: str) -> None:
    """Copy a markdown file."""
    shutil.copyfile(
        os.path.join(config["dirs"]["markdown"], old_file_name),
        os.path.join(config["dirs"]["markdown"], new_file_name),
    )
