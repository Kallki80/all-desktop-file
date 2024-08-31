import tkinter as tk
win=tk.Tk()
win.title("tic tac toe")
win.geometry("470x555")
win.configure(bg="purple")

turn=1
def fun(x):
    global turn
    if turn==1:
        # x.configure(text="O")  we can also write it like this
        x["text"]="O"
        turn=2
    else:
        x.configure(text="X")
        turn=1
    



lab1=tk.Label(win,text="Game",font=("Bradley Hand ITC",28),bg="purple",fg="white").grid(row=0,column=0,columnspan=3)
but4=tk.Button(win,text="",height=10,width=20,bd=5,bg="#e5fbd6",command=lambda:fun(but4))
but4.grid(row=1,column=0)
but5=tk.Button(win,text="",height=10,width=20,bd=5,bg="#e5fbd6",command=lambda:fun(but5))
but5.grid(row=1,column=1)
but6=tk.Button(win,text="",height=10,width=20,bd=5,bg="#e5fbd6",command=lambda:fun(but6))
but6.grid(row=1,column=2)
but7=tk.Button(win,text="",height=10,width=20,bd=5,bg="#e5fbd6",command=lambda:fun(but7))
but7.grid(row=2,column=0)
but8=tk.Button(win,text="",height=10,width=20,bd=5,bg="#e5fbd6",command=lambda:fun(but8))
but8.grid(row=2,column=1)
but9=tk.Button(win,text="",height=10,width=20,bd=5,bg="#e5fbd6",command=lambda:fun(but9))
but9.grid(row=2,column=2)
but1=tk.Button(win,text="",height=10,width=20,bd=5,bg="#e5fbd6",command=lambda:fun(but1))
but1.grid(row=3,column=0)
but2=tk.Button(win,text="",height=10,width=20,bd=5,bg="#e5fbd6",command=lambda:fun(but2))
but2.grid(row=3,column=1)
but3=tk.Button(win,text="",height=10,width=20,bd=5,bg="#e5fbd6",command=lambda:fun(but3))
but3.grid(row=3,column=2)

win.mainloop()