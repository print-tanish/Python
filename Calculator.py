
              
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {"+": add, "-": sub, "*": mul, "/": div}
yes_no = ""

while yes_no != "no":
    try:
        n1 = int(input("What is your first number? "))
        for ops in operations:
            print(ops)
        char = input("Enter the operation you would like to perform: ")
        n2 = int(input("Enter second number: "))
        ans = operations[char](n1, n2)
        print(f"{n1} {char} {n2} = {ans}")
        n1 = n2
        yes_no = input("Yes to continue, no to stop: ")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")

