import os

# add the title and url to the main file
def addOutputFile(folderCount, folderNames):    
    outputFile = open("../myExtension/popup/folders.txt", "w")
    
    toWrite = str(folderCount) + '\n'
    outputFile.writelines(toWrite)
    
    for name in folderNames:
        toWrite = name + '\n'
        #print(toWrite)
        outputFile.writelines(toWrite)
    
    outputFile.close()

    
    
    
print("\t\tStarting...")

print("\tFinding folders...")

path = "D:/Dev/Python/poli/Poller/ppl"

folderCount = 0
folderNames = []

for _, dirnames, _ in os.walk(path):
    folderCount += len(dirnames)
    if dirnames:
        folderNames = dirnames
    #print(dirnames)
#print(folderNames)
#print("{:,} files, {:,} folders".format(files, folders))
    
addOutputFile(folderCount, folderNames)
    
print("\n\n\t\tDone!")