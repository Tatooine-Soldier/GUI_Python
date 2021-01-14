import tkinter
from tkinter import *
import time 
import random


#Counter class for counter object
class Counter(object):
    def __init__(self):
        self._counter = 0
  
    def getCounter(self):
        return self._counter

    def increment(self):
        self._counter = self._counter + 1
        score["text"] = self._counter
        
    def decrement(self):              #used for rocket percentage
        self._counter = self._counter - 1
        
    def reset(self):
        self._counter = 0
    
    counter = property(getCounter)

    
#rocket class, object will have different values for each component
class RocketSpecs:
    def __init__(self,weight,power):
        self.weight = weight
        self.power = power
        
    def getWeight(self):
        return self.weight
    
    def getPower(self):
        return self.power
    
    def weightinc(self):
        self.weight += 1
        
    def powerinc(self):
        self.power += 1
        
    def resetWeight(self):
        self.weight = 0
        
rocket = RocketSpecs(0,0)


#gets the time and draws thwe rectangle in random position when start button pressed or when rectangle clicked
def cb2():
    canvas.delete(ALL)
    global timer1
    timer1 = time.time()
    randomx = random.randint(0,300)
    randomy = random.randint(0,250)
    rectangle = canvas.create_rectangle(randomx, randomy, randomx+30 , randomy+30, fill="blue", outline="red")
    canvas.tag_bind(rectangle, "<ButtonPress-1>", addCounter)


#increments counter when rectangle clicked on 
def addCounter(event):
    global timer2
    timer2 = time.time()
    if (timer2 - timer1) < 2:
        counter.increment()
        canvas.delete(ALL)
        cb2()
  

  

counter = Counter()


#function which draws the initial unfinished snowman picture, awaits keyboard input
def house():
    clearForGame()
    frame5.grid_remove()
    canvas.delete(ALL)
    frame2.grid_remove()
    frame6.grid_remove()
    score.grid_remove()
    nameLabel.grid()
    nameButton.grid()
    dinput.grid()
    points1 = [15,200,60,25,60,25,115,200,115,200,15,200]
    tree = canvas.create_polygon(points1,outline="green",fill="green",width=6)
    snowmanBottom = canvas.create_oval(250,150,350,250,fill="white")
    snowmanTop = canvas.create_oval(275,100,325,165,fill="white")
    ground = canvas.create_rectangle(0,250,400,300, fill="white")
    canvas.create_rectangle(55,203,75,250,fill="brown")
    canvas.configure(bg="black")
    instructionLabel["text"] = "Merry Christmas!\n\n INSTRUCTIONS \n Finish the picture:\n Star: 't'\n Lights: 'r'\n Present: 'e'\n Eyes: 's' \nCarrot: 'h'\n Arm: 'd'\n  Buttons: 'g'\n Add Hat: 'y'\n RESTART: 'f'"
   
    master.bind("<Key>", keyAdd)
    counter.reset()
    score["text"] = 0

