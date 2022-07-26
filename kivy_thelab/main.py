from ctypes.wintypes import SIZE
from tkinter import Button, Widget
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
import pygame
import random
class WidgetExample(GridLayout):
    count=1
    enable = BooleanProperty(True)
    my_text = StringProperty("hello")
    togg= StringProperty("OFF")
    def buttonclick(self):
        print("button clocked")
        self.my_text = str(self.count)
        self.count = self.count+1
    def toggles(self,widget):
        print("toggle stage "+ widget.state)
        if widget.state == "down":
            self.togg = "ON"
            self.enable = False
        else:
            self.togg = "OFF"  
            self.enable = True  
class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(60):
            b = Button(text=str(i+1), size_hint=(None,None),size=("100dp","100dp"))
            self.add_widget(b)
class GridLayoutExample(GridLayout):
    pass
class AnchorLayoutExample(AnchorLayout):
    pass
class BoxLayoutExample(BoxLayout):
    pass
"""   
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="A")
        b2 = Button(text="b")
        b3 = Button(text="c")
        self.orientation = "vertical"
        self.add_widget(b1)
        self.add_widget(b3)
        self.add_widget(b2)
"""        
class MainWidget(Widget):
    pass
class theLabApp(App):
    pass

theLabApp().run()