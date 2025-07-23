import random

user_name = "Robert"

def play_game():
    min = 1
    max = 100
    count = 0
    guess_value = random.randint(min,max)
    print(guess_value)
    print("==========猜數字遊戲===========\n")
    while(True):        
        count += 1
        keyin = int(input(f"猜數字範圍{min}~{max}:"))            
        if keyin >= min and keyin <= max:
            if(keyin == guess_value):
                print(f"賓果!猜對了,答案是:{guess_value}")
                print(f"您猜了{count}次")
                break
            elif keyin > guess_value:
                print("再小一點!")
                max = keyin - 1
            
            else:
                print("再大一點")
                min = keyin + 1

            print(f"您已經猜{count}次")
            
        else:
            print("請輸入提示範圍內的數字")


class Empty():
    pass