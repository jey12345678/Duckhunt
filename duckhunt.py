'''
Jeyason Jeyaparan and Justin Yan
June 15th 2018
duckhunt.py
create a playable duck hunt game
'''
from math import sqrt
from random import randint

import pygame
pygame.init()

#Set the game window.
WIDTH = 800
HEIGHT= 600
EXIT = 800



#Set the game window
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

#Define colours and fonts
LIGHTBLUE = (15, 197, 202)
LIGHTBROWN =(232, 187, 97)
GREEN =(44, 163, 83)
GREY = (128,128,128)
WHITE = (255,255,255)
ORANGE =(255, 150, 30)
YELLOW = (242, 238, 0)
BLUE = (0, 97, 255)
BROWN =(114, 83, 58) 
BROWNFLOOR = (214, 161, 77)

#Declare the types of text.
title = pygame.font.SysFont("Bauhaus 93",80)
subTitle = pygame.font.SysFont("Bauhaus 93",30)
font = pygame.font.SysFont("Elephant",48)
font2 = pygame.font.SysFont("Elephant",24)
font3 = pygame.font.SysFont("Arial",18,1)
font4 = pygame.font.SysFont("Elephant",96)

# Game Music
pygame.mixer.music.load('Title Screen.mp3')
pygame.mixer.music.set_volume(0.4)         
pygame.mixer.music.play(-1)

#gun Shot Sound
gunShots = pygame.mixer.Sound("Gun_loud.wav")
gunShots.set_volume(0.3)

#reload sound
reLoad = pygame.mixer.Sound("Gun_reloading.wav")
reLoad.set_volume(0.8)

#duck quacking sound
quack = pygame.mixer.Sound("Quack Quack.wav")
quack.set_volume(0.6)

#declare the variables for the ducks that are shot and the ducks that will be flying away.
ducksShot = 0
ducksFlownAway =0

#Declare the elasped time
elaspedTime = 0

#This is the score variable
score1 = 0

#Set the size of every grid piece
GRIDSIZE = 10

#declare inPlay variable
inPlay = True

#Variables for the gun and the bullet
bulletX = []
xGun = 400
gunSpeed = 20
yGun = 500
bulletY = []
bulletSpeed = 70
bulletAlive = []

#Variables for the ducks
numDucks = 10
ducksX = []
ducksY = []
ducksSpeed = []
ducksAlive = []

#Set time
BEGIN = pygame.time.get_ticks()
clock = pygame.time.Clock()
FPS = 24

#List of all images
grass = pygame.image.load("rsz_1grasslong.png")
trees = pygame.image.load("rsz_tree.png")
noSoundImage = pygame.image.load("nosound.png")
crossSign = pygame.image.load("rsz_crossmark.jpg")
mainScreenPic = pygame.image.load("duckmainscreen.jpg")
ducks = pygame.image.load("rsz_1duck.png")
backToMainMenuPicture = pygame.image.load("rsz_back-button.jpg")
dogPicture = pygame.image.load("46hjO1K.fw.png")
duckPicture = pygame.image.load("Duck_Hunt-logo-8044A0A3B6-seeklogo.com.fw.png")
waterGun = pygame.image.load("191596 (1).fw.png")
arrowKeys = pygame.image.load("b27f552f-74d1-4ed5-af69-3d72f7af72b0.fw.png")

#distance function
def distance(x1,y1,x2,y2):
        return sqrt((x1-x2)**2 + (y1-y2)**2)

#draw the messages that are supposed to appear on the screen
def drawMessages():
        
        ducksElaspedGraphics = font2.render("Time:"+str(round((elaspedTime)/1000.0,1))+"s",1,BLUE)
        ducksShotGraphics = font2.render("Ducks Shot: "+str((ducksShot)),1,BLUE)
        ducksFlownAwayGraphics = font2.render("Ducks Flown Away:"+str((ducksFlownAway)),1,BLUE)

        #Display the time on the screen.
        gameWindow.blit(ducksElaspedGraphics,(500,500))

        #Display the amount of ducks that were shot.
        gameWindow.blit(ducksShotGraphics,(500,520))

        #Display the amount of ducks that 
        gameWindow.blit(ducksFlownAwayGraphics,(500,540))
                
     
