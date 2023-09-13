# Track Object

class Track(): 
    """
    Generic Greyhound Racing Track 



    """
    #Attributes
    def __init__(self, distance:float, lanes:int):
        self.distance = distance    #distance from start line to finish line [float]
        self.lanes = lanes          #number of lanes on the track [int]
        self.elevation = 0.0        #elevation of track (might affect other things?)[float]
        self.shp = 0.1              #probability of something bad happening to one or more racers between 0-1 [float]
        

