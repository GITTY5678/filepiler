import sys
from engine.interpreter import Interpreter
def main():
    #1.check if file is provided
    if len(sys.argv)<2:
        print("ERROR: No .fp file provided")
        sys.exit(1)
    file_path=sys.argv[1]
    #2.extension
    if not file_path.endswith(".fp"):
        print("ERROR: File is not a .fp file")
        sys.exit(1)
    print("info: File validated")
    #3.read file
    try:
        with open(file_path,"r") as file:
            lines=file.readlines()
    except FileNotFoundError:
        print(f"ERROR: File '{file_path}' not found")
        sys.exit(1)
    #4.interpret
    interpreter=Interpreter()
    interpreter.run(lines)
if __name__=="__main__":
    main()