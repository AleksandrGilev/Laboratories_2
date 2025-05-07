import os
import shutil

def find_photo(src):
    
    if not os.path.exists(src):
        print("Указанная директория не существует!")
        return
    
    if not os.path.exists(dst):
        os.makedirs(dst)
        
    for root, dirs, files in os.walk(src):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.gif')):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(dst, file)
                shutil.copy(src_file, dst_file)
                
    shutil.make_archive(dst, 'zip', dst)
    
    
src = input("Введите путь до директория с фотографиями: ")
dst = input("Ввеидет путь до пустой директории: ")
find_photo(src)
#C:\Users\gilev\OneDrive\Desktop\Hogvards\Pycharm\Laboratories_2\Laba_2\folder_with_file_and_photos
