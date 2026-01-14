import sys
from engine.interpreter import Interpreter
def main():
    interpreter=Interpreter()
    
    print('''Filepiler Shell v1.0
A filesystem-first interactive shell
Type @help for commands''')
    
    while True:
        try:
            command=input("fp> ").strip()
            
            #exit command
            if command.lower()=="exit":
                print("Exiting Filepiler shell")
                break
            #ignore empty input
            if not command:
                continue
            interpreter.run([command])
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit")
        except Exception as e:
            print(f"\n[Shell Error] {e}")
                
if __name__=="__main__":
    main()