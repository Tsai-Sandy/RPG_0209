def start():
    print("有一天你剛走出們，發現世界變得不一樣了\n")
    print("你發現你來到了異世界，外面充滿著奇怪的生物\n")
    print("你正思考著該如何回到正常世界時，忽然有個人朝你了跑過來\n")
    print("他說他回家的路上充滿著怪物，想請你沿途保護他回家\n")
    print("請選擇你要\"拒絕\"他還是\"答應\"他")
    while True:
        move = input("> ")
        if move == "拒絕":
            print("你走回廚房拿了一把菜刀丟給他，並說了一句:武器給你了，祝你好運\n")
            print("便關上門，回到臥室躺在床上想回去的方法，順便補個眠\n")
            print("沒多久後一隻一隻長得莫名其妙怪物沖破門跑了進來\n")
            print("你因沒有武器可以防身，而成為牠的點心\n")
            dead("被怪物吃掉")
        elif move == "答應":
            print("你進廚房拿了一把菜刀，當作武器\n")
            print("拿了砧板，當作盾牌\n")
            print("踏上了幫助路人回家的冒險之旅\n")
            adventure()
            break
        else:
            print("輸入錯誤，請重新輸入")

def adventure():
    print("沒想到走沒多久，你就遇到一隻巨大的暴龍\n")
    print("請選擇使用\"菜刀\"還是\"砧板\"")
    while True:
        move = input("> ")
        if move == "菜刀":
            print("你將菜刀刺向暴龍")
            print("因為暴龍的皮太厚，並未造成傷害\n")
            print("暴龍被激怒了，他生氣地朝你跑來\n")
            print("看起來短短、無殺傷力的手手，抓向你的頸部\n")
            knief()
            break
        elif move == "砧板":
            print("你情急之下將砧板往他頭上丟去\n")
            print("你非常精準的命中他的頭部\n")
            print("暴龍暈了過去\n")
            keep_going()
            break
        else:
            print("輸入錯誤，請重新輸入")

def knief():
    print("請選擇你要\"閃避\"還是\"不閃避\"")
    while True:
        move = input("> ")
        if move == "閃避\n":
            print("你躲過了這次攻擊\n")
            print("但緊接者它的尾巴在你不注意時甩到你身上\n")
            print("你被打飛後，頭部撞上石頭而死亡\n")
            dead("頭部重傷\n")
        elif move == "不閃避":
            print("你認定他揮不到，便不閃躲\n")
            print("但意想不到的你被抓到了頸動脈\n")
            print("你因無法止血，失血過多當場死亡\n")
            dead("失血過多")
        else:
            print("輸入錯誤，請重新輸入")

def keep_going():
    print("你們撿起砧板，趁機快速通過\n")
    print("想不到後來路上根本沒什麼危險\n")
    print("遇到的就是一堆可愛的小動物\n")
    print("就這樣到了那個人的家\n")
    print("他為了感謝你將一樣物品當禮物送了給你\n")
    print("請選擇你要\"接受\"還是\"婉拒\"")
    while True:
        move = input("> ")
        if move == "接受":
            print("接下東西的同時你發現這東西有一個按鈕\n")
            print("按下的同時，景物瞬間轉換\n")
            good("你回到原來的世界了")
        elif move == "婉拒":
            print("他態度非常強硬地要你收下\n")
            print("在推拉下你不知道撞到甚麼暈了過去\n")
            good("這純粹是一場夢")
        else:
            print("輸入錯誤，請重新輸入")
         
def good(event):
    print("你發現%s\n"%event)
    print("純屬無邏輯腦洞")
    quit()

def dead(why):
    print("你死於「%s」" % why)
    quit()

start()