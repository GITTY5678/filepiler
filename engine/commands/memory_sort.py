import os
import time


def count_files(dir_path):
    file_count=0
    for _,_,files in os.walk(dir_path):
        file_count+=len(files)
    return file_count

def get_dir_size(dir_path,line_number):
    total_size=0
    processed=0
    
    total_files=count_files(dir_path)
    start_time=time.perf_counter()

    if total_files == 0:
        return 0

    for root,_,files in os.walk(dir_path):
        try:
            for f in files:
                processed+=1
                fp=os.path.join(root,f)
                total_size+=os.path.getsize(fp)
                
            if processed % 200 ==0 or processed==total_files:
                elapsed=time.perf_counter()-start_time
                rate=processed/elapsed if elapsed>0 else 0
                remaining_files=total_files-processed
                eta=remaining_files/rate if rate>0 else 0
                    
                print(
                    f"[PROGRESS] {processed}/{total_files} files | "
                    f"ETA ~{int(eta)}s"
                )
        except OSError:
            pass
    return total_size

def memory_sort(directory,sort_command,line_number):
    
    if not  os.path.isdir(directory):
        print(f"[Error] on line {line_number}: Path '{directory}' is not a valid directory")
        return
    if sort_command not in ("a","d"):
        print(f"[Error] on line {line_number}: Invalid sort command '{sort_command}'. Use 'a' for ascending or 'd' for descending.")
        return
    list_items=[]
    item=os.listdir(directory)
    for name in item:
        full_path=os.path.join(directory,name)
        try:
            if os.path.isfile(full_path):
                size=os.path.getsize(full_path)
                list_items.append(("FILE",name,size))
            elif os.path.isdir(full_path):
                size=get_dir_size(full_path,line_number)
                list_items.append(("DIR",name,size))
        except OSError:
            pass
    list_items.sort(key=lambda x:x[2],reverse=(sort_command=="d"))
    print(f"[Memory Sort] on line {line_number}: Sorted contents of '{directory}' ({'Descending' if sort_command=='d' else 'Ascending'} by size):")
    for item_type,name,size in list_items:
        print(f"  [{item_type}] {name} - {human_size(size)}")
    
def human_size(size):
    for unit in ['B','KB','MB','GB','TB']:
        if size<1024:
            return f"{size:.2f} {unit}"
        size/=1024
    return f"{size:.2f} PB"