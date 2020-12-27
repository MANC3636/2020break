import turtle as t
t1=t.Pen()

#functions for code reuse

length=100#global scope
length=45

def square(color, length):#header
    for x in "loop":
        t1.color(color)
        t1.fd(length)
        t1.left(90)
        #none

def move(length):
    t1.up()
    t1.fd(2*length)
    t1.left(75)
    t1.down()

#call the function
square("blue", 180)
move(30)
square("red", 50)
square("purple", 5)








t.mainloop()