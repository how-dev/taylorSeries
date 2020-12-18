from tkinter import *
import math
# ----------------------------------------------------------------------------------------------------------------------
taylor = Tk()
taylor['bg'] = 'pink'
taylor.title('Série de Howard')
# ----------------------------------------------------------------------------------------------------------------------


def seq():
    if str(eni.get()).isalpha() is False and str(lim.get()).isalpha() is False and str(var.get()).isalpha()\
            is False and str(con.get()).isalpha() is False:
        n = int(eni.get())
        i = int(lim.get())
        x = float(var.get())
        a = float(con.get())
        if n > i:
            res['text'] = '>n< sendo maior que >i<, o resultado é 0'
            res['font'] = 'Times', 11, 'bold'
        else:
            soma = 0
            for n in range(n, i + 1):
                soma += a / math.factorial(n) * math.pow(x - a, n)
            res['text'] = 'O resultado dessa somatória vale: {:.2f}'.format(soma)
            res['font'] = 'Times', 11, 'bold'
    else:
        res['text'] = 'Não numérico!'
        res['font'] = 'Times', 11, 'bold'


# ----------------------------------------------------------------------------------------------------------------------
eni = Entry(taylor, bd=2)
eni.place(x=52, y=70)
lim = Entry(taylor, bd=2)
lim.place(x=52, y=90)
var = Entry(taylor, bd=2)
var.place(x=52, y=110)
con = Entry(taylor, bd=2)
con.place(x=52, y=130)
# ----------------------------------------------------------------------------------------------------------------------
nl = Label(taylor, text='n  =', bg='pink', font=("Times", 10, 'bold'))
nl.place(x=18, y=70)
il = Label(taylor, text='i   =', bg='pink', font=("Times", 10, 'bold'))
il.place(x=18, y=90)
xl = Label(taylor, text='x  =', bg='pink', font=("Times", 10, 'bold'))
xl.place(x=18, y=110)
al = Label(taylor, text='a  =', bg='pink', font=("Times", 10, 'bold'))
al.place(x=18, y=130)
# ----------------------------------------------------------------------------------------------------------------------
res = Label(taylor, text='Resultado: ', bg='pink', font=("Times", 15, 'bold'))
res.place(x=50, y=154)
lb = Label(taylor, text=' Σ ', bg='pink', font=("Times", 20, 'bold'))
lb.place(x=260, y=93)
lb = Label(taylor, text='f(x) =', bg='pink', font=("Times", 10, 'bold'))
lb.place(x=235, y=100)
lb = Label(taylor, text='i', bg='pink', font=("Times", 10, 'bold'))
lb.place(x=275, y=82)
lb = Label(taylor, text='n', bg='pink', font=("Times", 10, 'bold'))
lb.place(x=273, y=121)
lb = Label(taylor, text='_', bg='pink', font=("Times", 22, 'bold'))
lb.place(x=292, y=78)
lb = Label(taylor, text='a', bg='pink', font=("Times", 10, 'bold'))
lb.place(x=295, y=90)
lb = Label(taylor, text='n!', bg='pink', font=("Times", 10, 'bold'))
lb.place(x=295, y=113)
lb = Label(taylor, text='(x - a)', bg='pink', font=("Times", 10, 'bold'))
lb.place(x=312, y=99)
lb = Label(taylor, text='n', bg='pink', font=("Times", 10, 'bold'))
lb.place(x=345, y=90)
lb = Label(taylor, text='Série de Taylor', bg='purple', font=("Times", 25, 'bold'))
lb.pack(side=TOP, fill=X)
# ----------------------------------------------------------------------------------------------------------------------
parede = Label(taylor, text='', bg='purple')
parede.pack(side=LEFT, fill=Y)
parede = Label(taylor, text='', bg='purple')
parede.pack(side=RIGHT, fill=Y)
# ----------------------------------------------------------------------------------------------------------------------
bt = Button(taylor, text='Calcular', width=35, height=2, command=seq, bg='purple', bd=8)
bt.place(x=30, y=200)
# ----------------------------------------------------------------------------------------------------------------------
taylor.geometry('380x270+1200+300')
taylor.mainloop()
# ----------------------------------------------------------------------------------------------------------------------
