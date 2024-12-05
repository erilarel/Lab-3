import tkinter as tk
import random
from PIL.ImageOps import expand
from redis.cluster import command
import pygame as pg


letters = [ str(i) for i in "abcdefghijklmnopqrstuvwxyz".upper()]
numbers = [ str(x) for x in range(1, 27)]
var = dict(zip(letters, numbers))
interval = [10, 11, 12, 13, 14, 15, 16]

def func_key():
    psw = [0] * 15
    for x in range(len(psw)):
        if x == 5 or x == 10:
            psw[x] = '-'
        else:
            psw[x] = random.choice(letters)

    sum_blok_1 = 0
    for i in psw[:5]:
        sum_blok_1 += int(var[i])
    sum_blok_1 //= len(psw[:5])

    sum_blok_2 = 0
    for i in psw[6:10]:
        sum_blok_2 += int(var[i])
    sum_blok_2 //= len(psw[6:10])

    sum_blok_3 = 0
    for i in psw[11:]:
        sum_blok_3 += int(var[i])
    sum_blok_3 //= len(psw[11:])

    if sum_blok_1 in interval and sum_blok_2 in interval and sum_blok_3 in interval:
        n = ''
        for c in range(len(psw)):
            n += psw[c]
        l2.configure(text=n)
    else:
        func_key()


window = tk.Tk()
window.title("Генерация ключа")
window.geometry('512x410')
window.resizable(width = False, height = False)


logo = tk.PhotoImage(file = 'preview_portal2.png')
bg_logo = tk.Label(window, image=logo)
bg_logo.grid(row = 0, column = 0)


btn = tk.Button(window, text = 'GENERATE KEY', bg='DeepPink4', fg='white', font=('Arial', 15), command = func_key)
btn.place(relx=0.5, rely=0.89, anchor='center')


frame = tk.Frame()
frame.place(relx = 0.5, rely = 0.53, anchor='center')
l2 = tk.Label(frame, text='XXXXX-XXXX-XXXX', background="#FFCDD2", foreground="#B71C1C", font = ('Book Old Style', 25, 'bold'))
l2.pack(expand = True)


pg.mixer.init()
pg.mixer.music.load('No_Cake_for_You_.mp3')
pg.mixer.music.play(-1)

window.mainloop()
