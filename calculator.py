from tkinter import Frame,Button,Label, StringVar,Tk

calci = Tk()
calci.geometry("500x500+450+100")
calci.resizable(0,0)

# button functions
data= StringVar()
val=""
def btn1_click():
    global val
    val=val+"1"
    data.set(val)
def btn2_click():
    global val
    val=val+"2"
    data.set(val)
def btn3_click():
    global val
    val=val+"3"
    data.set(val) 
def btnplus_click():
    global val
    val=val+"+"
    data.set(val)
def btn4_click():
    global val
    val=val+"4"
    data.set(val)
def btn5_click():
    global val
    val=val+"5"
    data.set(val)  
def btn6_click():
    global val
    val=val+"6"
    data.set(val)
def btnminus_click():
    global val
    val=val+"-"
    data.set(val) 
def btn7_click():
    global val
    val=val+"7"
    data.set(val)
def btn8_click():
    global val
    val=val+"8"
    data.set(val)
def btn9_click():
    global val
    val=val+"9"
    data.set(val)  
def btnmultiply_click():
    global val
    val=val+"*"
    data.set(val) 
def btnC_click():
    global val
    val=""
    data.set(val)
def btn0_click():
    global val
    val=val+"0"
    data.set(val)  
def btnequal_click():
    global val
    val=str(eval(val))
    data.set(val)
def btndivide_click():
    global val
    val=val+"/"
    data.set(val)    


calcilabel=Label(calci,text="",font=("arial",20,"bold"),anchor="se",textvariable=data)  
calcilabel.pack(fill="both",expand=True)
frame1=Frame(calci,bg="orange")
frame1.pack(fill="both",expand=True)
frame2=Frame(calci,bg="yellow")
frame2.pack(fill="both",expand=True)
frame3=Frame(calci,bg="blue")
frame3.pack(fill="both",expand=True)
frame4=Frame(calci,bg="green")
frame4.pack(fill="both",expand=True)  
# frame1 buttons
btn1=Button(frame1,text="1",font=("arial",20,"bold"),border=0,command=btn1_click)
btn1.pack(fill="both",expand=True,side="left")
btn2=Button(frame1,text="2",font=("arial",20,"bold"),border=0,command=btn2_click)
btn2.pack(fill="both",expand=True,side="left")
btn3=Button(frame1,text="3",font=("arial",20,"bold"),border=0,command=btn3_click)
btn3.pack(fill="both",expand=True,side="left")
btnplus=Button(frame1,text="+",font=("arial",20,"bold"),border=0,command=btnplus_click)
btnplus.pack(fill="both",expand=True,side="left")
# frame2 buttons
btn4=Button(frame2,text="4",font=("arial",20,"bold"),border=0,command=btn4_click)
btn4.pack(fill="both",expand=True,side="left")
btn5=Button(frame2,text="5",font=("arial",20,"bold"),border=0,command=btn5_click)
btn5.pack(fill="both",expand=True,side="left")
btn6=Button(frame2,text="6",font=("arial",20,"bold"),border=0,command=btn6_click)
btn6.pack(fill="both",expand=True,side="left")
btnminus=Button(frame2,text="-",font=("arial",20,"bold"),border=0,command=btnminus_click)
btnminus.pack(fill="both",expand=True,side="left")
# frame3 buttons
btn7=Button(frame3,text="7",font=("arial",20,"bold"),border=0,command=btn7_click)
btn7.pack(fill="both",expand=True,side="left")
btn8=Button(frame3,text="8",font=("arial",20,"bold"),border=0,command=btn8_click)
btn8.pack(fill="both",expand=True,side="left")
btn9=Button(frame3,text="9",font=("arial",20,"bold"),border=0,command=btn9_click)
btn9.pack(fill="both",expand=True,side="left")
btnmultiply=Button(frame3,text="*",font=("arial",20,"bold"),border=0,command=btnmultiply_click)
btnmultiply.pack(fill="both",expand=True,side="left")
# frame4 buttons
btnC=Button(frame4,text="C",font=("arial",20,"bold"),border=0,command=btnC_click)
btnC.pack(fill="both",expand=True,side="left")
btn0=Button(frame4,text="0",font=("arial",20,"bold"),border=0,command=btn0_click)
btn0.pack(fill="both",expand=True,side="left")
btnequal=Button(frame4,text="=",font=("arial",20,"bold"),border=0,command=btnequal_click)
btnequal.pack(fill="both",expand=True,side="left")
btndivide=Button(frame4,text="/",font=("arial",20,"bold"),border=0,command=btndivide_click)
btndivide.pack(fill="both",expand=True,side="left")
calci.mainloop()