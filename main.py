from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.lang import Builder
# from plyer.facades.gyroscope import Gyroscope
import webbrowser
import re, uuid
import requests
import time
import json
from  kivy.uix.screenmanager import NoTransition 
# from kivy import platform
# from kivy.config import Config
# if platform == 'android':
    # Config.set('graphics', 'resizable', False)





# Window.size = (340, 750)
# Window.rotation=0
point="http://techwaveindustries.xyz/mane/"
# point="http://localhost/mane/"

class Woye(MDCard, CommonElevationBehavior):
    pass
class Curve(Label, CommonElevationBehavior):
    pass
class Content(BoxLayout):
    pass
# business="""
# OneLineAvatarListItem:
#     text: "My Business"
#     secondary_text:"portarit"
#     tertiary_text:"paor"
#     hint_text:"4"
#     on_release:app.my_business()
#     ImageLeftWidget:
#         source:"images/business.png"
# """
owner="""
OneLineAvatarListItem:
    text: "App manager"
    secondary_text:"portarit"
    tertiary_text:"paor"
    hint_text:"4"
    on_release:app.open_mane()
    ImageLeftWidget:
        source:"images/user.png"
"""
building="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"{users} users"
    tertiary_text:"{amount} ksh"
    hint_text:"{id}"
    on_release:app.open_building(self.hint_text,self.text)
    ImageLeftWidget:
        source:"images/bui.png"
"""
tenanta="""
ThreeLineAvatarListItem:
    text: "Room {name}"
    id:orientation
    secondary_text:"Rent {users} "
    tertiary_text:"{amount} | agreement"
    hint_text:"{id}"
    on_release:app.delete(self.hint_text)
    ImageLeftWidget:
        source:"images/tenant.png"
"""
units="""
ThreeLineAvatarListItem:
    text: "Unit {name}"
    id:orientation
    secondary_text:"Cost {users} Ksh "
    tertiary_text:"{amount} "
    hint_text:"{id}"
    on_release:app.unit_click(self.hint_text)
    ImageLeftWidget:
        source:"images/unit.png"
"""
paymental="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"Room {users} Ksh )"
    tertiary_text:"{amount} Ksh balance"
    hint_text:"{id}"
    on_release:app.unit_click(self.hint_text)
    ImageLeftWidget:
        source:"images/balance.png"
"""
pay_type="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"B/N {users} "
    tertiary_text:"Acc {amount}"
    hint_text:"{id}"
    on_release:app.unit_click(self.hint_text)
    ImageLeftWidget:
        source:"images/money.png"
"""
tenants_ava="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"Rent {users} "
    tertiary_text:"Agreement {amount}"
    hint_text:"{id}"
    on_release:app.pass_add(self.hint_text)
    ImageLeftWidget:
        source:"images/tenant.png"
"""
by_voice="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"BSN : {users} "
    tertiary_text:"{amount}"
    hint_text:"{id}"
    
    ImageLeftWidget:
        source:"{image}"
"""
profile="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"{users} "
    tertiary_text:"Joined {amount}"
    hint_text:"{id}"
    on_release:app.acc_doto_opt(self.hint_text)
    ImageLeftWidget:
        source:"images/profile.png"
"""
free="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"{users} "
    tertiary_text:"{amount}"
    hint_text:"{id}"
    on_release:app.acc_doto_opt(self.hint_text)
    ImageLeftWidget:
        source:"images/profile.png"
"""
nyumba="""
ThreeLineAvatarListItem:
    text: "Room {name}"
    id:orientation
    secondary_text:"{users} "
    tertiary_text:"{amount}"
    hint_text:"{id}"
    on_release:app.mini_detail(self.hint_text,1)
    ImageLeftWidget:
        source:"images/profile.png"
"""
jiji="""
ThreeLineAvatarListItem:
    text: "Unit {name}"
    id:orientation
    secondary_text:"{users} "
    tertiary_text:"{amount}"
    hint_text:"{id}"
    on_release:app.mini_detail(self.hint_text,2)
    ImageLeftWidget:
        source:"images/profile.png"
"""
locat="""
OneLineAvatarListItem:
    text: "{name}"
    hint_text:"{id}"
    on_release:app.update_location(self.text)
    ImageLeftWidget:
        source:"images/profile.png"
"""
invoicee="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"Amount due {users} "
    tertiary_text:"Due date{amount}"
    hint_text:"{id}"
    on_release:app.user_methods(self.hint_text)
    ImageLeftWidget:
        source:"images/profile.png"
"""
staff="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"Task : {users} "
    tertiary_text:"salary : {amount}"
    hint_text:"{id}"
    on_release:app.mini_detail(self.hint_text,2)
    ImageLeftWidget:
        source:"images/profile.png"
"""
staff_payments="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:" {users} "
    tertiary_text:" {amount}"
    hint_text:"{id}"
    on_release:app.mini_detail(self.hint_text,2)
    ImageLeftWidget:
        source:"images/profile.png"
"""
staff_for_pay="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"Amount :  {users} "
    tertiary_text:"Receipt : {amount}"
    hint_text:"{id}"
    on_release:app.payment_register(self.text)
    ImageLeftWidget:
        source:"images/profile.png"
"""
bars="""
ThreeLineAvatarListItem:
    text: "{name}"
    id:orientation
    secondary_text:"{users} "
    tertiary_text:"{amount}"
    hint_text:"{id}"
    on_release:app.mess_click(self.text,self.secondary_text,self.tertiary_text,self.hint_text)
    ImageLeftWidget:
        source:"images/profile.png"
"""
improv="""
MDList:
    OneLineAvatarListItem:
        text: "Units"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        on_release:app.view_unit()
        ImageLeftWidget:
            source:"images/unit.png"
    OneLineAvatarListItem:
        text: "Tenants"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        
        on_release:app.tenants_payments()
        
        ImageLeftWidget:
            source:"images/tenant.png"

    OneLineAvatarListItem:
        text: "Invoices"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        on_release:app.invoice_list()
        ImageLeftWidget:
            source:"images/invoice.png"
    OneLineAvatarListItem:
        text: "Add payment"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
    
        on_release:app.choose_customer()
        
        ImageLeftWidget:
            source:"images/deposit.png"
    OneLineAvatarListItem:
        text: "Payments data"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        on_release:app.money(1)
        
        ImageLeftWidget:
            source:"images/pay.png"
    OneLineAvatarListItem:
        text: "Payment options"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        on_release:app.payment_listing()
        ImageLeftWidget:
            source:"images/options.png"

    OneLineAvatarListItem:
        text: "Edit business"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        on_release:app.mulch("edit_business")
        
        ImageLeftWidget:
            source:"images/edit.png"
    OneLineAvatarListItem:
        text: "Delete business"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        on_release:app.mulch("delete_business")
        ImageLeftWidget:
            source:"images/delete.png"
"""
improv2="""
MDList:
    OneLineAvatarListItem:
        text: "Units"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        on_release:app.view_unit()
        ImageLeftWidget:
            source:"images/land.png"
    OneLineAvatarListItem:
        text: "Edit business"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        on_release:app.mulch("edit_business")
        ImageLeftWidget:
            source:"images/edit.png"
    OneLineAvatarListItem:
        text: "Delete business"
        secondary_text:"portarit"
        tertiary_text:"paor"
        hint_text:"4"
        on_release:app.mulch("delete_business")
        ImageLeftWidget:
            source:"images/delete.png"
        
