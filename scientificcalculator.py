from tkinter import *
import math
#some font
font=('Consolas',15)#,'bold underline')

#function
def btnfun(event):
    b=event.widget
    if b['text']=='C':
        textfield.delete(0, END)
        return
    if b['text']=='D':
        ex = textfield.get()
        textfield.delete(0, END)
        textfield.insert(END, ex[:-1])
        return


    if b['text']=='=':
        try:
           ex=eval(textfield.get())
           textfield.delete(0,END)
           textfield.insert(END,ex)
           return
        except:
            textfield.delete(0, END)
            textfield.insert(END, 'Invalid expression')
            return


    textfield.insert(END,b['text'])
    #print(f)


#create a window
window=Tk()
window.title('Scientific cal')
window.geometry('450x300')
#creating heading
headlabel=Label(window,text='Normal Calculator',fg='red',font=('Consolas',16,'bold underline'),justify='center')
headlabel.pack()
#textfield
textfield=Entry(window,font=font,justify=CENTER,relief='solid',width=30)
textfield.pack(pady=10)
#Buttors
buttonframe=Frame(window)
buttonframe.pack()
#addinf button
tem=1
for i in range(3):
    for j in range(3):
        button = Button(buttonframe, text=str(tem),activebackground='orange',activeforeground='white', font=font,width=8,relief='solid')
        button.grid(row=i, column=j,padx=2,pady=2)
        button.bind('<Button-1>',btnfun)
        tem+=1
s=['0','.','=']
for k in range(3):
    button = Button(buttonframe, text=s[k], font=font, width=8, relief='solid',activebackground='orange',activeforeground='white')
    button.grid(row=3, column=k,padx=2,pady=2)
    button.bind('<Button-1>', btnfun)
s=['+','-','/','*']
for i in range(4):
    button = Button(buttonframe, text=s[i], font=font, width=8, relief='solid', activebackground='orange',
                    activeforeground='white')
    button.grid(row=i, column=3,padx=2,pady=2)
    button.bind('<Button-1>', btnfun)
button1 = Button(buttonframe, text='C', font=font, width=18, relief='solid', activebackground='orange',
                    activeforeground='white')
button1.grid(row=4, column=0,columnspan=2,padx=2,pady=2)
button1.bind('<Button-1>',btnfun)
button2 = Button(buttonframe, text='D', font=font, width=18, relief='solid', activebackground='orange',
                    activeforeground='white')
button2.grid(row=4, column=2,columnspan=2,padx=2,pady=2)
button2.bind('<Button-1>',btnfun)

###############################################################################################
#functions
def cal_sc(event):
    bt=event.widget
    tst=''
    if bt['text']=='√ ':
        try:
            ex = eval(textfield.get())
            tst=str(math.sqrt(ex))
        except:
            textfield.delete(0, END)
            textfield.insert(END, 'Invalid expression')
            return
        pass
    elif bt['text']=='^':
        try:
            ex =textfield.get().split(' ')
            tst=str(math.pow(int(ex[0]),int(ex[1])))
        except:
            textfield.delete(0, END)
            textfield.insert(END, 'Invalid expression')
            return
        pass
    elif bt['text']=='x!':
        try:
            ex = eval(textfield.get())
            tst=str(math.factorial(ex))
        except:
            textfield.delete(0, END)
            textfield.insert(END, 'Invalid expression')
            return
        pass
    elif bt['text']=='toRad':
        try:
            ex = eval(textfield.get())
            tst=str(math.radians(ex))
        except:
            textfield.delete(0, END)
            textfield.insert(END, 'Invalid expression')
            return
        pass
    elif bt['text']=='toDeg':
        try:
            ex = eval(textfield.get())
            tst=str(math.degrees(ex))
        except:
            textfield.delete(0, END)
            textfield.insert(END, 'Invalid expression')
            return
        pass
    elif bt['text'] == 'sin(θ)':
        try:
            ex = eval(textfield.get())
            tst=str(math.sin(ex))
        except:
            textfield.delete(0, END)
            textfield.insert(END, 'Invalid expression')
            return
        pass
    elif bt['text'] =='cos(θ)':
        try:
            ex = eval(textfield.get())
            tst=str(math.cos(ex))
        except:
            textfield.delete(0, END)
            textfield.insert(END, 'Invalid expression')
            return
        pass
    elif bt['text'] =='log()':
        try:
            ex = eval(textfield.get())
            tst=str(math.log(ex))
        except:
            textfield.delete(0, END)
            textfield.insert(END, 'Invalid expression')
            return
        pass
    elif bt['text'] =='cosec(θ)':
        try:
            ex = eval(textfield.get())
            tst=str(math.sinh(ex))
        except:
            textfield.delete(0, END)
            textfield.insert(END, 'Invalid expression')
            return
        pass
    elif bt['text'] =='tanh(θ)':
        try:
            ex = eval(textfield.get())
            tst=str(math.tanh(ex))
        except:
            textfield.delete(0, END)
            textfield.insert(END, 'Invalid expression')
            return
        pass
    elif bt['text'] =='cosh(θ)':
        try:
            ex = eval(textfield.get())
            tst=str(math.cosh(ex))
        except:
            textfield.delete(0, END)
            textfield.insert(END, 'Invalid expression')
            return
        pass
    else:
        try:
            ex = eval(textfield.get())
            tst=str(math.tan(ex))
        except:
            textfield.delete(0, END)
            textfield.insert(END, 'Invalid expression')
            return
        pass
    textfield.delete(0, END)
    textfield.insert(END, tst)


