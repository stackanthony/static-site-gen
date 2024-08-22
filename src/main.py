from src.classes.FileHandler import FileHandler
from src.classes.PageGenerator import PageGenerator


def main():
    static_dir = input(
        'Enter PATH of static directory (containing images or CSS files): '
    )

    dest_dir = input(
        "Enter PATH of directory where you'd like to place generated files: "
    )

    FileHandler.copy_files(static_dir, dest_dir)

    content_dir = input(
        'Enter PATH of content directory (contains markdown files / dirs of markdown files): '
    )

    template_file = input(
        'Enter PATH of template file (HTML file that contains {{Title}} and {{Content}}): '
    )

    PageGenerator.generate_pages_recursive(
        content_dir, template_file, dest_dir
    )


if __name__ == '__main__':
    main()
