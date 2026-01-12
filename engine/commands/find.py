import os
import time

def search_with_rules(app_path,search_path,rules,line_number):
    found=False
    is_file_targe="." in search_path
    app_depth=app_path.count(os.sep)
    
    for root,dirs,files in os.walk(app_path):
        #depth pruning
        if rules["max_depth"] is not None:
            depth=root.count(os.sep)-app_depth
            if depth>rules["max_depth"]:
                dirs.clear()
                continue
        #directory skipping
        if rules["skip_dirs"]:
            dirs[:] = [d for d in dirs if d not in rules["skip_dirs"]]
        #file relevance check
        if rules["use_relevant_files"]:
            dirs[:]=[d for d in dirs if d.lower() in search_path.lower() or search_path.lower() in d.lower()]
        #directory match
        for d in dirs:
            if d==search_path:
                full_path=os.path.join(root,d)
                print(f"[Success] on line {line_number}: Found directory at '{full_path}'")
                return True
        #file match
        for f in files:
            if f==search_path:
                full_path=os.path.join(root,f)
                print(f"[Success] on line {line_number}: Found file at '{full_path}'")
                return True
    return False


def find_path(app_path,search_path,line_number):
    if not os.path.exists(app_path):
        print("[fError] on line {}: Approximation path '{}' does not exist".format(line_number,app_path))
        return
    
    levels=[
        {
            "name":"level 1 search",
            "max_depth":2,
            "skip_dirs":{ ".git", "__pycache__", "node_modules",
                "venv", "AppData", ".idea", ".vscode"
            },
            "use_relevant_files":True
        },
        {
            "name":"level 2 search",
            "max_depth":4,
            "skip_dirs": {
                ".git", "__pycache__", "node_modules",
                "venv", "AppData"
        },
            "use_relevant_files":False
        },
        {
            "name":"level 3 search",
            "max_depth":None,
            "skip_dirs":{
                "__pycache__"
                },
            "use_relevant_files":False
        }
    ]
    for i,level in enumerate(levels):
        if i==2:
            print("[Warning] on line {}: Performing deep search, this may take a while...".format(line_number))
        found=search_with_rules(app_path,search_path,level,line_number)
        if found:
            return 
        print("[Info] on line {}: '{}' not found in {}, proceeding to next search level...".format(line_number,search_path,level["name"]))
    print(f"[ERROR] on line {line_number}: Could not find '{search_path}' in the application path.")
    
        