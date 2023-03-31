import random
 
choices = ["石头", "布", "剪刀"]
computer = random.choice(choices)
game_player = False
computer_score = 0  # 电脑的初始分数
player_score = 0  # 玩家的初始分数
while True:
    game_player = input("石头, 布 or  剪刀? \n").capitalize()
 
    # 判断玩家和电脑的选择
    if game_player == computer:
        print("平局!\n")
 
    elif game_player == "石头":
        if computer == "布":
            print("你输了!", computer, "covers", game_player,'\n')
            computer_score += 1
        else:
            print("你赢了!", game_player, "smashes", computer,'\n')
            player_score += 1
 
    elif game_player == "布":
        if computer == "剪刀":
            print("你输了!", computer, "cut", game_player,'\n')
            computer_score += 1
        else:
            print("你赢了!", game_player, "covers", computer,'\n')
            player_score += 1
 
    elif game_player == "剪刀":
        if computer == "石头":
            print("你输了", computer, "smashes", game_player,'\n')
            computer_score += 1
        else:
            print("你赢了✌️!", game_player, "cut", computer,'\n')
            player_score += 1
 
    elif game_player == '结束':
        print("——————最终得分——————")
        print(f"电脑:{computer_score}")
        print(f"玩家:{player_score}")
        break
    else:
        print("输入有误，请检查输入!")
    computer = random.choice(choices)
