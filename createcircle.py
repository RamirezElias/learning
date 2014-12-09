import turtle

turtle.home()
t = turtle

def square():
    for i in range(4):
        t.forward(200)
        t.right(90)

'''
t.pu()    
t.forward(70)
t.right(90)
t.forward(100)
t.pd()
t.circle(30)
'''

def dot1():
    t.penup()
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.dot(30)
    t.backward(50)
    t.left(90)
    t.backward(50)

def dot2():
    t.pu()
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.dot(30)
    t.backward(50)
    t.left(90)
    t.backward(100)
    t.pd()
   

def dot3():
    t.pu()
    t.forward(150)
    t.right(90)
    t.forward(50)
    t.dot(30, "green")
    t.backward(50)
    t.left(90)
    t.backward(150)
    t.pd()

def dot4():
    t.pu()
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.dot(30, "purple")
    t.backward(100)
    t.left(90)
    t.backward(50)
    t.pd()
def dot5():
    t.pu()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.dot(30)
    t.backward(100)
    t.left(90)
    t.backward(100)
    t.pd()
def dot6():
    t.pu()
    t.forward(150)
    t.right(90)
    t.forward(150)
    t.dot(30)
    t.backward(100)
    t.left(90)
    t.backward(150)
    t.pd()

def dot7():
    t.pu()
    t.forward(50)
    t.right(90)
    t.forward(150)
    t.dot(30)
    t.backward(150)
    t.left(90)
    t.backward(50)
    t.pd()

def dot8():
    t.pu()
    t.forward(100)
    t.right(90)
    t.forward(150)
    t.dot(30)
    t.backward(150)
    t.left(90)
    t.backward(100)
    t.pd()

def dot9():
    t.pu()
    t.forward(150)
    t.right(90)
    t.forward(150)
    t.dot(30)
    t.backward(150)
    t.left(90)
    t.backward(150)
    t.pd()

def side1():
    dot5()
    

def side2():
    dot3()
    dot7()
    
def side3():
    dot3()
    dot5()
    dot7()
def side4():
    dot1()
    dot3()
    dot7()
    dot9()
def side5():
    dot1()
    dot3()
    dot5()
    dot7()
    dot9()
def side6():
    dot1()
    dot2()
    dot3()
    dot7()
    dot8()
    dot9()


square()
side2()

     

