class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.data = []

    def len(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.data.pop()

def reverse_file(filename):
    S = ArrayStack()
    original = open(filename)

    for line in original:
        S.push(line.rstrip("\n"))
    original.close()

    output = open(filename, "w")

    while not S.is_empty():
        output.write(S.pop() + "\n")
    output.close()

    ofile = open(filename, "r")
    k = ofile.readlines()

    for i in k:
        print(i.rstrip())

def is_matched(expr):
    lefty = "({["
    righty = ")}]"
    S = ArrayStack()

    for c in expr:

        if c in lefty:
            S.push(c)

        elif c in righty:
            
            if S.is_empty():
                return False

            if righty.index(c) != lefty.index(S.pop()):
                return False

    return S.is_empty()

active = True

while active :
    print("\nMenu : \n 1. Reverse File \n 2. Matching Delimiters \n 3. Keluar")
    menu = int(input("Masukkan Menu Pilihan: "))

    if menu == 1 :
        nama_file = input("Masukkan Nama File : ")
        print(nama_f2ile + ".txt")
        reverse_file(nama_file + ".txt")

    elif menu == 2 :
        expression = input("Masukkan Expression : ")
        match = is_matched(expression)

        if match :
            print("\n Semua delimiters cocok")

        else :
            print("\n Ada delimiters yang tidak cocok")

    else :
        break
