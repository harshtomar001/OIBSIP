from  tkinter import *
from PIL import Image, ImageTk
import random
import pyperclip




window=Tk()
width=800
height=500
img = Image.open("img.png")
img = img.resize((250, 70))
photo = ImageTk.PhotoImage(img)

img1=Image.open("pg.png")
img1=img1.resize((200,70))
photo1=ImageTk.PhotoImage(img1)

window.title("Password Genrator")


window.config(bg="#0af7ef")
window.geometry("1920x1080")



label_1=Label(window,
            text="Password Generator",
            font=("Times New Roman Greek",20,'bold'),
            image=photo,
            pady=20,
            )
label_1.pack(side="top",pady=10)

def focus_in(event):
    if entry.get()=="Enter password length: ":
        entry.delete(0,END)
        entry.config(fg='black')

def focus_out(event):
    if entry.get()=="":
        entry.delete(0,END)
        entry.config(text='Enter password length: ',fg='grey')



entry_var = StringVar()
entry =Entry(window,textvariable=entry_var,fg="grey")
entry_var.set("Enter password length: ")



entry.pack()
entry.bind("<FocusIn>",focus_in)
entry.bind("<FocusOut>",focus_out)

frame=Frame(window,bg="#19f6fa",width=250,height=250,bd=2,relief="solid",padx=20,pady=20)

x=IntVar()
y=IntVar()
z=IntVar()
m=IntVar()
n=IntVar()



checkbox_1=Checkbutton(frame,text="Includes Number",
                       variable=x,
                       onvalue=1,
                       offvalue=0,
                       bg='#19f6fa'
                       ,compound="left",
                       anchor='w',font=("Brush Script MT 16 italic",20,'bold'),
                        activeforeground="black",
                       activebackground='#19f6fa')



checkbox_2=Checkbutton(frame,text="Includes Character",bg='#19f6fa',
                       variable=y,
                       onvalue=1,offvalue=0,
                       compound="left",
                       anchor='w'
                       ,font=("Brush Script MT 16 italic",20,'bold'),
                        activeforeground = "black",
                        activebackground = '#19f6fa'
                                                    )


checkbox_3=Checkbutton(frame,text="Includes uppercase character",bg='#19f6fa'
                       ,variable=z,onvalue=1,offvalue=0,
                       compound="left",
                       anchor='w',font=("Brush Script MT 16 italic",20,'bold'),activeforeground = "black",
                        activebackground = '#19f6fa')


checkbox_4=Checkbutton(frame,text="Includes lowercase character",bg='#19f6fa',
                       variable=m,onvalue=1,offvalue=0,
                       compound="left",
                       anchor='w',font=("Brush Script MT 16 italic",20,'bold'),activeforeground = "black",
                        activebackground = '#19f6fa')


checkbox_5=Checkbutton(frame,text="Includes Special character",bg='#19f6fa',
                       variable=n,onvalue=1,offvalue=0,
                       compound="left",
                       anchor='w',font=("Brush Script MT 16 italic",20,'bold'),activeforeground = "black",
                        activebackground = '#19f6fa')


checkbox_1.pack(fill="x")
#checkbox_2.pack(fill="x")
checkbox_3.pack(fill="x")
checkbox_4.pack(fill="x")
checkbox_5.pack(fill="x")
checkboxes=[(x,checkbox_1),
            (m,checkbox_4),
            (z,checkbox_3),

            (n,checkbox_5)]




def color():
    for c,cb in checkboxes:
        if c.get() == 1:
            cb.config(foreground="#faa40f")  # green when checked
        else:
            cb.config(foreground="black")


for _,cb in checkboxes:
    cb.config(command=color)


frame.pack(pady=12)



def result():

    try:
        label_2.config(height=5,bg='#0af7ef',fg="black")
        button["text"]="Copy"
        button.grid_forget()


        password =""
        final=""
        length = abs(int(entry.get()))
        if length>15:
            label_2.config(text="Too long PASSWORD")
            return
        upper_case=z.get()
        lower_case=m.get()
        numbers=x.get()
        #character =y.get()
        special_chr=n.get()
        u = False
        l = False
        N =  False
        s =  False
        if(upper_case == 1):
            u=True
        if (lower_case==1):
            l=True
        if (numbers==1):
            N=True
        if (special_chr==1):
            s=True

        if not(upper_case | lower_case |  numbers|  special_chr):
            label_2.config(text="Please select atleast one data types")
            return

        if N:
            password+="0123456789142413346524363634532243254363243421"
        if u:
            password+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if l:
            password += "abcdefghijklmnopqrstuvwxyz"
        if s:
            password+='"!@#$%^&*{}?|/.;<,>"'

        for i in range(length):
            final+=random.choice(password)
        frame_2.config(bg="#03fcf4")
        label_2.config(text=final,bg="#a2aee0",fg="#de0d3a",height=2,font=("aerial",20,"bold"))

        button.grid(row=1, column=1)


    except ValueError:
        label_2.config(text='Invalid Password Length!')



def copy():
    text=label_2["text"]
    pyperclip.copy(text)
    button.config(text="Copied!")




button=Button(window,pady=20,text="Generate Password",
              image=photo1,command=result)

button.pack(pady=10)


frame_2=Frame(window)

label_2=Label(frame_2,bg='#0af7ef')
label_2.grid(row=1,column=0)


button = Button(frame_2, command= copy,
                text="Copy",
                padx=10, bg="#0af7ef",
                activebackground="#0af7ef",
                activeforeground='black')


button.grid_forget()

frame_2.pack()

window.mainloop()
