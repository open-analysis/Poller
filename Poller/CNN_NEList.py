import os
import nltk
from nltk.tag.stanford import StanfordNERTagger as NERTagger

def findName(line):
    st = NERTagger('../poli_stanford_ner/stanford_ner/english.all.3class.distsim.crf.ser.gz', '../poli_stanford_ner/stanford_ner/stanford-ner-4.2.0.jar')
    
    pos = 0
    savedPos = -1
    multi_name = {}
    ret_names = []
    
    # classifying if there are names in the sentence
    for sent in nltk.sent_tokenize(line):
        tokens = nltk.tokenize.word_tokenize(sent)
        tags = st.tag(tokens)
        for tag in tags:
            if tag[1]=='PERSON': 
                print(tag)
                multi_name[pos] = tag
            pos += 1
    # where it starts to see if there's first, middle, and last names
    keys = isConsecutive(multi_name)
    if keys:
        #print("Multi name!")
        for keySet in keys:
            tmp = None
            for key in keySet:
                if tmp is None:
                    tmp = multi_name[key][0]
                else:
                    tmp += "_" + multi_name[key][0]
            #print("\t\t", tmp)
            ret_names.append(tmp)
    else:
        tmp = None
        for posInLine in multi_name:
            # if this is the first time through
            if savedPos == -1:
                savedPos = posInLine
            if savedPos+1 != posInLine:
                tmp = multi_name[savedPos][0]
                ret_names.append(tmp)
            savedPos = posInLine
    print(ret_names)
    return ret_names
    

'''
Checks if the given dictionary's keys are in (at least partial) sequential order
Must use numeric keys for this 
'''
def isConsecutive(d):
    if len(d) <= 1:
        return
    
    ret_keys = []
    curr_keys = []
    
    keys = list(d.keys())
    #print(keys, len(keys))
    for i in range(len(keys)):
        try:
            # if the keys are sequential add them to the list
            if keys[i+1] - keys[i] == 1:
                #print("Coolio")
                curr_keys.append(keys[i])
                curr_keys.append(keys[i+1])
            else:
                # if they're not, check if there's anything in the current list
                if curr_keys:
                    #print("\t\tBALLIN")
                    # if there is, remove any duplicates, sort it, 
                    # add to return keys, and clear the current list
                    tmp = list(set(curr_keys))
                    tmp.sort()
                    ret_keys.append(tmp)
                    curr_keys.clear()
        except:
            if i == len(keys):
                if curr_keys:
                    #print("\t\t\tBALLING pt2")
                    # if there is, remove any duplicates, sort it, 
                    # add to return keys, and clear the current list
                    tmp = list(set(curr_keys))
                    tmp.sort()
                    ret_keys.append(tmp)
                    curr_keys.clear()
            else:
                print("\t\t\t\t\tOUT OF BOUNDS")
                
            if i == len(keys)-1:
                #print("\tAt boundary")
                tmp = list(set(curr_keys))
                tmp.sort()
                #print(tmp)
                ret_keys.append(tmp)
    
    try:
        if ret_keys[0]:
            print(ret_keys)
            return(ret_keys)
        else:
            #print('\t', keys)
            for key in keys:
                tmpList = []
                #print('\t\t', key)
                tmpList.append(key)
                ret_keys.append(tmpList)
            if not ret_keys[0]:
                del ret_keys[0]
            print(ret_keys)
            return ret_keys
    except:
        pass

    

# add the title and url to the main file
def addOutputFile(titleLine, urlLine, names):    
    # creating the output file paths and names
    for name in names:
        if name:
            filePath = "ppl/" + name
            fileName = filePath + "/CNN_List.txt"
            try:
                os.mkdir(filePath)
                outputFile = open(fileName, "x")
            except:
                outputFile = open(fileName, "a")

            outputFile.seek(0, os.SEEK_END)

            toWrite = [titleLine, urlLine]

            outputFile.writelines(toWrite)
            outputFile.close()
    
    
    
    
print("\t\t\tStarting...")
    
inputFile = open("MainList.txt", "r")

inputFile.seek(0, os.SEEK_SET)

line = inputFile.readline()

print("\t\tFinding name...")
while line:

    if line[:5] == "https":
        line = inputFile.readline()
    print(line)
    
    names = findName(line)
    if names:
        # if a name is found in the title, write it out to the new file
        titleLine = line
        urlLine = inputFile.readline()
        addOutputFile(titleLine, urlLine, names)
    
    line = inputFile.readline()

inputFile.close()

print("Done!")