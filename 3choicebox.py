import easygui
best_love = easygui.choicebox(title="选择框",msg="请选择你喜欢的武器："
,choices= ['刀','🗡','🐲','戟','叉'])
easygui.msgbox(title="武器选择",msg="你选择了："+best_love,ok_button="离开")
