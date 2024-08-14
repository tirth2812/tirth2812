print(15.0/4+(8.0+3))
def show_todo():
    f=open("todo.txt", "r")
    lines=f.readlines()
    
    for i in lines:
        if "to" in i:
            print("to")
    
    for j in lines:
        if "do" in j:
            print("do")
            
show_todo()