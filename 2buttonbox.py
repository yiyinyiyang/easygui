import easygui
bestlove = easygui.buttonbox(title="我最爱的女友",msg="你最喜欢的女友是：",choices=["蛋疼","效力","玉蟾","李梅"])
type(bestlove)
easygui.msgbox(title="选择",msg="你的选择是:"+bestlove)