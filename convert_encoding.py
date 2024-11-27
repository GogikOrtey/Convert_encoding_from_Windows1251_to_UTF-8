import os

def convert_file_encoding(file_path, src_encoding='windows-1251', dest_encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=src_encoding, errors='ignore') as file:
            content = file.read()
        with open(file_path, 'w', encoding=dest_encoding) as file:
            file.write(content)
    except Exception as e:
        print(f"Ошибка при конвертации файла {file_path}: {e}")

def convert_project_encoding(root_directory):
    try:
        for subdir, _, files in os.walk(root_directory):
            for file in files:
                if (file.endswith('.cpp') or file.endswith('.h')):
                    file_path = os.path.join(subdir, file)
                    convert_file_encoding(file_path)
        print("Конвертация успешна!")
    except Exception as e:
        print(f"Ошибка при обработке директории {root_directory}: {e}")

if __name__ == "__main__":
    try:
        project_directory = os.getcwd()  # Текущая директория, в которой запущен скрипт
        convert_project_encoding(project_directory)
    except Exception as e:
        print(f"Ошибка при выполнении скрипта: {e}")
    input("Нажмите Enter, чтобы закрыть окно...")











# import os

# def convert_file_encoding(file_path, src_encoding='windows-1251', dest_encoding='utf-8'):
#     with open(file_path, 'r', encoding=src_encoding) as file:
#         content = file.read()
#     with open(file_path, 'w', encoding=dest_encoding) as file:
#         file.write(content)

# def convert_project_encoding(root_directory):
#     for subdir, _, files in os.walk(root_directory):
#         for file in files:
#             if (file.endswith('.cpp') or file.endswith('.h') or file.endswith('.txt')):
#                 file_path = os.path.join(subdir, file)
#                 convert_file_encoding(file_path)
#     print("Конвертация успешна!")

# if __name__ == "__main__":
#     try:
#         project_directory = os.getcwd()  # Текущая директория, в которой запущен скрипт
#         convert_project_encoding(project_directory)
#     except Exception as e:
#         print(f"Ошибка при выполнении скрипта: {e}")
#     input("Нажмите Enter, чтобы закрыть окно...")

    


