"""
Joshua David C. Sta. Rita
2010-42658
CMSC128 AB-4L
Assign 002: Programming a Simple Bioinformatics Library
"""
def getHammingDistance(str1, str2):
        """
        This function gets the number of characters that differ in ith position from position 1 to strlen(str1).
        Strings must be of the same length; never 0 or negative.
        """
        
        """
        Check for errors in input
        if the length of either strings is 0 or negative, or the two strings do not have the same length, return error if not(false)
        """
        if len(str1) == 0 or len(str2) == 0:
                return "Error! String length == 0!"
        if len(str1) < 0 or len(str2) < 0:
                return "Error! String length is negative!"        
        if len(str1) != len(str2):
                return "Error! Strings are not equal!"        
        #initialize hammingDistance variable; variable that the function will return
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
        Given the original string and a pattern, this function will count the number of occurrence of the pattern in the original/given string.
        """
        
        #initialization; count is the variable that the function will return(count of the pattern's occurence in the given string)
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
        Given an alphabet(string) where all letters are assumed to be unique, this
        function returns true if the variable string is a valid string based on the letters of alphabet.
        """
        
        #initialize boolean value; variable that the function will return; is the string valid, given the input alphabet?
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
        Given a genome string of some length q (where q>0), it returns the number of Gs minus the number of Cs in the first n nucleotides (q>=n). The value can be zero, negative or positive. The first position is one (1) not zero(0) as we typically associate with string implementations

        *IMPORTANT*
        The genome input(string) in this function is assumed to be correct(valid) since there is no function to check its validity; this function, however, is included in the implementation of getMaxSkewN() and getMinSkewN()
        """
        
        #initialize skew variable; variable that the function will return; simply, G minus(-) C
        skew = 0;
        #get the length of the given string
        q = len(string)
        
        #check for errors
        if not(q > 0) :
                return "Error! Genome(string) must be of length greater than 0!"
        if not(q >= n) :
                return "Error! Out of bounds; \"first n nucleotides\" input is greater than the genome length!"
        if n < 1:
                return "Error! Out of bounds; \"first n nucleotides\" input must be greater than or equal to 1!"
        
        #Get # of G's and C's until the n-1th(technically and syntactically nth due to Python's implementation of the .count() function) position then computer for G minus(-) C
        G = string.count("G",0,n)
        C = string.count("C",0,n)
        skew = G-C

        return skew

def getMaxSkewN(string, n):
        """
        Given a genome string of some length q (where q>0), it returns the maximum value of the number of Gs minus the number of Cs in the first n nucleotides (q>=n). The value can be zero, negative or positive. The first position is one (1) not zero(0) as we typically associate with string implementations.
        """
        #initialize G, C and maxSkew and the index "i"
        G = 0
        C = 0
        maxSkew = 0
        i = 0
        
        #get the length of the given string
        q = len(string)
        
        #check for errors
        if not(q > 0) :
                return "Error! Genome(string) must be of length greater than 0!"
        if not(q >= n) :
                return "Error! Out of bounds; \"first n nucleotides\" input is greater than the genome length!"
        if n < 1:
                return "Error! Out of bounds; \"first n nucleotides\" input must be greater than or equal to 1!"
        
        #loop through each and every character of the given string until the given position(n)
        #for character in string:
        while i < n:
                character = string[i]
                #increment G or C, depending on which between the two characters is found
                if character == "G":
                        G += 1
                elif character == "C":
                        C += 1
                #catch case for an invalid character, thus invalid genome
                elif not(character == "A" or character == "T"):
                        return "Invalid Genome sequence!"
                #compute the current skew value
                skew = G-C;
                #if the current skew value is greater than the maxSkew value, replace the value if maxSkew with the value of skew
                if skew > maxSkew:
                        maxSkew = skew
                i += 1
                
        return maxSkew

def getMinSkewN(string, n):
        """
        Given a genome string of some length q (where q>0), it returns the minimum value of the number of Gs minus the number of Cs in the first n nucleotides (q>=n). The value can be zero, negative or positive. The first position is one (1) not zero(0) as we typically associate with string implementations.
        """
        #initialize G, C, minSkew, skew and the index "i"
        G = 0
        C = 0
        minSkew = 0
        skew = 0
        i = 0
        
        #get the length of the given string
        q = len(string)
        
        #check for errors
        if not(q > 0) :
                return "Error! Genome(string) must be of length greater than 0!"
        if not(q >= n) :
                return "Error! Out of bounds; \"first n nucleotides\" input is greater than the genome length!"
        if n < 1:
                return "Error! Out of bounds; \"first n nucleotides\" input must be greater than or equal to 1!"
        
        #first iteration to set the initial value of minSkew
        #NOTE: This "preliminary" logic is unique and is not necessary in the case of getMaxSkewN()
        character = string[i]
        #increment G or C, depending on which between the two characters is found
        if character == "G":
                G += 1
        elif character == "C":
                C += 1
        #catch case for an invalid character, thus invalid genome
        elif not(character == "A" or character == "T"):
                return "Invalid Genome sequence!"
        #compute the current skew value
        skew = G-C;   
        #set minSkew value
        minSkew = skew
        #increment index
        i += 1
        
        #loop through each and every character after the first position of the given string until the given position(n); for all other iterations:
        while i < n:
                character = string[i]
                #increment G or C, depending on which between the two characters is found
                if character == "G":
                        G += 1
                elif character == "C":
                        C += 1
                #catch case for an invalid character, thus invalid genome
                elif not(character == "A" or character == "T"):
                        return "Invalid Genome sequence!"
                #compute the current skew value
                skew = G-C;

                #if the current skew value is less than the minSkew value, replace the value of minSkew with the value of skew
                if skew < minSkew:
                        minSkew = skew
                #increment index
                i += 1
                
        return minSkew
