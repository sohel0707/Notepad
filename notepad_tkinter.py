import tkinter as tk
import tkinter.messagebox as msg
from tkinter.filedialog import asksaveasfile,askopenfilename
from pathlib import Path
from functools import partial
TITLE="Untitled - Notepad"
TEXT=""
FILE=None
text1=None

ALL_TEXT=[]
SELECTED_STYLE=""
SELECTED_FONT=""
SELECTED_SIZE=""

def abc1():
    print("sohel bhai")
def open1(event=None):
    global FILE
    files = [('All Files', '*.*'),  
            ('Python Files', '*.py'), 
            ('Text Document', '*.txt')] 
    file1 = askopenfilename(filetypes = files, defaultextension = files)
    # FILE=file1.name
    FILE=Path(file1)
    f=open(FILE,'r')
    content=f.read()
    textArea.delete(1.0, tk.END)
    textArea.insert(tk.END, content)



def save2(event=None):
    global FILE
    FILE=None
    save1()
def save1(event=None):
    global FILE
    global text1,TITLE
    text1=textArea.get("1.0",tk.END)
    # text1.strip()
    if len(textArea.get("1.0", "end-1c")) == 0:
        print("Not found")
    else:
        FILE=save()
        if FILE is not None:
            TITLE = str(FILE) + " - Notepad"
        else:
            TITLE="Untitled - Notepad"
        root.title(TITLE)
        print(FILE)
def save():
    global text1
    global FILE
    # global TITLE
    # root.config(root.title=TITLE)
    if FILE is None:
        files = [('All Files', '*.*'),  
            ('Python Files', '*.py'), 
            ('Text Document', '*.txt')] 
        file1 = asksaveasfile(filetypes = files, defaultextension = files)
        print(file1.name)
        file1=Path(file1.name)
        openfile=open(file1,'w')
        openfile.write(text1)
        openfile.close()
        return file1
    else:
        openfile=open(FILE,'w')
        openfile.write(text1)
        openfile.close()
        return FILE
        # file1.encode('unicode_escape')







def new_file(event=None):
    global text1,FILE,TITLE
    text1=textArea.get("1.0",tk.END)
    # text1.strip()
    if len(textArea.get("1.0", "end-1c")) == 0:
        print("Not found")
    else:
        # newWindow = tk.Toplevel(root)
        # root.withdraw()
        confirm=msg.askyesnocancel(
                  title="Save On Close",
                  message="DO you want to save",default=msg.YES)
        if confirm:
            print("saved")
            save()
            textArea.delete("1.0","end")
            FILE=None
            TITLE="Untitled - Notepad"
            root.title(TITLE)
        elif confirm is None:
            print("cancel")
        else:
            print("Not saved")
            FILE=None
            TITLE="Untitled - Notepad"
            root.title(TITLE)
            textArea.delete("1.0","end")

def copy(event=None):
    global TEXT
    TEXT=textArea.selection_get()
    print(len(TEXT))


def paste(event=None):
    pos=textArea.index(tk.INSERT)
    textArea.insert(pos,TEXT)
font_size=10

def delete():
    textArea.event_generate(("<<Cut>>"))
def undo_add():
    global ALL_TEXT
    ALL_TEXT.append(textArea.get())
    print(ALL_TEXT)
def Undo():
    global ALL_TEXT
    if len(ALL_TEXT)!=0:
        text=ALL_TEXT.pop()
        textArea.delete(1.0,tk.END)
        textArea.insert(1.0,text)



def IncreseFontSize(event):
    global font_size
    # print(event.type())
    # font_size+=10
    if font_size+10<=140:
        textArea.config(font=("Helvetica", font_size+10))
        font_size+=10

def DecreseFontSize(event):
    global font_size
    # font_size-=10
    if font_size-10>=30:
        textArea.config(font=("Helvetica", font_size-10))
        font_size-=10
l1=""
l2=""
l3=""
fonts = ['Arial', "Courier New", "Comic Sans MS", "Fixedsys", "MS Sans Serif", 'MS Serif', "Symbol", "System",
         'Times New Roman', "Verdana"]
font_weight = ["normal", "bold", "italic"]
def setFontfamily(top1):
    global SELECTED_FONT,SELECTED_SIZE,SELECTED_STYLE
    if SELECTED_FONT!="" and SELECTED_STYLE !="" and SELECTED_SIZE!="":
        textArea.config(font=(SELECTED_FONT,SELECTED_SIZE,SELECTED_STYLE ))
    elif SELECTED_FONT!=""  and SELECTED_SIZE!="":
        textArea.config(font=(SELECTED_FONT,SELECTED_SIZE ))
    elif SELECTED_FONT!="" and SELECTED_STYLE !="":
        textArea.config(font=(SELECTED_FONT,12,SELECTED_STYLE ))
    elif SELECTED_STYLE !="" and SELECTED_SIZE!="":
        textArea.config(font=("Arial",SELECTED_SIZE,SELECTED_STYLE ))
    elif SELECTED_FONT!="" :
        textArea.config(font=SELECTED_FONT)
    elif SELECTED_STYLE!="":
        textArea.config(font=("Arial",12,SELECTED_STYLE))
    elif SELECTED_SIZE!="":
        textArea.config(font=("Arial",SELECTED_SIZE))

    SELECTED_FONT,SELECTED_SIZE,SELECTED_STYLE="","",""
    top1.destroy()
