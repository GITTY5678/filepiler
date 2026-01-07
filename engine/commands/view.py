import os
def view_path(path,line_number):
    if not os.path.exists(path):
        print("[Error] on line {}: Path '{}' does not exist".format(line_number,path))
        return
    
    #case 1:directory
    if os.path.isdir(path):
        print("[VIEW] Directory listing for:",path)
        try:
            for item in os.listdir(path):
                full_path=os.path.join(path,item)
                if os.path.isdir(full_path):
                    print("[DIR] ",item)
                else:
                    print("[FILE] ",item)
        except PermissionError:
            print("[Error] on line {}: Permission denied to access directory '{}'".format(line_number,path))
        return
    if os.path.isfile(path):
        print("[VIEW] File content for:",path)
        try:
            size=os.path.getsize(path)
            file_extension=os.path.splitext(path)[1].lower()
            print("[INFO] Size : {} bytes".format(size))
            print("[INFO] Extension : {}".format(file_extension))
        except PermissionError:
            print("[Error] on line {}: Permission denied to access file '{}'".format(line_number,path))
        return