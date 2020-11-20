import tkinter as tk

switch = True
temp   = [25 for i in range(5)]
mode, i = ['Auto', 'Cool', 'Dry', 'Fan', 'Heat'], 0
fan     = ['Auto' for i in range(5)]
swing   = ['Continously' for i in range(5)]
time, n = 0, 0
anti_b   = 'OFF'
energy_s = 'OFF'


def visual(on_switch):
    global switch
    
    if on_switch == True:

        if i == 0:
            top_1_label['text'] = f'{mode[i]}'
            top_2_label['text'] = ""
            top_3_label['text'] = ""
            top_4_label['text'] = ""
            top_5_label['text'] = ""

        elif i == 1:
            top_2_label['text'] = f'{mode[i]}'
            top_1_label['text'] = ""
            top_3_label['text'] = ""
            top_4_label['text'] = ""
            top_5_label['text'] = ""

        elif i == 2:
            top_3_label['text'] = f'{mode[i]}'
            top_2_label['text'] = ""
            top_1_label['text'] = ""
            top_4_label['text'] = ""
            top_5_label['text'] = ""

        elif i == 3:
            top_4_label['text'] = f'{mode[i]}'
            top_2_label['text'] = ""
            top_3_label['text'] = ""
            top_1_label['text'] = ""
            top_5_label['text'] = ""

        elif i == 4:
            top_5_label['text'] = f'{mode[i]}'
            top_2_label['text'] = ""
            top_3_label['text'] = ""
            top_4_label['text'] = ""
            top_1_label['text'] = ""
           
        left_1_label['text'] = f'Fan: {fan[i]}\nSwing: {swing[i]}   '
        left_2_label['text'] = f'Anti Bacteria Mode: {anti_b} \nEnergy Saving Mode: {energy_s}'
        right_label['text'] = f'{temp[i]} °C'
        top_right_bottom_label['text'] = "TEST"
        
        switch = False

    else:
        top_1_label['text'] = ""
        top_2_label['text'] = ""
        top_3_label['text'] = ""
        top_4_label['text'] = ""
        top_5_label['text'] = ""
        left_1_label['text'] = ""
        left_2_label['text'] = ""
        right_label['text'] = ""
        top_right_bottom_label['text'] = ""
        
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
    global time, n

    # if on_switch == False:
    pass

root = tk.Tk()
root.title("Remote AC")
on_switch_image = tk.PhotoImage(file="on-off-power-button.png")

canvas = tk.Canvas(root, height= 500, width=300, bg="#F4F4F2")
canvas.pack()


top_top_frame = tk.Frame(root, bg='#E8E8E8')
top_top_frame.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)


top_right_frame = tk.Frame(root, bg='#E8E8E8')
top_right_frame.place(relx=0.6, rely=0.15, relwidth=0.3, relheight=0.2)


top_right_bottom_frame = tk.Frame(root, bg='#E8E8E8')
top_right_bottom_frame.place(relx=0.6, rely=0.3, relwidth=0.3, relheight=0.05)


top_left_1_frame = tk.Frame(root, bg='#E8E8E8')
top_left_1_frame.place(relx=0.1, rely=0.15, relwidth=0.5, relheight=0.1)


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


left_1_label = tk.Label(top_left_1_frame, bg='#E8E8E8', anchor='n')
left_1_label.place(relwidth=1, relheight=1)


left_2_label = tk.Label(top_left_2_frame, bg='#E8E8E8')
left_2_label.place(relwidth=1, relheight=1)


right_label = tk.Label(top_right_frame, bg='#E8E8E8', anchor='n')
right_label.config(font=('helvetica', 28))
right_label.place(relwidth=1, relheight=1)


top_right_bottom_label = tk.Label(top_right_bottom_frame, bg='#E8E8E8', anchor='n')
top_right_bottom_label.place(relwidth=1, relheight=1)

root.mainloop()