#Create an endgame screen if the player did okay at the end!
def endGameOkay():
        while inPlay:
                #Fill the gameWindow as orange.
                gameWindow.fill(ORANGE)
                pygame.draw.rect(gameWindow,LIGHTBROWN,(0,500,800,100),0)
                 
                #Player score results
                scoreGraphics = font.render("Score:"+str((score1)),1,BLUE)
                pygame.draw.rect(gameWindow,WHITE,(45,100,690,350),6)
                gameWindow.blit(scoreGraphics,(100,100))
                gameOkay = font4.render("Good Try!",1,WHITE)
                gameWindow.blit(gameOkay,(150,225))
                okayMsg = font2.render("Better Luck Next Time!",1,WHITE)
                
                gameWindow.blit(okayMsg,(400,400))
                gameWindow.blit(crossSign, (750,0))
                
                #There is the sound image
                pygame.draw.rect(gameWindow,WHITE,(750,50,50,50),0)
                gameWindow.blit(noSoundImage,(750,50))
                
                for event in pygame.event.get():
                    if event.type==pygame.MOUSEBUTTONDOWN:
                            
                        #Exit Function
                        crossButton()
                        
                        #Mute Function
                        noSound()
                                 
                #Updates the screen
                pygame.display.update()
                
                
#Create an endgame screen if the player won at the end!
def endGameWin():
        while inPlay:
                
                #Fill the gameWindow as green.
                gameWindow.fill(GREEN)
                pygame.draw.rect(gameWindow,LIGHTBROWN,(0,500,800,100),0)
                
                #Player score results
                scoreGraphics = font.render("Score:"+str((score1)),1,BLUE)
                pygame.draw.rect(gameWindow,WHITE,(45,100,690,350),6)
                gameWindow.blit(scoreGraphics,(100,100))
                gameOkay = font4.render("You Win!",1,WHITE)
                gameWindow.blit(gameOkay,(160,225))
                okayMsg = font2.render("Great Job!",1,WHITE)
                
                gameWindow.blit(okayMsg,(400,400))
                gameWindow.blit(crossSign, (750,0))
                
                #There is the sound image
                pygame.draw.rect(gameWindow,WHITE,(750,50,50,50),0)
                gameWindow.blit(noSoundImage,(750,50))
        
                
                for event in pygame.event.get():
                    if event.type==pygame.MOUSEBUTTONDOWN:

                        #Exit Function
                        crossButton()

                        #Mute Function
                        noSound()

                #Updates the screen
                pygame.display.update()
        
#Create an endgame screen if the player lost at the end!
def endGameLose():
        while inPlay:
                
                #Fill the gameWindow as lightblue.
                gameWindow.fill(LIGHTBLUE)
                pygame.draw.rect(gameWindow,LIGHTBROWN,(0,500,800,100),0)

                #Players score results
                scoreGraphics = font.render("Score:"+str((score1)),1,BLUE)
                pygame.draw.rect(gameWindow,WHITE,(45,100,690,350),6)
                gameWindow.blit(scoreGraphics,(100,100))
                gameOkay = font4.render("Game Over!",1,WHITE)
                gameWindow.blit(gameOkay,(110,225))
                okayMsg = font2.render("You lose too bad!",1,WHITE)

                gameWindow.blit(okayMsg,(400,400))
                gameWindow.blit(crossSign, (750,0))
                
                #There is the sound image
                pygame.draw.rect(gameWindow,WHITE,(750,50,50,50),0)
                gameWindow.blit(noSoundImage,(750,50))
        
                for event in pygame.event.get():
                    if event.type==pygame.MOUSEBUTTONDOWN:
                            
                        #Exit Function
                        crossButton()

                        #Mutes Music
                        noSound()
                        
                #Updates the screen
                pygame.display.update()
        
