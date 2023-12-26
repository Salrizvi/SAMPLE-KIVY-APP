from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.metrics import dp
import ast
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from dotenv import load_dotenv
from supabase import create_client
from reportlab.pdfgen import canvas
from kivy.utils import platform
from kivymd.toast import toast

load_dotenv()
import os

# Load environment variables from .env file

# Access Superbase credentials
superbase_url = os.getenv('SUPERBASE_URL')
superbase_key = os.getenv('SUPERBASE_API_KEY')

# Create a Superbase client
superbase = create_client(superbase_url, superbase_key)

Window.size = (300, 500)
navigation_helper = """

Screen:
    ScreenManager:
        id: screen_manager
        LoginSc:
        Stud_data:
        Stud_Rept:
                                                         
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Danishgah Al-Najaf"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]                     
                        elevation:10
                    Widget:    
    
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                #https://raw.githubusercontent.com/HeaTTheatR/KivyMD-data/master/gallery/kivymddoc/md-label-font-style.gif
    
                AsyncImage:
                    source: 'https://jang.com.pk/assets/uploads/updates/2022-04-12/1073480_5538941_lhc-newww_updates.jpg'
    
                MDLabel:
                    text: '   Zafar Salman' 
                    font_Style: 'Subtitle1 '
                    size_hint_y: None
                    height: self.texture_size[1]
    
                MDLabel:
                    text: "   hi.salmanrizvi@gamil.com"
                    font_Style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Profile'
                            IconLeftWidget:
                                icon:'face-profile-woman'
                        OneLineIconListItem:
                            text:'Upload'
                            IconLeftWidget:
                                icon:'file-upload'
                        OneLineIconListItem:
                            text:'Logout'
                            IconLeftWidget:
                                icon:'logout'

<LoginSc>
    name:'LoginSc'
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(10)
        pos_hint: {'center_x': 0.5,'center_y': 0.9}
    
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(10)
                
            MDTextField:
                id: M_text_field1
                hint_text: 'User Name'
                helper_text:'Max Text Length 2'
                helper_text_mode: 'persistent'
                icon_left: 'school'
                pos_hint: {'center_x': 0.5,'center_y': 0.9}
                size_hint_x: None
                width :220
    
            MDTextField:
                id: M_text_field2
                hint_text: 'Password'
                helper_text:'Max Text Length 3'
                helper_text_mode: 'persistent'
                icon_left: 'book'
                pos_hint: {'center_x': 0.5,'center_y': 0.5}
                size_hint_x: None
                width :220
                
    BoxLayout:
        orientation: 'horizontal'
        spacing: dp(5)
        padding: dp(1)
        pos_hint: {'center_x': 0.7,'center_y': 0.7}
        
        MDRectangleFlatButton:
            text: 'Sign in'
            on_release: app.save_data()

        MDRectangleFlatButton:
            text: 'Sing up'
            on_release: root.manager.current ='Stud_data'
<Stud_data>
    name:'Stud_data'
    BoxLayout:
        orientation: 'vertical'
        pos_hint: {'center_x': 0.55,'center_y': 0.5}
        spacing: dp(5)
        padding: dp(1)       
        GridLayout:
            cols:2
            rows:10
            spacing: dp(0.2)

            Image:
                size: dp(15),dp(15)
                source: 'DNajaf.png'
                                                                                    
            MDLabel:
                text: "Danishgah Al-Najaf\\n Registration\\n Year-2024."
                font_style: 'H6'                                                         
                valign: 'bottom'
                halign: 'left'
                theme_text_color: 'Secondary'
              
            MDTextField:
                id: text_field1
                hint_text: 'Lavel'
                helper_text:'Max Text Length 2'
                helper_text_mode: 'persistent'
                icon_left: 'school'
                pos_hint: {'center_x': 0.37,'center_y': 0.7}
                size_hint_x: None
                width :120
    
            MDTextField:
                id: text_field2
                hint_text: 'RollNo.'
                helper_text:'Max Text Length 3'
                helper_text_mode: 'persistent'
                icon_left: 'book'
                pos_hint: {'center_x': 0.6,'center_y': 0.7}
                size_hint_x: None
                width :120
    
            GridLayout:
                cols: 1
                row_force_default: True
                row_default_height: dp(48)
                spacing: dp(.5)
            
                MDTextField:
                    id: text_field3
                    hint_text: "Student Name"
                    helper_text:'Max 25 Charector'
                    helper_text_mode: 'persistent'
                    icon_left: 'account'
                    pos_hint: {'center_x': 0.5,'center_y': 0.5}
                    size_hint_x: None
                    width :250
    
                MDTextField:
                    id: text_field4
                    hint_text: "Enter Father's Name"
                    helper_text:'Max 25 Charector'
                    helper_text_mode: 'persistent'
                    icon_left: 'account'
                    pos_hint: {'center_x': 0.5,'center_y': 0.5}
                    size_hint_x: None
                    width :250
    
                MDTextField:
                    id: text_field5
                    hint_text: 'Mobile No.'
                    helper_text:'XXXX XXXXXXX'
                    helper_text_mode: 'persistent'
                    icon_left: 'phone'
                    pos_hint: {'center_x': 0.37,'center_y': 0.7}
                    size_hint_x: None
                    width :250
    
                MDTextField:
                    id: text_field6
                    hint_text: 'Whatsup No.'
                    helper_text:'XXXX XXXXXXX'
                    helper_text_mode: 'persistent'
                    icon_left: 'phone'
                    pos_hint: {'center_x': 0.37,'center_y': 0.7}
                    size_hint_x: None
                    width :250
                
                    
                GridLayout:
                    cols:2
                    spacing: dp(10)
                    padding: dp(5)            
                    MDRaisedButton:
                        text: 'Save Data'
                        on_press: app.save_data()
            
                    MDRaisedButton:
                        text: 'Retrieve Data'  
                        on_press: app.retrieve_data()  

                    MDList:
                        id: data_list
                        size_hint_y: None
                        height: self.minimum_height
<Stud_Rept>
    name: 'Stud_Rept'
    BoxLayout:
        orientation: 'vertical'
        spacing: dp(30)
        ScrollView:
            do_scroll_x: True
            do_scroll_y: True
            GridLayout:
                cols: 1
                spacing: dp(10)
                padding: dp(30)
                size_hint_y: None
                height: self.minimum_height      
                MDList:
                    id: data_list  
        BoxLayout:
            orientation: 'horizontal'
            size_hint: (1, 0.1)
            spacing: dp(5)
            padding: dp(1)
            pos_hint: {'center_x': 0.7, 'center_y': 0.1}
            MDRectangleFlatButton:
                text: 'Back'
                on_release: root.manager.current = 'Stud_data'
            MDRectangleFlatButton:
                text: 'Print'
                on_release: app.print_data(app.retrieve_data())
"""