#each function in this class corresponds to a keyboard input which determines what is drawn
class presents:
    def __init__(self, x, y, x2, y2):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2

    def drawPresent():
        p1 = presents(81, 215, 120, 251)
        present = canvas.create_rectangle(p1.x,p1.y,p1.x2,p1.y2,fill="red")
        wrappingy = canvas.create_line(p1.x+21,p1.y+1,p1.x2-19,p1.y2-1,fill="yellow", width=5)
        wrappingx = canvas.create_line(p1.x+1,p1.y+18,p1.x2-1,p1.y2-18,fill="yellow",width=5)

    

    def drawHat():
        hb = presents(270,95,330,110) 
        htop = presents(280,60,320,96)
        bottom = canvas.create_rectangle(hb.x,hb.y,hb.x2,hb.y2,fill="gray40", outline="red")
        top = canvas.create_rectangle(htop.x,htop.y,htop.x2,htop.y2,fill="gray40", outline="red")

    def drawCarrot():
        carrot = canvas.create_polygon(294,135,302,135,302,135,298,160,298,160,294,135, outline="orange", fill="orange")

    def drawButtons():
        buttons_list = [175, 200, 225]
        for button in buttons_list:
            canvas.create_oval(292,button,304,button+10,fill="black")

    def drawStar():
        star_points = [60,17,40,25,60,17,80,25,80,25,65,10,65,10,80,5,80,5,65,0,40,25,55,10,55,10,40,5,40,5,55,0]
        canvas.create_polygon(star_points, fill="yellow",outline="yellow", width=5)

    def drawLights():
        row = [50,62,75]
        row1 = [38,50,62,74,85]
        row2 = [27,39,51,63,75,87,99]
        for light in row:
            canvas.create_oval(light,light+5,light+10,light,fill="white")
        for light1 in row1:
            canvas.create_oval(light1,light1+50,light1+10,light1+45,fill="red")
        for light2 in row2:
            canvas.create_oval(light2,light2+100,light2+10,light2+95,fill="gold")
        for light3 in row:
            canvas.create_oval(light3-23,light3+125,light3-13,light3+120,fill="white")

    def drawBranch():
        branch_points = [265,165,255,170,255,170,225,145,225,145,215,160,215,160,213,143,213,143,200,155,200,155,210,140,210,140,265,165 ]
        canvas.create_polygon(branch_points, fill="brown",outline="brown", width=2)

    def drawEyes():
        eye_list = [280,304]
        for eye in eye_list:
            canvas.create_oval(eye,125,eye+12,135,fill="black")

#waits for keyboard input to draw the snowman picture 
def keyAdd(event):
    if event.char == "e" or event.char == "E":
        presents.drawPresent()
    
    if event.char== "y" or event.char == "Y":
        presents.drawHat()
    
    if event.char == "h" or event.char == "H":
        presents.drawCarrot()
    
    if event.char == "g" or event.char == "G":
        presents.drawButtons()
    
    if event.char == "t" or event.char == "T":
        presents.drawStar()
    
    if event.char == "r" or event.char == "R":
        presents.drawLights()
    
    if event.char == "d" or event.char == "D":
        presents.drawBranch()

    if event.char == "s" or event.char == "S":
        presents.drawEyes()
    
    if event.char == "f" or event.char == "F":
        house()
 


#square objects created with coordinates and fill color, can move in any direction, enlarge and change colour 
class Squares:
    def __init__(self, x, y, x2, y2, colour):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.colour = colour
        
    def moveright(self):
        if self.x <= 400:
            self.x += 5
            self.y = self.y
            self.x2 += 5
            self.y2 = self.y2
        else:
            self.x = 0
            self.y = self.y
            self.x2 = 30
            self.y2 = self.y2
        self.draw()
    
    def moveleft(self):
        if self.x2 >= 0:
            self.x -= 5
            self.y = self.y
            self.x2 -= 5
            self.y2 = self.y2
        else:
            self.x = 400
            self.y = self.y
            self.x2 = 430
            self.y2 = self.y2
        self.draw()
        
    def moveup(self):
        if self.y2 >= 0:
            self.x = self.x
            self.y -= 5
            self.x2 = self.x2
            self.y2 -= 5
        else:
            self.x = self.x
            self.y = 300
            self.x2 = self.x2
            self.y2 = 330
        self.draw()
    
    def movedown(self):
        if self.y <= 300:
            self.x = self.x
            self.y += 5
            self.x2 = self.x2
            self.y2 += 5
        else:
            self.x = self.x
            self.y = 0
            self.x2 = self.x2
            self.y2 = 30
        self.draw()
            
        
    def bigger(self):
        self.x = self.x
        self.y = self.y
        self.x2 = self.x2+20
        self.y2 = self.y2+20
        
        
    def draw(self):
        canvas.create_rectangle(sq1.x, sq1.y, sq1.x2, sq1.y2, fill=sq1.colour)
        
    def blue(self):
        self.colour = "Blue"
        
    def green(self):
        self.colour = "Green"
        
    def orange(self):
        self.colour = "Orange"
        


    
    

sq1 = Squares(100, 120, 130, 150, "orange")
     
#this listens to what key is pressed which will determine the direction the object will move
def direction(event):
    if event.char == "d" or event.char == "D":
        sq1.moveright()
    if event.char == "a" or event.char == "A":
        sq1.moveleft()
    if event.char == "w" or event.char == "W":
        sq1.moveup()
    if event.char == "s" or event.char == "S":
        sq1.movedown()

    
      
        
