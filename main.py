import pygame
import random
from lerp import lerp
from dudepose import DudePose

pygame.init()
 
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 400
 
BLACK = (0,0,0)
WHITE = (255,255,255)
 
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption('My Cool Graphics')
clock = pygame.time.Clock()
 
families = []


    

class Tempo:
  startTime = 0
  msPerBeat = 500
  beatsPerMeasure = 4

  def __init__(self, beatsPerMinute, beatsPerMeasure, delay=0):
      
    self.msPerBeat = 1/(beatsPerMinute/(60*1000))
    
    self.startTime = pygame.time.get_ticks() + (delay * self.msPerBeat)
    self.beatsPerMeasure = beatsPerMeasure

  def getBeat(self):
    beats = self.getTotalBeats()
    fraction = beats - int(beats)
    whole = int(beats)
    measured = whole % self.beatsPerMeasure

    return measured + fraction

  def getTotalBeats(self):
    now = pygame.time.get_ticks()
    deltaTime = now - self.startTime
    beats = deltaTime/self.msPerBeat

    return beats

  def drawTempo(self, gameDisplay, position):
    beat = self.getBeat()
    beat = int(beat)

    for i in range(self.beatsPerMeasure):
      if i <= beat:
        pygame.draw.circle(gameDisplay, (0, 255, 0), [position[0] + i * 20, position[1]], 5)
    

pygame.mixer.init()
pygame.mixer.music.load('Village-People-YMCA.mp3')
pygame.mixer.music.play()

# create the shared Tempo object.
TEMPO = Tempo(126,4,2)
  
