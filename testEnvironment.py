"""
-----------------------
Main Program/Development Testing Environment
-----------------------
"""

#The following are test cases derived from the .pdf file of the assignment specifications

OhOne = getHammingDistance("AACCTT","GGCCTT")
print("Hamming Distance = "+str(OhOne)+"") #returns 2
OhOne = getHammingDistance("TCGGA","AAAAG")
print("Hamming Distance = "+str(OhOne)+"") #returns 5
OhOne = getHammingDistance("A","AG")
print("Hamming Distance = "+str(OhOne)+"\n\n") #returns "Error! Strings are not equal!"

Ohtwo = countSubstrPattern("AATATATAGG","GG")
print(Ohtwo) #returns 1
Ohtwo = countSubstrPattern("AATATATAGG","ATA")
print(Ohtwo) #returns 3
Ohtwo = countSubstrPattern("AATATATAGG","ACTGACTGACTG")
print(Ohtwo,"\n") #returns 0

print(isValidString("AAGGCTATGC","ACGT")) #returns true
print(isValidString("AAGGCTATGa","ACGT")) #returns false
print(isValidString("ACGT","ACGT")) #returns true
print(isValidString("ACGT101_","ACGT")) #returns false
print(isValidString("091212345","0123456789"),"\n") #returns true

print(getSkew("GGCCAC", 1)) #returns 1
print(getSkew("GGCCAC", 2)) #returns 2
print(getSkew("GGCCAC", 3)) #returns 1
print(getSkew("GGCCAC", 4)) #returns 0
print(getSkew("GGCCAC", 5),"\n") #returns 0

print(getMaxSkewN("GGCCAC", 1)) #returns 1
print(getMaxSkewN("GGCCAC", 2)) #returns 2
print(getMaxSkewN("GGCCAC", 3)) #returns 2
print(getMaxSkewN("GGCCAC", 4)) #returns 2
print(getMaxSkewN("GGCCAC", 5)) #returns 2
print(getMaxSkewN("G1GCCAC", 5)) #returns "Invalid Genome sequence!"

print(getMinSkewN("GGCCAC", 1)) #returns 1
print(getMinSkewN("GGCCAC", 2)) #returns 1
print(getMinSkewN("GGCCAC", 3)) #returns 1
print(getMinSkewN("GGCCAC", 4)) #returns 0
print(getMinSkewN("GGCCAC", 5)) #returns 0
print(getMinSkewN("GGCCAC", 6)) #returns -1
print(getMinSkewN("GGCCAC", 0)) #returns "Error! Out of bounds; "first n nucleotides" input must be greater than or equal to 1!"
