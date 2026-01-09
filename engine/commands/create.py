import os
def create_path(dir_path,file_name,line_number):
    full_path=os.path.join(dir_path,file_name)
    if os.path.exists(full_path):
        print("[Error] on line {}: Path '{}' aldeady exists".format(line_number,full_path))
        return
    try:
        with open(full_path,'w'):
            pass
        print("[CREATE] Created file at:",full_path)
    except PermissionError:
        print("[Error] on line {}: Permission denied to create file at '{}'".format(line_number,full_path))
    except FileNotFoundError:
        print("[Error] on line {}: Directory '{}' does not exist".format(line_number,dir_path))