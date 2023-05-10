# added some tags to beautify the epub code
# made the app window a bit responsive

import tkinter
import re
from tkinter import *
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

oyna = Tk()
oyna.title("Ebook Code Correcter") # working title

oyna.attributes('-topmost', 1)
oyna.resizable(False, False)            
oyna['background'] = '#025a6c'

txt = Text(oyna, width=45, height=11, font='Calibri 10',  wrap=WORD)
txt.focus()
txt.grid(row=0, column=0, padx=(5,0), pady=(5,0))

rslt = Text(oyna, width=45, height=11, font=('Calibri 10'),  wrap=WORD)
rslt.grid(row=1, column=0, padx=(5,0), pady=(5,5))

# adding vertical scrollbars to textboxes

scrl = Scrollbar(oyna)
scrl.grid(row=0, column=1, padx=(0,10), pady=(5,0), sticky="ns")
scrl.config(command=txt.yview)

scrl2 = Scrollbar(oyna)
scrl2.grid(row=1, column=1,  padx=(0,10), pady=(5,5), sticky="ns")
scrl2.config(command=rslt.yview)

def text_correcter():
    input_txt = txt.get(1.0, "end-1c")
    S = input_txt       # renaming so it can be easier to write
    
    a = "\n"            # identifying new line
    if a in S:
    	S = S.replace('\n', ' ')

    b = "</p>"
    if b in S:
        S = S.replace(f"{b}", f"{b}\n\n")

    c = "/>" 
    if c in S:
        S = S.replace(f"{c}", f"{c}\n")

    d = "</div>"
    if d in S:
        S = S.replace(f"{d}", f"{d}\n\n")

    e = "<body"
    if e in S:
        S = S.replace(f"{e}", f"\n  {e}")

    rslt.delete('1.0', 'end')
    rslt.insert("end", S)

def copy_to_clipboard():
    final_rslt = rslt.get('1.0', 'end-1c')
    cpy.clipboard_clear()
    cpy.clipboard_append(final_rslt)

def clear_entry():
    txt.delete('1.0', 'end')
    rslt.delete('1.0', 'end')

''' Following functions are used to change button color and font'''

def cyan_btn(event=None):
    btn.configure(bg="cyan", fg="black")

def cyan_btn2(event=None):
    clr.configure(bg="cyan", fg="black")

def cyan_btn3(event=None):
    cpy.configure(bg="cyan", fg="black")

def grey_btn(event=None):
    btn.configure(bg="#f0f0f0", fg="black")
    clr.configure(bg="#f0f0f0", fg="black")
    cpy.configure(bg="#f0f0f0", fg="black")

def info_popup(event=None):
    top = Toplevel(oyna)
    top.geometry('700x500')
    top.title("About: Ebook Code Correcter v0.1")
    Label(top, justify = "left", text="\nInfo:\
     \n✅ This program can be used for correcting unintended new lines in epub html documents.\
     \nHow to use the program:\
     \n • Use an Epub editor to get access to code of the book. (I recommend Calibre)\
     \n • Copy all the code of an html page.\
     \n • Paste it to the upper textbox, then click «Correct» button.\
     \n • In order to clear the textbox, click «Clear».\
     \n • In order to copy the ready code to the clipboard, click «Copy» button. \n\
     \nTo show up clipboard press Win+V together.\n\
     \nContacts:\
     \n🔗 Telegram: @Abdulloh_ID\
     \n🔗 Email: outergamer11@gmail.com").pack()
    Label(top, justify = "left", text="\n ©️ This program is made by Abdulloh Abdusamadov.").pack()

f1 = Button()
oyna.bind("<F1>", info_popup)

btn = Button(oyna, width=10, height=1, text="Correct", command=text_correcter)
btn.grid(row=0, column=2, sticky="s", padx=(0,5))

clr = Button(oyna, text="Clear", width=2, command=clear_entry)
clr.grid(row=0, column=2, sticky="new", padx=(0,5), pady=5)

cpy = Button(oyna, text="Copy", width=2, command=lambda:[copy_to_clipboard(), clear_entry()])
cpy.grid(row=1, column=2, sticky="sew", padx=(0,5), pady=(0,5))

''' Binding the mouse hover to specific buttons '''

btn.bind("<Enter>", cyan_btn)
btn.bind("<Leave>", grey_btn)

clr.bind("<Enter>", cyan_btn2)
clr.bind("<Leave>", grey_btn)

cpy.bind("<Enter>", cyan_btn3)
cpy.bind("<Leave>", grey_btn)

oyna.mainloop()