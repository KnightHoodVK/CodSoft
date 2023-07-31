from tkinter import *
import math

root=Tk()
root.title('Calculator')
root.geometry('245x170')

L=Label(root, text = "Caclulator")
L.place(x=2, y=10)
output=StringVar()
output_field = Entry(root, width = 39, textvariable=output, justify='center')
output_field.place(x=2, y=30)
output_field.focus()

result = ''

def press(num):
    global result
    result = result + str(num)
    output.set(result)

def eqi():
    global result
    total = str(eval(result))
    output.set(total)
    result = ""

def clear():
    global result
    result = ""
    output.set(result)

button1 = Button(root, text=' 1 ', command=lambda: press(1), height=1, width=7)
button2 = Button(root, text=' 2 ', command=lambda: press(2), height=1, width=7)
button3 = Button(root, text=' 3 ', command=lambda: press(3), height=1, width=7)
button4 = Button(root, text=' 4 ', command=lambda: press(4), height=1, width=7)
button5 = Button(root, text=' 5 ', command=lambda: press(5), height=1, width=7)
button6 = Button(root, text=' 6 ', command=lambda: press(6), height=1, width=7)
button7 = Button(root, text=' 7 ', command=lambda: press(7), height=1, width=7)
button8 = Button(root, text=' 8 ', command=lambda: press(8), height=1, width=7)
button9 = Button(root, text=' 9 ', command=lambda: press(9), height=1, width=7)
button0 = Button(root, text=' 0 ', command=lambda: press(0), height=1, width=7)

button7.place(x=2, y=80)
button8.place(x=62, y=80)
button9.place(x=122, y=80)

button4.place(x=2, y=105)
button5.place(x=62, y=105)
button6.place(x=122, y=105)

button1.place(x=2, y=130)
button2.place(x=62, y=130)
button3.place(x=122, y=130)

multiply = Button(root, text=' * ', command=lambda: press("*"), height=1, width=7)
divide = Button(root, text=' / ', command=lambda: press("/"), height=1, width=7)
decimal= Button(root, text='.', command=lambda: press('.'), height=1, width=7)
clear = Button(root, text='Clear', command=clear, height=1, width=7)
plus = Button(root, text=' + ', command=lambda: press("+"), height=1, width=7)
minus = Button(root, text=' - ', command=lambda: press("-"), height=1, width=7)
equal = Button(root, text=' = ', command=eqi, height=1, width=7)

multiply.place(x=2, y=55)
divide.place(x=62, y=55)
decimal.place(x=122, y=55)
clear.place(x=182, y=55)
plus.place(x=182, y=80)
minus.place(x=182, y=105)
equal.place(x=182, y=130)

root.mainloop()
