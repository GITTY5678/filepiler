from engine.commands.view import view_path
from engine.commands.create import create_path

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
        
            
    
        
            