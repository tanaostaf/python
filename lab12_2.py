#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

class Star:
  def get_x(self):
    return self._x
  
  def get_y(self):
    return self._y

  def set_x(self, x : float):
    self._x = x

  def set_y(self, y : float):
    self._y = y

  def get_name(self):
    return self._name

  def set_name(self, new_name):
    self._name = new_name

  x = property(get_x, set_x)
  y = property(get_y, set_y)

  name = property(get_name, set_name)

  def rotate(self, degree: float):
    self._ = self._x * math.cos(degree) - self._y * math.sin(degree)
    self._y = self._x * math.sin(degree) + self._y * math.cos(degree)

  def __init__(self, name : str, x : float = 0.0, y : float = 0.0):
    self._x = x
    self._y = y
    self._name = name

  def __cmp__(self, other):
    if self._y < other._y:
      return -1
    elif self._y == other._x:
      if self._x < other._x:
        return -1
      elif self._x > other.x:
        return 1
      else:
        return 0
    else:
      return 1

  def __lt__(self, other):
    return self.__cmp__(other) == 1

def Len(A : Star, B : Star):
  return math.sqrt((A.x + B.x)*(A.x + B.x) + (A.y + B.y)*(A.y + B.y))

class Sky:
  def get_stars(self):
    return self._stars
  
  def set_stars(self, stars):
    self._stars = stars

  stars = property(get_stars, set_stars)

  def rotate(self, degree : float):
    for star in self._stars:
      star.rotate(degree)
    self._stars.sort()

  def __init__(self):
    self._stars = []

degree = 0.0;
count = 0
sky = Sky()

with open('input.txt', 'r') as infile:
  line = infile.readline()
  t = line.split();
  degree = float(t[0])
  count = int(t[1])
  for i in range(1,count):
    line = infile.readline().split()
    if not line:
      break
    print(line)
    sky.stars.append(Star(line[0], float(line[1]), float(line[2])))

sky.rotate(degree)

out = open('output.txt', "w")

for star in sky.stars:
  out.write(star.name + ' ')

out.close()
input ('Press ENTER to exit')

