
from tkinter import *
from gtts import gTTS
from playsound import playsound
import os
import time

# Initialized window
root = Tk()
root.geometry('600x500')  # تكبير حجم الإطار
root.resizable(0, 0)
root.config(bg='#2c3e50')  # تغيير لون الخلفية إلى لون داكن مريح
root.title('GetProjects - TEXT_TO_SPEECH')

# Heading
Label(root, text='TEXT TO SPEECH', font='Helvetica 25 bold', bg='#2c3e50', fg='#ecf0f1').pack(pady=20)
Label(root, text='By GetProjects', font='Helvetica 12 bold', bg='#2c3e50', fg='#ecf0f1').pack(side=BOTTOM, pady=10)

# Label for text entry
Label(root, text='Enter Text Below', font='Helvetica 15', bg='#2c3e50', fg='#ecf0f1').place(x=20, y=70)

# Entry field (زيادة الحجم)
entry_field = Text(root, width='50', height='8', font='Helvetica 12', bg='#ecf0f1', fg='#2c3e50', relief='flat')
entry_field.place(x=20, y=110)

# Define functions
def Text_to_speech():
    Message = entry_field.get("1.0", "end-1c")  # تعديل لجلب النص من Text widget
    if Message.strip():  # التأكد أن النص غير فارغ
        # توليد اسم ملف فريد بناءً على الوقت الحالي
        file_name = f"speech_{int(time.time())}.mp3"
        # تحديد اللغة العربية
        speech = gTTS(text=Message, lang='ar', slow=False)
        speech.save(file_name)
        playsound(file_name)
        print(f"File saved as: {file_name}")  # يمكن حذف هذا السطر إذا كنت لا تحتاج إلى إخراج في الكونسول
    else:
        print("Please enter some text.")  # للتأكيد من إدخال المستخدم

def Exit():
    root.destroy()

def Reset():
    entry_field.delete('1.0', END)  # تعديل لمسح النص داخل Text widget

# Button animations
def on_enter(e, btn):
    btn['bg'] = '#34495e'  # عند تحريك المؤشر
def on_leave(e, btn):
    btn['bg'] = '#3498db'  # عند إزالة المؤشر

# Button style
button_style = {
    'font': 'Helvetica 15 bold', 
    'width': 10, 
    'bg': '#3498db', 
    'fg': '#ecf0f1', 
    'relief': 'flat', 
    'activebackground': '#2980b9', 
    'activeforeground': '#ecf0f1',
    'bd': 0
}

# Buttons with hover effect (زيادة عرض الأزرار)
play_btn = Button(root, text="PLAY", command=Text_to_speech, **button_style)
play_btn.place(x=50, y=350)
play_btn.bind("<Enter>", lambda e: on_enter(e, play_btn))
play_btn.bind("<Leave>", lambda e: on_leave(e, play_btn))

exit_btn = Button(root, text='EXIT', command=Exit, **button_style)
exit_btn.place(x=250, y=350)
exit_btn.bind("<Enter>", lambda e: on_enter(e, exit_btn))
exit_btn.bind("<Leave>", lambda e: on_leave(e, exit_btn))

reset_btn = Button(root, text='RESET', command=Reset, **button_style)
reset_btn.place(x=450, y=350)
reset_btn.bind("<Enter>", lambda e: on_enter(e, reset_btn))
reset_btn.bind("<Leave>", lambda e: on_leave(e, reset_btn))

# Infinite loop to run program
root.mainloop()
 
 
 
 
 
# import os
# import time
# from tkinter import *
# from TTS.tts.configs.xtts_config import XttsConfig
# from TTS.tts.models.xtts import Xtts
# from scipy.io.wavfile import write
# from playsound import playsound

# # تحميل نموذج TTS
# config = XttsConfig()
# config.load_json("./XTTS-v2/config.json")
# model = Xtts.init_from_config(config)
# model.load_checkpoint(config, checkpoint_dir="./XTTS-v2/")
# model.cuda()

# # إعداد واجهة Tkinter
# root = Tk()
# root.geometry('600x500')
# root.resizable(0, 0)
# root.config(bg='#2c3e50')
# root.title('GetProjects - TEXT_TO_SPEECH')

# # Heading
# Label(root, text='TEXT TO SPEECH', font='Helvetica 25 bold', bg='#2c3e50', fg='#ecf0f1').pack(pady=20)
# Label(root, text='By GetProjects', font='Helvetica 12 bold', bg='#2c3e50', fg='#ecf0f1').pack(side=BOTTOM, pady=10)

# # Label for text entry
# Label(root, text='Enter Text Below', font='Helvetica 15', bg='#2c3e50', fg='#ecf0f1').place(x=20, y=70)

# # Entry field
# entry_field = Text(root, width='50', height='8', font='Helvetica 12', bg='#ecf0f1', fg='#2c3e50', relief='flat')
# entry_field.place(x=20, y=110)

# # Function to generate speech using TTS
# def Text_to_speech():
#     Message = entry_field.get("1.0", "end-1c")
#     if Message.strip():
#         file_name = f"speech_{int(time.time())}.wav"
#         wav = model.tts(Message)
#         write(file_name, 22050, wav)
#         playsound(file_name)
#         print(f"File saved as: {file_name}")
#     else:
#         print("Please enter some text.")

# # Button animations
# def on_enter(e, btn):
#     btn['bg'] = '#34495e'

# def on_leave(e, btn):
#     btn['bg'] = '#3498db'

# # Button style
# button_style = {
#     'font': 'Helvetica 15 bold',
#     'width': 10,
#     'bg': '#3498db',
#     'fg': '#ecf0f1',
#     'relief': 'flat',
#     'activebackground': '#2980b9',
#     'activeforeground': '#ecf0f1',
#     'bd': 0
# }

# # Buttons with hover effect
# play_btn = Button(root, text="PLAY", command=Text_to_speech, **button_style)
# play_btn.place(x=50, y=350)
# play_btn.bind("<Enter>", lambda e: on_enter(e, play_btn))
# play_btn.bind("<Leave>", lambda e: on_leave(e, play_btn))

# exit_btn = Button(root, text='EXIT', command=root.destroy, **button_style)
# exit_btn.place(x=250, y=350)
# exit_btn.bind("<Enter>", lambda e: on_enter(e, exit_btn))
# exit_btn.bind("<Leave>", lambda e: on_leave(e, exit_btn))

# reset_btn = Button(root, text='RESET', command=lambda: entry_field.delete('1.0', END), **button_style)
# reset_btn.place(x=450, y=350)
# reset_btn.bind("<Enter>", lambda e: on_enter(e, reset_btn))
# reset_btn.bind("<Leave>", lambda e: on_leave(e, reset_btn))

# # Run the Tkinter loop
# root.mainloop()
 