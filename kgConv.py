from tkinter import *

window = Tk()
# variable declaration
kgVal = StringVar()

def kg_to_others():
    print(kgEntry.get())
    # t1.insert(END, e1_val.get())
    grams = float(kgEntry.get())* 1000
    t1.delete("1.0", END)
    t1.insert(END, grams)

    pounds = float(kgEntry.get())*2.20462
    t2.delete("1.0", END)
    t2.insert(END,pounds)

    ounces = float(kgEntry.get()) *35.274
    t3.delete("1.0", END)
    t3.insert(END, ounces)

# // text entry inside window
kgEntry = Entry(window, textvariable=kgVal)
kgEntry.grid(row=0, column=1)

l0=Label(window, text="Kg", bg="white", fg="black")
l0.grid(row=0,column=0)

# button inside window
b1 = Button(window, text="Convert", command=kg_to_others)
b1.grid(row=0, column=2)

# result area inside window
t1 = Text(window, height=1, width=10)
t1.grid(row=0, column=3)

t2 = Text(window, height=1, width=10)
t2.grid(row=1, column=3)

t3 = Text(window, height=1, width=10)
t3.grid(row=2, column=3)

l1=Label(window, text="grams", bg="blue", fg="white")
l1.grid(row=0,column=4)

l2=Label(window, text="pounds", bg="green", fg="white")
l2.grid(row=1,column=4)

l3=Label(window, text="ounces", bg="yellow", fg="black")
l3.grid(row=2,column=4)


window.mainloop()

