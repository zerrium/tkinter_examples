from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Text
import os
import glob

def all_notes(operation=None):
  current_dir = str(os.getcwd()) #get current working directory
  list_notes = glob.glob(current_dir+"/*.txt") #list all txt files in the given directory and returns strings (contain complete file path) in a list (using glob.glob because it's easier to filter file names/extensions)
  note_name = []
  for i in range(len(list_notes)):
    note_name.append(os.path.basename(list_notes[i][:-4])) #cut the strings in list_notes list to save only the file name (without complete file path) to the note_name list
  if operation=="Delete":
    note_name.append("Delete All")
  return note_name

def main_menu():
    window = Tk()
    window.title("Main menu")
    window.geometry('260x210')

    def button1_clicked():
        window.destroy()
        menu_1()

    def button2_clicked():
        window.destroy()
        menu_2()

    def button3_clicked():
        window.destroy()
        menu_3()

    def button4_clicked():
        window.destroy()
        sys.exit(0)

    button1 = Button(window, text="Create new note", font=("Calibri", "14"), command=button1_clicked, width=20)
    button1.place(x=25, y=10)
    button2 = Button(window, text="Load saved notes", font=("Calibri", "14"), command=button2_clicked, width=20)
    button2.place(x=25, y=60)
    button3 = Button(window, text="Delete saved notes", font=("Calibri", "14"), command=button3_clicked, width=20)
    button3.place(x=25, y=110)
    button4 = Button(window, text="Quit", font=("Calibri", "14"), command=button4_clicked, width=20)
    button4.place(x=25, y=160)
    window.mainloop()

def menu_1():
    window1 = Tk()
    window1.title("Create new note")
    window1.geometry('350x530')

    def button1_clicked():
        temp = textbox2.get(1.0, END)
        if textbox1.get()=="":
            messagebox.showerror("Error", "Enter the note title!")
        else:
            f = open(textbox1.get()+".txt", "w+")
            f.writelines(temp)
            messagebox.showinfo(textbox1.get(), "The note has been saved!")

    def button2_clicked():
        window1.destroy()
        main_menu()

    label1 = Label(window1, text="Enter note title:", font=("Calibri", "14"))
    label1.place(x=0, y=5)
    textbox1 = Entry(window1, width=20, font=("Calibri", "14"))
    textbox1.place(x=130, y=5)
    label2 = Label(window1, text="Note content:", font=("Calibri", "14"))
    label2.place(x=0, y=35)
    textbox2 = Text(window1, width=33, height=15, font=("Calibri", "14"))
    textbox2.place(x=5, y=65)
    button1 = Button(window1, text="Save", font=("Calibri", "14"), command=button1_clicked, width=20)
    button1.place(x=75, y=425)
    button2 = Button(window1, text="Return to main menu", font=("Calibri", "14"), command=button2_clicked, width=20)
    button2.place(x=75, y=475)
    window1.mainloop()

def menu_2():
    window2 = Tk()
    window2.title("Load saved notes")
    window2.geometry('260x210')

    def button1_clicked():
        if combobox.get() == "":
            messagebox.showerror("Error", "Please choose a note!")
        else:
            try:
                f = open(combobox.get()+".txt", "r")
            except FileNotFoundError:
                messagebox.showerror("Error", "The note does not exist!")
            else:
                temp = f.readlines()
                content = ""
                for i in temp:
                    content +=i
                messagebox.showinfo(combobox.get(), content)

    def button2_clicked():
        window2.destroy()
        main_menu()

    label1 = Label(window2, text="Choose notes:", font=("Calibri", "14"),)
    label1.place(x=0, y=5)
    combobox = ttk.Combobox(window2, values=all_notes(), font=("Calibri", "14"), width=22)
    combobox.place(x=5, y=40)
    button1 = Button(window2, text="Open", font=("Calibri", "14"), command=button1_clicked, width=20)
    button1.place(x=25, y=90)
    button2 = Button(window2, text="Return to main menu", font=("Calibri", "14"), command=button2_clicked, width=20)
    button2.place(x=25, y=140)
    window2.mainloop()

def menu_3():
    window3 = Tk()
    window3.title("Delete saved notes")
    window3.geometry('260x210')

    def button1_clicked():
        if combobox.get() == "":
            messagebox.showerror("Error", "Please choose a note!")
        else:
            if combobox.get()=="Delete All":
                for i in all_notes():
                    os.remove(i+".txt")
                messagebox.showinfo(combobox.get(), "Delete succeeded!")
                window3.destroy()
                main_menu()
            else:
                try:
                    os.remove(combobox.get()+".txt")
                except FileNotFoundError:
                    messagebox.showerror("Error", "The note does not exist!")
                else:
                    messagebox.showinfo(combobox.get(), "Delete succeeded!")
                    window3.destroy()
                    menu_3()

    def button2_clicked():
        window3.destroy()
        main_menu()

    label1 = Label(window3, text="Choose notes:", font=("Calibri", "14"),)
    label1.place(x=0, y=5)
    combobox = ttk.Combobox(window3, values=all_notes("Delete"), font=("Calibri", "14"), width=22)
    combobox.place(x=5, y=40)
    button1 = Button(window3, text="Delete", font=("Calibri", "14"), command=button1_clicked, width=20)
    button1.place(x=25, y=90)
    button2 = Button(window3, text="Return to main menu", font=("Calibri", "14"), command=button2_clicked, width=20)
    button2.place(x=25, y=140)
    window3.mainloop()

main_menu()
