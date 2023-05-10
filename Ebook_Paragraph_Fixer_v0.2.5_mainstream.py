# 09.05.23 | added mini app (one-button app) to the main app as a toplevel window
#            changed the cursor color to white
#            added a smooth switch function between main and mini windows

import tkinter
import re
from tkinter import *
import tkinter.ttk as ttk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.title("Ebook Code Correcter")
root.attributes('-topmost', 1)
root.resizable(False, False)
root['background'] = '#121212'

style = ttk.Style(root)
style.theme_use('clam')

txt = Text(root, width=45, height=11, font='Calibri 10', bg='#121212', fg='white',  wrap=WORD, insertbackground="white")
txt.focus()
txt.grid(row=0, column=0, padx=(5,0), pady=(5,0))

rslt = Text(root, width=45, height=11, font=('Calibri 10'), bg='#121212', fg='white', wrap=WORD, insertbackground="white")
rslt.grid(row=1, column=0, padx=(5,0), pady=(5,5))

# adding vertical scrollbars to textboxes

scrl = ttk.Scrollbar(root)
scrl.grid(row=0, column=1, padx=(0,5), pady=(5,0), sticky="ns")
scrl.config(command=txt.yview)
txt.config(yscrollcommand=scrl.set)

style.configure('Vertical.TScrollbar', bordercolor='#FF8C00', arrowcolor='#FF8C00', troughcolor='#00000C')

scrl2 = ttk.Scrollbar(root)
scrl2.grid(row=1, column=1,  padx=(0,5), pady=(5,5), sticky="ns")
scrl2.config(command=rslt.yview)
rslt.config(yscrollcommand=scrl2.set)

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
    rslt.config(state="normal")
    rslt.delete('1.0', 'end')
    update()

''' Following functions are used to change button color and font'''

def cyan_btn1(event=None):
    clr.configure(bg="orange", fg="black")

def cyan_btn2(event=None):
    cpy.configure(bg="orange", fg="black")

def grey_btn(event=None):
    clr.configure(bg="black", fg="orange")
    cpy.configure(bg="black", fg="orange")

# main function trigger

def combine(event=None):
    text_correcter()
    update()

txt.bind("<KeyRelease>", combine)
#txt.bind("<Enter>", combine)
#txt.bind("<Leave>", combine)

clr = Button(root, text="Clear", width=6, height=2, bg='#00000C', fg='orange', command=clear_entry)
clr.grid(row=0, column=2, sticky="new", padx=(2,5), pady=5)

cpy = Button(root, text="Copy", width=6, height=2, bg='#00000C', fg='orange', command=lambda:[copy_to_clipboard(), clear_entry()])
cpy.grid(row=1, column=2, sticky="sew", padx=(2,5), pady=5)

''' Binding the mouse hover to specific buttons '''

clr.bind("<Enter>", cyan_btn1)
clr.bind("<Leave>", grey_btn)

cpy.bind("<Enter>", cyan_btn2)
cpy.bind("<Leave>", grey_btn)

# adding character counter

def update(event=None):
    var.set(int(str(len(txt.get("1.0", 'end-1c')))))  # adjusted the keypress counter

var = StringVar()

# displaying number of characters within a textbox
charCount = Label(textvariable=var, bg='orange', fg='black')
charCount.grid(row=0, column=2, pady=5, padx=(0,5))

# extra app for easy use

def mini_app(event=None):
    top = Toplevel(root)
    top.title("Mini")
    top.geometry('100x90')
    top.attributes('-topmost', 1)
    top.attributes('-toolwindow', 1)
    top.resizable(False, False)
    top['background'] = '#121212'
    top.grab_set()

    window_width = 100
    window_height = 90

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    style = ttk.Style(top)
    style.theme_use('clam')

    top.geometry(f'+{center_x}+{center_y}')

    def text_correcter():
        input_txt = top.clipboard_get()
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
        
        btn_m.clipboard_clear()
        btn_m.clipboard_append(f"{S}")  

    ''' Following functions are used to change button color and font'''

    def black_btn_m1(event=None):
        btn_m.configure(bg="black", fg="cyan")
        btn_m.bind("<Enter>", cyan_btn_m)
        btn_m.bind("<Leave>", black_btn_m1)

    def cyan_btn_m(event=None):
        btn_m.configure(bg="cyan", fg="black")

    def black_btn_m2(event=None):
        btn_m.configure(bg="black", fg="orange")
        btn_m.bind("<Enter>", orange_btn_m)
        btn_m.bind("<Leave>", black_btn_m2)

    def orange_btn_m(event=None):
        btn_m.configure(bg="orange", fg= "black")

    f2 = Button()
    top.bind('<F2>', black_btn_m1)

    f3 = Button()
    top.bind('<F3>', black_btn_m2)

    btn_m = Button(top, text="Copy", width=6, height=2, command=lambda:[text_correcter()])
    btn_m.pack(fill=BOTH, expand=True)

    black_btn_m1()

    def info_popup(event=None):
        top2 = Toplevel(top)
        top2.attributes('-topmost', 1)
        top2.title("About: Ebook Code Correcter v0.2.5")
        Label(top2, justify = "left", padx=5, pady=5, text="Info:\
         \n✅ This program can be used for correcting unintended new lines in epub html documents.\n\
         \nHow to use this mini program:\
         \n • Use an epub editor to get access to code of the book. (I recommend Calibre)\
         \n • Copy all the code of an html page.\
         \n • Click the button.\
         \n • And that's it! The correct code is ready and has already been copied to your clipboard!\n\
         \nTo see clipboard press Win+V together.\n\
         \nContacts:\
         \n🔗 Telegram: @Abdulloh_ID\
         \n🔗 Email: outergamer11@gmail.com").pack()
        Label(top2, justify = "left", padx=5, pady=5, text="\n ©️ This program is made by Abdulloh Abdusamadov.").pack()

    f1 = Button()
    top.bind("<F1>", info_popup)

    def to_main_app(event=None):
        top.destroy()
        un_minimize()

    f5 = Button()
    top.bind('<F5>', to_main_app)

def info_popup(event=None):
    top = Toplevel(root)
    top.title("About: Ebook Code Correcter v0.2.5")
    Label(top, justify = "left", text="Info:\
     \n✅ This program can be used for correcting unintended new lines in epub html documents.\n\
     \nHow to use the program:\
     \n • Use an epub file editor to get access to code of the book. (I recommend Calibre)\
     \n • Copy all the code of an html page.\
     \n • Paste it to the upper textbox.\
     \n • The corrected text will appear in the lower textbox.\
     \n • Click «Clear» button to clear the textboxes.\
     \n • Click «Copy» button to copy the result to the clipboard.\n\
     \nTo see clipboard press Win+V together.\n\
     \nContacts:\
     \n🔗 Telegram: @Abdulloh_ID\
     \n🔗 Email: outergamer11@gmail.com").pack(padx=10, pady=(10,0))
    Label(top, justify = "left", text="\n ©️ This program is made by Abdulloh Abdusamadov.").pack(pady=(0,10))

def minimize(event=None):
    root.iconify()

def un_minimize(event=None):
    root.wm_state('normal')

def switch_combo(event=None):
    minimize()
    mini_app()

f1 = Button()
root.bind("<F1>", info_popup)

f5 = Button()
root.bind('<F5>', switch_combo)

root.mainloop()
