def add(a,b):
    answer=a+b
    print(str(a)+"+"+str(b)+"= "+str(answer))

def sub(a,b):
    answer=a-b
    print(str(a)+"-"+str(b)+"= "+str(answer))

def mult(a,b):
    answer=a*b
    print(str(a)+"*"+str(b)+"= "+str(answer))

def div(a,b):
    answer=a/b
    print(str(a)+"/"+str(b)+"= "+str(answer))

while(True):
    print("A, Addition")
    print("B, Subtraction")
    print("C, multiplication")
    print("D, Division")
    print("Exit")

    choice=input("Input your choice")

    if choice=="A" or choice=="a":
        print("Addition")
        a=int(input("Input first number"))
        b=int(input("input second number"))
        add(a,b)
    elif choice=="B" or choice=="b":
        print("Subtraction")
        a=int(input("Input first number"))
        b=int(input("input second number"))
        sub(a,b)
    elif choice=="C" or choice=="c":
        print("Multiplication")
        a=int(input("Input first number"))
        b=int(input("input second number"))
        mult(a,b)
    elif choice=="D" or choice=="d":
        print("Division")
        a=int(input("Input first number"))
        b=int(input("input second number"))
        div(a,b)
    elif choice=="E" or choice=="e":
        print("programe ended")
        quit()