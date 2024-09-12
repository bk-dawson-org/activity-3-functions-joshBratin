import math
def getCylinderVolume (radius, height):
    volume = math.pi * (radius **2) * height
    return volume

def getNumberOfSlices(radius, height, volumeOfSlices):
    volume = getCylinderVolume(radius, height)
    numberOfSlices = volume / volumeOfSlices
    return int(numberOfSlices)

print(getNumberOfSlices(13,7,20))