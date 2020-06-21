
from tkinter import *
from tkinter import filedialog as fd
from tkinter.ttk import Combobox
import os
from PIL import Image
from tkinter import messagebox


root=Tk()
root.title("Image_Conversion_App")
def png_click():
    global im
    value=combo.get()
    if (value=="PNG"):
        import_filename=fd.askopenfilename()
        if import_filename.endswith(".jpg"):
            im=Image.open(import_filename)
            export_filename=fd.asksaveasfilename(defaultextension=".png")
            im.save(export_filename)
            messagebox.showinfo("Success","File converted to PNG")
        else:
            messagebox.showerror("Fail!!","Error Interrupted!!!! Check Again")
    if (value=="JPEG"):
        import_filename=fd.askopenfilename()
        if import_filename.endswith(".jpg"):
            im=Image.open(import_filename)
            export_filename=fd.asksaveasfilename(defaultextension=".jpeg")
            im.save(export_filename)
            messagebox.showinfo("Success","File converted to .jpeg")
        else:
            messagebox.showerror("Fail!!","Error Interrupted!!!! Check Again")
    if (value=="BMP"):
        import_filename=fd.askopenfilename()
        if import_filename.endswith(".jpg"):
            im=Image.open(import_filename)
            export_filename=fd.asksaveasfilename(defaultextension=".bmp")
            im.save(export_filename)
            messagebox.showinfo("Success","File converted to .bmp ")
        else:
            messagebox.showerror("Fail!!","Error Interrupted!!!! Check Again")
    if (value=="GIF"):
        import_filename=fd.askopenfilename()
        if import_filename.endswith(".jpg"):
            im=Image.open(import_filename)
            export_filename=fd.asksaveasfilename(defaultextension=".gif")
            im.save(export_filename)
            messagebox.showinfo("Success","File converted to .gif")
        else:
            messagebox.showerror("Fail!!","Error Interrupted!!!! Check Again")
    else:
        messagebox.showwarning("Warning","Image Not Selected!!")
def jpeg_click():
    global im
    value=combo.get()
    if (value=="PNG"):
        import_filename=fd.askopenfilename()
        if import_filename.endswith(".jpeg"):
            im=Image.open(import_filename)
            export_filename=fd.asksaveasfilename(defaultextension=".png")
            im.save(export_filename)
            messagebox.showinfo("Success","File converted to PNG")
        else:
            messagebox.showerror("Fail!!","Error Interrupted!!!! Check Again")
    if (value=="JPG"):
        import_filename=fd.askopenfilename()
        if import_filename.endswith(".jpeg"):
            im=Image.open(import_filename)
            export_filename=fd.asksaveasfilename(defaultextension=".jpg")
            im.save(export_filename)
            messagebox.showinfo("Success","File converted to .jpg")
        else:
            messagebox.showerror("Fail!!","Error Interrupted!!!! Check Again")
    if (value=="BMP"):
        import_filename=fd.askopenfilename()
        if import_filename.endswith(".jpeg"):
            im=Image.open(import_filename)
            export_filename=fd.asksaveasfilename(defaultextension=".bmp")
            im.save(export_filename)
            messagebox.showinfo("Success","File converted to .bmp ")
        else:
            messagebox.showerror("Fail!!","Error Interrupted!!!! Check Again")
    if (value=="GIF"):
        import_filename=fd.askopenfilename()
        if import_filename.endswith(".jpeg"):
            im=Image.open(import_filename)
            export_filename=fd.asksaveasfilename(defaultextension=".gif")
            im.save(export_filename)
            messagebox.showinfo("Success","File converted to .gif")
        else:
            messagebox.showerror("Fail!!","Error Interrupted!!!! Check Again")
    else:
        messagebox.showwarning("Warning","Image Not Selected!!")
def bmp_click():
    global im
    value=combo.get()
    if (value=="PNG"):
        import_filename=fd.askopenfilename()
        if import_filename.endswith(".bmp"):
            im=Image.open(import_filename)
            export_filename=fd.asksaveasfilename(defaultextension=".png")
            im.save(export_filename)
            messagebox.showinfo("Success","File converted to .png")
        else:
            messagebox.showerror("Fail!!","Error Interrupted!!!! Check Again")
    if (value=="JPEG"):
        import_filename=fd.askopenfilename()
        if import_filename.endswith(".bmp"):
            im=Image.open(import_filename)
            export_filename=fd.asksaveasfilename(defaultextension=".jpeg")
            im.save(export_filename)
            messagebox.showinfo("Success","File converted to .jpeg")
        else:
            messagebox.showerror("Fail!!","Error Interrupted!!!! Check Again")
    if (value=="JPG"):
        import_filename=fd.askopenfilename()
        if import_filename.endswith(".bmp"):
            im=Image.open(import_filename)
            export_filename=fd.asksaveasfilename(defaultextension=".jpg")
            im.save(export_filename)
            messagebox.showinfo("Success","File converted to .jpg")
        else:
            messagebox.showerror("Fail!!","Error Interrupted!!!! Check Again")
    if (value=="GIF"):
        import_filename=fd.askopenfilename()
        if import_filename.endswith(".bmp"):
            im=Image.open(import_filename)
            export_filename=fd.asksaveasfilename(defaultextension=".gif")
            im.save(export_filename)
            messagebox.showinfo("Success","File converted to .gif")
        else:
            messagebox.showerror("Fail!!","Error Interrupted!!!! Check Again")
    else:
        messagebox.showwarning("Warning","Image Not Selected!!")
