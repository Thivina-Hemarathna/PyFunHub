import art

def add(n1, n2):
    print(f"{float(n1)} + {float(n2)} = {float(n1+n2)}")
    return n1 + n2

def sub(n1,n2):
    print(f"{float(n1)} - {float(n2)} = {float(n1 - n2)}")
    return n1 - n2

def mul(n1,n2):
    print(f"{float(n1)} * {float(n2)} = {float(n1 * n2)}")
    return n1 * n2

def div(n1,n2):
    print(f"{float(n1)} / {float(n2)} = {float(n1 / n2)}")
    return n1 / n2


operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}


while 1:
    print(art.logo)
    num=float(input("What's the first number?: "))
    yes = True

    while yes:
        print("+")
        print("-")
        print("*")
        print("/")
        num =float(operations[input("Pick an operation: ")](num,float(input("What's the next number?: "))))

        ans=input(f"Type 'y' to continue calculating  with {num}, or type 'n' to start a new calculator:")

        if ans=="y":
            yes=True
        else:
            yes=False
            print("\n" * 30)


