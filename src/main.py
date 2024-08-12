from src.classes.FileHandler import FileHandler
from src.classes.PageGenerator import PageGenerator


def main():
    FileHandler.copy_files('./static/', './public/')
    PageGenerator.generate_page(
        'content/index.md', 'template.html', 'public/index.html'
    )


if __name__ == '__main__':
    main()
