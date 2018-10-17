import re
from lcsObject import LCSObject

class LCSMap:

    def __init__(self) : # seq is a list of string
        self.LCSObjects = []
        self.lineId = 0

    #Insert a log entry in the LCSMap
    def insert(self, entry):
        seq = re.compile("[\\s]+").split(entry.strip())
        obj = self.getMatch(seq)

        # if no existing match create a new LCSObject, othwewise add the line id to an existing one
        if obj is None:
            obj = LCSObject(seq, self.lineId)
            self.LCSObjects.append(obj)
        else:
            obj.insert(seq, self.lineId)

        self.lineId += 1

    #Find LCSObject that is the closest match
    def getMatch(self, seq):
        bestMatch = None
        bestMatchLen = 0

        #Find LCS of all existing LCSObjects and determine if they're a match as described in the paper
        for obj in self.LCSObjects:
            #pruning
            if obj.length() < len(seq)/2 or  obj.length() > len(seq)*2:
                continue
            
            #get LCS and check i it's a match
            l = obj.getLCS(seq)
            if l >= len(seq)/2 and l > bestMatchLen:
                bestMatchLen = l
                bestMatch = obj
            
        return bestMatch
    
    # Returns LCSObject at a given index
    def objectAt(self, index):
        return self.LCSObjects[index]
    
    # return the number of LCSObjects
    def size(self):
        return len(self.LCSObjects)

    def toString(self) :
        tmp = "\t" + str(self.size()) + " Objects in the LCSMap\n\n"
        entryCount = 0
        for i in range( self.size() ) :
            tmp = tmp + "\tObject " + str(i) + ":\n\t\t" + self.objectAt(i).toString() + "\n"
            entryCount += self.objectAt(i).count()
		
        tmp = tmp + "\n\t" + str(entryCount) + " total entries found, " + str(self.lineId) + " expected."
        return tmp