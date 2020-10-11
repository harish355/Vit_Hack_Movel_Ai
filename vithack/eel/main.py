import eel
eel.init('web')

import os
@eel.expose
def left():
    print("left key pressed")
    os.system("python /home/mrstark/vithack/left.py")
    


@eel.expose
def right():
    print("right key pressed")
    os.system("python /home/mrstark/vithack/right.py")
    

@eel.expose
def up():
    print("up key pressed")
    os.system("python /home/mrstark/vithack/up.py")
    


@eel.expose
def down():
    print("down key pressed")
    os.system("python /home/mrstark/vithack/down.py")
    


@eel.expose
def joystick():
    print("Switching to joystick")
    os.system("python /home/mrstark/vithack/joystic.py")
    


@eel.expose
def sub_map():
    print("Creating Sub Map")
    os.system("python /home/mrstark/vithack/submap1.py")
    

@eel.expose
def sub_mapa():
    print("Creating Sub Map")
    os.system("python /home/mrstark/vithack/finalsubmap.py")
    
    


@eel.expose
def autono():
    print("Navigating")
    os.system("python3 /home/mrstark/vithack/main1.py")
    

    
    
#       ~~~~~~~~~~~~~~~~~~~~~~~~~Not Used~~~~~Just to Print~
eel.start('index.html',  port=8080, size=(700, 600))  # ),mode='chrome-app',
# cmdline_args=['--start-fullscreen', '--browser-startup-dialog'])
