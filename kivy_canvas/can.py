from ctypes.wintypes import SIZE
from curses.textpad import rectangle
import linecache
from tkinter import Y, Button, Widget
from turtle import color, width
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from tkinter import Canvas
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.properties import Clock
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.vertex_instructions import Ellipse
from kivy.metrics import dp
import random
import pygame
# Builder.load_file("canvas.kv")
class CanvasExample(Widget):
    pass
class CanvasExample1(Widget):
    pass
class CanvasExample2(Widget):
    pass
    x=100
    y=400
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            for i in range(0,100,2):
                Line(circle = (self.x,self.y,i),width=1)
            Line(points=(100,200,300,400),widtth=1)
            self.rect= Rectangle(pos=(600,200),size=(150,100))
            self.cic = Ellipse(pos=(500,200),size=(dp(50),(50)))
            
            
    def cb(self):
        x,y = self.rect.pos
        w,h=self.rect.size
        inc=10     
        dif =self.width-(x+w)
        
        if dif<inc:
            inc = dif
        x=x+dp(inc)  
       
        self.rect.pos=(x,y)
    def cirbutt(self):
        self.y+=50
    
class CanvasExample3(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.vx=dp(5)
        self.vy=dp(5)
        with self.canvas:
            self.ell=Ellipse(pos=(400,400),size=(dp(50),(50)))
            Clock.schedule_interval(self.update,1/60)
    def on_size(self,*args):
       
        
        print(self.width,self.height)        
        self.ell.pos=(self.width/2-25,self.height/2-25)       
    def update(self,dt):
        x,y=self.ell.pos
        x+=self.vx
        y+=self.vy
        self.ell.pos=(x,y)  
        if x+50>self.width:
            x=self.width
            self.vx=-5
        if y>self.height-50:
            y=self.height
            self.vy=-5
        if x<0:
            x=0
            self.vx=5
        if y<0:
            y=0
            self.vy=5     

          
             
        

"""
class WidgetExample(GridLayout):
    pass
class StackLayoutExample(StackLayout):
    pass
class GridLayoutExample(GridLayout):
    pass
class AnchorLayoutExample(AnchorLayout):
    pass
class BoxLayoutExample(BoxLayout):
    pass
class MainWidget(Widget):
    pass
"""
class canvas(App):
    pass
canvas().run()