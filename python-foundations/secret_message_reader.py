import os

def rename_files():
    file_list = os.listdir(r"/Users/lbain/code/personal/udacity/python-foundations/message")
    saved_path = os.getcwd()
    os.chdir(r"/Users/lbain/code/personal/udacity/python-foundations/message")
    for file_name in file_list:
        new_file_name = file_name.translate(None, "0123456789")
        print "file_name = " + file_name
        print "new_file_name = " + new_file_name
        os.rename(file_name, new_file_name)
    os.chdir(saved_path)

rename_files()