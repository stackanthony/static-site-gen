from classes.FileHandler import FileHandler


def main():
    FileHandler.copy_files("../static/", "../public")

if __name__ == "__main__":
    main()
