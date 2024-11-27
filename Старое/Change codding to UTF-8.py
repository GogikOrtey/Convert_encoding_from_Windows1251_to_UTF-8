import os

def convert_file_encoding(file_path, src_encoding='windows-1251', dest_encoding='utf-8'):
    with open(file_path, 'r', encoding=src_encoding) as file:
        content = file.read()
    with open(file_path, 'w', encoding=dest_encoding) as file:
        file.write(content)

def convert_project_encoding(root_directory):
    for subdir, _, files in os.walk(root_directory):
        for file in files:
            if file.endswith('.cpp'):
                file_path = os.path.join(subdir, file)
                convert_file_encoding(file_path)

# Укажите путь к корневому каталогу вашего проекта
project_directory = 'D:\Рабочий стол\ООП'
convert_project_encoding(project_directory)