#this function initialises the canvas for the flags game, removes all other redundant widgets
def moving():
    clearForGame()
    canvas.delete(ALL)
    instructionLabel["text"] = """Flags Game\n\nUsing 'awsd' keys:\nHold 'a'--> Left\nHold 'd'--> Right\nHold 'w'--> Up\nHold 's'--> Down\n\n
   *CHALLENGE*\n 1.Draw the flag\n  of Finland\n 2.Draw the flag\n  of Ireland\n (Hint: Use Enlarge to\n  cover more area)"""
    canvas.configure(bg="white")
    counter.reset()
    score["text"] = 0
    frame2.grid_remove()
    frame6.grid_remove()
    score.grid_remove()
    nameLabel.grid()
    nameButton.grid()
    dinput.grid()
    canvas.create_rectangle(sq1.x, sq1.y, sq1.x2, sq1.y2, fill="orange")
    
  ###FRAME AT BOTTOM FOR THE MOVEMENT GAME###
    frame5.grid()
  ###CONTROL PANEL, DIFFERENT COLOURS AND ENLARGE###
    blueButton = Button(frame5, text="BLUE", command=sq1.blue)
    blueButton.configure(width=12, bg="blue", fg="white")
    blueButton.grid(column=0, row=0)
    orangeButton = Button(frame5, text="ORANGE", command=sq1.orange)
    orangeButton.configure(width=12, bg="orange", fg="white")
    orangeButton.grid(column=1, row=0)
    greenButton = Button(frame5, text="GREEN", command=sq1.green)
    greenButton.configure(width=12, bg="green", fg="white")
    greenButton.grid(column=2, row=0)
    biggerButton = Button(frame5, text="ENLARGE", command=sq1.bigger)
    biggerButton.configure(width=9, bg="gray48", fg="white")
    biggerButton.grid(column=3, row=0)
    clearButton = Button(frame5, text="CLEAR", command=moving)
    clearButton.configure(width=9, bg="gray48", fg="white")
    clearButton.grid(column=4, row=0)
    ###LISTEN FOR AWSD KEY###
    master.bind("<Key>", direction)

#clear for Rocket Assembly game
def clearWhole():
    frame1.grid_remove()
    frame2.grid_remove()
    frame5.grid_remove()
    frame6.grid_remove()
    score.grid_remove()
    score.grid_remove()
    nameLabel.grid_remove()
    nameButton.grid_remove()
    dinput.grid_remove()
    counter.reset()
    frame6.grid()
    createForm()
   
    
def clearForGame():        #clear for the 2 second shape game
    frame1.grid()
    frame2.grid()
    frame5.grid_remove()
    frame6.grid_remove()
    score.grid()
    nameLabel.grid()
    nameButton.grid()
    dinput.grid()
    canvas.delete(ALL)
    instructionLabel["text"] = "Press Start Button \nClick within 2 secs\n\nGOOD LUCK!"
    canvas.configure(bg="white")
    counter.reset()
    score["text"] = 0


#process the input in the name entry, if there is any
def getName():
    name = dinput.get()
    if name:
        nameLabel["text"] = "Name: "+ name
        master.configure(bg="green")
        start.configure(bg="chartreuse2")
        nameButton.configure(bg="chartreuse2")
        dinput.configure(fg="green")
        instructionLabel.configure(bg="chartreuse2", width=16, height=20)

        frame1.configure(bg="green")
        frame2.configure(bg="green")

        name2 = Label(frame1, text=name, pady=10)
        name2.configure(width=32, fg="green",bg="chartreuse2", padx=0, font =("Helvetica", 16))
        name2.grid(column=2, row=0)

    else:
        nameLabel['text'] = "NO NAME ENTERED"
        canvas.delete(ALL)
        master.configure(bg="black")
        start.configure(bg="gray32")
        nameButton.configure(bg="gray32")

        frame1.configure(bg="black")
        frame2.configure(bg="black")


        
