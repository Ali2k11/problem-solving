#Q1
def getTotal(dictionary):
    total = 0
    for val in dictionary.values():
        total +=val
    return total

#Q2
def normalise(dictionary):
    numTotal=getTotal(dictionary)
    for key in dictionary:
        dictionary[key]= dictionary.get(key)*100//numTotal
    return dictionary
   
   
#Q3
def printNonZero(dictionary):
    for key, value in dictionary.items():
        if value >= 1:
            print(key, ' : ', value)



def analyse(votes,seats):
    voteNorm=normalise(votes)
    seatNorm=normalise(seats)
   

    for key in voteNorm:
       
        if voteNorm[key] != 0:
            print(key, ':', voteNorm[key], "% of Votes vs ",seatNorm[key],"% of seats")





#Q4-test
def analyse111(votes,seats):
    vnorm = normalise(votes)
    for key, value in votes.items():
        if value != 0:
            value *=100
            value = round(value)
   
           
    snorm = normalise(seats)
    if value != 0:
        for key, value in seats.items():
            value *=100
            value = round(value)
           

    for key in vnorm:
        print (key, ':', vnorm[key], "% of votes vs ",snorm[key],"% of seats")



#Q5
def addTo(myd1,myd2):
    for key in myd2:
        if key not in myd1:
            myd1[key]=myd2[key]
        elif key in myd1:
            myd1 [key]+=myd2[key]
    return (myd1)


#PART B

#Q6
def getConstituencies(file):
    myset=set()
    myfile=open(file)
    linelist=myfile.readlines()
    for line in linelist:
        pair=line.split(':')
        if len(pair)>=2 and pair[0]=="_Constituency":
            first=pair[0]
            second=pair[1]
            secondStrip=second.strip()
            myset.add(secondStrip)
    print(myset)

#Q7
def getParties (file) :
    myset1 = set()
    myfile = open(file)
    linelist = myfile.readlines()
    for line in linelist:
        pair=line.split(':')
        if len(pair)>=2 and pair[0]!='_Constituency"' and pair[0]!='_Seats':
            first=pair[0]
            firstStrip=first.strip()
            myset1.add(firstStrip)
    return myset1

print(getParties('ukeu2019.txt'))

    
