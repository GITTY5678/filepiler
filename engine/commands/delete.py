import os
def delete_path(path,line_number):
    if  not os.path.exists(path):
        print("[ERROR] on line {}: Path '{}' does not exist".format(line_number,path))
        return
    elif os.path.isdir(path):
        try:
            os.rmdir(path)
            print("[DELETE] Deleted directory at: {}".format(path))
            return
        except OSError:
            print("[ERROR] on line {}: Directory '{}' is not empty or cannot be deleted".format(line_number,path))
            return 
    elif os.path.isfile(path):
        try:
            os.remove(path)
            print("[DELETE] Deleted file at: {}".format(path))
            return
        except OSError:
            print("[ERROR] on line {}: File '{}' cannot be deleted".format(line_number,path))
            return
        