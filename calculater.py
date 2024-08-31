import tkinter as tk
win=tk.Tk()
win.title("calculater")
win.geometry("365x480")
win.configure(bg="blue")
win.resizable(False, False)

def num(x):
    val=e1.get()
    e1.delete(0,"end")
    e1.insert(0,val+x)
def symbol(x):
    val=e1.get()
    if val[-1]=="+" or val[-1]=="-" or val[-1]=="*" or val[-1]=="/" or val[-1]=="%":
        e1.delete(len(val)-1)
        e1.insert(len(val)-1,x)
    else:
        e1.insert(len(val),x)
def clear(x):
    if x=="c":
        e1.delete(0,"end")
    if x=="x":
        val=e1.get()
        e1.delete(len(val)-1)

def equal():
    val=e1.get()
    e1.delete(0,"end")
    e1.insert(0,eval(val))
    

e1 = tk.Entry(win, width=24,bg="blue",fg="white",font=("areal",20))
e1.grid(row=0,column=0,columnspan=4)
bc= tk.Button(win,height=2,width=5,text="C",font=("areal",20),command=lambda:clear("c"))
bc.grid(row=1,column=0)
bx= tk.Button(win,height=2,width=5,text="x",font=("areal",20),command=lambda:clear("x"))
bx.grid(row=1,column=1)
bdd= tk.Button(win,height=2,width=5,text="%",font=("areal",20),command=lambda:symbol("%"))
bdd.grid(row=1,column=2)
bp= tk.Button(win,height=2,width=5,text="+",font=("areal",20),command=lambda:symbol("+"))
bp.grid(row=1,column=3)
b9= tk.Button(win,height=2,width=5,text="9",font=("areal",20),command=lambda:num("9"))
b9.grid(row=2,column=0)
b8= tk.Button(win,height=2,width=5,text="8",font=("areal",20),command=lambda:num("8"))
b8.grid(row=2,column=1)
b7= tk.Button(win,height=2,width=5,text="7",font=("areal",20),command=lambda:num("7"))
b7.grid(row=2,column=2)
bs= tk.Button(win,height=2,width=5,text="-",font=("areal",20),command=lambda:symbol("-"))
bs.grid(row=2,column=3)
b6= tk.Button(win,height=2,width=5,text="6",font=("areal",20),command=lambda:num("6"))
b6.grid(row=3,column=0)
b5= tk.Button(win,height=2,width=5,text="5",font=("areal",20),command=lambda:num("5"))
b5.grid(row=3,column=1)
b4= tk.Button(win,height=2,width=5,text="4",font=("areal",20),command=lambda:num("4"))
b4.grid(row=3,column=2)
bd= tk.Button(win,height=2,width=5,text="/",font=("areal",20),command=lambda:symbol("/"))
bd.grid(row=3,column=3)
b3= tk.Button(win,height=2,width=5,text="3",font=("areal",20),command=lambda:num("3"))
b3.grid(row=4,column=0)
b2= tk.Button(win,height=2,width=5,text="2",font=("areal",20),command=lambda:num("2"))
b2.grid(row=4,column=1)
b1= tk.Button(win,height=2,width=5,text="1",font=("areal",20),command=lambda:num("1"))
b1.grid(row=4,column=2)
bm= tk.Button(win,height=2,width=5,text="*",font=("areal",20),command=lambda:symbol("*"))
bm.grid(row=4,column=3)
bdo= tk.Button(win,height=2,width=5,text=".",font=("areal",20),command=lambda:num("."))
bdo.grid(row=5,column=0)
b0= tk.Button(win,height=2,width=5,text="0",font=("areal",20),command=lambda:num("0"))
b0.grid(row=5,column=1)
be= tk.Button(win,height=2,width=10,text="=",fg="red",font=("areal",22), command=equal)
be.grid(row=5,column=2,columnspan=2)

win.mainloop()