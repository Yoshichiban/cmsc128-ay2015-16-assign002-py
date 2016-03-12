def getHammingDistance(str1, str2):
        """
        This function gets the number of characters that differ in ith position from position 1 to strlen(str1)
        Strings must be of the same length; never 0 or negative
        """
        
        """
        Check for errors in input
        if the length of either strings is 0 or negative, or the two strings do not have the same length, return error if not(false)
        """
        if len(str1) == 0 or len(str2) == 0:
                return "Error! String length = 0!"
        if len(str1) < 0 or len(str2) < 0:
                return "Error! String length is negative!"        
        if len(str1) != len(str2):
                return "Error! Strings are not equal!"        
        #initialize hammingDistance variable
        hammingDistance = 0
        
        #for-loop to iterate and then compare the characters for each and every position
        for char1,char2 in zip(str1,str2):
                #if the characters at the current position are different, increment the hammingDistance
                if char1!=char2:
                        #print(char1+char2+" : 0=Different")
                        hammingDistance  += 1
                """DEBUGGING:
                else:
                        print(char1+char2+" : 1=Same")
                print(hammingDistance)
                """
        #DEBUGGING: print(hammingDistance)
        return hammingDistance

def countSubstrPattern(original, pattern):
        count = 0
        i = 0
        length = len(pattern)
        while i < len(original):
                i = original.find(pattern,i)
                #catch the case where .find() returns -1 if no match is found; break the        loop
                if i == -1:
                        break
                #DEBUGGING: print(pattern+" found at",i)
                
                #an occurence of the pattern is found, increment count;
                #also increment index for the next search
                count += 1
                i += 1
        return count

"""
-----------------------
Main Program/Development Testing Environment
-----------------------
"""

OhOne = getHammingDistance("AACCTT","GGCCTT")
print("Hamming Distance = "+str(OhOne)+"\n")
OhOne = getHammingDistance("TCGGA","AAAAG")
print("Hamming Distance = "+str(OhOne)+"\n")
OhOne = getHammingDistance("A","AG")
print("Hamming Distance = "+str(OhOne)+"\n\n")

Ohtwo = countSubstrPattern("AATATATAGG","GG")
print(Ohtwo,"\n")
Ohtwo = countSubstrPattern("AATATATAGG","ATA")
print(Ohtwo,"\n")
Ohtwo = countSubstrPattern("AATATATAGG","ACTGACTGACTG")
print(Ohtwo,"\n")