def gif_click():
    global im
    value=combo.get()
    if (value=="PNG"):
        import_filename=fd.askopenfilename()
        if import_filename.endswith(".gif"):
            im=Image.open(import_filename)
            export_filename=fd.asksaveasfilename(defaultextension=".png")
            im.save(export_filename)
            messagebox.showinfo("Success","File converted to .png")
        else:
            messagebox.showerror("Fail!!","Error Interrupted!!!! Check Again")
    if (value=="JPEG"):
        import_filename=fd.askopenfilename()
        if import_filename.endswith(".gif"):
            im=Image.open(import_filename)
            export_filename=fd.asksaveasfilename(defaultextension=".jpeg")
            im.save(export_filename)
            messagebox.showinfo("Success","File converted to .jpeg")
        else:
            messagebox.showerror("Fail!!","Error Interrupted!!!! Check Again")
    if (value=="JPG"):
        import_filename=fd.askopenfilename()
        if import_filename.endswith(".gif"):
            im=Image.open(import_filename)
            export_filename=fd.asksaveasfilename(defaultextension=".jpg")
            im.save(export_filename)
            messagebox.showinfo("Success","File converted to .jpg")
        else:
            messagebox.showerror("Fail!!","Error Interrupted!!!! Check Again")
    if (value=="BMP"):
        import_filename=fd.askopenfilename()
        if import_filename.endswith(".gif"):
            im=Image.open(import_filename)
            export_filename=fd.asksaveasfilename(defaultextension=".bmp")
            im.save(export_filename)
            messagebox.showinfo("Success","File converted to .bmp")
        else:
            messagebox.showerror("Fail!!","Error Interrupted!!!! Check Again")
    else:
        messagebox.showwarning("Warning","Image Not Selected!!")


Label_1=Label(root,text="Browse A File", width=20, font=("bold",20))
Label_1.place(x=140,y=40)

v1=["PNG","JPEG","BMP","GIF"]
combo=Combobox(root,text="print",value=v1)
combo.set("SELECT")
combo.place(x=220,y=120)

v2=["PNG","JPG","BMP","GIF"]
combo=Combobox(root,text="print",value=v2)
combo.set("SELECT")
combo.place(x=220,y=200)

v3=["PNG","JPEG","JPG","GIF"]
combo=Combobox(root,text="print",value=v3)
combo.set("SELECT")
combo.place(x=220,y=280)

v4=["PNG","JPEG","JPG","BMP"]
combo=Combobox(root,text="print",value=v4)
combo.set("SELECT")
combo.place(x=220,y=360)

button1=Button(root,text="JPG", width=15, height=1, bg="royalblue",fg="white",font=("helvetica", 9, "bold"))
button1.place(x=80,y=120)
button1=Button(root,text="JPEG", width=15, height=1, bg="royalblue",fg="white",font=("helvetica", 9, "bold"))
button1.place(x=80,y=200)
button1=Button(root,text="BMP", width=15, height=1, bg="royalblue",fg="white",font=("helvetica", 9, "bold"))
button1.place(x=80,y=280)
button1=Button(root,text="GIF", width=15, height=1, bg="royalblue",fg="white",font=("helvetica", 9, "bold"))
button1.place(x=80,y=360)

button2=Button(root,text="Convert Image",width=15,height=1,bg="royalblue",fg="white",font=("helvetica",9,"bold"),command=png_click)
button2.place(x=380,y=120)
button2=Button(root,text="Convert Image",width=15,height=1,bg="royalblue",fg="white",font=("helvetica",9,"bold"),command=jpeg_click)
button2.place(x=380,y=200)
button2=Button(root,text="Convert Image",width=15,height=1,bg="royalblue",fg="white",font=("helvetica",9,"bold"),command=bmp_click)
button2.place(x=380,y=280)
button2=Button(root,text="Convert Image",width=15,height=1,bg="royalblue",fg="white",font=("helvetica",9,"bold"),command=gif_click)
button2.place(x=380,y=360)

label=Label(root,text="< Developed By:- Rohit Sahu >", font=("blue",10,"bold"))
label.place(x=380,y=450)
root.geometry("580x480+200+200")
root.mainloop()