import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from ..img import searchImg

#inisiasi window
window=Tk()

# CANVAS
# membuat canvas utuk shape
canvas=Canvas(window, width=1920, height=1080, bg='#FFD800')
canvas.pack()
# membuat garis pembatas atas
line1=canvas.create_line(100,150,1450,150, fill='black', width=5)
# membuat segu empat untuk frame gambar
rect1=canvas.create_rectangle(525,230,950,680, fill='#FFD1ED', width=5)
rect2=canvas.create_rectangle(1025,230,1450,680, fill='#D1FFFC', width=5)
rect3=canvas.create_rectangle(607,326,868,587, width=5, outline='black')
rect4=canvas.create_rectangle(1107,326,1368,587, width=5, outline='black')

# membuat logo kanan atas
logo = Image.open("src/guiinterface/logo.jpg")
logo2 = logo.resize((260,130), Image.ANTIALIAS)
new_logo = ImageTk.PhotoImage(logo2)
logo2 = tk.Label(image=new_logo, bg='#FFD800')
logo2.image = new_logo
logo2.place(x=1260, y=8)

# membuat label tulisan
# lable title program yang dibuat
lbltitle=Label(window, text="Face Recognition",fg='black', bg='#FCD801', font='Helvetica 40 bold', width=17, height=1, anchor='center')
lbltitle.place(x=500, y=40, height=80)
# lable insert dataset
lbldataset=Label(window, text="Insert Your Dataset",fg='black', bg='#FCD801', font='Helvetica 18 bold')
lbldataset.place(x=100, y=200)
# lable insert image
lblinsimg=Label(window, text="Insert Your Image",fg='black', bg='#FCD801', font='Helvetica 18 bold')
lblinsimg.place(x=100, y=360)
# lable result
# lblresult=Label(window, text="Result",fg='black', bg='#FCD801', font='Helvetica 18 bold')
# lblresult.place(x=100, y=590)
# lable execution time
lblresult=Label(window, text="Execution Time: ",fg='black', bg='#FCD801', font='Helvetica 14 bold')
lblresult.place(x=520, y=716)
# lable test image
lblresult=Label(window, text="Test Image",fg='black', bg='#FFD1ED', font='Helvetica 25 bold italic')
lblresult.place(x=648, y=257)
# lable close image
lblclrslt=Label(window, text="Closest Result",fg='black', bg='#D1FFFC', font='Helvetica 25 bold italic')
lblclrslt.place(x=1119, y=257)

folder = ''
lb1=Label(window, text=folder,fg='black', bg='#D1FFFC', font='Helvetica 10 bold italic')
lb1.place(x=300, y=100)
# membuat lable untuk menampilkan gambar
# foto blank image
blankpic = Image.open("src/guiinterface/blankpicture.jpg")
blankpic2 = blankpic.resize((256,256), Image.ANTIALIAS)
new_blankpic = ImageTk.PhotoImage(blankpic2)
# lable show image test
lblshowtestpic=Label(window, image=new_blankpic)
lblshowtestpic.place(x=610, y=329, height=256, width=256)
# lable closest image test
lblshowresultpic=Label(window, image=new_blankpic)
lblshowresultpic.place(x=1110, y=329, height=256, width=256)

# procedure untuk membuka file gambar
def open_file():
        global img
        filename = filedialog.askopenfilename(initialdir="/images", title="Select Image",
                           filetypes=(("jpg images","*.jpg"),("png images","*.png")))
        img = Image.open(filename)
        img = img.resize((256,256), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        lblshowtestpic['image'] = img
# procedure untuk membuka folder
def open_folder():
        global folder

        folder = filedialog.askdirectory(initialdir="/images", title="Select Folder")
        lb1.config(text=folder)

# membuat button untuk input data
# button untuk open folder dataset
btn1=tk.Button(window, text="Choose File", fg='black', bg='white', activebackground='#118DFF',
           activeforeground='white',font='Helvetica 12 bold', width=11, height=2, anchor='center',command=open_folder)
btn1.place(x=102, y=250)
# button unutk open file gambar
btn2=tk.Button(window, text="Choose File", fg='black', bg='white', activebackground='#118DFF',
           activeforeground='white',font='Helvetica 12 bold', width=11, height=2, anchor='center',command=open_file)
btn2.place(x=102, y=410)
# button untuk menampilkan hasil
btn3=tk.Button(window, text="Result",fg='black', bg='white', activebackground='#118DFF',
           activeforeground='white',font='Helvetica 18 bold', width=11, height=2, anchor='center',command=searchImg(folder))
btn3.place(x=100, y=590)


# konfigurasi windows
window.configure(bg='#FFD800')
window.title("FACE RECOGNITION CJ-STAR") 
window.geometry("1920x1080")
window.mainloop()