#initialises the rocket assembly frame
def createForm():
    titleToppings = Label(frame6, text="Rocket Assemble", bg="black",fg="white", padx=20)
    titleToppings.grid(row=0,column=0)
    addTopping = Label(frame6, text="""Target: Land on the Moon\nINSTRUCTIONS: \n1.Assume fuel, engines already included.\n2.Select your components below for your rocket. \n3.Boosters and command module are essential!\n4. Challenge: Get 100% chance\n\nHINT: Adding more components results in a heavier rocket,\n and a heavy rocket will decrease success rate...""")
    addTopping.grid(row=1,column=0)
    
#find out which checkboxes have been pressed then do something
def getToppings():     
    rocket.resetWeight()
    if landingvar.get() == 1:
        rocket.weightinc()
        counter.increment()
        landingLabel = Label(frame6, text="Go for launch", fg="green")
        landingLabel.grid(column=2,row=6)
    if landingvar.get() != 1:
        landingLabel = Label(frame6, text="Not selected", fg="red")
        landingLabel.grid(column=2,row=6)
        
    if commandvar.get() == 1:
        counter.increment()
        commandLabel = Label(frame6, text="Go for launch", fg="green")
        commandLabel.grid(column=2,row=5)
    if commandvar.get() != 1:
        commandLabel = Label(frame6, text="Not selected", fg="red")
        commandLabel.grid(column=2,row=5)
        
        
    if extravar.get() == 1:
        rocket.weightinc()
        counter.increment()
        extraLabel = Label(frame6, text="Go for launch", fg="green")
        extraLabel.grid(column=2,row=4)
    if extravar.get() != 1:
        extraLabel = Label(frame6, text="Not selected", fg="red")
        extraLabel.grid(column=2,row=4)
        
    if fuelvar.get() == 1:
        counter.increment()
        rocket.weightinc()
        fuelLabel = Label(frame6, text="Go for launch", fg="green")
        fuelLabel.grid(column=2,row=3)
    if fuelvar.get() != 1:
        fuelLabel = Label(frame6, text="Not selected", fg="red")
        fuelLabel.grid(column=2,row=3)
        
    if boostersvar.get() == 1:
        rocket.weightinc()
        counter.increment()
        boostersLabel = Label(frame6, text="Go for launch", fg="green")
        boostersLabel.grid(column=2,row=2)
    if boostersvar.get() != 1:
        boostersLabel = Label(frame6, text="Not selected", fg="red")
        boostersLabel.grid(column=2,row=2)
        
    
    if rovervar.get() == 1:
        rocket.weightinc()
        counter.increment()
        roverLabel = Label(frame6, text="Go for launch", fg="green")
        roverLabel.grid(column=2,row=7)
    if rovervar.get() != 1:
        roverLabel = Label(frame6, text="Not selected", fg="red")
        roverLabel.grid(column=2,row=7)
    calculate()
    
def weights():
    calculate()
    
#calculate the percentage based off the counter and rocket object values
def calculate():
    overallPercentage = 100
    chance = overallPercentage-(rocket.getWeight()*10)
    percentageLabel ["text"] = "Percentage Chance: {}%".format(chance)
    if counter.getCounter() < 2:
        percentageLabel ["text"] = "Percentage Chance: {}%\n\n Only {} components selected,\n rocket is incomplete.".format(chance, counter.getCounter())
    if rocket.getWeight() > 3:
        percentageLabel ["text"] = "Percentage Chance: 20%\n\n Many heavy components selected,\n fuel supply will drain before destination"
    if commandvar.get() != 1:
        percentageLabel["text"] = "Percentage Chance: 0%\n\n No Command Module selected!\nHow will you control the rocket???"
    if boostersvar.get() != 1:
        percentageLabel["text"] = "Percentage Chance: 0%\n\n Cannot leave atmosphere\nwithout booster rockets" 
    if counter.getCounter() == 3 and boostersvar.get() == 1 and commandvar.get() == 1 and landingvar.get() == 1:
        percentageLabel["text"] = "Percentage Chance: 100%\n\n SUCCESS" 
    counter.reset()
    
#reset the checkboxes(unticked)
def resetCheckboxes():
    counter.reset()
    percentageLabel["text"] = "Percentage Chance: 0%"
    boostersvar.set(0)
    fuelvar.set(0)
    extravar.set(0)
    commandvar.set(0)
    landingvar.set(0)
    rovervar.set(0)
    rocket.resetWeight()
    

