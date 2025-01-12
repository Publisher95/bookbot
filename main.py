def sort_on(myDict):
    return myDict['count']


def main():
    letterDict = {}
    listOfDicts = []
    wordCount = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    for words in file_contents.split():
        wordCount += 1

    for character in file_contents.lower():
        if character not in letterDict:
            letterDict[character] = 1
        else:
            letterDict[character] += 1
    
    for letters in letterDict:
        countDicts = {}
        countDicts['letter'] = letters 
        countDicts['count'] = letterDict[letters]
        listOfDicts.append(countDicts) 



    listOfDicts.sort(reverse=True, key=sort_on)    
    print(listOfDicts)



    print(f"There are {wordCount} words in this book.")

    for dicts in listOfDicts:


main()
