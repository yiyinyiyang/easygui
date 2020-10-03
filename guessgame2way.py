#使用for循环写猜数游戏 

import random,easygui
key= random.randint(1,100)
    
for i in range(0,6):
    user_guess = easygui.enterbox(title="猜数游戏",msg="请输入一个1至100的数"+"你有"+str(6-int(i))+"次机会",default="40")
    if int(user_guess) > key:
        if i!=5:
            easygui.msgbox(title="猜数游戏",msg="你猜的数是"+user_guess+"猜大了",ok_button="继续")
            guess_result = easygui.buttonbox(title="继续游戏",msg="你还继续游戏吗？你还有"+str(5-int(i))+"次机会",choices=["继续猜数","退出"])
        elif i==5:
            easygui.msgbox(title="猜数游戏",msg="你6次机会用完了,电脑生成的关键数是："+str(key),ok_button="结束")
            
    elif int(user_guess) < key:
        if i!=5:
            easygui.msgbox(title="猜数游戏",msg="你猜的数是"+user_guess+"猜小了",ok_button="继续")
            guess_result = easygui.buttonbox(title="继续游戏",msg="你还继续游戏吗？你还有"+str(5-int(i))+"次机会",choices=["继续猜数","退出"])
        elif i==5:
            easygui.msgbox(title="猜数游戏",msg="你6次机会用完了,电脑生成的关键数是："+str(key),ok_button="结束")

        
    elif key == int(user_guess):
        easygui.msgbox(title="猜数游戏",msg="你猜的数是"+user_guess+"恭喜你猜对了",ok_button="结束")
        break
    
    i += 1    