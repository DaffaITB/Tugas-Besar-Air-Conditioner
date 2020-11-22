import tkinter as tk
import datetime
import time
from PIL import ImageTk, Image

# Variabel
switch = True
temp   = [25 for i in range(5)]
mode, i = ['Auto', 'Cool', 'Dry', 'Fan', 'Heat'], 0
fan     = ['Auto' for i in range(5)]
swing   = ['Continously' for i in range(5)]
anti_b   = 'OFF'
energy_s = 'OFF'
t_hour = 0
t_min = 0
t_sec = 0
n = 0
t_now = ""


def visual(on_switch):
    global switch
    
    if on_switch == True:
        
        # Visual gambar untuk mode
        if i == 0:
            top_1_label.config(image=auto_mode)
            top_2_label.config(image="")
            top_3_label.config(image="")
            top_4_label.config(image="")
            top_5_label.config(image="")

        elif i == 1:
            top_1_label.config(image="")
            top_2_label.config(image=cool_mode)
            top_3_label.config(image="")
            top_4_label.config(image="")
            top_5_label.config(image="")

        elif i == 2:
            top_1_label.config(image="")
            top_3_label.config(image=dry_mode)
            top_2_label.config(image="")
            top_4_label.config(image="")
            top_5_label.config(image="")

        elif i == 3:
            top_1_label.config(image="")
            top_2_label.config(image="")
            top_3_label.config(image="")
            top_4_label.config(image=fan_mode)
            top_5_label.config(image="")

        elif i == 4:
            top_1_label.config(image="")
            top_2_label.config(image="")
            top_3_label.config(image="")
            top_4_label.config(image="")
            top_5_label.config(image=heat_mode)

        
        # Visual gambar untuk fan
        if fan[i] == 1:
            left_1_top_label.config(image=fan_1)

        elif fan[i] == 2:
            left_1_top_label.config(image=fan_2)

        elif fan[i] == 3:
            left_1_top_label.config(image=fan_3)

        else:
            left_1_top_label['text'] = "AUTO"
            left_1_top_label.config(image="")
            

        # Visual gambar untuk swing
        if  swing[i] == "Up":
            left_1_bottom_label.config(image=swing_up)
        
        elif swing[i] == "Mid":
            left_1_bottom_label.config(image=swing_mid)
        
        elif swing[i] == "Down":
            left_1_bottom_label.config(image=swing_down)
        
        else:
            left_1_bottom_label.config(image=swing_continous)
        

        # Visual untuk timer
        if t_now == "":
            top_right_bottom_2_label.config(text = f'{t_now}')

        else:
            top_right_bottom_2_label.config(text = f'TIMER: {t_now}')


        # Visual untuk yang lainnya
        left_2_label['text'] = f'Anti Bacteria: {anti_b} \nEnergy Saving: {energy_s}'
        right_label['text'] = f'{temp[i]} °C'
        
        switch = False

    else:
        # Visual ketika remote ac tidak nyala
        top_1_label.config(image="")
        top_2_label.config(image="")
        top_3_label.config(image="")
        top_4_label.config(image="")
        top_5_label.config(image="")
        left_1_top_label['text'] = ""
        left_1_top_label.config(image="")
        left_1_bottom_label.config(image="")
        left_2_label['text'] = ""
        right_label['text'] = ""
        top_right_bottom_2_label['text'] = ""
        
        switch = True


def temp_up(on_switch): 
    global temp

    if on_switch == False:

        if i == 0 or i == 1 or i == 2:
            if temp[i] == 30:
                temp[i] = 30
            else:
                temp[i] += 1

        if i == 3 or i == 4:
            if temp[i] == 35:
                temp[i] = 35
            else:
                temp[i] += 1

        visual(True)


def temp_down(on_switch):
    global temp
    
    if on_switch == False:

        if i == 0 or i ==1 or i == 2:
            if temp[i] == 16:
                temp[i] = 16
            else:
                temp[i] -= 1

        elif i == 3 or i == 4:
            if temp[i] == 20:
                temp[i] = 20
            else:
                temp[i] -= 1

        visual(True)


def mode_switch(on_switch):
    global mode, i

    if on_switch == False:
        if  i == 4:
            i = 0
        
        else:
            i += 1
        visual(True)


def fan_switch(on_switch):
    global fan, i
    
    if on_switch == False:
        
        if fan[i] == 3:
            fan[i] = "Auto"
        
        elif fan[i] == "Auto":
            fan[i] = 1
        
        else:
            fan[i] += 1
        visual(True)


def ab_switch(on_switch):
    global anti_b

    if on_switch == False:
        if anti_b == "OFF":
            anti_b = "ON"

        else:
            anti_b = "OFF"
        visual(True)


def saving_switch(on_switch):
    global energy_s

    if on_switch == False:
        if energy_s == "OFF":
            energy_s = "ON"

        else:
            energy_s = "OFF"
        visual(True)


