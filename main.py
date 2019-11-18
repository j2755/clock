''' 
Code of How to create Stopwatch 
'''
     
# Program to Show how to create a switch  
# import kivy module     
import kivy   
         
# base Class of your App inherits from the App class.     
# app:always refers to the instance of your application    
from kivy.app import App  
       
# this restrict the kivy version i.e   
# below this kivy version you cannot   
# use the app or software   
kivy.require('1.9.0') 
   
# The Builder is responsible for creating 
# a Parser for parsing a kv file 
from kivy.lang import Builder 
  
# The Properties classes are used 
# when you create an EventDispatcher. 
from kivy.properties import NumericProperty 
from kivy.properties import StringProperty
  
# BoxLayout arranges children in a vertical or horizontal box.  
# or help to put the children at the desired location.  
from kivy.uix.boxlayout import BoxLayout  
  
# he Clock object allows you to 
# schedule a function call in the future 
from kivy.clock import Clock 
import datetime as dt
  
# Create the .kv file and load it by using Builder 

   
# Create the Layout class 
class MainWidget(BoxLayout): 
    time_val=dt.datetime.now()
    
    time=StringProperty(time_val)


    number = NumericProperty() 
      
    def __init__(self, **kwargs): 
  
        
        super(MainWidget, self).__init__(**kwargs) 
  
        
        Clock.schedule_interval(self.update_time,.1)
  
       
  


    def update_time(self,ex):
        self.time=str(dt.datetime.now())

    def start(self): 
          
        Clock.unschedule(self.update_time) 
        Clock.schedule_interval(self.update_time,.1)
       
  

    def stop(self): 
        Clock.unschedule(self.update_time) 
  

class mainApp(App): 
    def build(self): 
        return MainWidget() 
  
 
mainApp().run() 