#使用while 循环写的猜数游戏


import random,easygui
key= random.randint(1,100)
tries = 0
user_guess = 0
easygui.msgbox(title="猜数游戏",msg="请输入一个1至100的数，你有6次机会")
while key != user_guess and tries < 6:
    user_guess = easygui.enterbox(title="猜数游戏",msg="请输入一个1至100的数，你还有"+str(6-int(tries))+"次机会",default="40")
    if not user_guess:
        break
    if int(user_guess) > key  :
        easygui.msgbox(title="猜数游戏",msg="你猜的数是"+user_guess+"猜大了",ok_button="继续")
        
    elif int(user_guess) < key:
        easygui.msgbox(title="猜数游戏",msg="你猜的数是"+user_guess+"猜小了",ok_button="继续")
        
    tries += 1

if  key == int(user_guess):
        easygui.msgbox(title="猜数游戏",msg="你猜的数是"+user_guess+"恭喜你猜对了",ok_button="结束")   
else:
    easygui.msgbox(title="猜数游戏",msg="6次机会已经用完了，你没有更多的机会啦!"+"电脑生成的关键数是："+str(key),ok_button="结束")    