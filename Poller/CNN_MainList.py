import os

# is the given line in the main file
def checkMainFile(line):
    try:
        mainFile = open("MainList.txt", "r")

        mainFile.seek(0, os.SEEK_SET)

        mainLine = mainFile.readline()
        while mainLine:
            #print(mainLine)
            if line == mainLine:
                #print("TRUE")
                mainFile.close()
                return True
            mainLine = mainFile.readline()

        mainFile.close()
    except:
        pass
    
    return False

# add the title and url to the main file
def addMainFile(titleLine, urlLine):
    mainFile = open("MainList.txt", "a")
    mainFile.seek(0, os.SEEK_END)
    
    #print(titleLine)
    #print(urlLine)
    
    toWrite = [titleLine, urlLine]
    
    mainFile.writelines(toWrite)
    #mainFile.write(urlLine)
    mainFile.close()

    
    

    
    
    
    
print("\t\tStarting...")
    
inputFile = open("../Scrapy/PoliticalPoller/PoliticalPoller/spiders/cnn.csv", "r")

#print(inputFile.read())
inputFile.seek(0, os.SEEK_SET)
#print("\n")

line = inputFile.readline()

while line:

    if line[:5] == "https":
        line = inputFile.readline()
    print(line)

    # is the title in the main file
    if not checkMainFile(line):
        titleLine = line
        urlLine = inputFile.readline()
        addMainFile(titleLine, urlLine)
        
    line = inputFile.readline()

inputFile.close()

print("\t\tDone!")