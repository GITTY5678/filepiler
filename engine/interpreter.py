from engine.commands.view import view_path
from engine.commands.create import create_path
from engine.commands.delete import delete_path
from engine.commands.find import find_path
from engine.commands.info import display_info
from engine.commands.memory_sort import memory_sort
from engine.commands.watch import watch_path
import os


class Interpreter:
    def __init__(self):
        self.cwd = os.getcwd()


    def resolve_path(self, path):
        if os.path.isabs(path):
            return path
        return os.path.abspath(os.path.join(self.cwd, path))

    
    def run(self, lines):
        for index, line in enumerate(lines, start=1):
            clean_line = line.strip()
            if not clean_line:
                continue

            if clean_line.startswith("@"):
                self.det_command(clean_line, index)
            else:
                print(f"[Error] Line {index}: Line must start with '@'")

    # command router
    def det_command(self, line, line_number):
        if line.startswith("@view"):
            self.handle_view(line, line_number)
        elif line.startswith("@create"):
            self.handle_create(line, line_number)
        elif line.startswith("@syntax"):
            self.handle_syntax()
        elif line.startswith("@delete"):
            self.handle_delete(line, line_number)
        elif line.startswith("@find"):
            self.handle_finder(line, line_number)
        elif line.startswith("@info"):
            self.handle_info(line, line_number)
        elif line.startswith("@memory_sort"):
            self.handle_memory(line, line_number)
        elif line.startswith("@watch"):
            self.handle_watch(line, line_number)
        elif line.startswith("@pwd"):
            self.handle_pwd()
        elif line.startswith("@cd"):
            self.handle_cd(line, line_number)
        elif line.startswith("@exit"):
            raise SystemExit
        elif line.startswith("@help"):
            self.handle_help()
        elif line.startswith("@clear"):
            os.system("cls" if os.name == "nt" else "clear")
        elif line.startswith("@about"):
            self.handle_about()
        else:
            print(f"[Error] Line {line_number}: Unknown command '{line.split()[0]}'")

    # handlers
    
    def handle_view(self, line, line_number):
        if "->" not in line:
            print(f"[Error] Line {line_number}: Missing '->' in @view")
            return

        _, path = line.split("->", 1)
        path = path.strip()

        if not path:
            print(f"[Error] Line {line_number}: No path specified")
            return

        path = self.resolve_path(path)
        view_path(path, line_number)

    def handle_create(self, line, line_number):
        if "->" not in line or "$" not in line:
            print(f"[Error] Line {line_number}: Invalid @create syntax")
            return

        _, value = line.split("->", 1)
        dir_path, file_name = value.split("$", 1)

        dir_path = dir_path.strip()
        file_name = file_name.strip()

        if not dir_path or not file_name:
            print(f"[Error] Line {line_number}: Missing directory or filename")
            return

        dir_path = self.resolve_path(dir_path)
        create_path(dir_path, file_name, line_number)

    def handle_delete(self, line, line_number):
        if "->" not in line:
            print(f"[Error] Line {line_number}: Missing '->' in @delete")
            return

        _, path = line.split("->", 1)
        path = path.strip()

        if not path:
            print(f"[Error] Line {line_number}: No path specified")
            return

        path = self.resolve_path(path)
        delete_path(path, line_number)

    def handle_finder(self, line, line_number):
        if "->" not in line or "$" not in line:
            print(f"[Error] Line {line_number}: Invalid @find syntax")
            return

        _, value = line.split("->", 1)
        base_path, name = value.split("$", 1)

        base_path = base_path.strip()
        name = name.strip()

        if not base_path or not name:
            print(f"[Error] Line {line_number}: Missing path or search name")
            return

        base_path = self.resolve_path(base_path)
        find_path(base_path, name, line_number)

    def handle_info(self, line, line_number):
        if "->" not in line:
            print(f"[Error] Line {line_number}: Missing '->' in @info")
            return

        _, path = line.split("->", 1)
        path = path.strip()

        if not path:
            print(f"[Error] Line {line_number}: No path specified")
            return

        path = self.resolve_path(path)
        display_info(path, line_number)

    def handle_memory(self, line, line_number):
        if "->" not in line or "$" not in line:
            print(f"[Error] Line {line_number}: Invalid @memory_sort syntax")
            return

        _, value = line.split("->", 1)
        path, order = value.split("$", 1)

        path = path.strip()
        order = order.strip()

        if not path or not order:
            print(f"[Error] Line {line_number}: Missing path or order")
            return

        path = self.resolve_path(path)
        memory_sort(path, order, line_number)

    def handle_watch(self, line, line_number):
        if "->" not in line:
            print(f"[Error] Line {line_number}: Missing '->' in @watch")
            return

        _, value = line.split("->", 1)
        value = value.strip()

        recursive = False

        if "$" in value:
            path, flag = value.split("$", 1)
            if flag.strip() == "r":
                recursive = True
            else:
                print(f"[Error] Line {line_number}: Unknown @watch flag")
                return
        else:
            path = value

        path = path.strip()

        if not path:
            print(f"[Error] Line {line_number}: No path specified")
            return

        path = self.resolve_path(path)
        watch_path(path, line_number, recursive)

    def handle_pwd(self):
        print(self.cwd)

    def handle_cd(self, line, line_number):
        if "->" not in line:
            print(f"[Error] Line {line_number}: Missing '->' in @cd")
            return

        _, path = line.split("->", 1)
        path = path.strip()

        if not path:
            print(f"[Error] Line {line_number}: No path specified")
            return

        path = self.resolve_path(path)

        if not os.path.exists(path):
            print(f"[Error] Line {line_number}: Path does not exist")
            return

        if not os.path.isdir(path):
            print(f"[Error] Line {line_number}: Not a directory")
            return

        self.cwd = path

    def handle_help(self):
        print("""
    Filepiler Shell Commands

    Shell:
    @help
    @exit
    @pwd
    @cd -> <path>

    Filesystem:
    @view -> <path>
    @find -> <path>$<name>
    @info -> <path>
    @memory_sort -> <dir>$<a|d>
    @watch -> <path>[$r]
    @create -> <dir>$<file>
    @delete -> <path>

    Notes:
    - Paths can be relative or absolute
    - Use $r for recursive watch
    """)
        
    def handle_about(self):
        print("""
Filepiler Shell v1.0
Built as a custom filesystem-oriented shell.

Features:
- File & directory inspection
- Search and analysis
- Live filesystem watching
- Interactive session with state

Author: HARIHARA SUTHAN S
""")

        

        
        
        
        
    
