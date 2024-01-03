# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 21:28:33 2023

@author: USER
"""
class Role:
    def __init__(self,name,hp,mp):
        self.__name = name
        self.__hp = hp
        self.__mp = mp
        
    def setHp(self,hp):
        self.__hp = hp

    def setMp(self,mp):
        self.__mp = mp
        
    def getName(self):
        return self.__name
    
    def getHp(self):
        return self.__hp
    
    def getMp(self):
        return self.__mp
    



class SwordsMan(Role):      
    
    def fight(self):
        print("劍士攻擊！")#扣對方8hp
        
    def skill1(self):
        print('三十六煩惱鳳！')#扣對方20hp&自身20mp
        
    def skill2(self):
        print('破山斬')#扣對方50hp&自身50mp
        
    def roleName(self):
        return 'SwordsMan'
    

class Advisor(Role):    
    
    def fight(self):
        print("嘴砲攻擊！")
        
    def skill(self):
        print('火龍陣之術！')#扣對方20hp&自身30mp
        
    def smart(self):
        print('招降之術！')#扣對方60hp&自身60mp
    
    def roleName(self):
         return 'Advisor'
   
    
class Dancer(Role):
    
    def fight(self):
        print("旋轉攻擊！")
        
    def skill(self):
        print('龍捲風攻擊！')#扣對方30hp&自身30mp

    def healing(self):
        print('治癒術！')#加隊友30hp&自身30mp
    
    def roleName(self):
         return 'Dancer'





















