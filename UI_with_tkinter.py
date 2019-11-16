from tkinter import *

window = Tk()

def convert_kg():
    grams = float(e2_value.get())*1000
    pounds = float(e2_value.get()) * 2.20462
    ounces = float(e2_value.get()) * 35.274
    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)


b1 = Button(window, text="Convert", command=convert_kg)
b1.grid(row=0,column=4)

e1=Label(window,text="Kg")
e1.grid(row=0,column=2)

e2_value=StringVar()
e2 = Entry(window,textvariable=e2_value)
e2.grid(row=0,column=3, rowspan=1)

t1=Text(window,height=1,width=20)
t1.grid(row=2,column=2)

t2=Text(window,height=1,width=20)
t2.grid(row=2,column=3)

t3=Text(window,height=1,width=20)
t3.grid(row=2,column=4)


window.mainloop()





# from tkinter import *
#
# window = Tk()
#
# def km_to_miles():
#     miles = float(e1_value.get())*1.6
#     t1.insert(END,miles)
#
# b1 = Button(window, text="Execute", command=km_to_miles)
# b1.grid(row=0,column=0)
#
# e1_value=StringVar()
# e1 = Entry(window,textvariable=e1_value)
# e1.grid(row=0,column=1)
#
# t1=Text(window,height=1,width=20)
# t1.grid(row=0,column=2)
#
# window.mainloop()