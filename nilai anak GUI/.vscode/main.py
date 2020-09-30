from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def percentage_to_decimal(i):
    return float(int(i[:-1])/100)

def button_clicked():
    try:
        nilai_tugas = int(textbox_tugas.get())
        if nilai_tugas<0 or nilai_tugas>100: raise ValueError
        nilai_uts = int(textbox_uts.get())
        if nilai_uts<0 or nilai_uts>100: raise ValueError
        nilai_uas = int(textbox_uas.get())
        if nilai_uas<0 or nilai_uas>100: raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Nilai tidak valid!")
    else:
        tugas = percentage_to_decimal(combobox_tugas.get())
        uts = percentage_to_decimal(combobox_uts.get())
        uas = percentage_to_decimal(combobox_uas.get())
        if tugas+uts+uas != 1:
            messagebox.showerror("Error", "Proporsi persentase nilai tidak sesuai!")
        else:
            tugas*=nilai_tugas
            uts*=nilai_uts
            uas*=nilai_uas
            total = tugas+uts+uas
            lulus = "Lulus!"
            if total<75: lulus = "Tidak lulus!"
            nilai_tertinggi = max([nilai_tugas, nilai_uts, nilai_uas])
            messagebox.showinfo("Pemberitahuan", str(lulus)+"\nNilai total: "+str(total)+
                "\nNilai tertinggi: "+str(nilai_tertinggi))
window = Tk()
window.title("Nilai GUI")
window.geometry('250x200')
label1 = Label(window, text="Input nilai:", font=("Calibri", "18"))
label1.place(x=0, y=0)
label2 = Label(window, text="Nilai tugas: ", font=("Calibri", "18"))
label2.place(x=0, y=40)
label3 = Label(window, text="Nilai UTS: ", font=("Calibri", "18"))
label3.place(x=0, y=80)
label4 = Label(window, text="Nilai UAS: ", font=("Calibri", "18"))
label4.place(x=0, y=120)
combobox_tugas = ttk.Combobox(window, values=["10%", "20%", "30%", "40%",
            "50%", "60%", "70%", "80%", "90%"])
combobox_tugas.place(x=120, y=50)
combobox_tugas.current(2)
combobox_tugas.configure(width=5)
combobox_uts = ttk.Combobox(window, values=["10%", "20%", "30%", "40%",
            "50%", "60%", "70%", "80%", "90%"])
combobox_uts.place(x=120, y=90)
combobox_uts.current(2)
combobox_uts.configure(width=5)
combobox_uas = ttk.Combobox(window, values=["10%", "20%", "30%", "40%",
            "50%", "60%", "70%", "80%", "90%"])
combobox_uas.place(x=120, y=130)
combobox_uas.current(3)
combobox_uas.configure(width=5)
label5 = Label(window, text="x", font=("Calibri", "18"))
label5.place(x=180, y=40)
label6 = Label(window, text="x", font=("Calibri", "18"))
label6.place(x=180, y=80)
label7 = Label(window, text="x", font=("Calibri", "18"))
label7.place(x=180, y=120)
textbox_tugas = Entry(window, width=5)
textbox_tugas.place(x=200, y=50)
textbox_uts = Entry(window, width=5)
textbox_uts.place(x=200, y=90)
textbox_uas = Entry(window, width=5)
textbox_uas.place(x=200, y=130)
button = Button(window, text="Done", command=button_clicked, width=15)
button.place(x=60, y=160)
window.mainloop()