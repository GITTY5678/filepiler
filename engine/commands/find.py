import os
import time
def find_path(app_path,search_path):
    start_time=time.perf_counter()
    found=False
    
    is_file_target='.' in search_path
    
    dirs_to_search={".git","__pycache__","node_modules","venv","AppData",".idea",".vscode"}
    
    try:
        for root,dirs,files in os.walk(app_path):
            
            if is_file_target:
                dirs[:]=[d for d in dirs if d not in dirs_to_search]
            
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
            if found:
                break
    except PermissionError:
        print(f"[Error]: Permission denied to access some directories under '{app_path}'")
        return
    end_time=time.perf_counter()
    elapsed_time=end_time-start_time
    if not found:
        print(f"[FIND] No file or directory named '{search_path}' found under '{app_path}'")
        return
    print(f"[TIME] Search completed in {elapsed_time:.4f} seconds")
    