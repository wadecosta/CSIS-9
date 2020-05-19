# drop ball game
# Wade Costa
import tkinter
# variables that describe the target
targetWidth = 50
targetHeight = 10
targetX = 0
# variables for the ball
isBall = False
ballX =0
ballY = 0
ballSize = 5
score = 0
windowHeight = 600
windowWidth = 400
targetY = windowHeight - targetHeight - 5

def drawGame():
    # draw game with line, ball and target
    global windowHeight, windowWidth, targetY
    
    # get the current size of the window
    windowHeight = w.winfo_height()
    windowWidth = w.winfo_width()

    targetY = windowHeight - targetHeight - 5
    
    w.delete("all")
    w.create_rectangle(targetX, targetY, targetX + targetWidth, targetY + targetHeight, fill = 'blue')
    w.create_line(0, windowHeight/5, windowWidth, windowHeight/5)

    w.create_text(50, 10, text = 'Score: ' + str(score), fill = 'red')

    if isBall == True:
        w.create_oval(ballX, ballY, ballX + ballSize, ballY + ballSize, fill = 'black')
    
    return

def update():
    global targetX, targetY, ballX, ballY, isBall, score, targetWidth, windowWidth, windowHeight 
    # update target rectangle
    targetX = targetX + 3
    if targetX > windowWidth:
        targetX = 0
    
    # update ball y coordinate
    if isBall :
        ballY = ballY + 10
        # if ball is at bottom of window, then ball disappears
        if ballY > windowHeight:
            isBall = False
    
    # if ball hits target, update score
    if isBall :
        if ballX > targetX and ballX < targetX + targetWidth and ballY > targetY :
            score = score + 1
            isBall = False
    
    drawGame()
    w.after(33, func=update)
    return

def buttonPress(event):
    global isBall, ballX, ballY, windowHeight
    # user press mouse button
    # start a ball dropping
    if (not isBall) and (event.y < windowHeight/5):
        # create the ball
        isBall = True
        ballX = event.x
        ballY = event.y
        drawGame()
        
    return

# the main program
# create window
top = tkinter.Tk()
w = tkinter.Canvas(top, width=windowWidth, height=windowHeight) 
# do this to get mouse button events sent to buttonPress function
w.bind('<Button-1>', buttonPress)
w.pack(fill=tkinter.BOTH, expand=tkinter.YES)
#start the game
update()
top.mainloop()
print("Thanks for playing. Your final score was: ",score)


