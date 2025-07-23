import tools     

def main():
    try:
        play_count = 0
        while(True):
            play_count += 1
            tools.play_game()
            is_continue = input("您還要繼續嗎(y,n)?")
            if is_continue == "n":
                break
            
        print(f"您共玩了{play_count}次")
        print("遊戲結束")
    except ValueError:
        print("格式錯誤")
        print("應用程式中斷")        
    except Exception as e:
        print(e)
        print("應用程式中斷")
    


if __name__ == "__main__":
    main()