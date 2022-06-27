from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
from kivy.lang import Builder
from datetime import datetime
import json
import requests as r
username="""
MDTextField:
    hint_text:"Enter Command..."
    helper_text:'please enter some text'
    helper_text_mode:'persistent' 
    pos_hint:{'center_x':0.5,'center_y':0.5}
    size_hint_x:None
    width:300
    icon_right:'android'
    icon_right_color:[0,0,1,1]

"""
class First(MDApp):
    def build(self):
        s=Screen()
        self.theme_cls.primary_palette='Blue'
        self.theme_cls.theme_style='Dark'
        self.btn=MDRectangleFlatButton(text='Click',pos_hint={'center_x':0.5,'center_y':0.4},on_release =self.press)
        self.user_input=Builder.load_string(username)
       
        s.add_widget(self.user_input)
        s.add_widget(self.btn)
        return s

    def press(self,obj):
        url='https://python-55822-default-rtdb.firebaseio.com/.json'    

        text_input=self.user_input.text
        t=datetime.now().strftime('%I:%M:%S %p ')
        print(text_input)
        if text_input !="":
            toast("Message Successfully send !")
            json_data='{"input":"'+text_input+'","time":"'+t+'"}'
            data=r.patch(url,json=json.loads(json_data))

            self.user_input.text=''
          
        else:
            toast("Please Enter something...")

myapp=First()
myapp.run()