def swing_switch(on_switch):
    global swing, i

    if on_switch == False:

        if  swing[i] == "Up":
            swing[i] = "Mid"
        
        elif swing[i] == "Mid":
            swing[i]  = "Down"
        
        elif swing[i] == "Down":
            swing[i]  = "Continously"
        
        else:
            swing[i]  = "Up"
        visual(True)


def timer(on_switch):
    global n, t_hour, t_min, t_sec, t_now

    if on_switch == False:
        
        if n == 0:
            t_hour = 0
            t_min = 15
            t_sec = 0

        elif n == 1:
            t_hour = 0
            t_min = 30
            t_sec = 0

        elif n == 2:
            t_hour = 1
            t_min = 0
            t_sec = 0

        elif n == 3:
            t_hour = 2
            t_min = 0
            t_sec = 0
            
        elif n == 4:
            t_hour = 3
            t_min = 0
            t_sec = 0

        elif n == 5:
            t_now = ""

        else: 
            n = 0

        if n != 5 :
            now = datetime.datetime.now()
            after = datetime.timedelta(hours=t_hour, minutes=t_min, seconds=t_sec)
            t_now = (now + after).strftime("%H:%M")

        root.after((t_hour*3600+t_min*60+t_sec)*1000, lambda: visual(False))

        n += 1
        visual(True)


def time_update():
    global time_count

    if switch == False:
        time_count = time.strftime("%A, %H:%M")
        top_right_bottom_1_label.config(text= f"time_count")
        root.after(1000, time_update)


root = tk.Tk()
root.title("Remote AC")


time_update()

# Image
auto_mode_pic = Image.open("./img/auto_mode.png")
auto_mode_pic = auto_mode_pic.resize((50, 50))
auto_mode = ImageTk.PhotoImage(auto_mode_pic)

cool_mode_pic = Image.open("./img/cool_mode.png")
cool_mode_pic = cool_mode_pic.resize((30, 30))
cool_mode = ImageTk.PhotoImage(cool_mode_pic)

dry_mode_pic = Image.open("./img/dry_mode.png")
dry_mode_pic = dry_mode_pic.resize((25, 25))
dry_mode = ImageTk.PhotoImage(dry_mode_pic)

fan_mode_pic = Image.open("./img/fan_mode.png")
fan_mode_pic = fan_mode_pic.resize((30, 30))
fan_mode = ImageTk.PhotoImage(fan_mode_pic)

heat_mode_pic = Image.open("./img/heat_mode.png")
heat_mode_pic = heat_mode_pic.resize((30, 30))
heat_mode = ImageTk.PhotoImage(heat_mode_pic)

fan_1_pic = Image.open("./img/fan_1.png")
fan_1_pic = fan_1_pic.resize((25, 25))
fan_1 = ImageTk.PhotoImage(fan_1_pic)

fan_2_pic = Image.open("./img/fan_2.png")
fan_2_pic = fan_2_pic.resize((25, 25))
fan_2 = ImageTk.PhotoImage(fan_2_pic)

fan_3_pic = Image.open("./img/fan_3.png")
fan_3_pic = fan_3_pic.resize((25, 25))
fan_3 = ImageTk.PhotoImage(fan_3_pic)

swing_up_pic = Image.open("./img/swing_up.png")
swing_up_pic = swing_up_pic.resize((25, 25))
swing_up = ImageTk.PhotoImage(swing_up_pic)

swing_mid_pic = Image.open("./img/swing_mid.png")
swing_mid_pic = swing_mid_pic.resize((25, 25))
swing_mid = ImageTk.PhotoImage(swing_mid_pic)

swing_down_pic = Image.open("./img/swing_down.png")
swing_down_pic = swing_down_pic.resize((25, 25))
swing_down = ImageTk.PhotoImage(swing_down_pic)

swing_continous_pic = Image.open("./img/swing_continous.png")
swing_continous_pic = swing_continous_pic.resize((25, 25))
swing_continous = ImageTk.PhotoImage(swing_continous_pic)
#------------------------------------------------

canvas = tk.Canvas(root, height= 500, width=300, bg="#F4F4F2")
canvas.pack()


top_top_frame = tk.Frame(root, bg='#E8E8E8')
top_top_frame.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)


top_right_frame = tk.Frame(root, bg='#E8E8E8')
top_right_frame.place(relx=0.6, rely=0.15, relwidth=0.3, relheight=0.2)


top_right_bottom_1_frame = tk.Frame(root, bg='#E8E8E8')
top_right_bottom_1_frame.place(relx=0.6, rely=0.25, relwidth=0.3, relheight=0.05)


top_right_bottom_2_frame = tk.Frame(root, bg='#E8E8E8')
top_right_bottom_2_frame.place(relx=0.6, rely=0.3, relwidth=0.3, relheight=0.05)


top_left_top_frame = tk.Frame(root, bg='#E8E8E8')
top_left_top_frame.place(relx=0.1, rely=0.15, relwidth=0.5, relheight=0.05)


