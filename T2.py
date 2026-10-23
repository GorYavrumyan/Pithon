num1 = int(input("Number 1 -  "))
num2 = int(input("Number 2 -  "))

if num1 > num2:
    print(num1, " > ", num2)
elif num2 > num1:
    print(num2, " > ", num1)
else:
    print("Թվերը հավասար են")


print(" ")
print(" ")


a = int(input("a -  "))
b = int(input("b -  "))
c = int(input("c -  "))

if a > b and a > c:
    print(a, " > ", b, " & ", c)
elif b > a and b > c:
    print(b, " > ", a, " & ", c)
elif c > a and c > b:
    print(c, " > ", a, " & ", b)
else:
    print(c, " = ", a, " = ", b)


print(" ")
print(" ")


num1 = int(input("Number 1 -  "))
print(num1, " +, -, *, / number 2")
OLperator = input("Operator -  ")
print(num1, OLperator, " Number 2")
num2 = int(input("Number 2 -  "))

if OLperator == "+":
    print(num1, " + ", num2, " = ", num1 + num2)
elif OLperator == "-":
    print(num1, " - ", num2, " = ", num1 - num2)
elif OLperator == "*":
    print(num1, " * ", num2, " = ", num1 * num2)
elif OLperator == "/":
    if num2 == 0:
        print("Eror")
    else:
        print(num1, " / ", num2, " = ", num1 / num2)
else:
    print("Eror")
