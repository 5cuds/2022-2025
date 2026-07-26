from winotify import Notification, audio
import random
             
list_imgs = ["eee.webp", "rrr.png"]    
                                                                                # duration="long" is longer u dumbass
msg = Notification(app_id="test app lol", title="Test", msg="Even More Test text lol", duration="short",
                   icon=f"C:\\Users\\Windows\\Documents\\QUO IMAGES\\{random.choice(list_imgs)}")

msg.set_audio( 
    audio.LoopingAlarm3,
    loop=False
)

msg.show()

