import pygame
from lerp import lerp,lerpList

class DudePose:

  def __init__(self, 
              headPos = [8,2],
              headRadius = 2,
              body = [[8,4],[8,12]],
              upperArmLeft = [[8,6],[11,4]],
              lowerArmLeft = [[11,4],[14,2]],
              upperArmRight = [[8,6], [5,4]],
              lowerArmRight = [[5,4], [2,2]],
              upperLegLeft = [[8,12], [10,14]],
              lowerLegLeft = [[10,14], [12,16]],
              upperLegRight = [[8,12], [6,14]],
              lowerLegRight = [[6,14], [4,16]]):

    self.headPos = headPos
    self.headRadius = headRadius
    self.body = body
    self.upperArmLeft = upperArmLeft
    self.lowerArmLeft = lowerArmLeft
    self.upperArmRight = upperArmRight
    self.lowerArmRight = lowerArmRight
    self.upperLegLeft = upperLegLeft
    self.lowerLegLeft = lowerLegLeft
    self.upperLegRight = upperLegRight
    self.lowerLegRight = lowerLegRight


  def drawLine(self, gameDisplay, position, scale, startingPoint, endingPoint, color = (0,0,0)):
    posAdjusted = (position[0], position[1] - (16*scale))

    pygame.draw.line(gameDisplay, color, (posAdjusted[0]+(startingPoint[0] * scale),posAdjusted[1]+(startingPoint[1] * scale)), (posAdjusted[0]+(endingPoint[0] * scale),posAdjusted[1]+(endingPoint[1] * scale)))


  def drawCircle(self, gameDisplay, position, scale, centerPoint, radius, color = (0,0,0), lineWidth=1):
  
    posAdjusted = (position[0], position[1] - (16*scale))

    pygame.draw.circle(gameDisplay, color, [posAdjusted[0] + (centerPoint[0]*scale),posAdjusted[1] + (centerPoint[1]*scale)], radius*scale, lineWidth)


  def draw(self, gameDisplay, position, scale):
    self.drawCircle(gameDisplay, position, scale, self.headPos, self.headRadius)
    self.drawLine(gameDisplay, position, scale, self.body[0], self.body[1])
    self.drawLine(gameDisplay, position, scale, self.upperArmLeft[0], self.upperArmLeft[1])
    self.drawLine(gameDisplay, position, scale, self.lowerArmLeft[0], self.lowerArmLeft[1])
    self.drawLine(gameDisplay, position, scale, self.upperArmRight[0], self.upperArmRight[1])
    self.drawLine(gameDisplay, position, scale, self.lowerArmRight[0], self.lowerArmRight[1])
    self.drawLine(gameDisplay, position, scale, self.upperLegLeft[0], self.upperLegLeft[1])
    self.drawLine(gameDisplay, position, scale, self.lowerLegLeft[0], self.lowerLegLeft[1])
    self.drawLine(gameDisplay, position, scale, self.upperLegRight[0], self.upperLegRight[1])
    self.drawLine(gameDisplay, position, scale, self.lowerLegRight[0], self.lowerLegRight[1])


  @classmethod
  def lerp(cls, startingPose, endingPose, fraction):
    newHeadPos = lerp(startingPose.headPos, endingPose.headPos, fraction)
    newHeadRadius = lerp([startingPose.headRadius], [endingPose.headRadius], fraction)
    newUpperArmLeft = lerpList(startingPose.upperArmLeft, endingPose.upperArmLeft, fraction)
    newLowerArmLeft = lerpList(startingPose.lowerArmLeft, endingPose.lowerArmLeft, fraction)
    newUpperArmRight = lerpList(startingPose.upperArmRight, endingPose.upperArmRight, fraction)
    newLowerArmRight = lerpList(startingPose.lowerArmRight, endingPose.lowerArmRight, fraction)
    newUpperLegLeft = lerpList(startingPose.upperLegLeft, endingPose.upperLegLeft, fraction)
    newLowerLegLeft = lerpList(startingPose.lowerLegLeft, endingPose.lowerLegLeft, fraction)
    newUpperLegRight = lerpList(startingPose.upperLegRight, endingPose.upperLegRight, fraction)
    newLowerLegRight = lerpList(startingPose.lowerLegRight, endingPose.lowerLegRight, fraction)


    return DudePose(headPos = newHeadPos,
                    headRadius = newHeadRadius[0],
                    upperArmLeft = newUpperArmLeft,
                    lowerArmLeft = newLowerArmLeft,
                    upperArmRight = newUpperArmRight,
                    lowerArmRight = newLowerArmRight,
                    upperLegLeft = newUpperLegLeft,
                    lowerLegLeft = newLowerLegLeft,
                    upperLegRight = newUpperLegRight,
                    lowerLegRight = newLowerLegRight                    
                    )