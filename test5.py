import tkinter

def code():
    global e
    global string
    string = e.get()
    print(string)
    e.delete(0, tkinter.END)

root=tkinter.Tk()
label = tkinter.Label(root, text="Input the CodeName")
label.pack()

e = tkinter.Entry(root)
e.pack()
e.focus_set()

b = tkinter.Button(root, text='okay', command=code)
b.pack(side='bottom')
