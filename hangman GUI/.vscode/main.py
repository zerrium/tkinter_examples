from nltk.corpus import words #buat list semua vocab inggris
from tkinter import *
from tkinter import messagebox
import random
import glob
import os

level1=[]; level2=[]; level3=[]; level4=[] #assign empty list
level5=[]; level6=[]; level7=[]; level8=[]
user_data=[] #isinya: password, level, number of played round, win, lose, username
fact=[ #akan muncul popup berisi fakta (yang dipilih salah satu secara random) mengenai bahasa inggris ketika game over, referensi: https://www.grammarly.com/blog/10-interesting-english-facts-guest/ dan https://www.scoopwhoop.com/inothernews/english-vinglish/
"A new English word is created every 98 minutes\nThat's 14.7 words per day!",
"'Time' is the most commonly used noun in English",
"'Scraunched' is the longest English word with one syllable\nAlong with the archaic word 'strengthed'\nScraunch is the sound your car makes on gravel",
"The word 'startling' is the only nine letter word in English where you can remove one letter at a time to create another word",
"The dot on top of 'i' and 'j' is called 'tittle'",
"'Oxyphenbutazone' is the highest scoring word in a game of scrabble",
"'Twyndyllyng' is the longest word in the English language without any vowels\nIt's an obsolete word pronounced 'twinlin' meaning twins\nA more commonly word though, is ' rhythms '",
"The word 'set' has the highest number of definitions in the dictionary",
"The word 'abstemious' has all the vowels in the alphabetical order\nOther such words include abstentious, aerious, arsenious and facetious",
"The English language does not have a script of its own\nThe script is actually borrowed from Latin",
"India has a higher English speaking population than United Kingdom!\nWorldwide, India comes second only to the USA in it's English speaking population\nThe empire strikes back, and how!",
"'I am' is the shortest complete sentence in the English language",
"A pangram sentence is one that contains every letter in the language\nFor example, the sentence 'The quick brown fox jumps over the lazy dog' is a pangram",
"The shortest, oldest, and most commonly used word is 'I'.",
"English is the language of the air\nThis means that all pilots have to identify themselves and speak in English while flying, regardless of their origin",
"Girl used to mean small boy or girl",
"The letter 'E' is the most used letter in English"]

def all_users():
        current_dir = str(os.getcwd()) #get current working directory
        list_notes = glob.glob(current_dir+"/*.txt") #list all txt files in the given directory and returns strings (contain complete file path) in a list (using glob.glob because it's easier to filter file names/extensions)
        user_name = []
        for i in range(len(list_notes)):
                user_name.append(os.path.basename(list_notes[i][:-4])) #cut the strings in list_notes list to save only the file name (without complete file path) to the note_name list
        return user_name

for i in words.words(): #words.words() function bawaan library nltk yg isinya list vocab inggris
        if len(i)>3:
                if len(i)==4: #semakin tinggi levelnya semakin panjang kata katanya
                        level1.append(i)
                elif len(i)==5:
                        level2.append(i)
                elif len(i)==6:
                        level3.append(i)
                elif len(i)==7:
                        level4.append(i)
                elif len(i)==8:
                        level5.append(i)
                elif len(i)==9:
                        level6.append(i)
                elif len(i)==10:
                        level7.append(i)
                else:
                        level8.append(i)