top_left_bottom_frame = tk.Frame(root, bg='#E8E8E8')
top_left_bottom_frame.place(relx=0.1, rely=0.2, relwidth=0.5, relheight=0.05)


top_left_2_frame = tk.Frame(root, bg='#E8E8E8')
top_left_2_frame.place(relx=0.1, rely=0.25, relwidth=0.5, relheight=0.1)


low_frame = tk.Canvas(root, bg='#F4F4F2')
low_frame.place(relx= 0.5, rely=0.35, relwidth=0.8, relheight=0.7, anchor='n')


on_button = tk.Button(low_frame, text="I O", fg="#FF0000" ,bg="#C4C4C4", command=lambda: visual(switch))
on_button.place(relx= 0.6875, rely =0.1375, relheight= 0.125, relwidth=0.125)


temp_up_button = tk.Button(low_frame, text="ʌ", bg="#C4C4C4", command=lambda :temp_up(switch))
temp_up_button.place(relx= 0.2, rely = 0.1, relheight= 0.08, relwidth=0.1)


temp_down_button = tk.Button(low_frame, text="v", bg="#C4C4C4", command=lambda :temp_down(switch))
temp_down_button.place(relx=0.2, rely = 0.2, relheight = 0.08, relwidth=0.1)


mode_button = tk.Button(low_frame, text="MODE", bg="#C4C4C4", command=lambda :mode_switch(switch))
mode_button.place(relx = 0.125, rely = 0.4, relheight=0.075, relwidth=0.25)


fan_button = tk.Button(low_frame, text="FAN", bg="#C4C4C4", command=lambda: fan_switch(switch))
fan_button.place(relx=0.625, rely=0.4,relheight=0.075, relwidth=0.25)


ab_mode_button = tk.Button(low_frame, text="ANTI-B", bg="#C4C4C4", command=lambda :ab_switch(switch))
ab_mode_button.place(relx=0.125, rely= 0.55, relheight=0.075, relwidth=0.25)


saving_mode_button = tk.Button(low_frame, text="SAVING", bg="#C4C4C4", command= lambda:saving_switch(switch))
saving_mode_button.place(relx=0.625, rely=0.55, relheight=0.075, relwidth=0.25)


swing_button = tk.Button(low_frame, text="SWING", bg="#C4C4C4", command= lambda: swing_switch(switch))
swing_button.place(relx=0.125, rely= 0.7, relheight=0.075, relwidth=0.25) # relx=0.5, rely= 0.7, relheight=0.075, relwidth=0.25, anchor='n'


timer_button = tk.Button(low_frame, text="TIMER", bg="#C4C4C4", command= lambda: timer(switch))
timer_button.place(relx=0.625, rely=0.7,relheight=0.075, relwidth=0.25)


top_1_label = tk.Label(top_top_frame, bg='#E8E8E8')
top_1_label.place(relx=0, relwidth=0.2, relheight=1)


top_2_label = tk.Label(top_top_frame, bg='#E8E8E8')
top_2_label.place(relx=0.2, relwidth=0.2, relheight=1)


top_3_label = tk.Label(top_top_frame, bg='#E8E8E8')
top_3_label.place(relx=0.4, relwidth=0.2, relheight=1)


top_4_label = tk.Label(top_top_frame, bg='#E8E8E8')
top_4_label.place(relx=0.6, relwidth=0.2, relheight=1)


top_5_label = tk.Label(top_top_frame, bg='#E8E8E8')
top_5_label.place(relx=0.8, relwidth=0.2, relheight=1)


# top_left_1_frame = tk.Frame(root, bg='#E8E8E8')
# top_left_1_frame.place(relx=0.1, rely=0.15, relwidth=0.5, relheight=0.1)


left_1_top_label = tk.Label(top_left_top_frame, bg='#E8E8E8', anchor='n')
left_1_top_label.place(relwidth=1, relheight=1)


left_1_bottom_label = tk.Label(top_left_bottom_frame, bg='#E8E8E8', anchor='n')
left_1_bottom_label.place(relwidth=1, relheight=1)


left_2_label = tk.Label(top_left_2_frame, bg='#E8E8E8')
left_2_label.place(relwidth=1, relheight=1)


right_label = tk.Label(top_right_frame, bg='#E8E8E8', anchor='n')
right_label.config(font=('helvetica', 28))
right_label.place(relwidth=1, relheight=1)


top_right_bottom_1_label = tk.Label(top_right_bottom_1_frame, bg='#E8E8E8', anchor='n')
top_right_bottom_1_label.place(relwidth=1, relheight=1)


top_right_bottom_2_label = tk.Label(top_right_bottom_2_frame, bg='#E8E8E8', anchor='n')
top_right_bottom_2_label.pack()


def time_update():

    if switch == True:
        time_count = time.strftime("%A, %H:%M")
        top_right_bottom_1_label.config(text= f"{time_count}")
        root.after(1000, time_update)

time_update()

root.mainloop()
