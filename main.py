def sort_on(myDict):
    return myDict['count']


def main():
    bookPath = "books/frankenstein.txt"
    letterDict = {}
    listOfDicts = []
    wordCount = 0
    with open(bookPath) as f:
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

    print(f"--- Begin report of {bookPath} ---")
    print(f"{wordCount} words found in the document\n")


    for dicts in listOfDicts:
        if dicts['letter'].isalpha():
            print(f"The '{dicts['letter']}' was found {dicts['count']} times")

    print("--- End report ---")

main()
