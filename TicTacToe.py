b=[" " for x in range(9)]
def print_board():
    row1="|{}|{}|{}|".format(b[0],b[1],b[2])
    row2="|{}|{}|{}|".format(b[3],b[4],b[5])
    row3="|{}|{}|{}|".format(b[6],b[7],b[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()
def player_move(icon):
    if icon=='X':
        number=1
    elif icon=='O':
        number=2
    print("Your turn player{}".format(number))
    ch=int(input("Enter your choice(1-9):").strip())
    if b[ch-1]==" ":
        b[ch-1]=icon
    else:
        print("The space is taken")
def is_draw():
    if " " not in b:
        return True
    else:
        return False
def is_victory(icon):
    if (b[0]==icon and b[1]==icon and b[2]==icon) or \
    (b[3]==icon and b[4]==icon and b[5]==icon) or \
    (b[6]==icon and b[7]==icon and b[8]==icon) or \
    (b[0]==icon and b[3]==icon and b[6]==icon) or \
    (b[1]==icon and b[4]==icon and b[7]==icon) or \
    (b[2]==icon and b[5]==icon and b[8]==icon) or \
    (b[2]==icon and b[4]==icon and b[6]==icon) or \
    (b[0]==icon and b[4]==icon and b[8]==icon):
        return True
    else:
        return False
while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X wins! congratulations")
        break
    elif is_draw():
        print("Its a draw")
        break
    player_move("O")
    
    if is_victory("O"):
        print_board()
        print("O wins! congratulations")
        break
    elif is_draw():
        print("Its a draw")
        break
