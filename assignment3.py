from AbacoStack import *

def main():
    number_of_colors = int(imput("Select the number of colors: "))
    dept = int(input("Select the depth: "))
    if number_of_colors<5 or number_of_colors>2:
        print("Enter a valid number of colors")
    elif dept<4 or dept>2:
        print("Enter a valid depth")
        return
    else:
        start= True
        while start:
            print("Enter your moves (Q or r): ")
            moves = input()
            if len(moves)>5:
                print("Only 5 moves at once")
            for i in moves:
                if move == "Q":
                    start = False
                print("Thank you for playing AbacoStack")

                           