"""
login_b="""
MDRaisedButton:
    text:"Continual"
    md_bg_color: (0/256, 201/256, 112/256, 1) 
    on_release:app.check_user()"""
login_m="""
Label:
    size_hint_x:0.06"""
# def porti():
# Orientation.set_portrait(reverse=False)

class MainApp(MDApp):
    # def porti(self):
    #     try:
        
    #         p=Gyroscope()
    #         p.disable()
    #     except IOError:
    #         pass
    #     else:
    #         pass

    height=""
    width=""
    poser=0.5
    zero="0"
    print("start of height_w-----------------------")
    print(height)
    print(width)
    print("end of height_w-----------------------")
    des=Window.size
    ridas=int(des[0])*10/350
    altura=int(des[0])*20/350
    lutspace=int(des[1])*20/750
    c1=int(des[1])*90/750
    csl=int(des[1])*540/750
    padding=int(des[0])*10/350
    dimex=Window.size
    high=dimex[1]*0.3814285714
    mdcardh=dimex[1]*0.6428571429
    spacingh=dimex[1]*0.01
    spaceop=dimex[0]*0.742857142
    spaceoph=str(dimex[1]*0.29333333)
    spacewidth=str(dimex[0]*1)
    xdim=dimex[0]*0.7
    ydim=dimex[1]*0.3
    hcomb=mdcardh+high
    global screen_manager
    #screen_manager = ScreenManager(transition=NoTransition())
    screen_manager = ScreenManager()
    def mulch(self,code):
        # screen_manager.current=code
        self.ai_builder(code,2)
    def build(self):
        self.title=""
        self.theme_cls.primary_palette='Blue'
        
        
       # screen_manager.add_widget(Builder.load_file("spage.kv"))
        return screen_manager
    def open_mane(self):
        # screen_manager.current="manager"
         self.ai_builder("manager",2)
    def backsies(self):
        # screen_manager.current="home"
         self.ai_builder("home",2)
    def login(self):
        self.ai_builder("login",2)
        try:
            if self.root.get_screen('login').ids.email.text!="" and self.root.get_screen('login').ids.passcode.text!="":
            
                macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
                passc=self.root.get_screen('login').ids.passcode.text
                email=self.root.get_screen('login').ids.email.text
                data1={"mac":macer,"pass":passc,"email":email}
                url=point+'log_in.php'
                r=requests.post(url,data=data1)
                rd=r.json()
                y=json.dumps(rd)
                z=json.loads(y)
                task=(z["sent"])
                namer=(z["name"])
                if task in ["1","2","3","4","5","6"]:
                    # screen_manager.current="home"
                    self.ai_builder("home",2)
                    self.root.get_screen('hide').ids.user_level.text="1"
                    self.root.get_screen('home').ids.code.title="Welcome "+namer
                    self.check_user
                
                else:
                    self.dialog = MDDialog(title="Insertions error",
                            text="Wrong password or email",
                            
                            )
                    self.dialog.open()
            else:
                self.dialog = MDDialog(title="Insertions missing",
                            text="Ensure that you have filled all the required data",
                            
                            )
                self.dialog.open()
        except IOError:
            self.connection_error()
        else:
            pass


    def confirm_code(self):
        self.ai_builder("view_help",1)
        try:
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            code=self.root.get_screen('confirm').ids.code.text
            if code !="":
                data1={"mac":macer,"cpde":code}
                url=point+'confirm.php'
                r=requests.post(url,data=data1)
                rd=r.json()
                y=json.dumps(rd)
                z=json.loads(y)
                task=(z["sent"])
                namer=(z["name"])
                print(task)
                if task=="5" or task=="1":
                    # screen_manager.current="home"
                    self.ai_builder("home",2)
                    self.root.get_screen('home').ids.code.title="Welcome "+namer 
                    print("1")
                    self.root.get_screen('hide').ids.user_level.text="1"
                
                elif task=="2":
                    
            
                    self.root.get_screen('home').ids.list.add_widget(conner)
                elif task=="3":
                    # screen_manager.current="home"
                    self.ai_builder("home",2)
                    print("1d")
                    self.root.get_screen('hide').ids.user_level.text="3"
                    conner=Builder.load_string(owner)
                    
                    self.root.get_screen('home').ids.list.add_widget(conner)
                elif task=="4":
                    # screen_manager.current="home"
                    self.ai_builder("home",2)
                    print("1ff")
                    conneer=Builder.load_string(owner)
                    self.root.get_screen('home').ids.list.add_widget(conneer)
            
            
                elif task=="0":
                    # screen_manager.current="login"
                    self.ai_builder("login",2)
                    self.dialog = MDDialog(title="Mismatch",
                            text="Your code was wrong, the code has been reset and sent",
                            
                            )
                    self.dialog.open()
            else:
                self.dialog = MDDialog(title="Empty textfield",
                            text="Your entry is empty, please enter a code",
                            
                            )
                self.dialog.open()

        except IOError:
            self.connection_error()
        else:
            pass
            

        
    def sign_up(self):
        
        try:
            if self.root.get_screen('signin').ids.name.text!="" and self.root.get_screen('signin').ids.email.text!="" and self.root.get_screen('signin').ids.phone.text !="" and self.root.get_screen('signin').ids.second.text !="" and self.root.get_screen('signin').ids.first.text !="":
                if self.root.get_screen('signin').ids.second.text == self.root.get_screen('signin').ids.first.text:
                    try:
                        
                        macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
                        passc=self.root.get_screen('signin').ids.second.text
                        name=self.root.get_screen('signin').ids.name.text
                        phone=self.root.get_screen('signin').ids.phone.text
                        email=self.root.get_screen('signin').ids.email.text
                        data1={"mac":macer,"pass":passc,"email":email,"phone":phone,"name":name}
                        url=point+'insert_user.php'
                        r=requests.post(url,data=data1)
                        rd=r.json()
                        y=json.dumps(rd)
                        z=json.loads(y)
                        task=(z["sent"])
                        if task=="1":
                            # screen_manager.current="confirm"
                            self.ai_builder("confirm",2)
                            #self.root.get_screen('home').ids.code.title="Welcome"
                            self.root.get_screen('hide').ids.user_level.text="1"
                        elif task=="0":
                            self.dialog = MDDialog(title="Account error",
                            text="Kindly use another email, an existing acc is using the email",
                            
                            )
                            self.dialog.open()
                    except IOError:
                        self.connection_error()
                    else:
                        pass


                else:
                    self.dialog = MDDialog(title="Mismatch",
                            text="Your password is different to your confirmation",
                            
                            )
                    self.dialog.open()
            else:
                self.dialog = MDDialog(title="Insertions missing",
                            text="Ensure that you have filled all the required data",
                            
                            )
                self.dialog.open()

        except IOError:
            pass
        else:
            pass
    def connection_error(self):
        # if self.root.get_screen('hide').ids.conn_error.text=="":
        self.dialog = MDDialog(title="Connection error",
                            text="An conection error occuured, kindly check your internet ",
                            
                            )
        self.dialog.open()
            # self.root.get_screen('hide').ids.conn_error.text="1"
        
    def check_user(self):
        try:
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            data1={"mac":macer}
            url=point+'check_user.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print("start of task-----------------------------")
            print(task)
            print("end of task-----------------------------")
            if task=="1":
                namer=(z["name"])
                county=(z["county"])
                subloc=(z["subloc"])
                email_data=(z["email_data"])
                self.root.get_screen('hide').ids.county.text=county
                self.root.get_screen('hide').ids.subloc.text=subloc
                self.root.get_screen('hide').ids.email_data.text=email_data
                print(county)
                print(subloc)
                print(email_data)
                
                
                # screen_manager.current="home"
                self.ai_builder("home",2)
                self.root.get_screen('home').ids.code.title="Welcome "+namer 
                print("1")
                self.root.get_screen('hide').ids.user_level.text="1"
            # elif task=="2":
            #     screen_manager.current="home"
            #     print("1c")
            #     self.root.get_screen('hide').ids.user_level.text="2"
            #     conner=Builder.load_string(business)
        
            #     self.root.get_screen('home').ids.list.add_widget(conner)
            elif task=="3":
                # screen_manager.current="home"
                self.ai_builder("home",2)
                print("1d")
                self.root.get_screen('hide').ids.user_level.text="3"
                conner=Builder.load_string(owner)
                
                self.root.get_screen('home').ids.list.add_widget(conner)
            elif task=="4":
                # screen_manager.current="home"
                self.ai_builder("home",2)
                print("1ff")
                self.root.get_screen('hide').ids.user_level.text="4"
                
                conneer=Builder.load_string(owner)
                self.root.get_screen('home').ids.list.add_widget(conneer)
            elif task=="5":
                # screen_manager.current="confirm"
                self.ai_builder("confirm",2)
                print("1f")
                self.root.get_screen('hide').ids.user_level.text="5"
            elif task=="0":
                # screen_manager.current="login"
                self.ai_builder("login",2)
                #self.root.get_screen('hide').ids.user_level.text="5"
            else:
                # screen_manager.current="login"
                self.ai_builder("login",2)
            self.dimesions()
        except IOError:
            self.connection_error()
        else:
            pass
    def log_out(self):
        try:
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            data1={"mac":macer}
            url=point+'log_out.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            
            print(task)
            if task=="1":
                # screen_manager.current="login"
                self.ai_builder("login",2)
            if task=="0":
                self.dialog = MDDialog(title="Error",
                                text="Log out failed, try again later",
                                
                                )
                self.dialog.open()
                
        except IOError:
            self.connection_error()
        else:
            pass
    def add_unit(self):
        business_name=self.root.get_screen('hide').ids.current_building.text
        pictorials=self.root.get_screen('hide').ids.picture_id.text
        print(business_name)
        if self.root.get_screen('add_unit').ids.room.text!="" and self.root.get_screen('add_unit').ids.rent.text!="" and self.root.get_screen('add_unit').ids.type.text !="" and self.root.get_screen('add_unit').ids.word.text !="":
            try:
                
                macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
                room=self.root.get_screen('add_unit').ids.room.text
                
                rent=self.root.get_screen('add_unit').ids.rent.text
                type=self.root.get_screen('add_unit').ids.type.text
                word=self.root.get_screen('add_unit').ids.word.text
                business_name=self.root.get_screen('hide').ids.current_building.text
                print(business_name)
                loc1="nyandarua"
                loc2="nyahururu"
                kind=self.root.get_screen('hide').ids.business_type.text
                print("start of kind---------------------------------------")
                print(kind)
                print("end of kind---------------------------------------")
                data1={"mac":macer,"room":room,"word":word,"type":type,"rent":rent,"business_name":business_name,"loc1":loc1,"loc2":loc2,"id":pictorials,"kind":kind}
                url=point+'add_unit.php'
                r=requests.post(url,data=data1)
                rd=r.json()
                y=json.dumps(rd)
                z=json.loads(y)
                task=(z["sent"])
                if task=="1":
                    self.dialog = MDDialog(title="Success ",
                    text="Unit added successfully, you can continual to add more")
                    self.dialog.open()
                    self.root.get_screen('add_unit').ids.room.text=""
                    self.root.get_screen('add_unit').ids.rent.text=""
                    self.root.get_screen('add_unit').ids.type.text=""
                    self.root.get_screen('add_unit').ids.word.text=""
                    self.root.get_screen('hide').ids.picture_id.text=""
                elif task=="0":
                    self.dialog = MDDialog(title="failure",
                    text="The unit name exists",
                    
                    )
                    self.dialog.open()
                elif task=="3":
                    self.dialog = MDDialog(title="Pictures",
                    text="Kindly add the 4 pictures",
                    
                    )
                    self.dialog.open()
                else:
                    self.dialog = MDDialog(title="Adding failed",
                    text="Contact customer care if problem persists",
                    
                    )
                    self.dialog.open()
            except IOError:
                self.connection_error()
            else:
                pass


            
        else:
            self.dialog = MDDialog(title="Insertions missing",
                        text="Ensure that you have filled all the required data",
                        
                        )
            self.dialog.open()
    def my_business(self):
        try:
            # screen_manager.current="my_buildings"
            self.ai_builder("my_buildings",2)
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            data1={"mac":macer}
            url=point+'my_business.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            if task=="1":
                self.root.get_screen('my_buildings').ids.header.title="Select building or land"
                info=(z["data"])
                list=info.split("*")
                length=len(list)-1
                print(length)
                print("i am")
                self.root.get_screen('my_buildings').ids.data.clear_widgets()
                for d in range(length):
                    ins=list[d]
                    ins2=ins.split("|")
                    print(ins2)
                    print("i ins")
                    id=ins2[0]
                    jina=ins2[1]
                    users=ins2[2]
                    total=ins2[3]
                    image=ins2[4]
                    type=ins2[5]
                    alex11={'name': jina,'users':users,'amount': total,'image':image,'id':type}
                    alex12=building.format(**alex11)
                    conner=Builder.load_string(alex12)
                    
                    self.root.get_screen('my_buildings').ids.data.add_widget(conner)


            if task=="0":
                self.root.get_screen('my_buildings').ids.header.title="Zero building or land available"
                self.root.get_screen('my_buildings').ids.data.clear_widgets()
                
                #screen_manager.current="my_buildings"
                self.ai_builder("my_buildings",2)
                
                
        except IOError:
            self.connection_error()
        else:
            pass

    def add_business(self,kind):
        
        if self.root.get_screen('add_building').ids.phone.text!="" and self.root.get_screen('add_building').ids.name.text!="" and self.root.get_screen('add_building').ids.link.text!="" and self.root.get_screen('add_building').ids.word.text !="":
            try:
                
                macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
                link=self.root.get_screen('add_building').ids.link.text
                
                name=self.root.get_screen('add_building').ids.name.text
                word=self.root.get_screen('add_building').ids.word.text
                phone=self.root.get_screen('add_building').ids.phone.text
                data1={"mac":macer,"link":link,"word":word,"name":name,"phone":phone,"kind":kind}
                url=point+'create_building.php'
                r=requests.post(url,data=data1)
                rd=r.json()
                y=json.dumps(rd)
                z=json.loads(y)
                task=(z["sent"])
                if task=="1":
                    self.dialog = MDDialog(title="Success",
                    text="Business added successfully")
                    self.dialog.open()
                    time.sleep(2)
                    self.my_business()
                    # screen_manager.current="my_buildings"
                    self.ai_builder("my_buildings",2)
                    
                elif task=="0":
                    self.dialog = MDDialog(title="Adding failed",
                    text="The business name is curently being used",
                    
                    )
                    self.dialog.open()
            except IOError:
                self.connection_error()
            else:
                pass


            
        else:
            self.dialog = MDDialog(title="Insertions missing",
                        text="Ensure that you have filled all the required data",
                        
                        )
            self.dialog.open()
    def delete(self,room):
        self.dialog = MDDialog(title="Delete confirmation",
                        text="confirm you would like to delete the user ?",
                        buttons=(MDRaisedButton(text='Back', on_release=self.close_dialog)
                                        ,MDRaisedButton(text='Approve',md_bg_color=(0/256,176/256,144/256,1), on_release=lambda x:self.approved(room)))
                                        )
                        
                        
        self.dialog.open()
    def close_dialog(self,obj):
        self.dialog.dismiss()
    def approved(self,room):
        
        try:
            print(room)
            # screen_manager.current="tenants"
            self.ai_builder("tenants",2)
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            business_name=self.root.get_screen('hide').ids.current_building.text
            print(business_name)
            data1={"mac":macer,"business_name":business_name,"room":room}
            url=point+'deletet.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print(task)
            if task=="1":
                self.dialog = MDDialog(title="Information",
                text="the tenant was deleted")
                self.dialog.open()
                self.tenants_payments()
                self.close_dialog
            if task=="0":
                self.dialog = MDDialog(title="Failed",
                text="the tenant was not deleted")
                self.dialog.open()
                
                
                
        except IOError:
            self.connection_error()
        else:
            pass
    def tenants_payments(self):
        try:
            # screen_manager.current="tenants"
            self.ai_builder("tenants",2)
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            business_name=self.root.get_screen('hide').ids.current_building.text
            print(business_name)
            data1={"mac":macer,"business_name":business_name}
            url=point+'tenants.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print(task)
            if task=="1":
                #self.root.get_screen('my_buildings').ids.header.title="Select building or land"
                info=(z["data"])
                list=info.split("*")
                length=len(list)-1
                print(length)
                print("i am")
                self.root.get_screen('tenants').ids.data.clear_widgets()
                for d in range(length):
                    ins=list[d]
                    ins2=ins.split("|")
                    print(ins2)
                    print("i ins")
                    id=ins2[0]
                    jina=ins2[1]
                    email=ins2[2]
                    word=ins2[3]
                    image=ins2[4]
                    alex11={'name': jina,'users':email,'amount': word,'image':image,'id':id}
                    alex12=tenanta.format(**alex11)
                    conner=Builder.load_string(alex12)
                    self.root.get_screen('tenants').ids.header.title="View tenants"
                    self.root.get_screen('tenants').ids.data.add_widget(conner)


            if task=="0":
                self.root.get_screen('tenants').ids.header.title="There are no tenants available"
                self.root.get_screen('tenants').ids.data.clear_widgets()
                
                #screen_manager.current="my_buildings"
                
                
        except IOError:
            self.connection_error()
        else:
            pass
    def open_building(self,pointer,pointer2):
        type=self.root.get_screen('hide').ids.business_type.text
        if pointer=="1":
            # screen_manager.current="building_tools"
            self.ai_builder("building_tools",2)
            lsan=Builder.load_string(improv)
            self.root.get_screen('building_tools').ids.improv.clear_widgets()
            self.root.get_screen('building_tools').ids.improv.add_widget(lsan)
            self.root.get_screen('hide').ids.current_building.text=pointer2
            self.root.get_screen('hide').ids.business_type.text=pointer
           # self.root.get_screen('hide').ids.business_phone.text
        if pointer=="2":
            # screen_manager.current="building_tools"
            self.ai_builder("building_tools",2)
            lsan=Builder.load_string(improv2)
            self.root.get_screen('building_tools').ids.improv.clear_widgets()
            self.root.get_screen('building_tools').ids.improv.add_widget(lsan)
            self.root.get_screen('hide').ids.current_building.text=pointer2
            self.root.get_screen('hide').ids.business_type.text=pointer
    def add_tenant(self):
        if self.root.get_screen('add_tenants').ids.tenant.text!="" and self.root.get_screen('add_tenants').ids.email.text!="" and self.root.get_screen('add_tenants').ids.room.text !="" and self.root.get_screen('add_tenants').ids.agreement.text !="":
            try:
                
                macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
                tenant=self.root.get_screen('add_tenants').ids.tenant.text
                email=self.root.get_screen('add_tenants').ids.email.text
                room=self.root.get_screen('add_tenants').ids.room.text
                agreement=self.root.get_screen('add_tenants').ids.agreement.text
                business_name=self.root.get_screen('hide').ids.current_building.text
                print("business_name")
                data1={"mac":macer,"name":tenant,"email":email,"room":room,"agreement":agreement,"business_name":business_name}
                url=point+'add_tenant.php'
                r=requests.post(url,data=data1)
                rd=r.json()
                y=json.dumps(rd)
                z=json.loads(y)
                task=(z["sent"])
                if task=="1" or task=="0":
                    if task=="0":
                        self.dialog = MDDialog(title="Information",
                        text="the tenant exists in more than 2 rooms")
                        self.dialog.open()
                    self.dialog = MDDialog(title="Success",
                    text="tenant added successfully, you can continual to add more")
                    self.dialog.open()
                    self.root.get_screen('add_tenants').ids.email.text=""
                    self.root.get_screen('add_tenants').ids.tenant.text=""
                    self.root.get_screen('add_tenants').ids.room.text=""
                    self.root.get_screen('add_tenants').ids.agreement.text=""
                    
                elif task=="3":
                    self.dialog = MDDialog(title="Adding failed",
                    text="Check the room number for spelling errors, if error persists indly contct customer care",
                    
                    )
                    self.dialog.open()
            except IOError:
                self.connection_error()
            else:
                pass


            
        else:
            self.dialog = MDDialog(title="Insertions missing",
                        text="Ensure that you have filled all the required data",
                        
                        )
            self.dialog.open()
    def view_unit(self):
        self.dimesions()
        try:
            # screen_manager.current="units"
            self.ai_builder("units",2)
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            business_name=self.root.get_screen('hide').ids.current_building.text
            data1={"mac":macer,"business_name":business_name}
            url=point+'view_units.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            if task=="1":
                self.root.get_screen('units').ids.header.title="Units (scroll the image <-->)"
                info=(z["data"])
                self.root.get_screen('hide').ids.unit_data.text=info
                list=info.split("*")
                length=len(list)-1
                print(length)
                print("i am")
                self.root.get_screen('units').ids.data.clear_widgets()
                for d in range(length):
                    ins=list[d]
                    ins2=ins.split("|")
                    print(ins2)
                    print("i ins")
                    id=ins2[0]
                    room=ins2[1]
                    rent=ins2[2]
                    keywords=ins2[3]
                    pic1=ins2[4]
                    pic2=ins2[5]
                    pic3=ins2[6]
                    alex11={'name': room,'users':rent,'amount':keywords,'image':pic1,'id':id}
                    alex12=units.format(**alex11)
                    conner=Builder.load_string(alex12)
                    
                    self.root.get_screen('units').ids.data.add_widget(conner)


            if task=="0":
                self.root.get_screen('units').ids.header.title="Zero units available"
                self.root.get_screen('units').ids.data.clear_widgets()
                
                #screen_manager.current="my_buildings"
                
                
        except IOError:
            self.connection_error()
        else:
            pass
    def unit_click(self,loc):
        info=self.root.get_screen('hide').ids.unit_data.text
        self.root.get_screen('hide').ids.unit_loc.text=loc
        list=info.split("*")
        length=len(list)-1
        print(length)
        print("i am")
        #self.root.get_screen('units').ids.data.clear_widgets()
        for d in range(length):
            ins=list[d]
            ins2=ins.split("|")
            print(ins2)
            print("i ins")
            id=ins2[0]
            if id==loc:
            
                pic1=ins2[4]
                pic2=ins2[5]
                pic3=ins2[6]
                self.root.get_screen('units').ids.p1.source=pic1
                self.root.get_screen('units').ids.p2.source=pic2
                self.root.get_screen('units').ids.p3.source=pic3

    def money(self,kind):
        try:
            self.root.get_screen('payments').ids.data.clear_widgets()
            # screen_manager.current="payments"
            self.ai_builder("payments",2)
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            business_name=self.root.get_screen('hide').ids.current_building.text
            data1={"mac":macer,"business_name":business_name,"kind":kind}
            url=point+'view_payments.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            if task=="1":
                self.root.get_screen('payments').ids.header.title="View payments"
                info=(z["data"])
                list=info.split("*")
                length=len(list)-1
                print(length)
                print("i am")
                self.root.get_screen('payments').ids.data.clear_widgets()
                for d in range(length):
                    ins=list[d]
                    ins2=ins.split("|")
                    print(ins2)
                    print("i ins")
                    id=ins2[0]
                    name=ins2[1]
                    room=ins2[2]
                    due=ins2[3]
                    pic=ins2[4]
                    alex11={'name': name,'users':room,'amount':due,'image':pic,'id':id}
                    alex12=paymental.format(**alex11)
                    conner=Builder.load_string(alex12)
                    
                    self.root.get_screen('payments').ids.data.add_widget(conner)


            if task=="0":
                self.root.get_screen('payments').ids.header.title="Zero payments available"
                self.root.get_screen('payments').ids.data.clear_widgets()
                
                #screen_manager.current="my_buildings"
                self.ai_builder("my_buildings",2)
                
        except IOError:
            self.connection_error()
        else:
            pass
    def money_options(self):
        self.dialog = MDDialog(title="View More",
                        text="What payments would you like to view",
                        buttons=(MDRaisedButton(text='Due', on_release=lambda x:self.money(1))
                                        ,MDRaisedButton(text='Paid',md_bg_color=(0/256,176/256,144/256,1), on_release=lambda x:self.money(2)),MDRaisedButton(text='Invoice', on_release=lambda x:self.send_invoice()))
                                        )
                        
                        
        self.dialog.open()
    def destination(self):
        self.dialog = MDDialog(title="Invoice destination",
                        text="Which users would you like to receive your invoice",
                        buttons=(MDRaisedButton(text='Due', on_release=lambda x:self.dispach(1))
                                        ,MDRaisedButton(text='All',md_bg_color=(0/256,176/256,144/256,1), on_release=lambda x:self.dispach(2)),MDRaisedButton(text='Email', on_release=lambda x:self.dispach(1)))
                                        )       
        self.dialog.open()
    def send_invoice(self):
        # screen_manager.current="invoice"
        self.ai_builder("invoice",2)
        self.dialog.dismiss()
    def invoice_list(self):
        try:
            # screen_manager.current="invoice_list"
            self.ai_builder("invoice_list",2)
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            business_name=self.root.get_screen('hide').ids.current_building.text
            
            data1={"mac":macer,"business_name":business_name}
            url=point+'view_invoice.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print("quota")
            print(task)
            if task=="1":
                self.root.get_screen('invoice_list').ids.header.title="View invoices sent"
                info=(z["data"])
                list=info.split("*")
                length=len(list)-1
                print(length)
                print("i am")
                self.root.get_screen('invoice_list').ids.data.clear_widgets()
                for d in range(length):
                    ins=list[d]
                    ins2=ins.split("|")
                    print(ins2)
                    print("i ins")
                    id=ins2[0]
                    service=ins2[1]
                    keywords=ins2[2]
                    amount=ins2[3]
                    pic=""
                    alex11={'name': service,'users':keywords,'amount':amount,'image':pic,'id':id}
                    alex12=by_voice.format(**alex11)
                    conner=Builder.load_string(alex12)
                    
                    self.root.get_screen('invoice_list').ids.data.add_widget(conner)


            if task=="0":
                print(task)
                self.root.get_screen('invoice_list').ids.header.title="Zero invoices available"
                self.root.get_screen('invoice_list').ids.data.clear_widgets()
                
                #screen_manager.current="my_buildings"
                
                
        except IOError:
            self.connection_error()
        else:
            pass
    def dispach(self,destination):
        self.dialog.dismiss()
        if self.root.get_screen('invoice').ids.service.text!="" and self.root.get_screen('invoice').ids.amount.text!="" and self.root.get_screen('invoice').ids.due_date.text!="" :
            try:
                
                macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
                email=self.root.get_screen('invoice').ids.email.text
                service=self.root.get_screen('invoice').ids.service.text
                amount=self.root.get_screen('invoice').ids.amount.text
                due=self.root.get_screen('invoice').ids.due_date.text
                business_name=self.root.get_screen('hide').ids.current_building.text
                data1={"mac":macer,"email":email,"amount":amount,"service":service,"key_giver":business_name,"due":due,"destination":destination}
                url=point+'send_invoice.php'
                r=requests.post(url,data=data1)
                rd=r.json()
                y=json.dumps(rd)
                z=json.loads(y)
                task=(z["sent"])
                if task=="1":
                    
                    self.dialog = MDDialog(title="Success",
                    text="Invoice sent successfully")
                    self.dialog.open()
                    self.root.get_screen('invoice').ids.email.text=""
                    self.root.get_screen('invoice').ids.service.text=""
                    self.root.get_screen('invoice').ids.amount.text=""
                    self.root.get_screen('invoice').ids.due_date.text=""
                    # screen_manager.current="building_tools"
                elif task=="0":
                    self.dialog = MDDialog(title="Sending failed",
                    text="Sending failed , if error persists kindly contact customer care",
                    
                    )    
                    self.dialog.open()
            except IOError:
                self.connection_error()
            else:
                pass


            
        else:
            self.dialog = MDDialog(title="Insertions missing",
                        text="Ensure that you have filled all the required data",
                        
                        )
            self.dialog.open()
    
    def delete_business(self):
        if self.root.get_screen('delete_business').ids.mail.text!="" and self.root.get_screen('delete_business').ids.password.text!="" :
            try:
                
                macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            
                passd=self.root.get_screen('delete_business').ids.password.text
                email=self.root.get_screen('delete_business').ids.mail.text
                business_name=self.root.get_screen('hide').ids.current_building.text
                data1={"mac":macer,"pass":passd,"email":email,"business_name":business_name}
                url=point+'delete_building.php'
                r=requests.post(url,data=data1)
                rd=r.json()
                y=json.dumps(rd)
                z=json.loads(y)
                task=(z["sent"])
                if task=="1":
                    
                    self.dialog = MDDialog(title="Success",
                    text="building deleted successfully")
                    self.dialog.open()
                    self.root.get_screen('delete_business').ids.mail.text=""
                    self.root.get_screen('delete_business').ids.password.text=""
                    # screen_manager.current="my_buildings"
                    self.ai_builder("my_buildings",2)
                    self.my_business()
                elif task=="0":
                    self.dialog = MDDialog(title="Deleting failed",
                    text="deletion failed , if error persists indly contact customer care",
                    
                    )    
                    self.dialog.open()
                    
                elif task=="3":
                    self.dialog = MDDialog(title="Authentication Failure",
                    text="deletion failed , if error persists indly contct customer care",
                    
                    )
                    self.dialog.open()
            except IOError:
                self.connection_error()
            else:
                pass


            
        else:
            self.dialog = MDDialog(title="Insertions missing",
                        text="Ensure that you have filled all the required data",
                        
                        )
            self.dialog.open()
    def edit_business(self):
        if self.root.get_screen('edit_business').ids.phone.text!="" and self.root.get_screen('edit_business').ids.link.text!="" and self.root.get_screen('edit_business').ids.word.text !="":
            try:
                
                macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
                link=self.root.get_screen('edit_business').ids.link.text
                word=self.root.get_screen('edit_business').ids.word.text
                phone=self.root.get_screen('edit_business').ids.phone.text
                business_name=self.root.get_screen('hide').ids.current_building.text
                data1={"mac":macer,"link":link,"word":word,"name":business_name,"phone":phone}
                url=point+'edit_business.php'
                r=requests.post(url,data=data1)
                rd=r.json()
                y=json.dumps(rd)
                z=json.loads(y)
                task=(z["sent"])
                if task=="1":
                    self.dialog = MDDialog(title="Success",
                    text="Business edited successfully")
                    self.dialog.open()
                    time.sleep(2)
                    self.my_business()
                    # screen_manager.current="my_buildings"
                    self.ai_builder("my_buildings",2)
                elif task=="0":
                    self.dialog = MDDialog(title="Editing failed",
                    text="The editing failed",
                    
                    )
                    self.dialog.open()
            except IOError:
                self.connection_error()
            else:
                pass


            
        else:
            self.dialog = MDDialog(title="Insertions missing",
                        text="Ensure that you have filled all the required data",
                        
                        )
            self.dialog.open()
    def add_payment(self):
        if self.root.get_screen('payment_detail').ids.kind.text!="" and self.root.get_screen('payment_detail').ids.bsn.text!="" and self.root.get_screen('payment_detail').ids.acc.text!="" and self.root.get_screen('payment_detail').ids.keyword.text!="" :
            try:
                 
                macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
                kind=self.root.get_screen('payment_detail').ids.kind.text
                bsn=self.root.get_screen('payment_detail').ids.bsn.text
                acc=self.root.get_screen('payment_detail').ids.acc.text
                keyword=self.root.get_screen('payment_detail').ids.keyword.text
                business_name=self.root.get_screen('hide').ids.current_building.text
                data1={"mac":macer,"kind":kind,"bsn":bsn,"acc":acc,"business_name":business_name,"keyword":keyword}
                url=point+'payment_detail.php'
                r=requests.post(url,data=data1)
                rd=r.json()
                y=json.dumps(rd)
                z=json.loads(y)
                task=(z["sent"])
                if task=="1":
                    
                    self.dialog = MDDialog(title="Success",
                    text="Payment method added successfully")
                    self.dialog.open()
                    self.root.get_screen('payment_detail').ids.kind.text=""
                    self.root.get_screen('payment_detail').ids.bsn.text=""
                    self.root.get_screen('payment_detail').ids.acc.text=""
                    self.root.get_screen('payment_detail').ids.keyword.text=""
                    self.payment_listing()
                    # screen_manager.current="payments_options"
                    self.ai_builder("payments_options",2)
                elif task=="0":
                    self.dialog = MDDialog(title="Adding failed",
                    text="The addition failed",
                    
                    )    
                    self.dialog.open()
            except IOError:
                self.connection_error()
            else:
                pass


            
        else:
            self.dialog = MDDialog(title="Insertions missing",
                        text="Ensure that you have filled all the required data",
                        
                        )
            self.dialog.open()
    def payment_listing(self):
        print("sasa")
        try:
            # screen_manager.current="payments_options"
            self.ai_builder("payments_options",2)
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            business_name=self.root.get_screen('hide').ids.current_building.text
            
            data1={"mac":macer,"business_name":business_name}
            url=point+'payment_listing.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print("quota")
            print(task)
            if task=="1":
                self.root.get_screen('payments_options').ids.header.title="View payments options"
                info=(z["data"])
                list=info.split("*")
                length=len(list)-1
                print(length)
                print("i am")
                self.root.get_screen('payments_options').ids.data.clear_widgets()
                for d in range(length):
                    ins=list[d]
                    ins2=ins.split("|")
                    print(ins2)
                    print("i ins")
                    id=ins2[0]
                    kind=ins2[1]
                    business_no=ins2[2]
                    acc=ins2[3]
                    keywords=ins2[4]
                    pic=""
                    alex11={'name': kind,'users':business_no,'amount':acc,'image':pic,'id':id}
                    alex12=pay_type.format(**alex11)
                    conner=Builder.load_string(alex12)
                    
                    self.root.get_screen('payments_options').ids.data.add_widget(conner)


            if task=="0":
                print(task)
                self.root.get_screen('payments_options').ids.header.title="Zero payments available"
                self.root.get_screen('payments_options').ids.data.clear_widgets()
                
                #screen_manager.current="my_buildings"
                
                
        except IOError:
            self.connection_error()
        else:
            pass 
    def choose_customer(self):
        try:
            self.root.get_screen('choose_customer').ids.data.clear_widgets()
            # screen_manager.current="choose_customer"
            self.ai_builder("choose_customer",2)
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            business_name=self.root.get_screen('hide').ids.current_building.text
            print(business_name)
            data1={"mac":macer,"business_name":business_name}
            url=point+'tenants.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print(task)
            if task=="1":
                #self.root.get_screen('my_buildings').ids.header.title="Select building or land"
                info=(z["data"])
                list=info.split("*")
                length=len(list)-1
                print(length)
                print("i am")
                self.root.get_screen('tenants').ids.data.clear_widgets()
                for d in range(length):
                    ins=list[d]
                    ins2=ins.split("|")
                    print(ins2)
                    print("i ins")
                    id=ins2[0]
                    jina=ins2[1]
                    email=ins2[2]
                    word=ins2[3]
                    image=ins2[4]
                    alex11={'name': jina,'users':email,'amount': word,'image':image,'id':id}
                    alex12=tenants_ava.format(**alex11)
                    conner=Builder.load_string(alex12)
                    self.root.get_screen('choose_customer').ids.header.title="Choose tenant to add payment"
                    self.root.get_screen('choose_customer').ids.data.add_widget(conner)


            if task=="0":
                self.root.get_screen('choose_customer').ids.header.title="There are no tenants available"
                self.root.get_screen('choose_customer').ids.data.clear_widgets()
                
                #screen_manager.current="my_buildings"
                
                
        except IOError:
            self.connection_error()
        else:
            pass
    def pass_add(self,point):
        self.root.get_screen('hide').ids.payment_tents.text=point
        
        # screen_manager.current="add_payment_manual"
        self.ai_builder("add_payment_manual",2)
    def insert_payment(self):
        if self.root.get_screen('add_payment_manual').ids.kind.text!="" and self.root.get_screen('add_payment_manual').ids.method.text!="" and self.root.get_screen('add_payment_manual').ids.receipt.text!="" and self.root.get_screen('add_payment_manual').ids.other.text!="" :
            try:
                
                macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
                kind=self.root.get_screen('add_payment_manual').ids.kind.text
                method=self.root.get_screen('add_payment_manual').ids.method.text
                receipt=self.root.get_screen('add_payment_manual').ids.receipt.text
                other=self.root.get_screen('add_payment_manual').ids.other.text
                business_name=self.root.get_screen('hide').ids.current_building.text
                id=self.root.get_screen('hide').ids.payment_tents.text
                data1={"mac":macer,"sent":kind,"id":id,"method":method,"receipt":receipt,"other":other,"key_giver":business_name}
                print(data1)
                print(id)
                url=point+'insert_payment.php'
                r=requests.post(url,data=data1)
                rd=r.json()
                y=json.dumps(rd)
                z=json.loads(y)
                task=(z["sent"])
                if task=="1":
                    
                    self.dialog = MDDialog(title="Success",
                    text="Payment keyed successfully")
                    self.dialog.open()
                    self.root.get_screen('add_payment_manual').ids.kind.text=""
                    self.root.get_screen('add_payment_manual').ids.method.text=""
                    self.root.get_screen('add_payment_manual').ids.receipt.text=""
                    self.root.get_screen('add_payment_manual').ids.other.text=""
                    # screen_manager.current="building_tools"
                    self.ai_builder("building_tools",2)
                elif task=="0":
                    self.dialog = MDDialog(title="Keying failed",
                    text="Keying failed , if error persists kindly contact customer care",
                    
                    )    
                    self.dialog.open()
            except IOError:
                self.connection_error()
            else:
                pass


            
        else:
            self.dialog = MDDialog(title="Insertions missing",
                        text="Ensure that you have filled all the required data",
                        
                        )
            self.dialog.open()
    def choose_kind(self):
        self.dialog = MDDialog(title="View type of profile",
                        text="What profile would you like to view",
                        buttons=(MDRaisedButton(text='All', on_release=lambda x:self.view_profiles(1))
                                        ,MDRaisedButton(text='Buildings',md_bg_color=(0/256,176/256,144/256,1), on_release=lambda x:self.view_profiles(2)),MDRaisedButton(text='Land', on_release=lambda x:self.view_profiles(3)))
                                        )
                        
                        
        self.dialog.open()
    def view_profiles(self,kind):
       
        try:
            search=self.root.get_screen('profiles').ids.search.text
            self.ai_builder("search",1)
            self.root.get_screen('profiles').ids.data.clear_widgets()
            # screen_manager.current="profiles"
            self.ai_builder("profiles",2)
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            business_name=self.root.get_screen('hide').ids.current_building.text
            print(business_name)
            data1={"mac":macer,"kind":kind,"search":search}
            url=point+'view_profiles.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print(task)
            if task=="1":
                #self.root.get_screen('my_buildings').ids.header.title="Select building or land"
                info=(z["data"])
                list=info.split("*")
                length=len(list)-1
                print(length)
                print("i am")
                self.ai_builder("profiles",1)
                self.root.get_screen('profiles').ids.data.clear_widgets()
                for d in range(length):
                    ins=list[d]
                    ins2=ins.split("|")
                    print(ins2)
                    print("i ins")
                    id=ins2[0]
                    jina=ins2[1]
                    keywords=ins2[2]
                    kind=ins2[3]
                    reg_date=ins2[4]
                    #pic="image/bui.png"
                    if kind=="1":
                        pic="images/bui.png"
                        jina1=jina+" Buildings"
                        alex11={'name': jina1,'users':keywords,'amount': reg_date,'image':pic,'id':id}
                        alex12=profile.format(**alex11)
                        conner=Builder.load_string(alex12)
                        self.root.get_screen('profiles').ids.header.title="Choose tenant to add payment"
                        self.root.get_screen('profiles').ids.data.add_widget(conner)
                    if kind=="2":
                        pic="images/bui.png"
                        jina1=jina+" Lands"
                        alex11={'name': jina1,'users':keywords,'amount': reg_date,'image':pic,'id':id}
                        alex12=profile.format(**alex11)
                        conner=Builder.load_string(alex12)
                        self.root.get_screen('profiles').ids.header.title="Choose tenant to add payment"
                        self.root.get_screen('profiles').ids.data.add_widget(conner)


            if task=="0":
                self.ai_builder("profiles",1)
                self.root.get_screen('profiles').ids.header.title="There are no tenants available"
                self.root.get_screen('profiles').ids.data.clear_widgets()
                
                #screen_manager.current="my_buildings"
                
                
        except IOError:
            self.connection_error()
        else:
            pass
    def profile_affect(self,kind):
        self.dialog.dismiss()
        level=self.root.get_screen('hide').ids.business_id_r.text
        print("start of business edit id----------------------------")
        print(level)
        print("start of business edit id----------------------------")
        try:
            self.ai_builder("profiles",1)
            search=self.root.get_screen('profiles').ids.search.text
            self.root.get_screen('profiles').ids.data.clear_widgets()
            # screen_manager.current="profiles"
            self.ai_builder("profiles",2)
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            business_name=self.root.get_screen('hide').ids.current_building.text
            print(business_name)
            data1={"mac":macer,"position":level,"kind":kind}
            url=point+'edit_profile.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print(task)
            if task=="1":
                self.dialog.dismiss()
                self.dialog = MDDialog(title="Success",
                text="operation suspended successfully")
                self.dialog.open()
                self.view_profiles(1)
            if task=="2":
                self.dialog.dismiss()
                self.dialog = MDDialog(title="Success",
                text="Business deleted successfully")
                self.dialog.open()
                self.view_profiles(1)
            if task=="4":
                self.dialog.dismiss()
                self.dialog = MDDialog(title="Success",
                text="Business unsuspended successfully")
                self.dialog.open()
                self.view_profiles(1)
            if task=="0":
                self.dialog.dismiss()
                self.dialog = MDDialog(title="Failure",
                text="Operation failed")
                self.dialog.open()
                self.view_profiles(1)
                
                #screen_manager.current="my_buildings"
                
                
        except IOError:
            self.connection_error()
        else:
            pass
    def acc_doto_opt(self,level):
        self.root.get_screen('hide').ids.business_id_r.text=level
        self.dialog = MDDialog(title="Edit Acc",
                        text="What would you like to do to the acc",
                        buttons=(MDRaisedButton(text='View', on_release=lambda x:self.profile_affect(3))
                                        ,MDRaisedButton(text='Lock/Unlock',md_bg_color=(0/256,176/256,144/256,1), on_release=lambda x:self.profile_affect(1)),MDRaisedButton(text='Delete', on_release=lambda x:self.profile_affect(2)))
                                        )
        self.dialog.open()
    def profile_opt(self):
        #self.root.get_screen('hide').ids.business_id.text=level
        self.dialog = MDDialog(title="viewership",
                        text="What would you like to view",
                        buttons=(MDRaisedButton(text='All', on_release=lambda x:self.view_profiles(1))
                                        ,MDRaisedButton(text='Live',md_bg_color=(0/256,176/256,144/256,1), on_release=lambda x:self.view_profiles(2)),MDRaisedButton(text='Suspended', on_release=lambda x:self.view_profiles(3)))
                                        )
        self.dialog.open()
    def acc_doto(self,level):
        try:
                
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            
            id=self.root.get_screen('hide').ids.business_id.text
            data1={"mac":macer,"id":id,"meta":level}
            print(data1)
            print(id)
            url=point+'acc_doto.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            if task=="2":
                self.dialog.dismiss()
                self.dialog = MDDialog(title="Success",
                text="Business suspended successfully")
                self.dialog.open()
            if task=="3":
                self.dialog.dismiss()
                self.dialog = MDDialog(title="Success",
                text="Business deleted successfully")
                self.dialog.open()
            elif task=="0":
                self.dialog.dismiss()
                self.dialog = MDDialog(title="operation failed",
                text="If error persists kindly contact app developer",
                
                )    
                self.dialog.open()
        except IOError:
            self.connection_error()
        else:
            pass

    def house(self,kind):
        self.dimesions()
        self.root.get_screen('hide').ids.behind.text="1"
        try:
            # screen_manager.current="house"
            self.ai_builder("house",2)
            self.root.get_screen('hide').ids.detail_id.text=""
            gps1=self.root.get_screen('hide').ids.county.text
            gps2=self.root.get_screen('hide').ids.subloc.text
            print("my name is gps1")
            print(gps1)
            print("my name is gps2")
            print(gps1)
            self.ai_builder("search",1)
            search=self.root.get_screen('search').ids.word.text
            self.ai_builder("profiles",1)
            self.root.get_screen('profiles').ids.data.clear_widgets()
            #screen_manager.current="profiles"
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            phone=self.root.get_screen('hide').ids.business_phone.text
           
            data1={"mac":macer,"kind":kind,"search":search,"phone":phone}
            url=point+'house.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print(task)
            if task=="1":
                #self.root.get_screen('my_buildings').ids.header.title="Select building or land"
                info=(z["data"])
                list=info.split("*")
                length=len(list)-1
                print(length)
                print("i am")
                self.root.get_screen('house').ids.data.clear_widgets()
                for d in range(length):
                    ins=list[d]
                    ins2=ins.split("|")
                    print(ins2)
                    print("i ins")
                    id=ins2[0]
                    info=ins2[1]
                    jina=ins2[2]
                    phone=ins2[3]
                    loc1=ins2[4]
                    loc2=ins2[5]
                    pic=ins2[6]
                    p1=ins2[7]
                    p2=ins2[8]
                    p3=ins2[9]
                    #pic="image/bui.png"
                    print("------------------------")
                    print(gps1+" -- "+loc1)
                    print(gps2+" -- "+loc2)
                    print("------------------------")
                    loc_block=self.root.get_screen('hide').ids.loc_block.text
                    if loc_block=="1":
                        if loc1==gps1:
                            if loc2==gps2:
                                pic="images/bui.png"
                                pic_loc=point+"uploads/"
                                alex11={'name': info,'users':jina,'amount': phone,'image':pic,'id':id}
                                alex12=nyumba.format(**alex11)
                                conner=Builder.load_string(alex12)
                                print(pic_loc+p1)
                                print(pic_loc+p2)
                                print(pic_loc+p3)
                                self.root.get_screen('house').ids.header.title="View buildings"
                                self.root.get_screen('').ids.data.add_widget(conner)
                    else:
                        pic="images/bui.png"
                        pic_loc=point+"uploads/"
                        alex11={'name': info,'users':jina,'amount': phone,'image':pic,'id':id}
                        alex12=nyumba.format(**alex11)
                        conner=Builder.load_string(alex12)
                        print(pic_loc+p1)
                        print(pic_loc+p2)
                        print(pic_loc+p3)
                        self.root.get_screen('house').ids.header.title="View buildings"
                        self.root.get_screen('house').ids.data.add_widget(conner)
                    


            if task=="0":
                self.root.get_screen('house').ids.header.title="There is no  housing available"
                self.root.get_screen('house').ids.data.clear_widgets()
                
                #screen_manager.current="my_buildings"
            if kind=="4" and self.root.get_screen('search').ids.word.text=="":
                self.dialog = MDDialog(title="Insertion error",
                text="Please insert something to search",
                
                )    
                self.dialog.open()
                # screen_manager.current="search"
                self.ai_builder("search",2)
                
        except IOError:
            self.connection_error()
        else:
            pass
    def shamba(self,kind):
        self.ai_builder("shamba",1)
        self.dimesions()
        self.root.get_screen('hide').ids.behind.text="2"
        try:
            # screen_manager.current="shamba"
            self.ai_builder("shamba",2)
            gps1=self.root.get_screen('hide').ids.county.text
            gps2=self.root.get_screen('hide').ids.subloc.text
            self.ai_builder("search",1)
            search=self.root.get_screen('search').ids.word.text
            
            self.root.get_screen('shamba').ids.data.clear_widgets()
            # screen_manager.current="shamba"
            
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            phone=self.root.get_screen('hide').ids.business_phone.text
            
            data1={"mac":macer,"kind":kind,"search":search,"phone":phone}
            url=point+'house.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print(task)
            if task=="1":
                #self.root.get_screen('my_buildings').ids.header.title="Select building or land"
                info=(z["data"])
                list=info.split("*")
                length=len(list)-1
                print(length)
                print("i am")
                self.root.get_screen('shamba').ids.data.clear_widgets()
                for d in range(length):
                    ins=list[d]
                    ins2=ins.split("|")
                    print(ins2)
                    print("i ins")
                    id=ins2[0]
                    info=ins2[1]
                    jina=ins2[2]
                    phone=ins2[3]
                    loc1=ins2[4]
                    loc2=ins2[5]
                    pic=ins2[6]
                    p1=ins2[7]
                    p2=ins2[8]
                    p3=ins2[9]
                    #pic="image/bui.png"
                  
                    loc_block=self.root.get_screen('hide').ids.loc_block.text
                    if loc_block=="1":
                        if loc1==gps1:
                            if loc2==gps2:
                                pic="images/bui.png"
                                pic_loc=point+"uploads/"
                                alex11={'name': info,'users':jina,'amount': phone,'image':pic,'id':id}
                                alex12=jiji.format(**alex11)
                                conner=Builder.load_string(alex12)
                                print(pic_loc+p1)
                                print(pic_loc+p2)
                                print(pic_loc+p3)
                                self.root.get_screen('shamba').ids.header.title="View lands"
                                self.root.get_screen('shamba').ids.data.add_widget(conner)
                    else:
                        pic="images/bui.png"
                        pic_loc=point+"uploads/"
                        alex11={'name': info,'users':jina,'amount': phone,'image':pic,'id':id}
                        alex12=jiji.format(**alex11)
                        conner=Builder.load_string(alex12)
                        print(pic_loc+p1)
                        print(pic_loc+p2)
                        print(pic_loc+p3)
                        self.root.get_screen('shamba').ids.header.title="View lands"
                        self.root.get_screen('shamba').ids.data.add_widget(conner)

            if task=="0":
                self.root.get_screen('shamba').ids.header.title='"Zero results"'
                self.root.get_screen('shamba').ids.data.clear_widgets()
            if kind=="4" and self.root.get_screen('search').ids.word.text=="":
                self.dialog = MDDialog(title="Insertion error",
                text="Please insert something to search",
                
                )    
                self.dialog.open()
                # screen_manager.current="search"
                # self.ai_builder("search",2)
                
                
        except IOError:
            self.connection_error()
        else:
            pass

    def back_intiator(self,lodc):
        print("a")
        loc=self.root.get_screen('hide').ids.behind.text
        if loc=="1":
            # screen_manager.current="house"
            self.ai_builder("house",2)
            print("1")
        if loc=="2":
            # screen_manager.current="shamba"
            self.ai_builder("shamba",2)
    def refresh_data(self,kind):
        if kind=="1":
            self.house(2)
        if kind=="1":
            self.shamba(2)
    def mini_detail(self,code,primal):
        try:
           
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            data1={"mac":macer,"code":code}
            url=point+'detail.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print(task)
            if task=="1":
                #self.root.get_screen('my_buildings').ids.header.title="Select building or land"
                info=(z["data"])
                list=info.split("*")
                length=len(list)-1
                print(length)
                print("i am")
                for d in range(length):
                    ins=list[d]
                    ins2=ins.split("|")
                    print(ins2)
                    print("i ins")
                    id=ins2[0]
                    info=ins2[1]
                    jina=ins2[2]
                    phone=ins2[3]
                    loc1=ins2[4]
                    loc2=ins2[5]
                    pic=ins2[6]
                    p1=ins2[7]
                    p2=ins2[8]
                    p3=ins2[9]
                    ic=ins2[10]
                    rent=ins2[11]
                    #pic="image/bui.png"
                    if primal==1:
                        self.root.get_screen('house').ids.p1.source=point+"uploads/"+p1
                        self.root.get_screen('house').ids.p2.source=point+"uploads/"+p2
                        self.root.get_screen('house').ids.p3.source=point+"uploads/"+p3
                        self.root.get_screen('house').ids.p4.source=point+"uploads/"+pic
                        self.root.get_screen('hide').ids.detail_id.text=code
                    if primal==2:
                        self.root.get_screen('shamba').ids.p1.source=point+"uploads/"+p1
                        self.root.get_screen('shamba').ids.p2.source=point+"uploads/"+p2
                        self.root.get_screen('shamba').ids.p3.source=point+"uploads/"+p3
                        self.root.get_screen('shamba').ids.p4.source=point+"uploads/"+pic
                        self.root.get_screen('hide').ids.detail_id.text=code
                    
                
                #screen_manager.current="my_buildings"
                
                
        except IOError:
            self.connection_error()
        else:
            pass
       # screen_manager.current="detail"
    def to_det(self):
        ct=self.root.get_screen('hide').ids.detail_id.text
        if ct=="":
            #self.dialog.dismiss()
            self.dialog = MDDialog(title="Selection",
                text="Please select an item",
                
                )    
            self.dialog.open()
        else:
            self.details(ct,1)
    def details(self,code,primal):
        print("start of detail id ---------------")
        print(code)
        print("end of detail id ---------------")
       # losc=self.root.get_screen('hide').ids.behind.text
        try:
           
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            data1={"mac":macer,"code":code}
            url=point+'detail.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print(task)
            if task=="1":
                #self.root.get_screen('my_buildings').ids.header.title="Select building or land"
                info=(z["data"])
                list=info.split("*")
                length=len(list)-1
                print(length)
                print("i am")
                self.ai_builder("shamba",1)
                self.root.get_screen('shamba').ids.data.clear_widgets()
                for d in range(length):
                    ins=list[d]
                    ins2=ins.split("|")
                    print(ins2)
                    print("i ins")
                    id=ins2[0]
                    info=ins2[1]
                    jina=ins2[2]
                    phone=ins2[3]
                    loc1=ins2[4]
                    loc2=ins2[5]
                    pic=ins2[6]
                    p1=ins2[7]
                    p2=ins2[8]
                    p3=ins2[9]
                    ic=ins2[10]
                    rent=ins2[11]
                    link=ins2[12]
                    #pic="image/bui.png"
                    self.ai_builder("detail",1)
                    self.root.get_screen('detail').ids.p1.source=point+"uploads/"+p1
                    self.root.get_screen('detail').ids.p2.source=point+"uploads/"+p2
                    self.root.get_screen('detail').ids.p3.source=point+"uploads/"+p3
                    self.root.get_screen('detail').ids.p4.source=point+"uploads/"+pic
                    self.root.get_screen('detail').ids.desc.text=ic
                    #self.root.get_screen('detail').ids.call.text=link
                    self.root.get_screen('hide').ids.loc_link.text=link
                    self.root.get_screen('detail').ids.lab0.text=phone
                    self.root.get_screen('detail').ids.lab1.text=rent
                    self.root.get_screen('detail').ids.locsa.text=loc1+", "+loc2
                    #self.root.get_screen('detail').ids.header.title="View lands"
                           
                    


            if task=="0":
                self.root.get_screen('shamba').ids.header.title='"Zero results"'
                self.root.get_screen('shamba').ids.data.clear_widgets()
                
                #screen_manager.current="my_buildings"
                
                
        except IOError:
            self.connection_error()
        else:
            pass
        # screen_manager.current="detail"
        self.ai_builder("detail",2)
    def places_mini(self,code):
        
        losc=self.root.get_screen('hide').ids.behind.text
        self.root.get_screen('hide').ids.count_code.text=str(code)

        try:
           
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            data1={"mac":macer,"code":code}
            url=point+'places.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print(task)
            if task=="1":
                #self.root.get_screen('my_buildings').ids.header.title="Select building or land"
                info=(z["data"])
                list=info.split("*")
                length=len(list)-1
                print(length)
                print("i am")
                self.root.get_screen('loc_play').ids.list.clear_widgets()
                for d in range(length):
                    ins=list[d]
                    ins2=ins.split("|")
                    print(ins2)
                    print("i ins")
                    id=ins2[0]
                    info=ins2[1]
                    alex11={'name': info,'id':id}
                    alex12=locat.format(**alex11)
                    conner=Builder.load_string(alex12)
                    
                    self.root.get_screen('loc_play').ids.list.add_widget(conner)
                    #pic="image/bui.png"
                    # screen_manager.current="loc_play"
                    self.ai_builder("loc_play",2)
                    #self.root.get_screen('detail').ids.header.title="View lands"
                           
           

            if task=="0":
                self.root.get_screen('loc_play').ids.code.title='"Zero results"'
                self.root.get_screen('loc_play').ids.list.clear_widgets()
                # screen_manager.current="loc_play"
                self.ai_builder("loc_play",2)
                #screen_manager.current="my_buildings"
                
                
        except IOError:
            self.connection_error()
        else:
            pass
        #screen_manager.current="detail" 
    def add_location(self):
        if self.root.get_screen('add_sublocation').ids.loc.text!="" and self.root.get_screen('add_sublocation').ids.link.text!="" and self.root.get_screen('add_sublocation').ids.key.text!="":
            try:
                 
                macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
                loc=self.root.get_screen('add_sublocation').ids.loc.text
                link=self.root.get_screen('add_sublocation').ids.link.text
                key=self.root.get_screen('add_sublocation').ids.key.text
                piccode=self.root.get_screen('hide').ids.piccode.text
                code=self.root.get_screen('hide').ids.count_code.text
                business_name=self.root.get_screen('hide').ids.current_building.text
                data1={"mac":macer,"link":link,"loc":loc,"key":key,"business_name":business_name,"piccode":piccode,"county":code}
                url=point+'add_location.php'
                r=requests.post(url,data=data1)
                rd=r.json()
                y=json.dumps(rd)
                z=json.loads(y)
                task=(z["sent"])
                if task=="1":
                    
                    self.dialog = MDDialog(title="Success",
                    text="sub-location  added successfully, you can add more")
                    self.dialog.open()
                    self.root.get_screen('add_sublocation').ids.loc.text=""
                    self.root.get_screen('add_sublocation').ids.link.text=""
                    self.root.get_screen('add_sublocation').ids.key.text=""
                    derft=int(code)
                    self.places_mini(derft)
                    # screen_manager.current="add_sublocation"
                    self.ai_builder("add_sublocation",2)
                elif task=="0":
                    self.dialog = MDDialog(title="Adding failed",
                    text="The addition failed, if error persist, contact customer care",
                    
                    )    
                    self.dialog.open()
                elif task=="3":
                    self.dialog = MDDialog(title="Adding failed",
                    text="The location is in existance, kindly use another name",
                    
                    )    
                    self.dialog.open()
            except IOError:
                self.connection_error()
            else:
                pass


            
        else:
            self.dialog = MDDialog(title="Insertions missing",
                        text="Ensure that you have filled all the required data",
                        
                        )
            self.dialog.open()
    def access_locations(self,codesy,name):
        losc=self.root.get_screen('hide').ids.behind.text
        self.root.get_screen('hide').ids.count_code.text=str(name)
        self.root.get_screen('hide').ids.county_selection.text=str(name)

        try:
            if codesy==0:
               self.root.get_screen('hide').ids.loc_block.title=""
            else:
                self.root.get_screen('hide').ids.loc_block.title="1"
                macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
                data1={"mac":macer,"code":codesy}
                url=point+'places.php'
                r=requests.post(url,data=data1)
                rd=r.json()
                y=json.dumps(rd)
                z=json.loads(y)
                task=(z["sent"])
                print(task)
                if task=="1":
                    #self.root.get_screen('my_buildings').ids.header.title="Select building or land"
                    info=(z["data"])
                    list=info.split("*")
                    length=len(list)-1
                    print(length)
                    print("i am")
                    self.root.get_screen('sublocations').ids.list.clear_widgets()
                    for d in range(length):
                        ins=list[d]
                        ins2=ins.split("|")
                        print(ins2)
                        print("i ins")
                        id=ins2[0]
                        info=ins2[1]
                        alex11={'name': info,'id':id}
                        alex12=locat.format(**alex11)
                        conner=Builder.load_string(alex12)
                        
                        self.root.get_screen('sublocations').ids.list.add_widget(conner)
                        #pic="image/bui.png"
                        # screen_manager.current="sublocations"
                        self.ai_builder("sublocations",2)
                        #self.root.get_screen('detail').ids.header.title="View lands"
                            
            

                if task=="0":
                    self.ai_builder("sublocations",1)
                    self.root.get_screen('sublocations').ids.code.title='"Zero results"'
                    self.root.get_screen('sublocations').ids.list.clear_widgets()
                    # screen_manager.current="sublocations"
                    self.ai_builder("sublocations",2)
                    #screen_manager.current="my_buildings"
                
                
        except IOError:
            self.connection_error()
        else:
            pass
        #screen_manager.current="detail"
    def higher_power(self):
        pointss=self.root.get_screen('hide').ids.behind.text
        if pointss=="1":
            # screen_manager.current="house"
            self.ai_builder("house",2)
        if pointss=="2":
            # screen_manager.current="shamba"
            self.ai_builder("shamba",2)
    def search_items(self):
        if self.root.get_screen('search').ids.word.text!="":
            try:
                pointss=self.root.get_screen('hide').ids.behind.text
                if pointss=="1":
                    # screen_manager.current="house"
                    self.ai_builder("house",2)
                    self.house(4)
                if pointss=="2":
                    # screen_manager.current="shamba"
                    self.ai_builder("shamba",2)
                    self.shamba(4)
            except IOError:
                self.connection_error()
            else:
                pass
        


            
        else:
            self.dialog = MDDialog(title="Insertions missing",
                        text="insert something to search",
                        
                        )
            self.dialog.open()
    def update_location(self,subloc):
        loca=self.root.get_screen('hide').ids.county_selection.text
        try:
           
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            data1={"mac":macer,"county":loca,"loc":subloc}
            url=point+'update_location.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print(task)
            if task=="1":
                #self.root.get_screen('my_buildings').ids.header.title="Select building or land"
                
                self.root.get_screen('hide').ids.county.text=loca
                self.root.get_screen('hide').ids.subloc.text=str(subloc)
                self.dialog = MDDialog(title="New location",
                text="The new location has been added",
                
                )    
                self.dialog.open()       
                
            if task=="0":
                self.dialog = MDDialog(title="Operation Failed",
                text="if error persist kindly contact customer care",
                
                )    
                self.dialog.open()    
                #screen_manager.current="my_buildings"
                
                
        except IOError:
            self.connection_error()
        else:
            pass
    def user_invoices_data(self):
        # screen_manager.current="user_invoices"
        self.ai_builder("user_invoices",2)
        try:
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            
            email=self.root.get_screen('hide').ids.email_data.text
            data1={"mac":macer,"email":email}
            url=point+'invoice_listing.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print(task)
            if task=="1":
                #self.root.get_screen('my_buildings').ids.header.title="Select building or land"
                info=(z["data"])
                list=info.split("*")
                length=len(list)-1
                print(length)
                print("i am")
                self.root.get_screen('user_invoices').ids.data.clear_widgets()
                for d in range(length):
                    ins=list[d]
                    ins2=ins.split("|")
                    print(ins2)
                    print("i ins")
                    id=ins2[0]
                    title=ins2[1]
                    amount=ins2[2]
                    due=ins2[3]
                    alex11={'name': title,'users':amount,'amount': due,'id': id}
                    alex12=invoicee.format(**alex11)
                    conner=Builder.load_string(alex12)
                    #self.root.get_screen('choose_customer').ids.header.title="Choose tenant to add payment"
                    self.root.get_screen('user_invoices').ids.data.add_widget(conner)
                    #pic="image/bui.png"
                    
                
                           
                    


            if task=="0":
                
                self.root.get_screen('user_invoices').ids.header.title='"Zero results"'
                self.root.get_screen('user_invoices').ids.data.clear_widgets()
                
                #screen_manager.current="my_buildings"
                
                
        except IOError:
            self.connection_error()
        else:
            pass
       # screen_manager.current="detail"
    def user_methods(self,names):
        # screen_manager.current="payment_method"
        self.ai_builder("payment_method",2)
        try:
            
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            business_name=self.root.get_screen('hide').ids.current_building.text
            
            data1={"mac":macer,"business_name":names}
            url=point+'payment_listing.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print("quota")
            print(task)
            if task=="1":
                self.root.get_screen('payment_method').ids.header.title="View payments options"
                info=(z["data"])
                list=info.split("*")
                length=len(list)-1
                print(length)
                print("i am")
                self.root.get_screen('payment_method').ids.data.clear_widgets()
                for d in range(length):
                    ins=list[d]
                    ins2=ins.split("|")
                    print(ins2)
                    print("i ins")
                    id=ins2[0]
                    kind=ins2[1]
                    business_no=ins2[2]
                    acc=ins2[3]
                    keywords=ins2[4]
                    pic=""
                    alex11={'name': kind,'users':business_no,'amount':acc,'image':pic,'id':id}
                    alex12=pay_type.format(**alex11)
                    conner=Builder.load_string(alex12)
                    
                    self.root.get_screen('payment_method').ids.data.add_widget(conner)


            if task=="0":
                print(task)
                self.root.get_screen('payment_method').ids.header.title="Zero methods available"
                self.root.get_screen('payment_method').ids.data.clear_widgets()
                
                #screen_manager.current="my_buildings"
                
                
        except IOError:
            self.connection_error()
        else:
            pass 
    def view_staff(self):
        # screen_manager.current="staff"
        self.ai_builder("staff",2)
        try:
            
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            business_name=self.root.get_screen('hide').ids.current_building.text
            
            data1={"mac":macer}
            url=point+'view_staff.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print("quota")
            print(task)
            if task=="1":
                self.root.get_screen('staff').ids.header.title="View my staff"
                info=(z["data"])
                list=info.split("*")
                length=len(list)-1
                print(length)
                print("i am")
                self.root.get_screen('staff').ids.data.clear_widgets()
                for d in range(length):
                    ins=list[d]
                    ins2=ins.split("|")
                    print(ins2)
                    print("i ins")
                    id=ins2[0]
                    kind=ins2[1]
                    business_no=ins2[2]
                    acc=ins2[3]
                    #keywords=ins2[4]
                    pic=""
                    alex11={'name': kind,'users':business_no,'amount':acc,'image':pic,'id':id}
                    alex12=staff.format(**alex11)
                    conner=Builder.load_string(alex12)
                    
                    self.root.get_screen('staff').ids.data.add_widget(conner)


            if task=="0":
                print(task)
                self.root.get_screen('staff').ids.header.title="Zero staff available"
                self.root.get_screen('staff').ids.data.clear_widgets()
                
                #screen_manager.current="my_buildings"
                
                
        except IOError:
            self.connection_error()
        else:
            pass 
    def add_staff(self):
        if self.root.get_screen('add_staff').ids.position.text!="" and self.root.get_screen('add_staff').ids.salary.text!="" and self.root.get_screen('add_staff').ids.second.text!="":
            try:
                 
                macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
                position=self.root.get_screen('add_staff').ids.position.text
                salary=self.root.get_screen('add_staff').ids.salary.text
                email=self.root.get_screen('add_staff').ids.second.text
                business_name=self.root.get_screen('hide').ids.current_building.text
                data1={"mac":macer,"position":position,"salary":salary,"email":email}
                url=point+'add_staff.php'
                r=requests.post(url,data=data1)
                rd=r.json()
                y=json.dumps(rd)
                z=json.loads(y)
                task=(z["sent"])
                if task=="1":
                    
                    self.dialog = MDDialog(title="Success",
                    text="Staff was added successfully, you can add more")
                    self.dialog.open()
                    self.root.get_screen('add_staff').ids.position.text=""
                    self.root.get_screen('add_staff').ids.salary.text=""
                    self.root.get_screen('add_staff').ids.second.text=""
                   
                    # screen_manager.current="add_staff"
                    self.ai_builder("add_staff",2)
                elif task=="0":
                    self.dialog = MDDialog(title="Adding failed",
                    text="The addition failed( check if email is correct ), if error persist, contact customer care",
                    
                    )    
                    self.dialog.open()
            except IOError:
                self.connection_error()
            else:
                pass


            
        else:
            self.dialog = MDDialog(title="Insertions missing",
                        text="Ensure that you have filled all the required data",
                        
                        )
            self.dialog.open()
    def view_staff_payments(self):
        # screen_manager.current="staff_payments"
        self.ai_builder("staff_payments",2)
        try:
            
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            business_name=self.root.get_screen('hide').ids.current_building.text
            
            data1={"mac":macer}
            url=point+'staff_payments.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print("quota")
            print(task)
            if task=="1":
                self.root.get_screen('staff_payments').ids.header.title="View staff payments"
                info=(z["data"])
                list=info.split("*")
                length=len(list)-1
                print(length)
                print("i am")
                self.root.get_screen('staff_payments').ids.data.clear_widgets()
                for d in range(length):
                    ins=list[d]
                    ins2=ins.split("|")
                    print(ins2)
                    print("i ins")
                    id=ins2[0]
                    kind=ins2[1]
                    business_no=ins2[2]
                    acc=ins2[3]
                    #keywords=ins2[4]
                    pic=""
                    alex11={'name': kind,'users':business_no,'amount':acc,'image':pic,'id':id}
                    alex12=staff_payments.format(**alex11)
                    conner=Builder.load_string(alex12)
                    
                    self.root.get_screen('staff_payments').ids.data.add_widget(conner)


            if task=="0":
                print(task)
                self.root.get_screen('staff_payments').ids.header.title="Zero staff payments available"
                self.root.get_screen('staff_payments').ids.data.clear_widgets()
                
                #screen_manager.current="my_buildings"
                
                
        except IOError:
            self.connection_error()
        else:
            pass 
        #self.dialog.dismiss()
    def add_staff_payments(self):
        # screen_manager.current="staff_payments"
        self.ai_builder("staff_payments",2)
        try:
            
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            business_name=self.root.get_screen('hide').ids.current_building.text
            
            data1={"mac":macer}
            url=point+'view_staff.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print("quota")
            print(task)
            if task=="1":
                self.root.get_screen('staff_payments').ids.header.title="Select staff to add payment"
                info=(z["data"])
                list=info.split("*")
                length=len(list)-1
                print(length)
                print("i am")
                self.root.get_screen('staff_payments').ids.data.clear_widgets()
                for d in range(length):
                    ins=list[d]
                    ins2=ins.split("|")
                    print(ins2)
                    print("i ins")
                    id=ins2[0]
                    kind=ins2[1]
                    business_no=ins2[2]
                    acc=ins2[3]
                    #keywords=ins2[4]
                    pic=""
                    alex11={'name': kind,'users':business_no,'amount':acc,'image':pic,'id':id}
                    alex12=staff_for_pay.format(**alex11)
                    conner=Builder.load_string(alex12)
                    
                    self.root.get_screen('staff_payments').ids.data.add_widget(conner)


            if task=="0":
                print(task)
                self.root.get_screen('staff_payments').ids.header.title="Zero staff available"
                self.root.get_screen('staff_payments').ids.data.clear_widgets()
                
                #screen_manager.current="my_buildings"
                
                
        except IOError:
            self.connection_error()
        else:
            pass 
        self.dialog.dismiss()
    def payment_register(self,position):
        
        # screen_manager.current="add_staff_pay"
        self.ai_builder("add_staff_pay",2)
        self.root.get_screen('hide').ids.current_staff.text=position
        print(position)
    def payment_entry(self):
        names=self.root.get_screen('hide').ids.current_staff.text
        if self.root.get_screen('add_staff_pay').ids.amount.text!="" and self.root.get_screen('add_staff_pay').ids.method.text!="" and self.root.get_screen('add_staff_pay').ids.receipt.text!="" and self.root.get_screen('add_staff_pay').ids.other.text!="":
            try:
                 
                macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
                amount=self.root.get_screen('add_staff_pay').ids.amount.text
                method=self.root.get_screen('add_staff_pay').ids.method.text
                receipt=self.root.get_screen('add_staff_pay').ids.receipt.text
                other=self.root.get_screen('add_staff_pay').ids.other.text
                business_name=self.root.get_screen('hide').ids.current_building.text
                data1={"mac":macer,"jina":names,"amount":amount,"method":method,"receipt":receipt,"description":other}
                url=point+'add_staff_pay.php'
                r=requests.post(url,data=data1)
                rd=r.json()
                y=json.dumps(rd)
                z=json.loads(y)
                task=(z["sent"])
                if task=="1":
                    
                    self.dialog = MDDialog(title="Success",
                    text="Payment was added successfully, you can add more")
                    self.dialog.open()
                    self.root.get_screen('add_staff_pay').ids.amount.text=""
                    self.root.get_screen('add_staff_pay').ids.method.text=""
                    self.root.get_screen('add_staff_pay').ids.receipt.text=""
                    self.root.get_screen('add_staff_pay').ids.other.text=""
                    # screen_manager.current="add_staff_pay"
                    self.ai_builder("add_staff_pay",2)
                elif task=="0":
                    self.dialog = MDDialog(title="Adding failed",
                    text="The addition failed , if error persist, contact the developer",
                    
                    )    
                    self.dialog.open()
            except IOError:
                self.connection_error()
            else:
                pass


            
        else:
            self.dialog = MDDialog(title="Insertions missing",
                        text="Ensure that you have filled all the required data",
                        
                        )
            self.dialog.open()
    def staff_payments_options(self):

        self.dialog = MDDialog(title="View More",
                        text="What would you like to do",
                        buttons=(MDRaisedButton(text='View Payments', on_release=lambda x:self.view_staff_payments())
                                        ,MDRaisedButton(text='Add payments',md_bg_color=(0/256,176/256,144/256,1), on_release=lambda x:self.add_staff_payments()))
                                        )
                        
        self.dialog.open()         
    def view_logistics(self):
        # screen_manager.current="logistics"
        self.ai_builder("logistics",2)
        try:
                
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
    
            business_name=self.root.get_screen('hide').ids.current_building.text
            data1={"mac":macer}
            url=point+'logistics.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
           
            info=(z["data"])
            list=info.split("*")
            length=len(list)-1
            
                
            ins2=info.split("*")
            print(ins2)
            print("i ins")
            users=ins2[0]
            owners=ins2[1]
            buildings=ins2[2]
            lands=ins2[3]
            locations=ins2[4]
            outside=ins2[5]
                
        
            self.root.get_screen('logistics').ids.users.secondary_text=users
            self.root.get_screen('logistics').ids.owners.secondary_text=owners
            self.root.get_screen('logistics').ids.buildings.secondary_text=buildings
            self.root.get_screen('logistics').ids.lands.secondary_text=lands
            self.root.get_screen('logistics').ids.locations.secondary_text=locations
            self.root.get_screen('logistics').ids.outside.secondary_text=outside
                  
            
        except IOError:
            self.connection_error()
        else:
            pass

    def suggestions(self):
       # names=self.root.get_screen('hide').ids.current_staff.text
        if self.root.get_screen('help').ids.contact.text!="" and self.root.get_screen('help').ids.care.text!="":
            try:
                 
                macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
                phone=self.root.get_screen('help').ids.contact.text
                care=self.root.get_screen('help').ids.care.text
                
                data1={"mac":macer,"jina":"","phone":phone,"barua":care}
                url=point+'add_message.php'
                r=requests.post(url,data=data1)
                rd=r.json()
                y=json.dumps(rd)
                z=json.loads(y)
                task=(z["sent"])
                if task=="1":
                    
                    self.dialog = MDDialog(title="Success",
                    text="Message was sent successfully, you can add more")
                    self.dialog.open()
                    self.root.get_screen('help').ids.contact.text=""
                    self.root.get_screen('help').ids.care.text=""
                elif task=="0":
                    self.dialog = MDDialog(title="Sending failed",
                    text="The propagation failed , if error persist, contact the developer",
                    
                    )    
                    self.dialog.open()
            except IOError:
                self.connection_error()
            else:
                pass


            
        else:
            self.dialog = MDDialog(title="Insertions missing",
                        text="Ensure that you have filled all the required information",
                        
                        )
            self.dialog.open()
    def view_help(self,kind):
        # screen_manager.current="view_help"
        self.ai_builder("view_help",2)
        try:
            
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            business_name=self.root.get_screen('hide').ids.current_building.text
            
            data1={"kind":kind}
            url=point+'view_help.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print("quota")
            print(task)
            if task=="1":
                self.root.get_screen('view_help').ids.header.title="Select staff to add payment"
                info=(z["data"])
                list=info.split("*")
                length=len(list)-1
                print(length)
                print("i am")
                self.root.get_screen('view_help').ids.data.clear_widgets()
                for d in range(length):
                    ins=list[d]
                    ins2=ins.split("|")
                    print(ins2)
                    print("i ins")
                    id=ins2[0]
                    jina=ins2[1]
                    phone=ins2[2]
                    barua=ins2[3]
                    #keywords=ins2[4]
                    pic=""
                    alex11={'name': jina,'users':phone,'amount':barua,'image':pic,'id':id}
                    alex12=bars.format(**alex11)
                    conner=Builder.load_string(alex12)
                    
                    self.root.get_screen('view_help').ids.data.add_widget(conner)


            if task=="0":
                print(task)
                self.root.get_screen('view_help').ids.header.title="Zero messages available"
                self.root.get_screen('view_help').ids.data.clear_widgets()
                
                #screen_manager.current="my_buildings"
                
                
        except IOError:
            self.connection_error()
        else:
            pass 
        #self.dialog.dismiss()
    def help_options(self):
        self.dialog = MDDialog(title="View More",
                        text="What messages would you like to view",
                        buttons=(MDRaisedButton(text='New', on_release=lambda x:self.view_help(1))
                                        ,MDRaisedButton(text='Read',md_bg_color=(0/256,176/256,144/256,1), on_release=lambda x:self.view_help(2)))
                                        )
                        
                        
        self.dialog.open()
    def mess_click(self,kutoka,mesaa,m2,ht):
        self.root.get_screen('hide').ids.ht.text=ht
        messag=mesaa+"\n\n"+m2
        self.dialog = MDDialog(title=kutoka,
                        text=messag,
                        buttons=(MDRaisedButton(text='Exit', on_release=lambda x:self.dialog.dismiss())
                                        ,MDRaisedButton(text='Mark/Unmark',md_bg_color=(0/256,176/256,144/256,1), on_release=lambda x:self.mark_as_read(1)))
                                        )
                        
                        
        self.dialog.open()


    def mark_as_read(self,kind):
        id=self.root.get_screen('hide').ids.ht.text
        try:
            
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            business_name=self.root.get_screen('hide').ids.current_building.text
            
            data1={"mark":kind,"id":id}
            url=point+'mark_as_read.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print("quota")
            print(task)
            if task=="1":
                self.dialog.dismiss()
                
                self.dialog = MDDialog(title="Sucesss",
                        text="The message status was adjusted",
                          )
                        
                        
                self.dialog.open()
                

            if task=="0":
                self.dialog.dismiss()
                self.dialog = MDDialog(title="Failed",
                        text="The adjustment failed, contact developer if error proceed",
                     )
                        
                        
                self.dialog.open()
                
                
        except IOError:
            self.connection_error()
        else:
            pass 
    def delete_units(self):
        id=self.root.get_screen('hide').ids.ht.text
        loc=self.root.get_screen('hide').ids.unit_loc.text
        try:
            
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            business_name=self.root.get_screen('hide').ids.current_building.text
            
            data1={"room":loc,"business_name":business_name}
            url=point+'delete_unit.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            print("quota")
            print(task)
            if task=="1":
                #self.dialog.dismiss()
                
                self.dialog = MDDialog(title=loc,
                        text="The unit was deleted",
                          )
                        
                        
                self.dialog.open()
                

            if task=="0":
                self.dialog.dismiss()
                self.dialog = MDDialog(title="Failed",
                        text="The unit was not deleted",
                     )
                        
                        
                self.dialog.open()
                
                
        except IOError:
            self.connection_error()
        else:
            pass 
    def my_detail(self):
        print("wower")
        try:
            
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            business_name=self.root.get_screen('hide').ids.current_building.text
            
            data1={"mac":macer}
            url=point+'acc_info.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["data"])
            task2=task.replace("|","\n")
            self.dialog = MDDialog(title="My details",
                        text=task2,
                                        )
                        
                        
            self.dialog.open()
                #screen_manager.current="my_buildings"
        except IOError:
            self.connection_error()
        else:
            pass 
    def change_pass(self):
        if self.root.get_screen('my_acc').ids.email.text!="" and self.root.get_screen('my_acc').ids.current.text!="" and self.root.get_screen('my_acc').ids.new.text!="" and self.root.get_screen('my_acc').ids.confirm.text!="":
            try:
                 
                macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
                email=self.root.get_screen('my_acc').ids.email.text
                current=self.root.get_screen('my_acc').ids.current.text
                new=self.root.get_screen('my_acc').ids.new.text
                confirm=self.root.get_screen('my_acc').ids.confirm.text
                data1={"mac":macer,"email":email,"current":current,"new":new,"confirm":confirm}
                url=point+'adjust_detail.php'
                r=requests.post(url,data=data1)
                rd=r.json()
                y=json.dumps(rd)
                z=json.loads(y)
                task=(z["sent"])
                if task=="1":
                    self.root.get_screen('my_acc').ids.email.text=""
                    self.root.get_screen('my_acc').ids.current.text=""
                    self.root.get_screen('my_acc').ids.new.text=""
                    self.root.get_screen('my_acc').ids.confirm.text=""
                    self.dialog = MDDialog(title="Success",
                    text="details were successfully adjusted")
                    self.dialog.open()
                elif task=="0":
                    self.dialog = MDDialog(title="Sending failed",
                    text="The propagation failed , if error persist, contact the developer",
                    
                    )    
                    self.dialog.open()
            except IOError:
                self.connection_error()
            else:
                pass


            
        else:
            self.dialog = MDDialog(title="Insertions missing",
                        text="Ensure that you have filled all the required information",
                        
                        )
            self.dialog.open()
            
    def picture_setup(self):
        try:
                
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            data1={"mac":macer}
            url=point+'pictures.php'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            task=(z["sent"])
            if task>"1":
                self.root.get_screen('hide').ids.picture_id.text=task
                link=point+"picture_add.php?id="+task+"&point=0"
                webbrowser.open(link)
            elif task=="0":
                self.dialog = MDDialog(title="Operation failed",
                text="The operation  failed , if error persist, contact the developer",
                
                )    
                self.dialog.open()
        except IOError:
            self.connection_error()
        else:
            pass
    def dimesions(self):
        try:
            # print("start of self height_w-----------------------")
            # print(self.height)
            # print(self.width)
            # print("end of self height_w-----------------------")
            macer=str((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
            data1={"mac":macer}
            url=point+'height.html'
            r=requests.post(url,data=data1)
            rd=r.json()
            y=json.dumps(rd)
            z=json.loads(y)
            self.height=(z["height"])
            self.width=(z["width"])
            self.pos=str((z["pos"]))
            print("start of self height_w-----------------------")
            print(self.height)
            print(self.width)
            print(self.pos)
            print("end of self height_w-----------------------")

            # # mdcardh=height
            # self.root.get_screen('hide').ids.height.text=height
            # self.root.get_screen('hide').ids.width.text=width
        except IOError:
            self.connection_error()
        else:
            pass
   
    # def call_dude()
    
    def on_start2(self):
        self.dialog = MDDialog(title="Loading",
                        text="Please wait a minute the information to be loaded",
                        
                        )
        self.dialog.open()
        Clock.schedule_once(self.strart3, 3)
    def strart3(self,obj):

        
        self.builder_sec()
        #self.root.get_screen('spage').ids.login_b.add_widget(Builder.load_string(login_b))
       # self.root.get_screen('spage').ids.login_b.add_widget(Builder.load_string(login_m))
        self.check_user()
    def ai_builder(self,screen,level):
        print(screen)
        screens=self.root.get_screen('hide').ids.screens.text
        if screen in screens and level != 1 :
            screen_manager.transition=NoTransition()
            screen_manager.current=screen
            # self.ai_builder(screen)
        if screen not in screens:
            if level==1:
                name=screen+".kv"
                screen_manager.add_widget(Builder.load_file(name))
                self.root.get_screen('hide').ids.screens.text=screens+","+screen
            if level==2:
                name=screen+".kv"
                screen_manager.add_widget(Builder.load_file(name))
                self.root.get_screen('hide').ids.screens.text=screens+","+screen
                screen_manager.transition=NoTransition()
                screen_manager.current=screen
            # self.ai_builder(screen,2)

    def open_link(self):
        link=self.root.get_screen('hide').ids.loc_link.text
        webbrowser.open(link)
        print("start of self height_w-----------------------")
        print(self.height)
        print(self.width)
        print("end of self height_w-----------------------")

    def on_start(self):
        # self.check_user()
      #  self.user_data_listing()
        # self.porti()
        screen_manager.add_widget(Builder.load_file("spage.kv"))
        screen_manager.current="spage"

        screen_manager.add_widget(Builder.load_file("hide.kv"))
        # Window.canvas.ask_update()
        # Clock.schedule_once(self.on_start2, 3)



    
MainApp().run() 
        