class Dude:
  animationFinished = True
  
  
  def __init__(self, position, size):
    self.position = position
    self.size = size
    self.leftHanded = random.randrange(100) < 20
    # default the time to a random time so that all animations don't start at exactly
    # the same time
    self.time = pygame.time.get_ticks() + random.randrange(3000)
    self.frameCount = 0

  def getExtentsRect(self):
    return pygame.Rect([0, 0, 16*self.size, 16*self.size])

  def drawLine(self, gameDisplay, startingPoint, endingPoint, color = (0,0,0)):
    scale = self.size
    posAdjusted = (self.position[0], self.position[1] - (16*scale))

    pygame.draw.line(gameDisplay, color, (posAdjusted[0]+(startingPoint[0] * scale),posAdjusted[1]+(startingPoint[1] * scale)), (posAdjusted[0]+(endingPoint[0] * scale),posAdjusted[1]+(endingPoint[1] * scale)))


  def drawCircle(self, gameDisplay, centerPoint, radius, color = (0,0,0), lineWidth=1):
    scale = self.size
    posAdjusted = (self.position[0], self.position[1] - (16*scale))

    pygame.draw.circle(gameDisplay, color, [posAdjusted[0] + (centerPoint[0]*scale),posAdjusted[1] + (centerPoint[1]*scale)], radius*scale, lineWidth)


  def drawStanding(self, gameDisplay):
    
    # this was just to show you that we could possibly do this another way.
    # ignore for now
    # L8,4,8,12,2,2,8,6,14,2,8,6,8,12,4,14,8,1,12,14
    # C8,2,2

    # body
    self.drawLine(gameDisplay, (8,4), (8,12) )

    # left arm
    self.drawLine(gameDisplay, (2,2), (8,6))

    # right arm
   
    self.drawLine(gameDisplay, (14,2), (8,6))

    # left leg
   
    self.drawLine(gameDisplay, (8,12), (4,16))
    # right leg
    
    self.drawLine(gameDisplay, (8,12), (12,16))

    # draw head
    self.drawCircle(gameDisplay, (8,2), 2)

    # wouldn't it be nice to just be able to do this instead!
    # [[(8,12), (4,6)], [(8,12), (12,16)]]


  def drawTap(self, gameDisplay):

    # body
    self.drawLine(gameDisplay, (8,4), (8.5,12) )

    # left arm
    self.drawLine(gameDisplay, (3,3), (8,6))
    self.drawLine(gameDisplay, (2,3), (3,3))

    # right arm
   
    self.drawLine(gameDisplay, (14,2), (8,6))

    # left leg
   
    self.drawLine(gameDisplay, (8.5,12), (4,16))
    # right leg
    
    self.drawLine(gameDisplay, (8.5,12), (11,14))
    self.drawLine(gameDisplay, (11,14), (12,16))

    # draw head
    self.drawCircle(gameDisplay, (8,2), 2)


  def drawM(self, gameDisplay):
  
    # draw the M in YMCA

    # body
    self.drawLine(gameDisplay, (8,4), (8,12) )

    # left arm
    self.drawLine(gameDisplay, (4,6), (8,6))
    self.drawLine(gameDisplay, (4,6), (4,8))

    # right arm
   
    self.drawLine(gameDisplay, (12,6), (8,6))
    self.drawLine(gameDisplay, (12,6), (12,8))

    # left leg
   
    self.drawLine(gameDisplay, (8,12), (4,16))
    # right leg
    
    self.drawLine(gameDisplay, (8,12), (12,16))

    # draw head
    self.drawCircle(gameDisplay, (8,2), 2, (255,0,0))


  def drawC(self, gameDisplay):
  
    # draw the C in YMCA

    # body
    self.drawLine(gameDisplay, (8,4), (8,12) )

    # left arm
    self.drawLine(gameDisplay, (4,6), (8,6))
    self.drawLine(gameDisplay, (4,6), (4,0))
    self.drawLine(gameDisplay, (4,0), (12,0))

    # right arm
   
    self.drawLine(gameDisplay, (12,6), (8,6))

    # left leg
   
    self.drawLine(gameDisplay, (8,12), (4,16))
    # right leg
    
    self.drawLine(gameDisplay, (8,12), (12,16))

    # draw head
    self.drawCircle(gameDisplay, (8,2), 1.9, (0,255,0))


  def drawA(self, gameDisplay):
    
    # draw the A in YMCA
    # body
    self.drawLine(gameDisplay, (8,4), (8,12) )

    # left arm
    self.drawLine(gameDisplay, (4,6), (8,6))
    self.drawLine(gameDisplay, (4,6), (7,1))

    # right arm
   
    self.drawLine(gameDisplay, (12,6), (8,6))
    self.drawLine(gameDisplay, (12,6), (9,1))

    # left leg
   
    self.drawLine(gameDisplay, (8,12), (4,16))
    # right leg
    
    self.drawLine(gameDisplay, (8,12), (12,16))

    # draw head
    self.drawCircle(gameDisplay, (8,2), 2, (255,0,0))


  def animateYMCA(self, gameDisplay):

    beat = TEMPO.getBeat()
    totalBeats = TEMPO.getTotalBeats()

    if beat < 2:
      self.drawStanding(gameDisplay)
    elif beat < 3:
      self.drawM(gameDisplay)
    elif beat < 3.5:
      self.drawC(gameDisplay)
    else:
      self.drawA(gameDisplay)

    if totalBeats - self.startingBeat >= 4:
      # we're done with our animation, so return True
      return True
    
    # we're not done with our animation so return False
    return False


  def animateStanding(self, gameDisplay):
    # the standing animation will have the Dude tap their hand

    beat = TEMPO.getBeat()
    totalBeats = TEMPO.getTotalBeats()

    if beat - int(beat) < .2:
      self.drawTap(gameDisplay)
    else:
      self.drawStanding(gameDisplay)

    if totalBeats - self.startingBeat >= 4:
      # we're done with our animation, so return True
      return True

    return False

  def draw(self,gameDisplay):
    # pose = DudePose(headRadius=4)
    # pose.draw(gameDisplay, self.position, self.size)

    pose = DudePose()

    poseM = DudePose(lowerArmLeft=[[12,6],[12,8]],
                      upperArmLeft=[[8,6],[12,6]],
                      lowerArmRight=[[4,6],[4,8]],
                      upperArmRight=[[8,6],[4,6]])


    poseBigHead = DudePose(headRadius=3)
    
    poseRunning1 = DudePose(upperLegLeft=[[8,12], [8,14]],
                            lowerLegLeft=[[8,14], [8,16]],
                            upperLegRight=[[8,12],[10,14]],
                            lowerLegRight=[[10,14],[9,16]])


    # pose.draw(gameDisplay, self.position, self.size)

    # poseHalfWay = DudePose.lerp(pose, poseM, .25)

    # poseHalfWay.draw(gameDisplay, self.position, self.size)

    beat = TEMPO.getBeat()


    if beat - int(beat) < .5:
        headBeat = DudePose.lerp(pose, poseBigHead, (beat-int(beat))*2, pose, ["headRadius"])
    else:
        headBeat = DudePose.lerp(poseBigHead, pose, (beat-int(beat)-.5)*2, pose, ["headRadius"])

    if beat - int(beat) < 1:
        lerp = DudePose.lerp(pose, poseRunning1, (beat-int(beat)), headBeat, ["upperLegLeft", "lowerLegLeft", "upperLegRight", "lowerLegRight"])

    if beat < 1:
      lerp.draw(gameDisplay, self.position, self.size)
    elif beat < 1.5:
      lerpPose = DudePose.lerp(pose, poseM, (beat-1)*2, lerp, ["lowerArmLeft", "upperArmLeft", "lowerArmRight", "upperArmRight"])
      lerpPose.draw(gameDisplay, self.position, self.size)
    else:
      lerpPose = DudePose.lerp(pose, poseM, 1, lerp, ["lowerArmLeft", "upperArmLeft", "lowerArmRight", "upperArmRight"])
      lerpPose.draw(gameDisplay, self.position, self.size)


    # if self.animationFinished:
    #   animations = [self.animateStanding, self.animateYMCA, self.animateYMCA, self.animateYMCA]
    #   self.startingBeat = TEMPO.getTotalBeats()

    #   # alternate between the standing animation and the YMCA
    #   # animation

    #   self.animation = animations[self.frameCount % len(animations)]
    #   self.frameCount = self.frameCount + 1

    # if self.animation:
    #   self.animationFinished = self.animation(gameDisplay)

    