class LoginSc(Screen):
    pass

class Stud_data(Screen):
    pass

class Stud_Rept(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Stud_data(name = 'Stud_data'))
sm.add_widget(Stud_Rept(name = 'Stud_Rept'))

class DemoApplication(MDApp):
    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen
    def save_data(self):
        #table_name = 'School'
        stud_data_screen = self.root.ids.screen_manager.get_screen('Stud_data')
        data_to_insert = {
            "Lavel": stud_data_screen.ids.text_field1.text,
            "RollNo": stud_data_screen.ids.text_field2.text,
            "Student_Name": stud_data_screen.ids.text_field3.text,
            "Fathers_Name": stud_data_screen.ids.text_field4.text,
            "Mobile_No": stud_data_screen.ids.text_field5.text,
            "Whatsup_No": stud_data_screen.ids.text_field6.text,
        }

        try:
            data = superbase.table("School").insert([data_to_insert]).execute()
            print("Insertion successful. Response:", data)
        except Exception as e:
            print("Failed to insert data. Error:", str(e))
    
    Stud_tab_head = ''
    Stud_tab_row = ''
    def retrieve_data(self):
        try:
            # Fetch data from Supabase
            data = superbase.table("School").select("*").execute()
            response = str(data)
            final_response = response[5:-11]
            #print(final_response)

            list_string = ast.literal_eval(final_response)
            #print(list_string)

            stu_rept_screen = self.root.ids.screen_manager.get_screen('Stud_Rept')
            stu_rept_screen.ids.data_list.clear_widgets()

            keys = list_string[0].keys()
            max_widths = {key: max(len(str(key)), max(len(str(data_dict[key])) for data_dict in list_string)) for key in keys}

            header_row = " | ".join(f"{key:<{max_widths[key]}}" for key in keys)
            stu_rept_screen.ids.data_list.add_widget(MDLabel(text=header_row))

            for data_dict in list_string:
                row_values = " | ".join(f"{str(data_dict[key]):<{max_widths[key]}}" for key in keys)
                stu_rept_screen.ids.data_list.add_widget(MDLabel(text=row_values))

            self.root.ids.screen_manager.current = 'Stud_Rept'
        except Exception as e:
            print("Failed to retrieve data. Error:", str(e))

    def print_data(self, obj):
        pass

if __name__ == '__main__':
    DemoApplication().run()