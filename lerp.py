def add(point1, point2):
  dimensions = len(point1)

  result = []
  for i in range(dimensions):
    result.append(point1[i] + point2[i])
  
  return result

def subtract(point1, point2):
  dimensions = len(point1)

  result = []
  for i in range(dimensions):
    result.append(point1[i] - point2[i])
  
  return result

def scale(point1, scale):
  dimensions = len(point1)

  result = []
  for i in range(dimensions):
    result.append(scale * point1[i])
  
  return result


def lerp(start, end, fraction):
  # assumes that the start and end points
  # have the same dimensionality

  delta = subtract(end, start)
  scaledDelta = scale(delta, fraction)
  
  return add(start, scaledDelta)


def lerpList(start, end, fraction):
  length = len(start)
  result = []
  for i in range(length):
    result.append(lerp(start[i], end[i], fraction))
  
  return result
