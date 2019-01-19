from tkinter import * 
# first make a window
window = Tk()

def km_to_miles():
    print(e1_val.get())
    # t1.insert(END, e1_val.get())
    miles = float(e1_val.get())* 1.6
    t1.insert(END, miles)

# button inside the window
e1_val = StringVar()
b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)

# text entry box inside the window
e1 = Entry(window, textvariable=e1_val)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)


window.mainloop()

