import os


def _get_link_name(folder_path: str) -> str:
    """
    Generates a name for the symbolic link based on the folder path.

    Args:
        folder_path (str): The path to the folder.
    """

    base_name = os.path.basename(folder_path)
    return base_name


def create_folder_link(folder_path: str) -> None:
    """
    Creates a symbolic link to a folder.

    Args:
        folder_path (str): The path to the folder.
    """

    folder_name = os.path.basename(folder_path)
    os.symlink(folder_path, folder_name)
    print(f"Symbolic link created: {folder_name} -> {folder_path}")


if __name__ == "__main__":
    folder_path = input("Enter the path to the folder (Split with space): ")
    all_folders = folder_path.split()
    for folder_path in all_folders:
        create_folder_link(folder_path)
