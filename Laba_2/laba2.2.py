import os 
import shutil
    
def file_size(archive_path, extract_dir):
    
    if not os.path.exists( directory):
        print("Указанная директория не существует!")
        return
    
    shutil.unpack_archive(archive_path, extract_dir)
    
    total_size = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath  = os.path.join(root, file)
            total_size += os.path.getsize(root)
    
    print(f"Суммарнфй размер файлов: {total_size} байт")

directory_zip = input("Введите путь до директории: ")
directory = input("Введите путь до директории для извлечения из архива: ")

file_size(directory_zip, directory)

#C:\Users\gilev\OneDrive\Desktop\Hogvards\Pycharm\Laboratories_2\Laba_2\folder_with_file_and_photos.zip
#C:\Users\gilev\OneDrive\Desktop\Hogvards\Pycharm\Laboratories_2\Laba_2\unpackd zip