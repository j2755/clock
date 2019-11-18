
   
import kivy   
  
from kivy.app import App  
       
  
kivy.require('1.9.0') 
   

from kivy.lang import Builder 

from kivy.properties import NumericProperty 
from kivy.properties import StringProperty
  
  
from kivy.uix.boxlayout import BoxLayout  
  
# he Clock object allows you to 

from kivy.clock import Clock 
import datetime as dt

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