master = Tk()
master.title("Assignment 2")
master.geometry("900x600")
master.configure(bg="red")

###MENU###
menu_bar= tkinter.Menu(master)
master.config(menu=menu_bar)
sub_menu= tkinter.Menu(menu_bar)
sub_menu1= tkinter.Menu(menu_bar)

menu_bar.add_cascade(label="Canvas", menu=sub_menu)
sub_menu.add_command(label="Shape game", command=clearForGame)
sub_menu.add_command(label="Draw Picture", command=house)
sub_menu.add_command(label="Flags", command=moving)
menu_bar.configure(bg="gray42")
sub_menu.configure(bg="gray70")

menu_bar.add_cascade(label="Checkboxes", menu=sub_menu1)
sub_menu1.add_command(label="Rocket Assembly", command=clearWhole)
sub_menu1.configure(bg="gray70")


###FRAME CONTAINING THE CANVAS###
frame1 = Frame(master, bd=10, bg="black", relief="ridge")
frame1.grid(column=2, row=5, padx=15)
canvas = Canvas(frame1, width=400, height=300)
canvas.grid(column=2, row=5, sticky="n")


score = Label(master, text=0)
score.configure(width=20)
score.grid(column=1, row=4, padx=10)


###START BUTTON###
frame2 = Frame(master, bd=10, bg="red", relief="raised")
frame2.grid(column=1, row=5, padx=10)

start = Button(frame2, text="START", command=cb2)
start.grid(column=1, row=4)
start.configure(height=5, padx=22, width=5, fg="black", bg="pink")

startreset = Button(frame2, text="RESET", command=clearForGame)
startreset.grid(column=2, row=4)
startreset.configure(height=5)


instructionLabel = Label(frame1, text="INSTRUCTIONS \n Press Start Button \nClick within 2 secs\n\nGOOD LUCK!")
instructionLabel.configure(bg="gray78", width=16, height=20)
instructionLabel.grid(column=6, row=5, padx=2)

  


###NAME ENTRY 3 PARTS AT TOP###
nameLabel = Label(master, text="Enter name below:")
nameLabel.configure(width=21)
nameLabel.grid(column=2, row=1 )
dinput = Entry(master)
dinput.grid(column=2, row=2)
dinput.configure(width=24)

nameButton = Button(master, text="SUBMIT NAME", command=getName)
nameButton.configure(width=20, bg="pink")
nameButton.grid(column=2, row=4)


#frame5 holds the colour buttons for squares
frame5 = Frame(master, bd=10, relief="raised")  
frame5.grid(column=2,row=8,pady=15)
frame5.grid_remove()


frame6 = Frame(master, bd=10, bg="gray95", width=80)  
frame6.grid(column=3,row=10,pady=30,padx=100)
frame6.grid_remove()
 
###CHECKBOXES###
boostersvar = IntVar()
boosters = Checkbutton(frame6, text="Booster Rockets",variable=boostersvar).grid(row=2, sticky=W)
fuelvar = IntVar()
fuel = Checkbutton(frame6, text="Backup Engine", variable=fuelvar).grid(row=3, sticky=W)
extravar = IntVar()
extrafuel = Checkbutton(frame6, text="Extra Fuel", variable=extravar).grid(row=4, sticky=W)
commandvar = IntVar()
command = Checkbutton(frame6, text="Command Module", variable=commandvar).grid(row=5, sticky=W)
landingvar = IntVar()
landing = Checkbutton(frame6, text="Lunar Module", variable=landingvar).grid(row=6, sticky=W)
rovervar = IntVar()
rover = Checkbutton(frame6, text="Lunar Rover", variable=rovervar).grid(row=7, sticky=W)
submitorder = Button(frame6, text="Launch", command=getToppings)    
submitorder.grid(column=2,row=8)   
resetrocket = Button(frame6, text="Reset", command=resetCheckboxes)    
resetrocket.grid(column=1,row=8)   

percentageLabel = Label(frame6, text=0)
percentageLabel.grid(column=1, row=10)

master.mainloop()

