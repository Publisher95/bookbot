def main():
    letterDict = {}
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
        

    




    printf("There are {wordCount} words in this book.")




main()
