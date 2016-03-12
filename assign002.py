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
        """
        Given a string original and pattern, we will count the number of occurrence
        of pattern in original.
        """
        
        #initialization
        count = 0
        i = 0
        length = len(pattern)
        
        #loop through the whole length of the given/original string
        while i < len(original):
                #find an occurence of the pattern in the given/original string
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

def isValidString(string, alphabet):
        """
        Given an alphabet string where all letters are assumed to be unique, this
        function returns true if the string str is a valid string based on the letters of alphabet.
        """
        
        #initialize boolean value
        boolean = True
        
        #loop through each character in the given string
        for character in string:
                #compare current character to the alphabet; if the current character is NOT IN the given alphabet, set the variable boolean to False
                if character not in alphabet:
                        boolean = False
                        return boolean
        return boolean
        
def getSkew(string, n):
        """
        Given a genome str of some length q (where q>0), it returns the number of Gs minus the number of Cs in the first n nucleotides (q>=n). The value can be zero, negative or positive. The first position is one (1) not zero(0) as we typically associate with string implementations
        """
        
        #initialize skew variable
        skew = 0;
        #get the length of the given string
        q = len(string)
        
        #check for errors
        if not(q > 0) :
                return "Error! Genome(string) must be of length greater than 0!"
        if not(q >= n) :
                return "Error! Out of bounds; first n nucleotides count input is greater than the genome length!"
        
        #Get # of G's and C's until the n-1th(technically and syntactically nth due to Python's implementation of the .count() function) position then computer for G minus(-) C
        G = string.count("G",0,n)
        C = string.count("C",0,n)
        skew = G-C

        return skew

"""
-----------------------
Main Program/Development Testing Environment
-----------------------
"""

#The following are test cases derived from the .pdf file of the assignment specifications

OhOne = getHammingDistance("AACCTT","GGCCTT")
print("Hamming Distance = "+str(OhOne)+"")
OhOne = getHammingDistance("TCGGA","AAAAG")
print("Hamming Distance = "+str(OhOne)+"")
OhOne = getHammingDistance("A","AG")
print("Hamming Distance = "+str(OhOne)+"\n\n")

Ohtwo = countSubstrPattern("AATATATAGG","GG")
print(Ohtwo)
Ohtwo = countSubstrPattern("AATATATAGG","ATA")
print(Ohtwo)
Ohtwo = countSubstrPattern("AATATATAGG","ACTGACTGACTG")
print(Ohtwo)

print(isValidString("AAGGCTATGC","ACGT")) #returns true
print(isValidString("AAGGCTATGa","ACGT")) #returns false
print(isValidString("ACGT","ACGT")) #returns true
print(isValidString("ACGT101_","ACGT")) #returns false
print(isValidString("091212345","0123456789")) #returns true

print(getSkew("GGCCAC", 1)) #returns 1
#print(getSkew("GGCCAC", 2)) #returns 2
#print(getSkew("GGCCAC", 3)) #returns 1
#print(getSkew("GGCCAC", 4)) #returns 0
#print(getSkew("GGCCAC", 5)) #returns 0