def window1(): #Sign in dan Sign up
        def button1(): #Sign up
                user_data.clear()
                if user_name_textbox.get()=="" or password_textbox.get()=="":
                        messagebox.showwarning("Alert", "Incomplete field")
                else:
                        found = False
                        for i in all_users():
                                if i==user_name_textbox.get():
                                        found = True
                                        messagebox.showerror("Error", "This username already exsists, try another username!")
                                        break
                        if not found:
                                f = open(user_name_textbox.get()+".txt", "w")
                                f.writelines(password_textbox.get()+"\n1\n0\n0\n0")
                                user_data.append(user_name_textbox.get())
                                f.close()
                                window1.destroy()
                                window2()

        def button2(): #Sign in
                user_data.clear()
                if user_name_textbox.get()=="" or password_textbox.get()=="":
                        messagebox.showwarning("Alert", "Incomplete field")
                else:
                        found = False
                        for i in all_users():
                                if i==user_name_textbox.get():
                                        found = True
                                        f = open(user_name_textbox.get()+".txt", "r")
                                        for i in f.readlines():
                                                if "\n" in i:
                                                        user_data.append(i[:-1]) #buang \n di f.readlines
                                                else:
                                                        user_data.append(i)
                                        f.close()
                                        if user_data[0]==password_textbox.get():
                                                user_data.append(user_name_textbox.get())
                                                window1.destroy()
                                                window2()
                                        else:
                                                messagebox.showerror("Error", "Incorrect password!")
                                        break
                        if not found:
                                messagebox.showerror("Error", "Invalid username!")

        window1 = Tk()
        window1.title("Hangman GUI")
        window1.geometry('290x200')
        label1 = Label(window1, text="Welcome to Hangman!", font=("Calibri", "18"))
        label1.place(x=0, y=0)
        label2 = Label(window1, text="Sign in to start playing", font=("Calibri", "14"))
        label2.place(x=0, y=30)
        label3 = Label(window1, text="Sign up to create account", font=("Calibri", "14"))
        label3.place(x=0, y=55)
        label4 = Label(window1, text="Username: ", font=("Calibri", "14"))
        label4.place(x=0, y=90)
        user_name_textbox = Entry(window1, width=30)
        user_name_textbox.place(x=95, y=95)
        label5 = Label(window1, text="Password: ", font=("Calibri", "14"))
        label5.place(x=0, y=115)
        password_textbox = Entry(window1, show="*", width=30)
        password_textbox.place(x=95, y=120)
        button1 = Button(window1, text="Sign Up", font=("Calibri", "14"), command=button1, width=12)
        button1.place(x=10, y=150)
        button2 = Button(window1, text="Sign In", font=("Calibri", "14"), command=button2, width=12)
        button2.place(x=150, y=150)
        window1.mainloop()

wo=[]
number_of_wrong=0
number_of_correct=0
win_in_row=0
random_word = ""
guessed_word=[]
img = ['000.png','001.png', '002.png', '003.png', '004.png', '005.png', '006.png', '007.png', '008.png', '009.png', '010.png']
ph_img = []
        
