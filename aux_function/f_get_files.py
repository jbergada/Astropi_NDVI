from os import listdir

def f_get_files(path):
    file_list = []

    for file in listdir(path):
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith('.bmp') :
            file_list.append(file)

    return file_list




