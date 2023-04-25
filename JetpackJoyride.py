from cmu_graphics import *
import math
import random

def onAppStart(app):
    app.BestDistance=0
    app.distance=0
    app.bestDistance=0
    app.totalCoins=0
    app.coinAdder=1
    app.thisGameCoins=0
    app.gameOver=False
    app.inMenus=False
    app.playing=True
    app.stepsPerSecond=10
    app.width=900
    app.divisor=30
    app.height=(app.width//2)
    app.boardWidth=(app.width*4)//3
    app.boardHeight=(app.height*9)//10
    app.rows=app.boardHeight//app.divisor
    app.cols=app.boardWidth//app.divisor
    app.boardLeft=0
    app.boardTop=(app.height-app.boardHeight)//2
    app.cellBorderWidth=2
    app.board=[([None]*app.cols) for row in range(app.rows)]
    app.steps=0
    app.zapperList=[]
    app.missileList=[]
    app.laserList=[]
    app.playerCx=(app.boardWidth//app.cols)*4
    app.playerCy=app.boardTop+(app.boardHeight-(app.boardHeight//app.rows))
    app.playerRadius=(((app.boardHeight//app.rows)*2)//3)
    app.player=player(app)
    ##magnet
    ##https://www.freeiconspng.com/img/45627
    app.magnetImage='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/magnet.png'
    ##coins
    ##https://wikoles.net/uploads/posts/2022-09/jetpack-joyride-1.webp
    app.coinImage='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/coin.png'
    app.doubleCoinsImage='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/doubleCoin.png'
    ##gravityBelt
    ##https://static.wikia.nocookie.net/jetpackjoyride/images/a/a2/GravityBelt.png/revision/latest?cb=20120428052909
    app.gravityBeltImage='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/gravityBelt.png'
    ##pathFinder
    ##https://static.wikia.nocookie.net/speed-city/images/c/c6/GreenCircleIMG.png/revision/latest?cb=20190304214856
    app.pathFinderImage='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/pathFinder.png'
    app.magnetism=button('gadget',(app.width/2)-30,70,0,app.magnetImage,magnetismGadgetToggle)
    app.doubleCoins=button('gadget',(app.width/2)+(app.width/8)-30,70,0,app.doubleCoinsImage,doubleCoinsGadgetToggle)
    app.gravityBelt=button('gadget',(app.width/2)+(app.width/4)-30,70,0,app.gravityBeltImage,gravityBeltGadgetToggle)
    app.pathFinder=button('gadget',(app.width/2)+(app.width*3/8)-30,70,0,app.pathFinderImage,pathFinderGadgetToggle)
    app.selectedGadget=None
    ##default
    ##https://static.wikia.nocookie.net/jetpackjoyride/images/c/c8/Machine_Gun_Jetpack_%28Icon%29.jpg/revision/latest?cb=20210326125315
    app.defaultJetpack='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/default.png'
    ##balloon
    ##https://static.wikia.nocookie.net/jetpackjoyride/images/f/fb/DIY_Jetpack_%28icon%29.jpg/revision/latest?cb=20210326125613
    app.balloonJetpackImage='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/balloon.png'
    ##teddy
    ##https://static.wikia.nocookie.net/jetpackjoyride/images/2/26/Teddy_Jetpack.jpg/revision/latest?cb=20210326125741
    app.teddyJetpackImage='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/teddy.png'
    ##rocket
    ##https://static.wikia.nocookie.net/jetpackjoyride/images/5/5d/Blast_Off_Jetpack_%28icon%29.jpg/revision/latest?cb=20210326130110
    app.rocketJetpackImage='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/rocket.png'
    ##angel
    ##https://static.wikia.nocookie.net/jetpackjoyride/images/a/a8/Party_Jetpack_%28icon%29.jpg/revision/latest?cb=20210326132930
    app.partyJetpackImage='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/party.png'
    app.balloonJetpack=button('jetpack',(app.width/2)-30,220,0,
                              app.balloonJetpackImage,jetpackFunction)
    app.teddyJetpack=button('jetpack',(app.width/2)+(app.width/8)-30,220,0,
                            app.teddyJetpackImage,jetpackFunction)
    app.rocketJetpack=button('jetpack',(app.width/2)+(app.width/4)-30,220,0,
                             app.rocketJetpackImage,jetpackFunction)
    app.partyJetpack=button('jetpack',(app.width/2)+(app.width*3/8)-30,220,0,
                             app.partyJetpackImage,jetpackFunction)
    app.selectedJetpack=None
    app.buttonList=[app.magnetism,app.doubleCoins,app.gravityBelt,
                    app.pathFinder,app.balloonJetpack,app.teddyJetpack,
                    app.rocketJetpack,app.partyJetpack]
    app.gBelt=False
    app.pathList=[]
    app.tempPathList=[]
    app.pathIndex=0
    app.path=False
    app.dy=0
    app.d2y=2
    app.boosting=False
    app.grounded=True
    app.ceilinged=False
    app.coinRadius=12
    app.coinCollectRadius=app.playerRadius
    app.allCoinsList=[]
    app.gameOver=False
    app.playGameButtonX=(app.width*3)/5
    app.playGameButtonY=(app.height*3)/4
    app.playGameButtonWidth=app.width/3
    app.playGameButtonHeight=app.height/6
    app.zappersOn=True
    app.missilesOn=False
    app.lasersOn=False
    app.coinsOn=True
    app.zapped=False
    app.burnt=False
    app.backX1=0
    app.backX2=app.width
    app.backY=0
    app.background=rgb(63,76,113)
    app.columns=[column(0),column(app.width/2),column(app.width)]
    app.lights=[light((app.width/2)-70),light(((app.width/2)-70)+app.width)]
    app.tempSteps=0
    ##IMAGES
    ##https://static.wikia.nocookie.net/jetpackjoyride/images/0/01/BarryFullSpriteSheet.png/revision/latest/scale-to-width-down/250?cb=20210603110718
    ##https://express.adobe.com/sp/design/post/urn:aaid:sc:VA6C2:896e421d-5470-4fd2-b5d6-cb0ad68cb17a?workflow=quicktask&qId=remove-background&actionLocation=seo&autoDownload=true
    ##(adobeExpress to remove background)
    ##BARRY SPRITESHEET
    app.characterSpriteSheet='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/B5BE4421-A864-45FB-9963-808F7BBB49FD_adobe_express.png'
    app.characterImage1='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/characterImage1.png'
    app.characterImage2='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/characterImage2.png'
    app.characterImage3='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/characterImage3.png'
    app.characterImage4='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/characterImage4.png'
    app.characterImages=[app.characterImage1,app.characterImage2,app.characterImage3,app.characterImage4]
    app.characterImageIndex=0
    app.characterImage=app.characterImage1
    app.characterBoostImage='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/characterBoostImage.png'
    app.zapped1='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/zapped1.png'
    app.zapped2='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/zapped2.png'
    app.burnt1='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/burnt1.png'
    app.burnt2='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/burnt2.png'
    app.ded='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/ded.png'
    ##profile
    ##https://static.wikia.nocookie.net/jetpackjoyride/images/1/12/BarrySpriteJJ1.png/revision/latest/scale-to-width-down/250?cb=20210603104616
    app.profile='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/profile.png'
    ##missiles
    ##https://static.wikia.nocookie.net/jetpackjoyride/images/4/42/MissileJammer.png/revision/latest/thumbnail/width/360/height/360?cb=20120428044536
    app.fastRedMissile='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/fastRedMissile.png'
    ##https://static.wikia.nocookie.net/jetpackjoyride/images/9/94/EzyDodgeMissiles.png/revision/latest/thumbnail/width/360/height/360?cb=20120428172654
    app.slowBlueMissile='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/slowBlueMissile.png'
    ##https://static.wikia.nocookie.net/jetpackjoyride/images/5/51/About_to_come.png/revision/latest?cb=20120503044614
    app.redMissileWarning='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/redMissileWarning.png'
    app.blueMissileWarning='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/blueMissileWarning.png'
    ##lasers
    ##https://static.wikia.nocookie.net/jetpackjoyride/images/d/d7/Fires_laser.png/revision/latest?cb=20120511034357
    app.laserEnd='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/laserEnd.png'
    ##https://i.imgur.com/zAtRU1W.jpg
    app.laserWarning='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/laserWarning.png'
    ##https://cdn.mobygames.com/screenshots/16820647-jetpack-joyride-ipad-beware-of-flashing-lasers.png
    app.laserActive='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/laserActive.png'
    ##zappers
    ##https://static.wikia.nocookie.net/jetpackjoyride/images/a/ad/Dezapinator.PNG/revision/latest/thumbnail/width/360/height/360?cb=20120526011759
    app.zapperEnd='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/zapperEnd.png'
    ##background
    ##in game background was drawn based off of the original game by 'Halfbrick Studios'
    ##menu background
    ##data:image/jpeg;base64,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
    app.menuBackground='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/menuBackground.png'
    ##https://static.vecteezy.com/system/resources/previews/008/450/119/non_2x/hologram-podium-futuristic-circle-blue-hud-podium-modern-technology-gaming-vector.jpg
    app.hologram='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/hologram.jpg'
    ##inGameMusic
    ##https://vgmsite.com/soundtracks/jetpack-joyride/nrledqme/Jetpack%20Joyride.mp3
    inGameMusic='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/inGameMusic.mp3'
    #app.inGameMusic=Sound(inGameMusic)
    ##menuMusic
    ##https://downloads.khinsider.com/cp/add_album/10524
    menuMusic='/Users/patlucas/Desktop/15-112/15-112-Term-Project-1/menuMusic.mp3'
    #app.menuMusic=Sound(app.menuMusic)

class player:
    def __init__(self,app):
        self.x=app.playerCx
        self.y=app.playerCy
        self.width=app.playerRadius*2-5
        self.height=app.playerRadius*2-5
        self.left=self.x-(self.width/2)
        self.right=self.x+(self.width/2)
        self.top=self.y-(self.height/2)
        self.bottom=self.y+(self.height/2)

def onKeyPress(app,key):
    if app.playing and not app.gameOver:
        if not app.gBelt:
            if key=='space':
                app.grounded=False
                app.boosting=True
        else:
            if key=='space':
                app.boosting=not app.boosting

def onKeyRelease(app,key):
    if app.playing and not app.gameOver:
        if not app.gBelt:
            if key=='space':
                app.ceilinged=False
                app.boosting=False

def onMousePress(app,mouseX,mouseY):
    if app.inMenus:
        if pressInPlayGame(app,mouseX,mouseY):
            app.gameOver=False
            app.inMenus=False
            app.playing=True
        else:
            for button in app.buttonList:
                button.checkForPress(app,mouseX,mouseY)
            for button in app.buttonList:
                button.callButtonFunction(app)

def onStep(app):
    if app.playing:
        cellWidth,cellHeight=getCellSize(app)
        #app.menuMusic.pause()
        #app.inGameMusic.play(loop=True)
        if app.gameOver:
            app.boosting=False
            #app.inGameMusic.pause()
            #app.menuMusic.play(loop=True)
            if (app.stepsPerSecond>1):
                if app.grounded:
                    app.stepsPerSecond/=1.3
            else:
                app.playing=False
        if app.path:
            if app.steps%13==0:
                app.pathIndex=0
                app.tempPathList=pathFind(app)
            if app.tempPathList!=[]:
                app.pathList.append(pathCoordinate(app.width-
                    cellWidth*25/2,app.tempPathList[app.pathIndex]))
            app.pathIndex+=1
        app.player.y=app.playerCy
        app.player.top=app.playerCy-(app.player.width/2)
        app.player.bottom=app.playerCy+(app.player.width/2)
        cycleCharacterGraphic(app)
        checkCollisions(app)
        keepPlayerInBounds(app)
        moveBackground(app)
        movePlayer(app)
        moveObjects(app)
        #app.playingScreen to the left and loop image
        addObjects(app)
        movePath(app)
        app.distance+=1
        app.steps+=1
        if app.steps%50==0:
            app.stepsPerSecond+=0.1
    else:
        app.stepsPerSecond=10
        if app.distance>=app.bestDistance:
            app.bestDistance=app.distance
        app.distance=0
        app.steps=0
        app.tempSteps=0
        app.totalCoins+=app.thisGameCoins
        app.thisGameCoins=0
        app.zapperList=[]
        app.missileList=[]
        app.laserList=[]
        app.coinList=[]
        app.pathList=[]
        app.tempPathlist=[]
        app.pathIndex=0
        app.board=[([None]*app.cols) for row in range(app.rows)]
        app.zapped=False
        app.burnt=False
        app.zappersOn=True
        app.missilesOn=False
        app.lasersOn=False
        app.coinsOn=True
        app.inMenus=True

class pathCoordinate:
    def __init__(self,x,y):
        self.x=x
        self.y=y

def pathFind(app):
    cellWidth,cellHeight=getCellSize(app)
    return findPath(app,app.height/2,app.width-
                (cellWidth*25/2),[])

##will pathFind x steps into the future    
def findPath(app,possibleY,x,L):
    cellWidth,cellHeight=getCellSize(app)
    if len(L)==13:
        return L
    else:
        for direction in range(-1,2):
            if direction==-1:
                direction=0
            elif direction==0:
                direction=-1
            if((possibleY+(cellHeight*direction)>app.boardTop) and
               (possibleY+(cellHeight*direction)<app.boardTop+app.boardHeight)
               and (doesNotCollide(app,possibleY+(cellHeight*direction),x,L))):
                possibleY+=(cellHeight*direction)
                L.append(possibleY)
                x+=cellWidth
                solution=findPath(app,possibleY,x,L)
                if solution!=[]:
                    return solution
                x-=cellWidth
                possibleY-=(cellHeight*direction)
                L.pop()
        return []

def doesNotCollide(app,possibleY,x,L):
    cellWidth,cellHeight=getCellSize(app)
    row,col=getCell(app,x,possibleY)
    for row in range(app.rows):
        for col in range(app.cols):
            cellLeft,cellTop=getCellLeftTop(app,row,col)
            if (app.board[row][col]!=None):
                zapperPoints=[(cellLeft,cellTop),
                (cellLeft+cellWidth,cellTop),(cellLeft,cellTop+cellHeight),
                (cellLeft+cellWidth,cellTop+cellHeight)]
                for (xZ,yZ) in zapperPoints:
                    if ((x-(app.player.width/2)<=xZ<=x+(app.player.width/2)) and
                        (possibleY-(app.player.height/2)<=yZ<=
                         possibleY+(app.player.height/2))):
                        return False
    for missile in app.missileList:
        if (distance(x,possibleY,missile.posX,missile.height)<
            app.playerRadius+missile.radius+15):
            return False
    steps=app.steps
    for laser in app.laserList:
        height=laser.height
        moving=laser.moving
        for i in range (len(L)+1):
            height+=moving*8
            if ((height+cellHeight>app.boardTop+app.height)or
                (height<app.boardTop)):
                moving=-moving
        if (steps+len(L)-laser.time)>20:
            activated=True
        elif(steps+len(L)-laser.time)>60:
            activated=False
        else:
            activated=laser.activated
        if (((abs(height-possibleY)<=app.playerRadius)or
            (abs(possibleY-(height+cellHeight))<=app.playerRadius))
            and activated):
            return False
    return True

def movePath(app):
    cellWidth,cellHeight=getCellSize(app)
    for pathCoordinate in app.pathList:
        pathCoordinate.x-=cellWidth
        if pathCoordinate.x<0:
            app.pathList.pop(0)

def cycleCharacterGraphic(app):
    if not app.gameOver:
        if app.grounded:
            app.characterImageIndex=(app.characterImageIndex+1)%4
            app.characterImage=app.characterImages[app.characterImageIndex]
        else:
            app.characterImage=app.characterBoostImage
    else:
        if not app.grounded:
            if app.zapped:
                if app.steps%2!=0:
                    app.characterImage=app.zapped1
                else:
                    app.characterImage=app.zapped2
            elif app.burnt:
                if app.steps%2!=0:
                    app.characterImage=app.burnt1
                else:
                    app.characterImage=app.burnt2
        else:
            app.characterImage=app.ded

def checkCollisions(app):
    cellWidth,cellHeight=getCellSize(app)
    for row in range(app.rows):
        for col in range(app.cols):
            cellLeft,cellTop=getCellLeftTop(app,row,col)
            if (app.board[row][col]!=None):
                zapperPoints=[(cellLeft,cellTop),
                (cellLeft+cellWidth,cellTop),(cellLeft,cellTop+cellHeight),
                (cellLeft+cellWidth,cellTop+cellHeight)]
                for (x,y) in zapperPoints:
                    if ((app.player.left<=x<=app.player.right) and
                        (app.player.top<=y<=app.player.bottom)):
                        app.gameOver=True
                        app.zapped=True    
    for missile in app.missileList:
        if (distance(app.playerCx,app.playerCy,missile.posX,missile.height)<
            app.playerRadius+missile.radius):
            app.gameOver=True
            app.burnt=True
    for laser in app.laserList:
        if (((abs(laser.height-app.playerCy)<=app.playerRadius)or
            (abs(app.playerCy-(laser.height+cellHeight))<=app.playerRadius))
            and(laser.activated)):
            app.gameOver=True 
            app.burnt=True
    for coinList in app.allCoinsList:
        for coin in coinList:
            if (distance(app.playerCx,app.playerCy,coin.x,coin.y)<=
                app.coinCollectRadius+app.coinRadius and (coin.coinFill=='gold')):
                coin.coinFill=None
                app.thisGameCoins+=app.coinAdder

def keepPlayerInBounds(app):
    if (app.playerCy+app.playerRadius+app.dy>app.boardTop+app.boardHeight):
        app.dy=0
        app.playerCy=app.boardTop+app.boardHeight-(app.playerRadius)
        app.grounded=True
    elif (app.playerCy-app.playerRadius+app.dy<app.boardTop):
        app.dy=0
        app.playerCy=app.boardTop+app.playerRadius
        app.ceilinged=True
    else:
        if app.playerCy!=(app.boardTop+app.boardHeight-(app.playerRadius)):
            app.grounded=False
        if app.playerCy!=(app.boardTop+app.playerRadius):
            app.ceilinged=False

def movePlayer(app):
    if app.boosting:
        if ((not app.ceilinged)and(app.dy>-30)):
            app.dy-=app.d2y
    else:
        if ((not app.grounded)and(app.dy<30)):
            app.dy+=app.d2y
    app.playerCy+=app.dy
    app.player.y=app.playerCy
    app.player.top+=app.dy
    app.player.bottom+=app.dy

def moveBackground(app):
    cellWidth,cellHeight=getCellSize(app)
    for column in app.columns:
        if column.x<=-60:
            column.x=(app.width*3/2)-60
        column.x-=cellWidth
    for light in app.lights:
        if light.x<=-10:
            light.x=(app.width*2)-10
        light.x-=cellWidth

def moveObjects(app):
    cellWidth,cellHeight=getCellSize(app)
    for zapper in app.zapperList:
        zapper.x1-=cellWidth
        zapper.x2-=cellWidth
        zapper.col-=1
    for zapper in app.zapperList:
        if (zapper.col+zapper.pixels<0):
            app.zapperList.remove(zapper)
    for missile in app.missileList:
        if (app.steps-missile.time<40):
                missile.height=app.playerCy
        else:
            missile.activated=True
            if missile.type==1:
                if missile.posX>=(app.width//2):
                    missile.height=app.playerCy
            missile.posX-=missile.speed
    for missile in app.missileList:
        if (missile.posX+missile.radius<0):
            app.missileList.remove(missile)
    for laser in app.laserList:
        if ((laser.height<app.boardTop) or 
            (laser.height+cellHeight>app.boardTop+app.boardHeight)):
            laser.moving=-laser.moving
        laser.height+=4*laser.moving
    for laser in app.laserList:        
        if ((app.steps-laser.time)>40):
            laser.activated=True
        else:
            laser.activated=False
    for laser in app.laserList:
        if (app.steps-laser.time>80):
            app.laserList.remove(laser)
    for coinList in app.allCoinsList:
        for coin in coinList:
            coin.x-=cellWidth
    for coinList in app.allCoinsList:
        if coinList==[]:
            app.allCoinsList.remove(coinList)
        else:
            for coin in coinList:
                if coin.x<0:
                    coinList.remove(coin)

def addObjects(app):
    #ADDED div by app.stepsPerSecond so more generate as game goes on
    if app.steps>=50:
        if app.steps%500==0:
            app.tempSteps=0
            app.lasersOn=(not app.lasersOn) 
        else:
            if app.steps%100==0:
                if random.randrange(6)==5:
                    app.zappersOn=False
                else:
                    app.zappersOn=True
        if app.lasersOn:
            app.zappersOn=False
            app.missilesOn=False
            if (app.tempSteps%(1000//app.stepsPerSecond)==0 or app.tempSteps==0):
                addLaser(app)
            app.tempSteps+=1
        else:
            if app.zappersOn:
                if (app.tempSteps%(500//app.stepsPerSecond)==0 and 
                    app.laserList==[] and app.tempSteps<=480):
                    addZapper(app)
                if (app.tempSteps%(1000//app.stepsPerSecond)==0 and 
                    app.laserList==[] and app.tempSteps<=480):
                    addMissile(app)
            else:
                if (app.tempSteps%(200//app.stepsPerSecond)==0 and 
                    app.laserList==[] and app.tempSteps<=480):
                    addMissile(app)
            app.tempSteps+=1
        if app.coinsOn:
            if app.steps%50==0:
                addCoinList(app)

def redrawAll(app):
    drawBackground(app)
    if app.playing:
        cellWidth, cellHeight = getCellSize(app)
        if app.gameOver:
            drawLabel('GAME OVER',app.width/2,app.height/3,size=50,fill='red',
                      border='black',bold=True)
        drawLabel(f'{app.distance} M',app.width-20,20,size=23,fill='white',
                  border='black',borderWidth=1,bold=True,align='right')
        drawLabel(f'{app.thisGameCoins}',20,20,size=23,fill='gold',
                  border='black',borderWidth=1,bold=True,align='left')
        if app.selectedGadget!=None:
            drawImage(app.selectedGadget.image,(app.width/2),20,
                    width=app.width/18,height=app.width/18,align='center')
        #drawBoard(app)
        #drawPlayerHitbox(app)
        drawObjects(app)
        drawCoinGraphic(app)
        drawZapperGraphic(app)
        drawMissileGraphic(app)
        drawLaserGraphic(app)
        drawPath(app)
        drawCharacterGraphic(app)
    elif app.inMenus:
        drawMenuInterface(app)
        drawProfile(app)

def drawPath(app):
    for pathCoordinate in app.pathList:
        drawCircle(pathCoordinate.x,pathCoordinate.y,10,opacity=80,
                   fill=rgb(30,230,5),border='white')

def drawCoinGraphic(app):
    for coinList in app.allCoinsList:
        for coin in coinList:     
            if coin.coinFill!=None:   
                drawImage(app.coinImage,coin.x,coin.y,
                width=app.coinRadius*2,height=app.coinRadius*2,align='center')

def drawCharacterGraphic(app):
    #drawImage(app.characterSpriteSheet,0,0)
    drawImage(app.characterImage,app.playerCx,app.playerCy,
              width=app.playerRadius*3,height=app.playerRadius*3,align='center')
    if app.selectedJetpack!=None and not app.gameOver:
        if app.grounded:
            angle=25
        else:
            angle=0
        drawImage(app.selectedJetpack.image,app.playerCx-15,app.playerCy,
            width=app.playerRadius*4,height=app.playerRadius*4,
            align='center',rotateAngle=angle)

def drawMissileGraphic(app):
    for missile in app.missileList:
        if missile.type==0:
            if not missile.activated:
                drawImage(app.redMissileWarning,app.width-missile.radius-5,
                app.playerCy-2,width=missile.radius*2.5,
                height=missile.radius*2.5,align='center')
            else:
                drawImage(app.fastRedMissile,missile.posX,missile.height,
                width=missile.radius*4,height=missile.radius*4.25,align='center')
        else:
            if not missile.activated:
                drawImage(app.blueMissileWarning,app.width-missile.radius-5,
                app.playerCy,width=missile.radius*2.5,height=missile.radius*2.5,
                align='center')
            else:
                drawImage(app.slowBlueMissile,missile.posX,missile.height+2,
                width=missile.radius*4,height=missile.radius*4.5,align='center')

def drawLaserGraphic(app):
    cellWidth, cellHeight = getCellSize(app)
    for laser in app.laserList:
        drawImage(app.laserEnd,0,laser.height,width=cellWidth,
                  height=cellHeight)
        drawImage(app.laserEnd,app.width,laser.height,width=cellWidth,
                  height=cellHeight,rotateAngle=180,align='right-top')
        if not laser.activated:
            drawImage(app.laserWarning,cellWidth,laser.height+(cellHeight/2)-2,
                    width=app.width-(2*cellWidth),height=4)
        else:
            drawImage(app.laserActive,cellWidth,laser.height,
                    width=app.width-(2*cellWidth),height=cellHeight)

def drawZapperGraphic(app):
    if app.zapperList!=[]:
        cellWidth, cellHeight = getCellSize(app)
        for zapper in app.zapperList:
            sideLength=zapper.pixels*cellWidth
            if zapper.angle==0:
                angle=0
                mult=2
                length=sideLength
            elif zapper.angle==1:
                angle=-45
                mult=3
                length=sideLength*(2**0.5)
            elif zapper.angle==2:
                angle=90
                mult=2
                length=sideLength
            else:
                angle=45
                mult=3
                length=sideLength*(2**0.5)
            posX=(zapper.x1+zapper.x2)/2
            posY=(zapper.y1+zapper.y2)/2

            drawRect(posX,posY,length-cellWidth,cellHeight*7/8,fill='yellow',
                    border='gold',rotateAngle=angle,borderWidth=7,align='center')
            drawImage(app.zapperEnd,zapper.x1,zapper.y1,align='center',
                    rotateAngle=angle+180,width=cellWidth*mult,height=cellHeight*mult)
            drawImage(app.zapperEnd,zapper.x2,zapper.y2,align='center',
                    rotateAngle=angle,width=cellWidth*mult,height=cellHeight*mult)
class column:
    def __init__(self,x):
        self.x=x
    def drawColumn(self,app):
        drawRegularPolygon(self.x,60,60,3,
                fill=rgb(131,139,164),rotateAngle=180)
        drawRegularPolygon(self.x,app.height-60,60,3,
                fill=rgb(131,139,164))
        drawLine(self.x,0,self.x,app.height,fill=rgb(131,139,164),
                 lineWidth=20)
        
class light:
    def __init__(self,x):
        self.x=x
    def drawLight(self,app):
        drawCircle(self.x,app.boardTop+70,10,fill='red',border='black')

def drawBackground(app):
    if app.playing:
        for column in app.columns:
            column.drawColumn(app)
        for light in app.lights:
            light.drawLight(app)
        drawRect(-2,0,app.width+4,app.boardTop*2,fill='lightGrey',border='black')
        drawRect(-2,app.boardHeight,app.width+4,
                 app.boardTop*2,fill='lightGrey',border='black')
        drawRect(0,app.boardTop*2,app.width,app.boardTop,fill=rgb(131,139,164),
                 border='black')
        drawRect(0,app.boardHeight-app.boardTop,app.width,app.boardTop,fill=
                 rgb(131,139,164),border='black')
    else:
        drawImage(app.menuBackground,app.width*2/5,0,
                  width=app.width*3/5,height=app.height)
        drawImage(app.hologram,0,0,
              width=app.width*2/5,height=app.height)     
        drawLine(app.width*2/5,0,app.width*2/5,app.height,fill='red',lineWidth=5)
        drawImage(app.coinImage,30,75,width=50,height=50,align='left')  

def drawMenuInterface(app):
    drawLine((app.width*2/5)+2,app.height/4,app.width-2,app.height/4,
             fill='lightGrey',opacity=80,lineWidth=100)
    drawLine((app.width*2/5)+2,app.height*4/7,app.width-2,app.height*4/7,
             fill='lightGrey',opacity=80,lineWidth=100)
    drawRect(app.playGameButtonX,app.playGameButtonY,app.playGameButtonWidth,
             app.playGameButtonHeight,fill='gold',
             borderWidth=5,border='black')
    drawRect((app.width*7/10),40,170,50,fill='lightGrey',
             borderWidth=5,opacity=80,border='black',align='center')
    drawRect((app.width*7/10),(app.height/2)-40,180,50,fill='lightGrey',
             borderWidth=5,opacity=80,border='black',align='center')
    for button in app.buttonList:
        button.drawButton(app)
    drawMenuLabels(app)

def drawMenuLabels(app):
    drawLabel('GADGETS',(app.width*7)/10,40,size=30,fill='red',bold=True)
    drawLabel('JETPACKS',(app.width*7)/10,(app.height/2)-40,size=30,fill='red',bold=True)
    drawLabel('PLAY AGAIN',(app.width*9)/10,(app.height*5)/6,
    size=40,bold=True,align='right')
    drawLabel(f':{app.totalCoins}',80,70,size=40,align='left',fill='gold',
              bold=True,border='black')
    drawLabel(f'BEST DIST: {app.bestDistance}M',30,30,size=23,align='left',
              fill='white',bold=True,border='black',borderWidth=1)

def drawObjects(app):
    for zapper in app.zapperList:
        zapper.drawZapper(app)
    # for missile in app.missileList:
    #     if not missile.activated:
    #         missile.drawMissileWarning(app)
    #     else:
    #         missile.drawMissile()
    # for laser in app.laserList:
    #     laser.drawLaser(app)
    # for coinList in app.allCoinsList:
    #     for coin in coinList:
    #         coin.drawCoin(app)  

def drawProfile(app):
    drawImage(app.profile,app.width/8,app.height*1/3,
              width=app.width/5,height=app.width/5)
    if app.selectedGadget!=None:
        drawImage(app.selectedGadget.image,(app.width/4)+10,(app.height/2)+25,
                  width=app.width/20,height=app.width/20)
    if app.selectedJetpack!=None:
        drawImage(app.selectedJetpack.image,(app.width/7),(app.height/2)+40,
                  width=app.width/5,height=app.width/5,align='center')
    else:
        drawImage(app.defaultJetpack,(app.width/7),(app.height/2)+40,
                  width=app.width/5,height=app.width/5,align='center')


#Obstacles***
#angles: 0=horizontal,1=45 degrees, 2=vertical, 3=135 degrees
#pixels: in range of (2*app.rows)//3? of app.rows--longer zappers are less likely?
#zappers
class zapper:
    def __init__(self,app,pixels,angle,heightRow,col):
        cellWidth,cellHeight=getCellSize(app)
        self.pixels=pixels
        self.angle=angle
        self.heightRow=heightRow
        self.col=col
        self.x1,self.y1=getCellLeftTop(app,self.heightRow,self.col)
        self.x1+=(cellWidth*3/2)
        self.y1+=(cellWidth/2)
        heightRow=self.heightRow
        if self.angle==0:
            self.x2=self.x1+((self.pixels-1)*cellWidth)
            self.y2=self.y1
        elif self.angle==1:
            self.x2=self.x1+((self.pixels-1)*cellWidth)
            self.y2=self.y1-((self.pixels-1)*cellHeight)
            while ((heightRow-self.pixels)<-1):
                heightRow+=1
                self.y1+=cellHeight
                self.y2+=cellHeight
                self.heightRow+=1
        elif self.angle==2:
            self.x2=self.x1
            self.y2=self.y1+((self.pixels-1)*cellHeight)
            while ((heightRow+self.pixels)>app.rows):
                heightRow-=1
                self.y1-=cellHeight
                self.y2-=cellHeight
                self.heightRow-=1
        else:
            self.x2=self.x1+((self.pixels-1)*cellWidth)
            self.y2=self.y1+((self.pixels-1)*cellHeight)
            while ((heightRow+self.pixels)>app.rows):
                heightRow-=1
                self.y1-=cellHeight
                self.y2-=cellHeight
                self.heightRow-=1
    def __repr__(self):
        return f'col:{self.col},{self.pixels} pixels'
    def drawZapper(self,app):
        cellWidth, cellHeight = getCellSize(app)
        drawCircle(self.x1,self.y1,5)
        drawCircle(self.x2,self.y2,5)
        heightRow=self.heightRow
        col=self.col
        if self.angle==0:
            for i in range (self.pixels):
                app.board[heightRow][col]='yellow'
                col+=1
            if(app.board[heightRow][col]=='yellow'):
                app.board[heightRow][col]=None
        elif self.angle==1:
            for i in range(self.pixels):
                app.board[heightRow][col]='yellow'
                if(app.board[heightRow][col+1]=='yellow'):
                    app.board[heightRow][col+1]=None
                heightRow-=1
                col+=1
        elif self.angle==2:
            for i in range(self.pixels):
                app.board[heightRow][col]='yellow'
                if(app.board[heightRow][col+1]=='yellow'):
                    app.board[heightRow][col+1]=None
                heightRow+=1
        elif self.angle==3:
            for i in range(self.pixels):
                app.board[heightRow][col]='yellow'
                if(app.board[heightRow][col+1]=='yellow'):
                    app.board[heightRow][col+1]=None
                heightRow+=1
                col+=1

def addZapper(app):
    randPixels=random.randrange(3,((app.rows)//2)+1)
    randAngle=random.randrange(4)
    randRowHeight=random.randrange(app.rows)
    initialCol=((app.cols*3)//4)
    app.zapperList.append(zapper(app,randPixels,randAngle,randRowHeight,initialCol))
##missiles
##0=small&fast,1=large&slow
class missile:
    def __init__(self,app,type,time,height,posX):
        self.type=type
        self.time=time
        self.height=height
        self.posX=posX
        self.radius=10*type+20
        self.speed=(app.stepsPerSecond*3)/(type+1)
        self.activated=False
    def drawMissileWarning(self,app):
        drawCircle(app.width-self.radius-5,app.playerCy,self.radius,fill=None,border='red')
    def drawMissile(self):
        drawCircle(self.posX,self.height,self.radius,fill='red')
  
def addMissile(app):
    randType=random.randrange(2)
    app.missileList.append(missile(app,randType,app.steps,app.playerCy,app.width+50))
##lasers
##moving:0=not moving,-1=up,1=down
class laser:
    def __init__(self,height,time,moving):
        self.height=height
        self.moving=moving
        self.time=time
        self.activated=False
    def drawLaser(self,app):
        cellHeight=app.boardHeight//app.rows
        if self.activated:
            laserOpacity=30
        else:
            laserOpacity=10
        drawRect(0,self.height,app.boardWidth,cellHeight,fill='red',opacity=laserOpacity)
  
def addLaser(app):
    cellHeight=app.boardHeight//app.rows
    randomHeight=(random.randrange(app.rows)*cellHeight)+app.boardTop
    randomDirection=random.randrange(2)
    if randomDirection==0:
        randomDirection=-1
    app.laserList.append(laser(randomHeight,app.steps,randomDirection))

##coins
class coin:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.coinFill='gold'
    def drawCoin(self,app):
        drawCircle(self.x,self.y,app.coinRadius,fill=self.coinFill)

def addCoinList(app):
    coinHeight=random.randrange(app.boardTop+app.coinRadius,app.boardTop+app.boardHeight)
    coinCols=random.randrange(11)
    coinRows=random.randrange(4)
    while (coinHeight+(app.coinRadius*2*coinRows)>
           app.boardTop+app.boardHeight):
        coinHeight-=1
    firstCoinX=app.width+app.coinRadius
    firstCoinY=coinHeight
    coinList=[]
    for row in range(coinRows):
        for col in range(coinCols):
            coinList.append(coin(firstCoinX+(col*app.coinRadius*2)+5,
            coinHeight+(row*app.coinRadius*2)+5))
    app.allCoinsList.append(coinList)

##player
def drawPlayerHitbox(app):
    drawCircle(app.playerCx,app.playerCy,app.playerRadius,border='black',fill=None)
    drawRect(app.player.x,app.player.y,app.player.width,app.player.height,
             border='red',fill=None,align='center')
    drawCircle(app.player.x,app.player.top,3)
    drawCircle(app.player.x,app.player.bottom,3)
    drawCircle(app.player.left,app.player.y,3)
    drawCircle(app.player.right,app.player.y,3)
#buttons
class button:
    def __init__(self,type,x,y,price,image,buttonFunction):
        self.type=type
        self.x=x
        self.y=y
        self.price=price
        self.width=80
        self.height=80
        self.image=image
        self.buttonFunction=buttonFunction
        self.unlocked=False
    def __eq__(self,other):
        if isinstance(other,button)and self.x==other.x and self.type==other.type:
            return True
        else:
            return False
    def drawButton(self,app):
        if self.unlocked:
            buttonFill=None
        else:
            buttonFill='grey'
        if self.type=='gadget':
            if app.selectedGadget==self:
                buttonBorder='green'
            else:
                buttonBorder='red'
        elif self.type=='jetpack':
            if app.selectedJetpack==self:
                buttonBorder='green'
            else:
                buttonBorder='red'
        drawImage(self.image,self.x+5,self.y+5,width=self.width-10,height=self.height-10)
        drawRect(self.x,self.y,self.width,self.height,fill=buttonFill,
                 opacity=80,border=buttonBorder,borderWidth=5)
        if not self.unlocked:
            drawLabel(f'{self.price}',self.x+(self.width/2),
                self.y+(self.height/2),fill='gold',size=30,bold=True,border='black')
    def checkForPress(self,app,mouseX,mouseY):
        if ((self.x<=mouseX<=self.x+self.width)and
            (self.y<=mouseY<=self.y+self.height)):
            if (app.totalCoins>=self.price and self.unlocked!=True):
                self.unlocked=True
                app.totalCoins-=self.price
            if (self.type=='gadget'):
                if (self.unlocked and app.selectedGadget!=self):
                    app.selectedGadget=self
                else:
                    app.selectedGadget=None
            elif (self.type=='jetpack'):
                if (self.unlocked and app.selectedJetpack!=self):
                    app.selectedJetpack=self
                else:
                    app.selectedJetpack=None
    def callButtonFunction(self,app):   
        self.buttonFunction(self,app)

def magnetismGadgetToggle(self,app):
    if self==app.selectedGadget:
        app.coinCollectRadius=app.playerRadius+50
    else:
        app.coinCollectRadius=app.playerRadius

def doubleCoinsGadgetToggle(self,app):
    if self==app.selectedGadget:
        app.coinAdder=2
    else:
        app.coinAdder=1

def gravityBeltGadgetToggle(self,app):
    if self==app.selectedGadget:
        app.gBelt=True
    else:
        app.gBelt=False

def pathFinderGadgetToggle(self,app):
    if self==app.selectedGadget:
        app.path=True
    else:
        app.path=False

def jetpackFunction(self,app):
    pass

def pressInPlayGame(app,mouseX,mouseY):
    if((app.playGameButtonX<=mouseX<=app.playGameButtonX+
        app.playGameButtonWidth)and(app.playGameButtonY<=mouseY<=
        app.playGameButtonY+app.playGameButtonHeight)):
        return True
    else:
        return False


#FROM CMU CS ACADEMY
def distance(x0, y0, x1, y1):
    return ((x1 - x0)**2 + (y1 - y0)**2)**0.5

def drawBoard(app):
    for row in range(app.rows):
        for col in range(app.cols):
            color = app.board[row][col]
            drawCell(app, row, col, color)

def drawCell(app, row, col, color):
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
             fill=color, border='lightGrey',
             borderWidth=app.cellBorderWidth)

def getCell(app, x, y):
    dx = x - app.boardLeft
    dy = y - app.boardTop
    cellWidth, cellHeight = getCellSize(app)
    row = math.floor(dy / cellHeight)
    col = math.floor(dx / cellWidth)
    if (0 <= row < app.rows) and (0 <= col < app.cols):
      return (row, col)
    else:
      return None

def getCellLeftTop(app, row, col):
    cellWidth, cellHeight = getCellSize(app)
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)

def getCellSize(app):
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows
    return (cellWidth, cellHeight)

def drawBoard(app):
    for row in range(app.rows):
        for col in range(app.cols):
            color = app.board[row][col]
            drawCell(app, row, col,color)

def main():
    runApp()

if __name__=='__main__':
    main()