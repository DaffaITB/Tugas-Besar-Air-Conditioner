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


#-Penetapan-variabel------------------------------
switch = True
temp = 18
mode = 1
fan = 2
swing = 'OFF'
anti_b = 'OFF'
energy_s = 'OFF'

#-Pembuatan-function------------------------------
def clear():
    system("cls")


def visual():
    if switch == True:
        print(f'Temp: {temp}   '  + f'Fan: {fan}')
        print(f'Mode: {mode}    ' + f'Swing: {swing}')
        print(f'Anti Bacteria Mode: {anti_b}    ' + f'Energy Saving Mode: {energy_s}   ')
    else:
        print("OFF")


def remote():
    global switch, temp, mode, fan, swing, anti_b, energy_s

    visual()

    print("""
    List of Instructions:
    1. ON
    2. OFF
    3. Temp Up
    4. Temp Down
    5. Mode
    6. Fan
    7. Swing ON
    8. Swing OFF
    9. Anti Bacteria Mode ON
    10. Anti Bacteria Mode OFF
    11. Energy Saving Mode ON
    12. Energy Saving Mode OFF
    """
    )

    remote_input = int(input("Your instructions: "))

    while remote_input not in range(1, 13):
        print("Your instructions is not in the list.")
        remote_input = int(input("Your instrucions: "))

    if remote_input == 1:
        
        switch = True

    elif remote_input == 2:
        
        switch = False

    elif remote_input == 3:
        
        if temp == 30:
            temp = temp

        else:
            temp += 1

    elif remote_input == 4:
        
        if temp == 18:
            temp = temp

        else:
            temp -= 1

    elif remote_input == 5:
        
        if mode == 4:
            mode = 1

        else:
            mode += 1

    elif remote_input == 6:
        
        if fan == 3:
            fan = 1

        else:
            fan += 1

    elif remote_input == 7:
        
        swing = "Auto"

    elif remote_input == 8:
        
        swing = "OFF"
    
    elif remote_input == 9:

        anti_b = "ON"

    elif remote_input == 10:

        anti_b = "OFF"

    elif remote_input == 11:

        energy_s = "ON"
    
    elif remote_input == 12:

        energy_s = "OFF"
    clear()


#-Program-yg-dijalankan---------------------------
clear()

switch = True
while switch == True:
    remote()
else:
    visual()