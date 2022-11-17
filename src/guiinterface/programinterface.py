import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

#inisiasi window
window=Tk()

background = Image.open("background.png")
background2 = background.resize((1532,790), Image.ANTIALIAS)
new_background = ImageTk.PhotoImage(background2)
finalbg = tk.Label(image=new_background)
finalbg.image = new_background
finalbg.place(x=0, y=0)

# membuat lable untuk menampilkan gambar
# foto blank image
blankpic = Image.open("blankpicture.jpg")
blankpic2 = blankpic.resize((256,256), Image.ANTIALIAS)
new_blankpic = ImageTk.PhotoImage(blankpic2)
# lable show image test
lblshowtestpic=Label(window, image=new_blankpic, borderwidth=3, relief='solid')
lblshowtestpic.place(x=615, y=369, height=256, width=256)
# lable closest image test
lblshowresultpic=Label(window, image=new_blankpic, borderwidth=3, relief='solid')
lblshowresultpic.place(x=1117, y=369, height=256, width=256)

folder = ''
folderlabel=Label(window, text=folder[10:],fg='black', bg='#D1FFFC', font='Helvetica 10 bold italic')
folderlabel.place(x=75, y=362)

file = ''
filelabel=Label(window, text=folder[10:],fg='black', bg='#D1FFFC', font='Helvetica 10 bold italic')
filelabel.place(x=75, y=552)

# procedure untuk membuka file gambar
def open_file():
        global img
        filename = filedialog.askopenfilename(initialdir="/images", title="Select Image",
                           filetypes=(("jpg images","*.jpg"),("png images","*.png")))
        img = Image.open(filename)
        img = img.resize((256,256), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        lblshowtestpic['image'] = img
        filelabel.config(text=filename)
# procedure untuk membuka folder
def open_folder():
        global folder
        folder = filedialog.askdirectory(initialdir="/images", title="Select Folder")
        folderlabel.config(text=folder)

# membuat button untuk input data
# button untuk open folder dataset
button1 = Image.open("button1.png")
button1resized=button1.resize((180,40), Image.ANTIALIAS)
buttoninp1 = ImageTk.PhotoImage(button1resized)
btn1=tk.Button(window, image=buttoninp1,borderwidth=0, relief='solid',bg='black', activebackground='black',command=open_folder)
btn1.place(x=75, y=300)
# button unutk open file gambar
button2 = Image.open("button2.png")
button2resized=button2.resize((180,40), Image.ANTIALIAS)
buttoninp2 = ImageTk.PhotoImage(button2resized)
btn2=tk.Button(window, image=buttoninp2,borderwidth=0, relief='solid',bg='black', activebackground='black',command=open_file)
btn2.place(x=75, y=490)
# button unutk result
button3 = Image.open("button3.png")
button3resized=button3.resize((307,132), Image.ANTIALIAS)
buttoninp3 = ImageTk.PhotoImage(button3resized)
btn2=tk.Button(window, image=buttoninp3,borderwidth=0, relief='solid',bg='black', activebackground='black')
btn2.place(x=75, y=625)

# konfigurasi windows
window.configure(bg='#FFD800')
window.title("FACE RECOGNITION CJ-STAR") 
window.geometry("1920x1080")
window.mainloop()