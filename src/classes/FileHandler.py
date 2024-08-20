import os, shutil


class FileHandler:
    def __init__(self) -> None:
        pass

    @staticmethod
    def copy_files(source_dir: str, dest_dir: str) -> bool:
        # clean destination directory
        source_dir_entries: list[str] = os.listdir(source_dir)
        if source_dir_entries:
            FileHandler.delete_files(dest_dir)

        for file_name in source_dir_entries:
            source_path = os.path.join(source_dir, file_name)
            dest_path = os.path.join(dest_dir, file_name)

            try:
                if os.path.isfile(source_path) and os.path.exists(dest_dir):
                    shutil.copy(source_path, dest_path)
                    continue

                FileHandler.create_dir(dest_path)
                FileHandler.copy_files(source_path, dest_path)
            except Exception as err:
                print(
                    f'Failed to copy files from {source_path} to {dest_path}. Reason: {err}'
                )
                return False

        return True

    @staticmethod
    def list_dir_entries(path: str) -> list[str]:
        # check if dir param is a valid directory
        if not os.path.isdir(path):
            raise Exception('Not a valid directory path')

        return os.listdir(path)

    @staticmethod
    def is_file(file_path: str) -> bool:
        return os.path.isfile(file_path)

    @staticmethod
    def replace_word_file(read_path: str, dest_path: str, old: str, new: str):
        with open(read_path, 'r') as file:
            filedata = file.read()

        filedata = filedata.replace(old, new)

        with open(dest_path, 'w') as file:
            file.write(filedata)

    @staticmethod
    def write_to_file(content: str, dest_path: str):
        try:
            with open(dest_path, "w") as file:
                file.write(content)
        except Exception as err:
            print(f"Unable to write to file. Reason: {err}")

    @staticmethod
    def create_dir(path: str) -> bool:
        try:
            os.mkdir(path)
            print(f"Created Directory: {path}")
        except Exception as err:
            print(f'Unable to create directory. Reason: {err}')
            return False

        return True

    @staticmethod
    def delete_files(dir: str) -> bool:
        print(f"Deleting files from {dir}")
        for file_name in os.listdir(dir):
            file_path = os.path.join(dir, file_name)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as err:
                print(f'Failed to delete {file_path}. Reason: {err}')
                return False

        return True