class Family:
  def __init__(self, position, size):
    self.position = position
    self.size = size

    self.members = []

    x = position[0]
    # 80% chance that we have a mom
    if random.randrange(100) < 80:
      mom = Dude((x, position[1]), 5 * size)
      self.members.append(mom)
      x = x + mom.getExtentsRect().width
    # 80% chance that we have a dad
    if random.randrange(100) < 80:
      dad = Dude((x, position[1]), 4 * size)
      self.members.append(dad)
      x = x + dad.getExtentsRect().width

    for i in range(random.randrange(4)):
      kid = Dude((x, position[1]), (random.randrange(3) + 1) * size)
      self.members.append(kid)
      x = x + kid.getExtentsRect().width

  def getExtentsRect(self):
    width = 0
    height = 0
    for i in self.members:
      memberRect = i.getExtentsRect()
      width = width + memberRect.width
      if memberRect.height > height:
        height = memberRect.height
    
    return pygame.Rect([0, 0, width, height])

  def draw(self, gameDisplay):
    for i in self.members:
      i.draw(gameDisplay)  



def setup():
  gameDisplay.fill(WHITE)
  pygame.display.update()

  global families

  rows = 5
  for y in range(rows):
    columns = 7 * (y+1)
    # columns = 10
    if y % 2 == 1:
      xPos = 25
    else:
      xPos = 0
    for x in range(columns):
      family = Family((xPos,DISPLAY_HEIGHT - 200 * (y/rows)), 1 - y/rows)
      xPos = xPos + family.getExtentsRect().width
      families.append(family)


  # family = Family((100,100), 1)
  # families.append(family)


def graphicsLoop(): 
    gameExit = False
 
    while not gameExit:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print("Goodbye.")
                quit()
 
 
        # erase the screen on each loop by filling the screen white
        gameDisplay.fill(WHITE)

        TEMPO.drawTempo(gameDisplay, (10,10))
        for i in families:
          i.draw(gameDisplay)


        # startingColor = (255,127,0)
        # endingColor = (0,127,255)

        # for i in range(100):
        #   pygame.draw.line(gameDisplay, lerp(startingColor, endingColor, i/100),[100 + i,0], [100+i, 100])

        pygame.display.update()
    
        
        # limit the refresh rate to 60 fps
        clock.tick(60)


print(lerp((0,0,0), (255,255,255), 2))

setup()
graphicsLoop()