#redrawgameWindow function used in the game
def reDrawGameWindow():

    #Fill the gameWindow as lightblue.
    gameWindow.fill(LIGHTBLUE)
        
    #Create the lightbrown rectangle
    pygame.draw.rect(gameWindow,LIGHTBROWN,(0,500,800,100),0)

    #Create the grass
    gameWindow.blit(grass,(0,300))
    
    
    #Create the crossbutton
    gameWindow.blit(crossSign,(750,0))

    #Create no sound button
    pygame.draw.rect(gameWindow,WHITE,(750,50,50,50),0)
    gameWindow.blit(noSoundImage,(750,50))

    
    #There is the sound image
    pygame.draw.rect(gameWindow,WHITE,(750,50,50,50),0)
    gameWindow.blit(noSoundImage,(750,50))

    #Make the sun
    pygame.draw.circle(gameWindow,YELLOW,(50,50),40,0)

    
    #Create the ducks    
    for i in range(numDucks):
        if ducksAlive[i] == True:
                gameWindow.blit (ducks,(ducksX[i],ducksY[i]))
                
                
    #Create the bullets            
    for i in range(len(bulletX)):
            pygame.draw.ellipse(gameWindow,BLUE,(bulletX[i],bulletY[i],10,20),0)
            
   #Make tree x reference variable
    treeXRef = 0

    #Create the six trees
    for i in range(6):
        gameWindow.blit(trees,(treeXRef,100))
        treeXRef = treeXRef+150
        
    #Make a cloud x reference variable
    cloudXRef = 110

    #Make clouds
    for i in range(4):
        pygame.draw.circle(gameWindow,WHITE,(cloudXRef+ 40,50),30,0)
        pygame.draw.circle(gameWindow,WHITE,(cloudXRef,50),20,0)
        pygame.draw.circle(gameWindow,WHITE,(cloudXRef+80,50),20,0)
        cloudXRef = cloudXRef+150
        
    
    

        
#Create the game function        
def game():

    #Declare the variables that are going to be used in the game function    
    xGun = 400
    yGun = 500    
    ref = -5000
    speed = 5
    

    #Declare the global variables, since they will be used in different functions later on.
    global elaspedTime
    global ducksShot
    global ducksFlownAway
    global score1
    
    #Create the ducks
    for i in range(numDucks):
      ducksX.append(ref)
      ducksY.append(randint(0,HEIGHT/2))
      ducksSpeed.append(speed)
      ducksAlive.append(True)
      ref = ref+300
      speed = speed+1

      
      
    while inPlay and (ducksShot+ducksFlownAway)<numDucks:
            
       #re draw the game window.
        reDrawGameWindow()     
        clock.tick(FPS)
        
        #Create the timer
        elaspedTime = pygame.time.get_ticks()-BEGIN
        
        #Create the gun
        pygame.draw.rect(gameWindow,ORANGE,(xGun,yGun,30,100),0)
        pygame.draw.rect(gameWindow,BLUE,(xGun+30,yGun+70,30,30),0)
        
        for event in pygame.event.get():
              
            #If the mouse is clicked on, then the nosound function and cross button function will activate.
            if event.type == pygame.MOUSEBUTTONDOWN:
               crossButton()
               noSound()


               
            if event.type == pygame.KEYDOWN:  
                #If upper arrow key is pressed, bullets will shoot out.
                    if event.key == pygame.K_UP:
                            for i in range(numDucks):
                                    bulletX.append(xGun+30/2)
                                    bulletY.append(yGun)
                                    gunShots.play()
                                    
                                    
        keys = pygame.key.get_pressed()
        #Make the gun move
        if keys[pygame.K_LEFT] and xGun >0:
                xGun = xGun - gunSpeed
        if keys[pygame.K_RIGHT] and xGun<WIDTH-50:
                xGun = xGun+gunSpeed
                
        
                
        #if ducks fly away to the end, they disappear
        for i in range(numDucks):
            ducksX[i] = ducksX[i]+ducksSpeed[i]
            if ducksAlive[i] and (ducksX[i]>EXIT):
                    ducksAlive[i] = False
                    quack.play()
                    ducksFlownAway = ducksFlownAway+1
                    print ducksFlownAway,"flown away!"
                    
        #If the ducks are shot than they disappear             
        for i in reversed(range(len(bulletX))):
                bulletY[i] = bulletY[i] - bulletSpeed
                print round(distance(bulletX[i],bulletY[i],ducksX[i],ducksY[i]),0)
                if round(distance(bulletX[i],bulletY[i],ducksX[i],ducksY[i]),0)<=100 and ducksAlive[i] == True: 
                        ducksAlive[i] = False
                        ducksShot = ducksShot+1
                        print ducksShot,"ducks were shot!"
                if bulletY[i]<0:
                        bulletX.pop(i)
                        bulletY.pop(i)
                        

        #Draw the messages
        drawMessages()
        pygame.display.update()

    pygame.time.delay(3000)
    score1 = (ducksShot*10   )-(ducksFlownAway*5)   
    if ducksFlownAway >= 3:
        endGameLose()
    elif ducksShot == 10:
        endGameWin()
        
    elif ducksShot<=9 and ducksFlownAway<3:
         endGameOkay()
        
       
