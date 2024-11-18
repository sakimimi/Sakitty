def a():
    print('addition')
    ent1 = float(input("type in the number"))
    ent2 = float(input("type in the number"))
    addition = ent1+ent2
    print(addition)

def b():
    print("subtraction")
    ent1 = float(input("type in the number"))
    ent2 = float(input("type in the number"))
    subtraction = ent1-ent2
    print(subtraction)

def c():
     print("multiplication")
     ent1 = float(input("type in the number"))
     ent2 = float(input("type in the number"))
     multiplication = ent1*ent2
     print(multiplication)

def d():
    print("division")
    ent1 = float(input("what is the mass?"))
    ent2 = float(input("what is the area?"))
    division = ent1 + ent2
    print(division)

def e():
    print("area")
    length = float(input("what is the length?"))
    breadth = float(input("what is the breadth?"))
    area = length*breadth
    print(area)

def main():
     choice = input("what question do you want to work on :")
     if choice == "a":
        a()
     elif choice == "b":
        b()
     elif choice == "c":
        c()
     elif choice == "d":
        d()
     elif choice == "e":
        e()
     else:
         print("invalid")


if __name__ == '__main__':
     main()