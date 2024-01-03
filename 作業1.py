# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:00:33 2023

@author: USER
"""


from Role import Role,SwordsMan,Advisor,Dancer
import random


if __name__ == '__main__':
    
    player = list()
    com = list()
    S = 'SwordsMan'
    A = 'Advisor'
    D = 'Dancer'

    #我方陣營    
    for i in range(3):
        p = int(input('劍士按1，軍師按2，舞者按3：'))
        name = input('輸入角色姓名：')
        if p == 1:
            player.append(SwordsMan(name,120,80))
            
            
        elif p == 2:
            player.append(Advisor(name,100,140))
            
    
        else:
            player.append(Dancer(name,130,120))
            
        print(player[i].getName(),'加入我方陣營！')
    print()
        
        
    #敵方陣營          
    for i in range(3):
        c = random.randint(1, 3)
        name = ['關羽','曹操','趙雲','如來','佐助','阿凱','尤諾','諾艾兒']
        
        #random.choice(name)從串列中隨機抓取一個項目值
        if c == 1:
            com.append(SwordsMan(random.choice(name),120,80))
            print('劍士：',end='')
            
        elif c == 2:
            com.append(Advisor(random.choice(name),100,140))          
            print('軍師：',end='')
          
        else:
            com.append(Dancer(random.choice(name),130,120))
            print('舞者：',end='')
            
        print(com[i].getName(),'加入敵方陣營！')
    print()
    print('戰鬥開始！')
    print()
    RR = 0
            
    while len(player) > 0 and len(com) > 0:

        a = random.choice(player)               #兩陣營各選一個人
        b = random.choice(com)

        n = random.randint(1,100)               #n從1到100隨機取1個
        
        RR += 1
        print('第%d回合開始！'%RR)
        
        if n % 2 == 0:                          #n為偶數時我方攻擊
            print(a.getName(),'攻擊',b.getName())
            print(a.getName(),'使出：',end='')
            
            if a.getMp() <= 0:                  #如果mp小於0則只能使出普攻
                a.fight()
                blood = random.randint(8, 15)
                cost = 0
                
            else:                               #判斷是誰出招，因為各角色招式不同
                num = random.randint(1, 10)     
                blood = 0
                cost = 0
                heal = 0
                
                if a.roleName() == S:           #S為劍士出招 
                    if num % 4 == 0 and a.getMp() >= 20:           #低機率使出二技或三技
                        a.skill1()
                        blood = random.randint(18, 25)
                        cost = 20
                        
                    elif num % 7 == 0 and a.getMp() >= 50:
                        a.skill2()
                        blood = random.randint(40, 55)
                        cost = 50
                        
                    else:
                        a.fight()
                        blood = random.randint(8, 15)
                        cost = 0
                        
                elif a.roleName() == A:
                    if num % 4 == 0 and a.getMp() >= 30:           #低機率使出二技或三技
                        a.skill()
                        blood = random.randint(18, 25)
                        cost = 30
                        
                    elif num % 7 == 0 and a.getMp() >= 60:
                        a.smart()
                        blood = random.randint(55, 70)
                        cost = 60
                        
                    else:
                        a.fight()
                        blood = random.randint(8, 15)
                        cost = 0
                        
                elif a.roleName() == D:
                    if num % 4 == 0 and a.getMp() >= 30:           #低機率使出二技或三技
                        a.skill()
                        blood = random.randint(25, 35)
                        cost = 30
                        
                    elif num % 7 == 0 and a.getMp() >= 30:
                        a.healing()
                        blood = 0
                        cost = 30
                        heal = 30
                        team = random.choice(player)
                        team.setHp(team.getHp() + heal)
                        print(team.getName(),'受到了治療！')
                        
                    else:
                        a.fight()
                        blood = random.randint(8, 15)
                        cost = 0
                        
            b.setHp(b.getHp() - blood)                  #結算
            a.setMp(a.getMp() - cost)
            print(b.getName(),'的血量剩下：',b.getHp())
            print(a.getName(),'的魔力剩下：',a.getMp())
            print()
            
        else:                                   #n為奇數時對方攻擊
            print(b.getName(),'攻擊',a.getName())
            print(b.getName(),'使出：',end='')
            
            if b.getMp() <= 0:                  #如果mp小於0則只能使出普攻
                b.fight()
                blood = random.randint(8, 15)
                cost = 0
                
            else:                               #判斷是誰出招，因為各角色招式不同
                num = random.randint(1, 10)     
                blood = 0
                cost = 0
                heal = 0
                
                if b.roleName() == S:           #S為劍士出招 
                    if num % 4 == 0 and b.getMp() >= 20:           #低機率使出二技或三技
                        b.skill1()
                        blood = random.randint(18, 25)
                        cost = 20
                        
                    elif num % 7 == 0 and b.getMp() >= 50:
                        b.skill2()
                        blood = random.randint(40, 55)
                        cost = 50
                        
                    else:
                        b.fight()
                        blood = random.randint(8, 15)
                        cost = 0
                        
                elif b.roleName() == A:
                    if num % 4 == 0 and b.getMp() >= 30:           #低機率使出二技或三技
                        b.skill()
                        blood = random.randint(18, 25)
                        cost = 30
                        
                    elif num % 7 == 0 and b.getMp() >= 60:
                        b.smart()
                        blood = random.randint(55, 70)
                        cost = 60
                        
                    else:
                        b.fight()
                        blood = random.randint(8, 15)
                        cost = 0
                        
                elif b.roleName() == D:
                    if num % 4 == 0 and b.getMp() >= 30:           #低機率使出二技或三技
                        b.skill()
                        blood = random.randint(25, 35)
                        cost = 30
                        
                    elif num % 7 == 0 and b.getMp() >= 30:
                        b.healing()
                        blood = 0
                        cost = 30
                        heal = 30
                        team = random.choice(com)
                        team.setHp(team.getHp() + heal)
                        print(team.getName(),'受到了治療！')
                        
                    else:
                        b.fight()
                        blood = random.randint(8, 15)
                        cost = 0
                        
            a.setHp(a.getHp() - blood)
            b.setMp(b.getMp() - cost)
            print(a.getName(),'的血量剩下：',a.getHp())
            print(b.getName(),'的魔力剩下：',b.getMp())
            print()

        #判斷生命值是否皆大於0，否則移除
        obj1 = filter(lambda obj : obj.getHp() > 0,player)
        player = list(obj1)
        
        obj2 = filter(lambda obj : obj.getHp() > 0,com)
        com = list(obj2)

            
            
    if len(player) == 0:
        print('敵方勝利！')    

    else:
        print('我方勝利！')            
                    
                    
                






            

