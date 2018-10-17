import re

class LCSObject:

    def __init__(self, seq, lineId) : # seq is a list of string
        self.LCSseq = seq
        self.lineIds = [lineId]

    def getLCS(self, seq): # seq is a list of string
        count = 0
        lastMatch = -1

        # Loop through current sequence using the simple loop approach described in the paper
        for w in self.LCSseq:
            if w == "*":
                continue

            for j in range( lastMatch + 1, len(seq) ):
                if  w == seq[j]:
                    lastMatch = j
                    count += 1
                    break
        return count

    # Insert a line into the LCSObject
    def insert(self, seq, lineId):
        self.lineIds.append(lineId)
        tmp = ""
        # Create the new sequence by looping through it
        lastMatch = -1
        placeholder = False  # Decides whether or not to add a * depending if there is already one preceding or not
        for w in self.LCSseq:
            if w == "*":
                if not placeholder:
                    tmp = tmp + "* "
                placeholder = True
                continue
            
            for j in range( lastMatch + 1, len(seq) ):
                if w == seq[j]:
                    placeholder = False
                    tmp = tmp + w + " "
                    lastMatch = j 
                    break
                elif not placeholder:
                    tmp = tmp + "* "
                    placeholder = True

        self.LCSseq = re.compile("[\\s]+").split(tmp.strip()) #remove ends whitespace and split words.

    # Lenght for pruning
    def length(self):
        return len( self.LCSseq )
    
    # Count of lineIds in this LCSObject
    def count(self):
        return len( self.lineIds)

    # to string method for testing
    def toString(self):
        tmp = ""

        for s in self.LCSseq:
            tmp = tmp + s + " "

        tmp = tmp + "\n\t\t{"
        
        for id in self.lineIds:
            tmp = tmp + str(id) + ", "

        return tmp[0:-2] + "}"