scframe=Frame(window)
busqrt = Button(scframe, text='√ ', font=font, width=8, relief='solid', activebackground='orange',
                    activeforeground='white')
busqrt.grid(row=0, column=2,padx=2,pady=2)
busqrt.bind('<Button-1>',cal_sc)
bupow = Button(scframe, text='^', font=font, width=8, relief='solid', activebackground='orange',
                    activeforeground='white')
bupow.grid(row=0, column=1,padx=2,pady=2)
bupow.bind('<Button-1>',cal_sc)
bufac = Button(scframe, text='x!', font=font, width=8, relief='solid', activebackground='orange',
                    activeforeground='white')
bufac.grid(row=0, column=0,padx=2,pady=2)
bufac.bind('<Button-1>',cal_sc)
burad = Button(scframe, text='toRad', font=font, width=8, relief='solid', activebackground='orange',
                    activeforeground='white')
burad.grid(row=0, column=3,padx=2,pady=2)
burad.bind('<Button-1>',cal_sc)
budeg = Button(scframe, text='toDeg', font=font, width=8, relief='solid', activebackground='orange',
                    activeforeground='white')
budeg.grid(row=1, column=3,padx=2,pady=2)
budeg.bind('<Button-1>',cal_sc)
busin = Button(scframe, text='sin(θ)', font=font, width=8, relief='solid', activebackground='orange',
                    activeforeground='white')
busin.grid(row=1, column=0,padx=2,pady=2)
busin.bind('<Button-1>',cal_sc)
bucos = Button(scframe, text='cos(θ)', font=font, width=8, relief='solid', activebackground='orange',
                    activeforeground='white')
bucos.grid(row=1, column=1,padx=2,pady=2)
bucos.bind('<Button-1>',cal_sc)
butan = Button(scframe, text='tan(θ)', font=font, width=8, relief='solid', activebackground='orange',
                    activeforeground='white')
butan.grid(row=1, column=2,padx=2,pady=2)
butan.bind('<Button-1>',cal_sc)
bulog = Button(scframe, text='log()', font=font, width=8, relief='solid', activebackground='orange',
                    activeforeground='white')
bulog.grid(row=2, column=3,padx=3,pady=2)
bulog.bind('<Button-1>',cal_sc)
burs = Button(scframe, text='sinh(θ)', font=font, width=8, relief='solid', activebackground='orange',
                    activeforeground='white')
burs.grid(row=2, column=0,padx=2,pady=2)
burs.bind('<Button-1>',cal_sc)
burc = Button(scframe, text='cosh(θ)', font=font, width=8, relief='solid', activebackground='orange',
                    activeforeground='white')
burc.grid(row=2, column=1,padx=2,pady=2)
burc.bind('<Button-1>',cal_sc)
burt = Button(scframe, text='tanh(θ)', font=font, width=8, relief='solid', activebackground='orange',
                    activeforeground='white')
burt.grid(row=2, column=2,padx=2,pady=2)
burt.bind('<Button-1>',cal_sc)



global normal
normal=True


def scl():
    global normal
    if normal==True:
        headlabel.config(text='scientific calculator ')
        normal=False
        window.geometry('600x500')
        buttonframe.pack_forget()
        scframe.pack(pady=20)
        buttonframe.pack()
    else:
        headlabel.config(text='Normal calculator ')
        scframe.pack_forget()
        window.geometry('450x300')
        normal = True


menubar=Menu(window)
mode=Menu(menubar,font=('Consolas',10),tearoff=0)
mode.add_checkbutton(label='scientific calculator ',command=scl)
menubar.add_cascade(label='Mode',menu=mode)
window.config(menu=menubar)



window.mainloop()
