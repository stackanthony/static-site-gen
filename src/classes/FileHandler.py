import os, shutil
class FileHandler:
    def __init__(self) -> None:
        pass

    @staticmethod
    def copy_files(source_dir: str, dest_dir: str) -> bool:
        # clean destination directory
        FileHandler.delete_files(dest_dir)

        return True

    @staticmethod
    def delete_files(dir: str):
        for file_name in os.listdir(dir):
            file_path = os.path.join(dir, file_name)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as err:
                print(f"Failed to delete {file_path}. Reason: {err}")

