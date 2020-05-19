import tkinter

headX = 50
headY = 50
headSize = 50
scale = 10
tailTick = -1

# function to draw the dog
def drawDog():

    # Head
    headWidth = scale * 7.1
    headHeight = scale * 4.4

    #Body
    bodyWidth = scale * 20
    bodyHeight = scale * 10
    bodyX = headX + scale * 3
    bodyY = headY + scale * 2

    # Eye
    eyeX = headX + scale * 3
    eyeY = headY + scale * 0.5
    eyeWidth = scale * 1.4

    # Nose
    noseX = headX + scale * -0.25
    noseY = headY + scale * 0.5
    noseWidth = scale / 1.10

    # Ear
    earX = headX + scale * 5.2
    earY = headY + scale * 0.7
    earWidth = scale * 1.25
    earHeight = scale * 4.75

    # Leg 1
    legX = bodyX + scale 
    legY = bodyY + scale * 7
    legWidth = scale * 2.5
    legHeight = scale * 7.2

    # Leg 2
    legX2 = bodyX + scale * 2.5
    legY2 = bodyY + scale * 7
    legWidth2 = scale * 5
    legHeight2 = scale * 7.2

    # Leg 3
    legX3 = bodyX + scale * 14
    legY3 = bodyY + scale * 7
    legWidth3 = scale * 5
    legHeight3 = scale * 7.2

    # Leg4
    legX4 = bodyX + scale * 16
    legY4 = bodyY + scale * 7
    legWidth4 = scale * 1
    legHeight4 = scale * 7.2

    # Tail
    tailX = bodyX + scale * 18
    tailY = bodyY + scale * 1.5

    if (tailTick is -1):
        tailXEnd = scale * 1
        tailYEnd = scale * 0.5
    else:
        tailXEnd = scale * 1
        tailYEnd = scale
    
    w.delete('all')
    w.create_line(tailX, tailY, tailX + tailXEnd, tailY + tailYEnd, width = 8 * scale, fill = 'brown') # tail
    w.create_oval(legX, legY, legX + legWidth, legY + legHeight, fill = 'yellow') # leg 1
    w.create_oval(legX3, legY3, legX3 + legWidth, legY3 + legHeight3, fill = 'yellow') # leg 3
    w.create_oval(bodyX, bodyY, bodyX + bodyWidth, bodyY + bodyHeight, fill = 'yellow') # body
    w.create_oval(headX, headY, headX + headWidth, headY + headHeight, fill = 'yellow') # head
    w.create_oval(eyeX, eyeY, eyeX + eyeWidth, eyeY + eyeWidth, fill = 'blue') # eye
    w.create_oval(noseX, noseY, noseX + noseWidth, noseY + noseWidth, fill = 'black') # nose
    w.create_oval(earX, earY, earX + earWidth, earY + earHeight, fill = 'brown') # ear
    w.create_oval(legX2, legY2, legX2 + legWidth, legY2 + legHeight2, fill = 'yellow') # leg 2
    w.create_oval(legX4, legY4, legX4 + legWidth, legY4 + legHeight4, fill = 'yellow') # leg 4
   
    
    

def gCallback():
    global scale
    scale = scale + 10
    drawDog()

# this code is called when shrink button is pressed
def sCallback():
    global scale
    scale = scale - 10
    drawDog()

def wag():
    global tailTick
    tailTick = -1*tailTick   # change position of tail
    drawDog()
    w.after(500, func=wag)   # set next timer wag 500 ms = 0.5 seconds


#  create window
top = tkinter.Tk()

#  add drawing canvas to window
w = tkinter.Canvas(top, bg="light grey")

# add Grow and Shrink button to window
growButton = tkinter.Button(top, text="Grow", command=gCallback)
growButton.pack()

shrinkButton = tkinter.Button(top, text="Shrink", command=sCallback)
shrinkButton.pack()


# draw the man
drawDog()

# after draw the dog
w.after(500, func=wag)   # set timer for tail wag, 500 ms = 0.5 seconds


# expand canvas to fill window
w.pack(fill=tkinter.BOTH, expand=tkinter.YES) 

# process window events     
top.mainloop()

# continue here after user closes the window.
print ("Thank you for playing Growdog.")