def getFontfamily(top1):
    global l1,l2,l3,fonts,font_weight,SELECTED_FONT,SELECTED_SIZE,SELECTED_STYLE
    l1=l1.curselection()
    if len(l1)>0:
        SELECTED_FONT=fonts[l1[0]]

    l2=l2.curselection()
    if len(l2)>0:
        SELECTED_STYLE=font_weight[l2[0]]

    l3=l3.get()
    if int(l3)>5 and int(l3)<140:
        SELECTED_SIZE=l3

    setFontfamily(top1)

def font():
    global l1,l2,l3,font_weight,fonts
    top1=tk.Toplevel(root)

    top1.geometry("400x500+700+100")
    tk.Label(top1,text="Font").grid(row=0,column=0)
    tk.Label(top1,text="Font Style").grid(row=0,column=1)
    tk.Label(top1,text="Font Size").grid(row=0,column=2)
    l1=tk.Listbox(top1,exportselection=0)
    # l1.insert(["sohel","is"])
    l1.grid(row=1,column=0)
    l2=tk.Listbox(top1,exportselection=0)
    l2.grid(row=1,column=1,padx=10,pady=20)
    l3=tk.Entry(top1)
    l3.grid(row=1,column=2,pady=20)

    ok=tk.Button(top1,text="Ok",width=15,command=partial(getFontfamily,top1))
    ok.grid(row=2,column=1)
    cancel=tk.Button(top1,text="Cancel",width=15,command=top1.destroy)
    cancel.grid(row=2,column=2)

    for i in fonts:
        l1.insert(tk.END,i)
    for i in font_weight:
        l2.insert(tk.END,i)




root=tk.Tk()
root.geometry("1120x550")
root.minsize(1120,550)
menu1=tk.Menu(root)
file=tk.Menu(menu1)
file.add_command(label="New     Ctrl + N",command=new_file,font = ('Verdana', 8))
file.add_command(label="New Window   Ctrl + Shift + N",command=abc1,font = ('Verdana', 8))
file.add_command(label="Open...     Ctrl + o",command=open1,font = ('Verdana', 8))
file.add_command(label="Save        Ctrl + s",command=save1,font = ('Verdana', 8))
file.add_command(label="Save As...  Ctrl + Shift + s",command=save2,font = ('Verdana', 8))
file.add_command(label="Page Setup",command=abc1,font = ('Verdana', 8))
file.add_command(label="Print...",command=abc1,font = ('Verdana', 8))
file.add_command(label="Exit",command=exit,font = ('Verdana', 8))
menu1.add_cascade(label="File",menu=file)

edit=tk.Menu(menu1)
edit.add_command(label="copy  Ctrl + c", command=copy,font = ('Verdana', 8))
edit.add_command(label="paste  Ctrl + v", command=paste,font = ('Verdana', 8))
edit.add_command(label="Delete", command=delete,font = ('Verdana', 8))
edit.add_command(label="Cut", command=delete,font = ('Verdana', 8))
edit.add_command(label="Undo", command=Undo,font = ('Verdana', 8))
menu1.add_cascade(label="Edit", menu=edit,font = ('Verdana', 8))

format1=tk.Menu(menu1)
format1.add_command(label="Font...", command=font,font = ('Verdana', 8))
menu1.add_cascade(label="Format", menu=format1,font = ('Verdana', 8))

textArea = tk.Text(root)
textArea.pack(expand=True,fill="both",padx=(10,25),pady=10)
#fileMenu.add_command(label="File", command=abc1)
root.config(menu=menu1)

# Bind the shortcuts
root.bind("<Control-Up>",IncreseFontSize)
root.bind("<Control-Down>",DecreseFontSize)
root.bind("<Control-s>",save1)
root.bind("<Control-Shift-s>",save2)
root.bind("<Control-n>",new_file)
root.bind("<Control-o>",open1)
root.bind("<Control-c>",copy)
root.bind("<Control-v>",paste)
textArea.bind("<KP_Enter>",undo_add)


sBarx=tk.Scrollbar(textArea,orient=tk.HORIZONTAL)
sBarx.pack(side=tk.BOTTOM,fill=tk.X)
sBarx.config(command=textArea.xview)
textArea.config(xscrollcommand=sBarx.set)

sBary=tk.Scrollbar(textArea,orient=tk.VERTICAL)
sBary.pack(side=tk.RIGHT,fill=tk.Y)
sBary.config(command=textArea.yview)
textArea.config(yscrollcommand=sBary.set)

root.iconbitmap('logo.ico')

root.title(TITLE)

# root.update_idletasks()


root.mainloop()
