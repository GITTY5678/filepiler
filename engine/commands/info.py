import os

def display_info(path_file,line_number):
    if os.path.isfile(path_file):
        info_file(path_file,line_number)
    elif os.path.isdir(path_file):
        info_directory(path_file,line_number)

def info_file(file_path,line_number):
    size=os.path.getsize(file_path)
    name=os.path.basename(file_path)
    ext=os.path.splitext(name)[1]
    abs_path=os.path.abspath(file_path)
    
    print(f"[Info] on line {line_number}: File Information:")
    print(f"  Name: {name}")
    print(f"  Size: {size} bytes")
    print(f"  Extension: {ext}")
    print(f"  Absolute Path: {abs_path}")
    
def info_directory(dir_path,line_number):
    total_size=0
    file_count=0
    folder_count=0
    for root,dirs,files in os.walk(dir_path):
        folder_count+=len(dirs)
        
        for f in files:
            try:
                file_count+=1
                fp=os.path.join(root,f)
                total_size+=os.path.getsize(fp)
            except OSError:
                pass
    abs_path=os.path.abspath(dir_path)
    print(f"[Info] on line {line_number}: Directory Information:")
    print(f"  Path: {abs_path}")
    print(f"  Total Size: {total_size} bytes or {total_size/1024:.2f} KB or {total_size/(1024*1024):.2f} MB")
    print(f"  Total Files: {file_count}")
    print(f"  Total Folders: {folder_count}")