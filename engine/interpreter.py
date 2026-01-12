from engine.commands.view import view_path
from engine.commands.create import create_path
from engine.commands.delete import delete_path
from engine.commands.find import find_path
from engine.commands.info import display_info
import os
class Interpreter:
    def run(self,lines):
        for index,line in enumerate(lines,start=1):
            clean_line=line.strip()
            if not clean_line:
                continue
            if clean_line.startswith("@"):
                self.det_command(clean_line,index)
            else:
                print(f"Syntax Error on line {index}: Line must start with '@'")
    def det_command(self,line,line_number):
        if line.startswith("@view"):
            self.handle_view(line,line_number)
        elif line.startswith("@create"):
            self.handle_create(line,line_number)
        elif line.startswith("@syntax"):
            self.handle_syntax()
        elif line.startswith("@delete"):
            self.handle_delete(line,line_number)
        elif line.startswith("@find"):
            self.handle_finder(line,line_number)
        elif line.startswith("@info"):
            self.handle_info(line,line_number)
        else:
            print(f"[Error] on line {line_number}: Unknown command '{line.split()[0]}'")
    def handle_view(self,line,line_number):
        if "->" not in line:
            print(f"[Error] on line {line_number}: Missing '->' in @view command")
            return
        _,path=line.split("->",1)
        path=path.strip()
        if not path:
            print(f"[Error] on line {line_number}: No path specified in @view command")
            return
        view_path(path,line_number)
    def handle_create(self,line,line_number):
        if "$" not in line or "->" not in line:
            print(f"[Error] Line {line_number}: Invalid @create syntax: missing '$' or '->'")
            return
        _,create_comm=line.split("->",1)
        dir_path,file_name=create_comm.split("$",1)
        dir_path=dir_path.strip()
        file_name=file_name.strip()
        if not dir_path or not file_name:
            print(f"[Error] Line {line_number}: Invalid @create syntax: directory path or file_name missing")
            return
        create_path(dir_path,file_name,line_number)
    def handle_syntax(self):
        with open("C:\\Users\\HARIHARA SUTHAN\\Documents\\GitHub\\filepiler\\docs\\syntax.txt","r") as syntax_file:
            syntax_content=syntax_file.read()
            print(syntax_content)
        return
    def handle_delete(self,line,line_number):
        if "->" not in line:
            print(f"[Error] Line {line_number}: Invalid @delete syntax: missing '->'")
            return
        _,del_line=line.split("->",1)
        del_line=del_line.strip()
        
        if not del_line:
            print(f"[ERROR] on line {line_number}: No path specified in @delete command")
        delete_path(del_line,line_number)
    def handle_finder(self,line,line_number):
        if "$" not in line or "->" not in line:
            print(f"[Error] Line {line_number}: Invalid @find syntax: missing '$' or '->'")
            return
        _,find_comm=line.split("->",1)
        app_path,search_path=find_comm.split("$",1)
        app_path=app_path.strip()
        search_path=search_path.strip()
        if not app_path or not search_path:
            print("[fError] Line {line_number}: Invalid @find syntax: application path or search path missing")
            return
        find_path(app_path,search_path,line_number)
    def handle_info(self,line,line_number):
        if "->" not in line:
            print(f"[ERROR] on line {line_number}: Missing '->' in @info command")
            return
        _,path_line=line.split("->",1)
        path_line=path_line.strip()
        if not path_line:
            print(f"[ERROR] on line {line_number}: No path specified in @info command")
            return
        display_info(path_line,line_number)
        
        
        
        
    