def window2(): #window utama
        def number_of_words(i): #tampilin brp banyak word yg ada di level itu
                text = ""
                if i=="1":
                        text = str(len(level1))
                elif i=="2":
                        text = str(len(level2))
                elif i=="3":
                        text = str(len(level3))
                elif i=="4":
                        text = str(len(level4))
                elif i=="5":
                        text = str(len(level5))
                elif i=="6":
                        text = str(len(level6))
                elif i=="7":
                        text = str(len(level7))
                elif i=="8":
                        text = str(len(level8))
                label7.configure(text="Number of words in this level: "+text)
        def sign_out(): #untuk keluar
                user_data.clear()
                window2.destroy()
                window1()
        def reset(): #kondisi ketika game over atau berhenti main dan reset ke kondisi awal
                global number_of_correct
                global number_of_wrong
                global guessed_word
                global random_word
                global wo
                global ph_img
                number_of_wrong=0
                number_of_correct=0
                random_word=""
                guessed_word.clear()
                label2.configure(text="Level: "+user_data[1])
                label3.configure(text="Round: "+str(int(user_data[2])+1))
                label4.configure(text="Win: "+user_data[3])
                label5.configure(text="Lose: "+user_data[4])
                label6.configure(image=ph_img[0])
                number_of_words(user_data[1])
                button2.configure(text="Start playing", command=start_playing)
                button1.configure(state='normal')
                button3.place_forget()
                textbox.place_forget()
                for i in wo:
                        i.destroy()
                wo.clear()
        def start_playing(): #kondisi ketika game mulai
                global random_word
                global wo
                button2.configure(text="Stop playing", command=reset)
                button1.configure(state=DISABLED)
                x=0
                if user_data[1]=="1":
                        random_word=random.choice(level1)
                        x=205
                elif user_data[1]=="2":
                        random_word=random.choice(level2)
                        x=195
                elif user_data[1]=="3":
                        random_word=random.choice(level3)
                        x=185
                elif user_data[1]=="4":
                        random_word=random.choice(level4)
                        x=175
                elif user_data[1]=="5":
                        random_word=random.choice(level5)
                        x=165
                elif user_data[1]=="6":
                        random_word=random.choice(level6)
                        x=155
                elif user_data[1]=="7":
                        random_word=random.choice(level7)
                        x=145
                elif user_data[1]=="8":
                        random_word=random.choice(level8)
                        x=5
                random_word=random_word.upper()
                for i in range(len(random_word)):
                        wo.append(Label(window2, text="_", font=("Calibri", "22")))
                        wo[i].place(x=x, y=160)
                        x+=20
                textbox.place(x=235, y=210)
                button3.place(x=165, y=240)
        def guess(): #kondisi ketika user menebak huruf
                user_input = textbox.get()
                textbox.delete(0, END)
                correct_input=True
                global number_of_correct
                global number_of_wrong
                global guessed_word
                global random_word
                global win_in_row
                global wo
                global ph_img
                if user_input=="":
                        correct_input=False
                        messagebox.showerror("Error", "You have not guessed anything!")
                elif len(user_input)>1:
                        correct_input=False
                        messagebox.showerror("Error", "You only may guess one character")
                elif not ((ord(user_input)>=65 and ord(user_input)<=90) or (ord(user_input)>=97 and ord(user_input)<=122)):
                        correct_input=False
                        messagebox.showerror("Error", "Invalid input, try again!")
                if len(guessed_word)!=0 and correct_input:
                        for i in guessed_word:
                                if i == user_input.upper():
                                        messagebox.showwarning("Alert", "You have guessed that word!")
                                        correct_input = False
                if correct_input and number_of_wrong<10 and number_of_correct<len(random_word):
                        user_input = user_input.upper()
                        found = False
                        guessed_word.append(user_input)
                        for i in range(len(random_word)):
                                if random_word[i]==user_input:
                                        found=True
                                        number_of_correct+=1
                                        wo[i].configure(text=user_input)
                        if found:
                                messagebox.showinfo("Info", "You are correct!")
                        else:
                                messagebox.showinfo("Info", "You are wrong :(")
                                number_of_wrong+=1
                                label6.configure(image=ph_img[number_of_wrong])
                                        
                        if number_of_correct==len(random_word) or number_of_wrong>=10: #kondisi game over
                                if number_of_correct==len(random_word) and number_of_wrong<10:
                                        messagebox.showinfo("Hangman GUI", "You win!\nThe word is: "+random_word)
                                        user_data[3]=str(int(user_data[3])+1)
                                        win_in_row+=1
                                        if win_in_row==3:
                                                messagebox.showinfo("Hangman GUI", "Level up!")
                                                user_data[1]=str(int(user_data[1])+1)
                                                win_in_row=0
                                elif number_of_wrong>=10:
                                        messagebox.showinfo("Hangman GUI", "You lose :(\nThe word is: "+random_word)
                                        user_data[4]=str(int(user_data[4])+1)
                                        if win_in_row!=0:
                                                win_in_row=0
                                messagebox.showinfo("Fun fact!", random.choice(fact))
                                user_data[2]=str(int(user_data[2])+1)
                                f = open(user_data[5]+".txt", "w+")
                                f.writelines(user_data[0]+"\n"+user_data[1]+"\n"+user_data[2]+"\n"+user_data[3]+"\n"+user_data[4])
                                f.close()
                                reset()
        #kondisi awal
        global ph_img
        global img
        window2=Tk()
        window2.title("Hangman GUI")
        window2.geometry('500x300')
        for i in img:
                ph_img.append(PhotoImage(file=i))
        label1 = Label(window2, text="User: "+user_data[5], font=("Calibri", "14"))
        label1.place(x=0, y=0)
        label2 = Label(window2, text="Level: "+user_data[1], font=("Calibri", "14"))
        label2.place(x=0, y=25)
        label3 = Label(window2, text="Round: "+str(int(user_data[2])+1), font=("Calibri", "14"))
        label3.place(x=0, y=50)
        label4 = Label(window2, text="Win: "+user_data[3], font=("Calibri", "14"))
        label4.place(x=150, y=25)
        label5 = Label(window2, text="Lose: "+user_data[4], font=("Calibri", "14"))
        label5.place(x=150, y=50)
        label6= Label(window2, image=ph_img[0])
        label6.place(x=320, y=5)
        label7 = Label(window2, font=("Calibri", "14"))
        label7.place(x=0, y=75)
        number_of_words(user_data[1])
        button1 = Button(window2, text="Sign out", font=("Calibri", "14"), command=sign_out ,width=20)
        button1.place(x=20, y=110)
        button2 = Button(window2, text="Start playing", font=("Calibri", "14"), command=start_playing, width=20)
        button2.place(x=270, y=110)
        button3 = Button(window2, text="Guess!", font=("Calibri","14"), command=guess, width=15)
        textbox = Entry(window2, width=1, font=("Calibri", "14"))
        window2.mainloop()

window1()