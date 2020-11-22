from os import system
import time
import datetime

#  Anggota Kelompok:
#   1. Adiyansa Prasetya Wicaksana (16520227)
#   2. Muhammad Daffa Rasyid (16520147)
#   3. Mumtaz Humam Alfian Zulva (16520447)

# KAMUS
# switch = boolean
# temp = int
# mode = int
# temp = int
# fan = int




# ALGORITMA


#-Penetapan-variabel------------------------------------------------------------
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

#-Pembuatan-function------------------------------------------------------------
def clear():
    system("cls")


def visual():
    if switch == True:
        print(f'Temp: {temp}                   Fan: {fan[i]}')
        print(f'Mode: {mode[i]}                 Swing: {swing[i]}')
        print(f'Anti Bacteria Mode: {anti_b}    Energy Saving Mode: {energy_s}   ')
        print(datetime.datetime.now().strftime("%A, %H:%M"))
        print('Timer:', str(t_hour).zfill(2), ":", str(t_min).zfill(2), ":", str(t_sec).zfill(2))

    else:
        print("OFF")

def timer():
    global t_hour, t_min, t_sec, switch

    print("Set timer:")
    t_hour = int(input("Jam: "))
    t_min = int(input("Menit: "))
    t_sec = int(input("Detik: "))
    while True:            
        t_sec -= 1
        time.sleep(1)
        clear()
        visual()
        if t_hour == 0 and t_min == 0 and t_sec == 0:
            switch = False
            break
        if t_sec == 0:
            t_sec = 60
            t_min -= 1
        if t_min == -1:
            t_min = 59
            t_hour -= 1
        if t_hour == -1:
            t_hour = 23
        
            

def remote():
    global switch, temp, mode, i, fan, swing, anti_b, energy_s

    visual()

    print("""
    List of Instructions:
    1. ON/OFF
    2. Temp Up
    3. Temp Down
    4. Mode
    5. Fan
    6. Swing
    7. Anti Bacteria Mode
    8. Energy Saving Mode
    9. Set timer
    """
    )

    remote_input = input("Your instructions: ")

    while type(remote_input) == str:
        try:
            remote_input = int(remote_input)
        except:
            print("Your instruction must be a number.")
            remote_input = input("Your instructions: ")


    while remote_input not in range(1, 10):
        print("Your instructions is not in the list.")
        remote_input = int(input("Your instrucions: "))

    if remote_input == 1:
        
        if switch == True:
            switch = False

        else:
            switch = True

    elif remote_input == 2:
        
        if i == 0 or 1 or 2 :
            if temp[i] == 30:
                temp[i] = 30
            else:
                temp[i] += 1
        elif i == 3 or 4 :
            if temp[i] == 35:
                temp[i] = 35
            else:
                temp[i] += 1

    elif remote_input == 3:
        
        if i == 0 or 1 or 2 :
            if temp[i] == 16:
                temp[i] = 16
            else:
                temp[i] -= 1
        elif i == 3 or 4 :
            if temp[i] == 20:
                temp[i] = 20
            else:
                temp[i] += 1

    elif remote_input == 4:
        
        if  i == 4:
            i = 0
        
        else:
            i += 1

    elif remote_input == 5:
        
        if fan[i] == 3:
            fan[i] = "Auto"
        
        elif fan[i] == "Auto":
            fan[i] = 1
        
        else:
            fan[i] += 1

    elif remote_input == 6:
        
        if  swing[i] == "up":
            swing[i] = "mid"
        
        elif swing[i] == "mid":
             swing[i]  = "down"
        
        elif swing[i] == "down":
             swing[i]  = "continously"
        
        else:#swing[i] == "continously"
              swing[i]  = "up"

    elif remote_input == 7:
        
        if anti_b == "OFF":
            anti_b = "ON"
        
        else:#anti_b=="ON"
            anti_b = "OFF"

    elif remote_input == 8:

        if energy_s == "OFF":
            energy_s = "ON"
        
        else:#energy_s=="ON"
            energy_s = "OFF"

    elif remote_input == 9:
        timer()
    
    clear()


#-Program-yg-dijalankan---------------------------------------------------------
clear()

switch = True
while switch == True:
    remote()
else:
    visual()
