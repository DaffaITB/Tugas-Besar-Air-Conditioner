from os import system

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

#-Pembuatan-function------------------------------------------------------------
def clear():
    system("cls")


def visual():
    if switch == True:
        print(f'Temp: {temp[i]}                   Fan: {fan[i]}')
        print(f'Mode: {mode[i]}                 Swing: {swing[i]}')
        print(f'Anti Bacteria Mode: {anti_b}    Energy Saving Mode: {energy_s}   ')
    else:
        print("OFF")


def remote():
    global switch, temp, mode, i, fan, swing, anti_b, energy_s

    visual()

    print("""
    List of Instructions:
    1. ON
    2. OFF
    3. Temp Up
    4. Temp Down
    5. Mode
    6. Fan
    7. Swing
    8. Anti Bacteria Mode
    9. Energy Saving Mode
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
        
        switch = True

    elif remote_input == 2:
        
        switch = False

    elif remote_input == 3:
        
        if temp[0] == 30:
            temp[0] = 30
        elif temp[1] == 30:
            temp[1] = 30
        elif temp[2] == 30:
            temp[2] = 30
        elif temp[3] == 35:
            temp[3] = 35
        elif temp[4] == 35:
            temp[4] = 35

        else:
            temp[i] += 1

    elif remote_input == 4:
        
        if temp[0] == 16:
            temp[0] = 16
        elif temp[1] == 16:
            temp[1] = 16
        elif temp[2] == 16:
            temp[2] = 16
        elif temp[3] == 20:
            temp[3] = 20
        elif temp[4] == 20:
            temp[4] = 20
        
        else:
            temp[i] -= 1

    elif remote_input == 5:
        
        if  i == 4:
            i = 0
        
        else:
            i += 1

    elif remote_input == 6:
        
        if fan[i] == 3:
            fan[i] = "Auto"
        
        elif fan[i] == "Auto":
            fan[i] = 1
        
        else:
            fan[i] += 1

    elif remote_input == 7:
        
        if  swing[i] == "up":
            swing[i] = "mid"
        
        elif swing[i] == "mid":
             swing[i]  = "down"
        
        elif swing[i] == "down":
             swing[i]  = "continously"
        
        else:#swing[i] == "continously"
              swing[i]  = "up"

    elif remote_input == 8:
        
        if anti_b == "OFF":
            anti_b = "ON"
        
        else:#anti_b=="ON"
            anti_b = "OFF"

    elif remote_input == 9:

        if energy_s == "OFF":
            energy_s = "ON"
        
        else:#energy_s=="ON"
            energy_s = "OFF"
    
    clear()


#-Program-yg-dijalankan---------------------------------------------------------
clear()

switch = True
while switch == True:
    remote()
else:
    visual()
