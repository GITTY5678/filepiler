import os
import time


def snapshot(dir_path):
    state={}
    try:
        for name in os.listdir(dir_path):
            full_path=os.path.join(dir_path,name)
            try:
                stat=os.stat(full_path)
                state[name]=(stat.st_mtime,stat.st_size,os.path.isdir(full_path))
            except OSError:
                pass
    except OSError:
        pass
    return state

def watch_path(dir_path,line_number,interval=1):
    if not os.path.exists(dir_path):
        print(f"[Error] on line {line_number}: Path '{dir_path}' does not exist")
        return
    if not os.path.isdir(dir_path):
        print(f"[Error] on line {line_number}: Path '{dir_path}' is not a directory")
        return
    print(f"[WATCH] Monitoring directory: {dir_path}")
    print(f"[WATCH] Press Ctrl+C to stop watching.")
    
    prev=snapshot(dir_path)
    
    try:
        while True:
            time.sleep(interval)
            curr=snapshot(dir_path)
            
            for name in curr.keys()-prev.keys():
                print(f"[CREATED] '{name}' was created.")
            for name in prev.keys()-curr.keys():
                print(f"[DELETED] '{name}' was deleted.")
            for name in curr.keys()&prev.keys():
                if curr[name][:2]!=prev[name][:2]:
                    print(f"[MODIFIED] '{name}' was modified.")
            prev=curr
    except KeyboardInterrupt:
        print("\n[WATCH] Stopped monitoring.")