#crossButton function
def crossButton():
    #If user clicks the x button then the pygame turns off.
    if 750<=pygame.mouse.get_pos()[0]<=800 and 0<=pygame.mouse.get_pos()[1]<=50:
        pygame.quit()

#noSound function
def noSound():
        if 750<=pygame.mouse.get_pos()[0]<=800 and 50<=pygame.mouse.get_pos()[1]<=100:
            if pygame.mixer.music.get_busy() == True:
                pygame.mixer.music.stop()
            else:
                pygame.mixer.music.play(-1)
                
#Back to Main Menu function
def backToMainMenu():
        if 750<= pygame.mouse.get_pos()[0]<=800 and 100<=pygame.mouse.get_pos()[1]<=150:
                mainMenu(mouseActive)
                pygame.display.update()
        
#The how to play the game function
def howToPlayGame():
    while inPlay:
        gameWindow.fill(LIGHTBLUE)
        #Title of the How to Play Function
        title = font.render("How To Play", 1,WHITE)
        gameWindow.blit(title,(250,50))
        
        #Headers of controls and objectives
        controls = font2.render("Controls", 1,WHITE)
        gameWindow.blit(controls,(100,150))
        objective = font2.render("Objective", 1,WHITE)
        gameWindow.blit(objective,(540,150))
        
        #Lists of Controls
        controls1 = font3.render("User presses up arrow key to shoot", 1,WHITE)
        gameWindow.blit(controls1,(25,200))
        controls2 = font3.render("User presses left arrow key to move left", 1,WHITE)
        gameWindow.blit(controls2,(25,300))
        controls3 = font3.render("User presses right arrow key to move right", 1,WHITE)
        gameWindow.blit(controls3,(25,400))
        
        #List of Objectives
        objective1 = font3.render("Your goal is to shoot all ten ducks that", 1,WHITE)
        gameWindow.blit(objective1,(400,200))
        objective2 = font3.render("fly across the screen, if possible!", 1,WHITE)
        gameWindow.blit(objective2,(400,225))
        objective3 = font3.render("If  three  ducks fly away then it is game over!", 1,WHITE)
        gameWindow.blit(objective3,(400,300))
        objective6 = font3.render("So pay attention to the screen!", 1,WHITE)
        gameWindow.blit(objective6,(400,400))
        objective8 = font3.render("Ducks may use objects i.e clouds,trees", 1,WHITE)
        gameWindow.blit(objective8,(400,425))
        objective9 = font3.render("to throw off the player", 1,WHITE)
        gameWindow.blit(objective9,(400,450))
        objective10 = font3.render("Score is determined by amount of ducks shot!",1,WHITE)
        gameWindow.blit(objective10,(400,500))
        objective11 = font3.render("10 points are awarded to every duck you shoot.",1,WHITE)
        gameWindow.blit(objective11,(400,525))
        objective12 = font3.render("You lose 5 points times every ducks flown away.",1,WHITE)
        gameWindow.blit(objective12,(400,550))
        
        #Game Pictures
        gameWindow.blit(crossSign, (750,0))
        gameWindow.blit(dogPicture, (12.5,6.25))
        gameWindow.blit(duckPicture, (500,-40))
        gameWindow.blit(arrowKeys, (-40,400))
        gameWindow.blit(waterGun, (475,150))
        
        #There is the sound image
        pygame.draw.rect(gameWindow,WHITE,(750,50,50,50),0)
        gameWindow.blit(noSoundImage,(750,50))
        
        #There is the back to main menu image
        gameWindow.blit(backToMainMenuPicture,(750,100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                crossButton()
                noSound()
                backToMainMenu()

#function for main menu
def mainMenu(mouseActive):
    
    #Have game window be filled light blue.
    gameWindow.fill(LIGHTBLUE)
        
    #Create the lightbrown rectangle
    pygame.draw.rect(gameWindow,LIGHTBROWN,(0,400,800,200))

    #Create the main screen picture
    gameWindow.blit(mainScreenPic,(0,0))
    
    #Create Duck Hunt Title
    gameTitle = title.render("DUCK HUNT",1,WHITE)
    gameWindow.blit(gameTitle,(50,330))

    #Create the Authors Initials.
    initials = subTitle.render("By:Jeyason and Justin",1,WHITE)
    gameWindow.blit(initials,(500,330))
    
    #Make xReference and yReference variables for main menu ducks.
    xRef = 0
    xRef1 = 500
    yRef = 200

    #Make three ducks going up.
    for i in range(3):
        gameWindow.blit(ducks,(xRef,yRef))
        yRef= yRef -100
        xRef=xRef+120

    #Make three ducks
    for i in range(3):
        gameWindow.blit(ducks,(xRef1,yRef))
        yRef = yRef + 100
        xRef1 = xRef1+100

    #Make the sun
    pygame.draw.circle(gameWindow,YELLOW,(50,50),40,0)

    #Make the clouds
    pygame.draw.circle(gameWindow,WHITE,(450,40),30,0)
    pygame.draw.circle(gameWindow,WHITE,(410,40),20,0)
    pygame.draw.circle(gameWindow,WHITE,(490,40),20,0)
    pygame.draw.circle(gameWindow,WHITE,(180,40),30,0)
    pygame.draw.circle(gameWindow,WHITE,(140,40),20,0)
    pygame.draw.circle(gameWindow,WHITE,(220,40),20,0)
    
    #cross sign image
    gameWindow.blit(crossSign,(750,0))

    #There is the sound image
    pygame.draw.rect(gameWindow,WHITE,(750,50,50,50),0)
    
    gameWindow.blit(noSoundImage,(750,50))

    while inPlay:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                #Print the mouse coordinates
                print pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]

                #If the mouse goes over the how to play box or the play the game box, then it should turn from green to grey.
                if 50<= pygame.mouse.get_pos()[0]<=370 and 420<=pygame.mouse.get_pos()[1]<=570:
                    pygame.draw.ellipse(gameWindow,GREY,(50,420,320,150))
                else:
                    pygame.draw.ellipse(gameWindow,GREEN,(50,420,320,150))
       
                if 470<=pygame.mouse.get_pos()[0]<=790 and 420<=pygame.mouse.get_pos()[1]<=570:
                    pygame.draw.ellipse(gameWindow,GREY,(430,420,320,150))
                else:
                    pygame.draw.ellipse(gameWindow,GREEN,(430,420,320,150))
      
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                #If the user clicks the how to play button, then the how to play function should play and if the user clicks the play the game button, the game function should play.
                if 50<= pygame.mouse.get_pos()[0]<=370 and 420<=pygame.mouse.get_pos()[1]<=570:
                    game()
                elif 470<=pygame.mouse.get_pos()[0]<=790 and 420<=pygame.mouse.get_pos()[1]<=570:
                    howToPlayGame()
                    
                crossButton()
                noSound()
        howToPlay = subTitle.render("How To Play!",1,WHITE)
        gameWindow.blit(howToPlay,(500,480))
        playTheGame = subTitle.render("Play The Game!",1,WHITE)
        gameWindow.blit(playTheGame,(100,480))
        pygame.display.update()

while inPlay:
    mouseActive = pygame.mouse.get_focused()
    mainMenu(mouseActive)
    pygame.display.update()


            

    


                    
