import os

def find_files(directory, extenchion):
    
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extenchion):
                print(os.path.join(root, file))


directory = input("Введите путь до директории: ")
extenchion = input("Введите разрешение файлов (Ex: .txt; .jpg): ")

find_files(directory, extenchion)

#C:\Users\gilev\OneDrive\Desktop\Hogvards\Pycharm\Laboratories_2\Laba_2\folder_with_file_and_photos