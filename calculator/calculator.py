def priority(x):
    if x == "^":
        return 3
    if x == "*" or x == "/":
        return 2
    if x == "+" or x == "-":
        return 1
    
def main():
    operators = []
    values = []
    x = "3*2+8/2^3"
    print(x)
    for i in x:
        print(f"{i}\t\t{operators}\t\t{values}")
        if i.isnumeric():
            values.append(int(i))
        elif len(operators) == 0:
            operators.append(i)
        else:
            top = operators[-1]
            if priority(top) < priority(i): #type: ignore
                operators.append(i)
            else:   
                operators.pop()
                b = values.pop()
                a = values.pop()
                result = 0
                if top == "^":
                    result = a**b
                elif top == "*":
                    result = a*b
                elif top == "/":
                    result = a/b
                elif top == "+":
                    result = a+b
                elif top == "-":
                    result = a-b
                values.append(result)
                operators.append(i)
        
    while len(operators) > 0:
        print(f"{operators}\t\t{values}")
        top = operators.pop()
        b = values.pop()
        a = values.pop()
        result = 0
        if top == "^":
            result = a**b
        elif top == "*":
            result = a*b
        elif top == "/":
            result = a/b
        elif top == "+":
            result = a+b
        elif top == "-":
            result = a-b
        values.append(result)
    print(values.pop())

if __name__ == "__main__":
    main()