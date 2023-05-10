''' They rejected my app. This project must end here. '''

# one-button app
# added some tags to beautify the epub code
# made the app window a bit responsive

import tkinter
import re
from tkinter import *
import tkinter.ttk as ttk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

root = Tk()

root.title("The Correcter")
root.geometry('100x90')
root.attributes('-topmost', 1)
root.attributes('-toolwindow', 1)
root['background'] = '#121212'

window_width = 100
window_height = 90

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

style = ttk.Style(root)
style.theme_use('clam')

root.geometry(f'+{center_x}+{center_y}')

def text_correcter():
    input_txt = root.clipboard_get()
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
    
    btn.clipboard_clear()
    btn.clipboard_append(f"{S}")  

''' Following functions are used to change button color and font'''

def black_btn1(event=None):
    btn.configure(bg="black", fg="cyan")
    btn.bind("<Enter>", cyan_btn)
    btn.bind("<Leave>", black_btn1)

def cyan_btn(event=None):
    btn.configure(bg="cyan", fg="black")

def black_btn2(event=None):
    btn.configure(bg="black", fg="orange")
    btn.bind("<Enter>", orange_btn)
    btn.bind("<Leave>", black_btn2)

def orange_btn(event=None):
    btn.configure(bg="orange", fg= "black")
    
# side function

def info_popup(event=None):
    top = Toplevel(root)
    top.title("About: Ebook Code Correcter v0.2")
    Label(top, justify = "left", text="Info:\
     \n✅ This program can be used for correcting unintended new lines in epub html documents.\n\
     \nHow to use the program:\
     \n • Use an Epub editor to get access to code of the book. (I recommend Calibre)\
     \n • Copy all the code of an html page.\
     \n • Click the button.\
     \n • And that's it! The correct code is ready!\n\
     \nTo see clipboard press Win+V together.\n\
     \nContacts:\
     \n🔗 Telegram: @Abdulloh_ID\
     \n🔗 Email: outergamer11@gmail.com").pack(padx=10, pady=(10,0))
    Label(top, justify = "left", text="\n ©️ This program is made by Abdulloh Abdusamadov.").pack(pady=(0,10))

f1 = Button()
root.bind("<F1>", info_popup)

f2 = Button()
root.bind('<F2>', black_btn2)

f3 = Button()
root.bind('<F3>', black_btn1)

btn = Button(root, text="Copy", width=6, height=2, command=lambda:[text_correcter()])
btn.pack(fill=BOTH, expand=True)

black_btn1()

root.mainloop()
