# 21.08.23 | Refactored the code.

# 09.05.23 | Added mini app (one-button app) to the main app as a toplevel window.
#            Changed the cursor color to white.
#            Added a smooth switch function between main and mini windows.

import tkinter
from tkinter import *
import tkinter.ttk as ttk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

root = Tk()
root.title("Ebook Paragraph Fixer")
root.attributes('-topmost', 1)
root.resizable(False, False)
root['background'] = '#121212'

style = ttk.Style(root)
style.theme_use('clam')

txt_box = Text(root, width=45, height=11, font='Calibri 10', bg='#121212', fg='white',  wrap=WORD, insertbackground="white")
txt_box.focus()
txt_box.grid(row=0, column=0, padx=(5,0), pady=(5,0))

rslt_box = Text(root, width=45, height=11, font=('Calibri 10'), bg='#121212', fg='white', wrap=WORD, insertbackground="white")
rslt_box.grid(row=1, column=0, padx=(5,0), pady=(5,5))

# Adding vertical scrollbars to textboxes

scrl_bar = ttk.Scrollbar(root)
scrl_bar.grid(row=0, column=1, padx=(0,5), pady=(5,0), sticky="ns")
scrl_bar.config(command=txt_box.yview)
txt_box.config(yscrollcommand=scrl_bar.set)

style.configure('Vertical.TScrollbar', bordercolor='#FF8C00', arrowcolor='#FF8C00', troughcolor='#00000C')

scrl_bar2 = ttk.Scrollbar(root)
scrl_bar2.grid(row=1, column=1,  padx=(0,5), pady=(5,5), sticky="ns")
scrl_bar2.config(command=rslt_box.yview)
rslt_box.config(yscrollcommand=scrl_bar2.set)

def text_correcter():
    input_txt = txt_box.get(1.0, "end-1c")
    S = input_txt       # renaming so it can be easier to write
    
    # Identifying new lines
    if "\n" in S:
        S = S.replace('\n', ' ')

    tag1 = "<html"
    if tag1 in S:
        S = S.replace(f"{tag1}", f"\n{tag1}")

    tag2 = "</html>"   
    if tag2 in S:
        S = S.replace(f"{tag2}", f"\n{tag2}")

    tag3 = "<head>"   
    if tag3 in S:
        S = S.replace(f"{tag3}", f"\n  {tag3}\n")

    tag4 = "</head>"
    if tag4 in S:
        S = S.replace(f"{tag4}", f"{tag4}\n")

    tag5 = "</title>"
    if tag5 in S:
        S = S.replace(f"{tag5}", f"{tag5}\n")

    tag6 = "/>" 
    if tag6 in S:
        S = S.replace(f"{tag6}", f"{tag6}\n")

    tag7 = "<body"
    if tag7 in S:
        S = S.replace(f"{tag7}", f"\n  {tag7}")

    tag8 = "</body>"
    if tag8 in S:
        S = S.replace(f"{tag8}", f"\n{tag8}\n")

    tag9 = "<h3"
    if tag9 in S:
        S = S.replace(f"{tag9}", f"\n{tag9}")

    tag10 = '<p class="noindent">'
    if tag10 in S:
        S = S.replace(f"{tag10}", f"\n{tag10}")

    tag11 = "<p"
    if tag11 in S:
        S = S.replace(f"{tag11}", f"\n{tag11}")

    tag12 = "</p>"
    if tag12 in S:
        S = S.replace(f"{tag12}", f"{tag12}\n")

    tag_13 = "<div" 
    if tag_13 in S:
        S = S.replace(f"{tag_13}", f"\n{tag_13}")

    tag_14 = "</div>"
    if tag_14 in S:
        S = S.replace(f"{tag_14}", f"{tag_14}\n")

    rslt_box.delete('1.0', 'end')
    rslt_box.insert("end", S)

def copy_to_clipboard():
    final_result = rslt_box.get('1.0', 'end-1c')
    cpy.clipboard_clear()
    cpy.clipboard_append(final_result)

def clear_entry():
    txt_box.delete('1.0', 'end')
    rslt_box.config(state="normal")
    rslt_box.delete('1.0', 'end')
    update_counter()

''' Following functions are used to change button color and font '''

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
    update_counter()

txt_box.bind("<KeyRelease>", combine)

clr = Button(root, text="Clear", width=6, height=2, bg='#00000C', fg='orange', command=clear_entry)
clr.grid(row=0, column=2, sticky="new", padx=(2,5), pady=5)

cpy = Button(root, text="Copy", width=6, height=2, bg='#00000C', fg='orange', command=lambda:[copy_to_clipboard(), clear_entry()])
cpy.grid(row=1, column=2, sticky="sew", padx=(2,5), pady=5)

''' Binding the mouse hover to specific buttons '''

clr.bind("<Enter>", cyan_btn1)
clr.bind("<Leave>", grey_btn)

cpy.bind("<Enter>", cyan_btn2)
cpy.bind("<Leave>", grey_btn)

# Adding a character counter

def update_counter(event=None):
    var.set(int(str(len(txt_box.get('1.0', 'end-1c')))))  # adjusted the keypress counter

var = StringVar()

# Displaying number of characters within a textbox
char_counter = Label(textvariable=var, bg='orange', fg='black')
char_counter.grid(row=0, column=2, pady=5, padx=(0,5))

def info_popup(event=None):
    top = Toplevel(root)
    top.title("About: Ebook Paragraph Fixer v0.2.5")
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

f1 = Button()
root.bind("<F1>", info_popup)

root.mainloop()