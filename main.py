import sys
import os.path
import glob
py_path = os.getcwd() #C:\Users\user\PycharmProjects\pythonProject7
file_path = os.path.join(os.getcwd(), '/py-homework-basic-files/2.4.files/sorted')
print(file_path)

#glob.glob(pathname, *, root_dir=None, dir_fd=None, recursive=False, include_hidden=False)
list_of_files = glob.glob(pathname=file_path, recursive=False)        # create the list of file
#sort files by number of lines
lines_file_dict = {}
text_file_dict = {}
for file_name in list_of_files:
    FI = open(file_name, 'r')
    count = 0
    for line in FI:
        count +=1
    lines_file_dict.setdefault(file_name, count)
    copied_text = file_name.read()
    text_file_dict.setdefault(file_name, copied_text)
    FI.close()
sorted_files = sorted(lines_file_dict.items(), key=lambda x: x[1], reverse=False)
#print line by line
result_path = os.path.join(os.getcwd(), "result_file.txt")
with open(result_path, mode="a") as file:
    count_files = 0
    for i in sorted_files:
        file_to_print = text_file_dict.get(i)
        result_file.write(i)
        count_files += 1
        count_lines = 0
        for line in file_to_print:
            count_lines +=1
            result_file.write(f'Строка номер {count_lines} файла номер {count_files}')
