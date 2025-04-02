from graphics import *

class Button:


 def __init__(self, win, center, width, height, label):


  radius = width/2.0 * height/2.0
  x, y = center.getX(), center.getY()
  self.center = Point(x, y)
  self.xmax, self.xmin = x + radius, x - radius
  self.ymax, self.ymin = y + radius, y - radius
  p1 = Point(x, y)

  self.rect = Circle(p1, radius)
  self.rect.setFill('lightgray')
  self.rect.draw(win)
  self.label = Text(center, label)
  self.label.draw(win)
  self.deactivate()

 def clicked(self, p):
  return (self.active and self.xmin <= p.getX() <= self.xmax and self.ymin <= p.getY() <= self.ymax)

 def getLabel(self):

  return self.label.getText()

 def activate(self):

  self.label.setFill('black')
  self.rect.setWidth(2)
  self.active = True

 def deactivate(self):
  self.label.setFill('darkgrey')
  self.rect.setWidth(1)
  self.active = False


  def update(self, win, label):
   self.label.undraw()
   center = self.center
   self.label = Text(center, label)
   self.active = False
   self.label.draw(win)