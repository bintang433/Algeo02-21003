import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

#inisiasi window
window=Tk()

var_path_file=StringVar()
var_image_file=StringVar()

# gambar background
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
folderlabel=Label(window, text=folder,fg='black', bg='#D1FFFC', font='Helvetica 10 bold italic')
folderlabel.place(x=75, y=363)

file = ''
filelabel=Label(window, text=folder,fg='black', bg='#D1FFFC', font='Helvetica 10 bold italic')
filelabel.place(x=75, y=553)

# procedure untuk membuka file gambar
def open_file():
        global img
        filename = filedialog.askopenfilename(initialdir="/images", title="Select Image",
                           filetypes=(("jpg images","*.jpg"),("png images","*.png")))
        var_image_file.set(filename)
        var_image_file.get()
        img = Image.open(filename)
        img = img.resize((256,256), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        lblshowtestpic['image'] = img
        filelabel.config(text=filename[:40])

# procedure untuk membuka folder
def open_folder():
        global folder
        folder = filedialog.askdirectory(initialdir="/images", title="Select Folder")
        var_path_file.set(folder)
        var_path_file.get()
        folderlabel.config(text=folder[:40])

# procedure untuk running waktu dari programnya
run = False
m,s = 0,0

# procedure memulai waktu
def start_time():
        global run
        if not run:
                update_time()
                run = True

# procedure menghentikan waktu
def stop_time():
        global run
        if run:
                time_label.after_cancel(time_update)
                run = False

# procedure mereset waktu
def reset_time():
        global run
        if run:
                time_label.after_cancel(time_update)
                run = False
        global m,s
        m,s = 0,0
        time_label.config(text='00.00')

# procedure update bergeraknya waktu
def update_time():
        global m,s
        global time_update
        s = s+1
        if s == 60:
                m = m+1
                s = 0
        min_string = f'{m}' if m > 9 else f'0{m}'
        sec_string = f'{s}' if s > 9 else f'0{s}'
        # if var_image_file && var_path_file: (mengecek ketika variabel folder dan image sudah ada)
        time_label.config(text=min_string+'.'+sec_string)
        time_update = time_label.after(1000, update_time)
                             
time_label = Label(window, text='00.00', font='Helvetica 23 bold', bg='white', fg='black')
time_label.place(x=746, y=708)


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
btn2=tk.Button(window, image=buttoninp3,borderwidth=0, relief='solid',bg='black', activebackground='black',command=start_time)
btn2.place(x=75, y=624.5)

# konfigurasi windows
window.configure(bg='#FFD800')
window.title("FACE RECOGNITION CJ-STAR") 
window.geometry("1920x1080")
window.mainloop()