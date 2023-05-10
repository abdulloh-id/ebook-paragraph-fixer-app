# added some tags to beautify the epub code
# made the app window a bit responsive

import tkinter
import re
from tkinter import *
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

oyna = Tk()                             
oyna.title("Ebook Code Correcter")

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
scrl.grid(row=0, column=1, padx=(0,5), pady=(5,0), sticky="ns")
scrl.config(command=txt.yview)

scrl2 = Scrollbar(oyna)
scrl2.grid(row=1, column=1,  padx=(0,5), pady=(5,5), sticky="ns")
scrl2.config(command=rslt.yview)

def text_correcter():
    input_txt = txt.get(1.0, "end-1c")
    S = input_txt       # renaming so it can be easier to write
    
    a = "\n"            # identifying new line
    if a in S:
    	S = S.replace('\n', ' ')

    b1 = '<p class="noindent">'
    if b1 in S:
        S = S.replace(f"{b1}", f"\n{b1}")

    b2 = "<p"
    if b2 in S:
        S = S.replace(f"{b2}", f"\n{b2}")

    b3 = "</p>"
    if b3 in S:
        S = S.replace(f"{b3}", f"{b3}\n")

    c1 = "</title>"
    if c1 in S:
        S = S.replace(f"{c1}", f"{c1}\n")

    c2 = "/>" 
    if c2 in S:
        S = S.replace(f"{c2}", f"{c2}\n")

    d1 = "<div" 
    if d1 in S:
        S = S.replace(f"{d1}", f"\n{d1}")

    d2 = "</div>"
    if d2 in S:
        S = S.replace(f"{d2}", f"{d2}\n")

    e = "<body"
    if e in S:
        S = S.replace(f"{e}", f"\n  {e}")

    f = "</body>"
    if f in S:
        S = S.replace(f"{f}", f"\n{f}\n")

    g1 = "<html"
    if g1 in S:
        S = S.replace(f"{g1}", f"\n{g1}")

    g2 = "</html>"   
    if g2 in S:
        S = S.replace(f"{g2}", f"\n{g2}")

    h = "<head>"   
    if h in S:
        S = S.replace(f"{h}", f"\n  {h}\n")

    i = "</head>"
    if i in S:
        S = S.replace(f"{i}", f"{i}\n")

    j = "<h3"
    if j in S:
        S = S.replace(f"{j}", f"\n{j}")

    rslt.delete('1.0', 'end')
    rslt.insert("end", S)

def copy_to_clipboard():
    final_rslt = rslt.get('1.0', 'end-1c')
    cpy.clipboard_clear()
    cpy.clipboard_append(final_rslt)

def clear_entry():
    txt.delete('1.0', 'end')
    rslt.delete('1.0', 'end')
    update()

''' Following functions are used to change button color and font'''

def cyan_btn1(event=None):
    clr.configure(bg="cyan", fg="black")

def cyan_btn2(event=None):
    cpy.configure(bg="cyan", fg="black")

def grey_btn(event=None):
    clr.configure(bg="#f0f0f0", fg="black")
    cpy.configure(bg="#f0f0f0", fg="black")

# main function triggers

def combine(event=None):
    text_correcter()
    update()

txt.bind("<Enter>", combine)
txt.bind("<Leave>", combine)
txt.bind("<KeyRelease>", combine)

# side function

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

clr = Button(oyna, text="Clear", width=8, command=clear_entry)
clr.grid(row=0, column=2, sticky="new", padx=(0,5), pady=(5,0))

cpy = Button(oyna, text="Copy", width=8, command=lambda:[copy_to_clipboard(), clear_entry()])
cpy.grid(row=1, column=2, sticky="sew", padx=(0,5), pady=(0,5))

''' Binding the mouse hover to specific buttons '''

clr.bind("<Enter>", cyan_btn1)
clr.bind("<Leave>", grey_btn)

cpy.bind("<Enter>", cyan_btn2)
cpy.bind("<Leave>", grey_btn)

# adding character counter

def update(event=None):
    var.set(int(str(len(txt.get("1.0", 'end-1c')))))  # adjusted the keypress counter

var = StringVar()

Label(oyna, text="Characters:").grid(row=0, column=2, pady=(0, 60), padx=(0,5))

# displaying number of characters within a textbox
charCount = Label(textvariable=var)
charCount.grid(row=0, column=2, pady=5, padx=(0,5))

oyna.mainloop()