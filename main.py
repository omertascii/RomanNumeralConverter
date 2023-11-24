import tkinter
from tkinter import *
from tkinter import messagebox

window = Tk()
FONT = ('poppins', 25, 'bold')


def window_settings():
    bg1 = '#f87a17'
    bg2 = '#fd580a'
    window.title("Roman Numeral Converter")
    window.config(bg=bg1)

    my_label1 = Label(window,text="Bir roma rakamı giriniz",font=FONT,bg=bg1)
    my_label1.pack(padx=25,pady=20)

    entry = Entry(window,bg=bg2,fg='white')
    entry.pack(padx=25, pady=10)
    entry.focus()


    my_button = Button(window, text="Hesapla",bg=bg2, command=lambda: button_click(entry=entry, my_label2= my_label2))
    my_button.pack()

    divider = Canvas(window, height=1, bg=bg2)
    divider.pack(fill='x')

    my_label2 = Label(window,text=f"Result:",font=FONT, bg=bg1)
    my_label2.pack(padx=10,pady=10)




def button_click(entry, my_label2):
    num1 = entry.get()

    controls = control(num1)

    if controls:
        result = convert_to_number(num1)
        my_label2.config(text=f'Result: {result}')

    else:
        messagebox.showerror(title="Error!",message="Invalid Value")






def control(num1):
    roman_character = {"I", "V", "X", "L", "C", "D", "M"}
    controls = True
    value_quantity = 1
    current_char = num1[0]

    for character in num1[1:]:
        if character not in roman_character:
            controls = False
            break
        else:
            if character == roman_character:
                value_quantity += 1
            else:
                current_char = character
                value_quantity = 1

        if value_quantity > 3:
            controls = False
            break

    return controls


def convert_to_number(num1):
    roma_number = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":100}

    total = 0
    old_value = 0

    for value in num1[::-1]:
        numeric_value = roma_number[value]

        if numeric_value >= old_value:
            total += numeric_value
        else:
            total -= numeric_value

        old_value = numeric_value
    return total












window_settings()
window.mainloop()


