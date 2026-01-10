import os
def find_path(app_path,search_path):
    found=False
    try:
        for root,dirs,files in os.walk(app_path):
            for d in dirs:
                if d==search_path:
                    full_path=os.path.join(root,d)
                    print(f"[FIND] Found directory at: {full_path}")
                    found=True
            for f in files:
                if f==search_path:
                    full_path=os.path.join(root,f)
                    print(f"[FIND] Found file at: {full_path}")
                    found=True
    except PermissionError:
        print(f"[Error]: Permission denied to access some directories under '{app_path}'")
        return
    if not found:
        print(f"[FIND] No file or directory named '{search_path}' found under '{app_path}'")
        return
    