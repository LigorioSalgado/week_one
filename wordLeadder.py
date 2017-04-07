def wordLadder(beginWord, endWord, wordList, limit = 50):

    def closeWords(word1, word2):
        return sum(letter[0] != letter[1] for letter in zip(word1, word2)) == 1

    paths = [[beginWord]]
    nextList = [x for x in wordList if x != beginWord]

    index = 0
    while index < len(paths):
        currentPath = paths[index]
        print("currentPath->")
        print(currentPath)
        currentWord = currentPath[-1]
        print("Current word ->"+currentWord)
        currentList = nextList[:]
        print("currentList ->")
        print(currentList)
        for newWord in currentList:
            if closeWords(currentWord, newWord):
                newPath = currentPath + [newWord]
                print("Newpath ->")
                print(newPath)
                nextList.remove(newWord)
                if newWord == endWord:
                    return (len(newPath))
                else:
                    paths.append(newPath)
                    print("paths ->")
                    print(paths)
        index += 1

    return 0

if __name__=='__main__':
    beginWord= "hot"
    endWord= "dog"
    wordList= ["hot",
               "dog",
               "cog",
               "pot",
               "dot"]
    print(wordLadder(beginWord, endWord, wordList))