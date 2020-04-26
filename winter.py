import pyperclip
import random
import json
from re import compile
words = []
winterKeyRegex = "^([A-Za-z]{1}|[#]+|[\?]+)(\s{1}([A-Za-z]{1}|[#]+|[\?]+))*$"


def generateLetterWildcard(winterKeyItem):
    generated = getRandonWord(length=len(winterKeyItem))
    return generated


def generateNumericWildcard(winterKeyItem):
    generated = ""
    for char in winterKeyItem:
        generated = generated + str(random.randint(0, 9))
    return generated


controlChars = {
    "?": generateLetterWildcard,
    "#": generateNumericWildcard,
}


def main(clipboardContext=None):
    global words
    if(matchRegex(fromClipboard, winterKeyRegex)):
        winterKey = fromClipboard.split()
        words = loadWords()
        parseWinterKey(winterKey)
    else:
        print("Sorry, that's not a valid winterkey.")


def loadWords():
    with open("./words.json") as f:
        words = json.load(f)
    return words


def matchRegex(inputString, pattern):
    matchPattern = compile(pattern)
    res = matchPattern.match(inputString)
    return res


def parseWinterKey(winterKey):
    generated = []
    for winterKeyItem in winterKey:
        generatedItem = parseWinterKeyItem(winterKeyItem)
        generated.append(generatedItem)
    winterPassword = " ".join(generated)
    pyperclip.copy(winterPassword)
    print(winterPassword)


def getRandonWord(startingLetter=None, length=None):
    global words
    filtered = []
    if (startingLetter):
        filtered = [word for word in words if word.startswith(
            startingLetter.lower())]
    if (length):
        filtered = [word for word in words if len(word) == length]
    chosenWord = random.choice(filtered)
    if (startingLetter) and (startingLetter.isupper()):
        chosenWord = chosenWord.capitalize()
    return chosenWord


def parseWinterKeyItem(winterKeyItem):
    generated = ""
    if (winterKeyItem.isalpha()):
        # Letter, -> generate word
        generated = getRandonWord(startingLetter=winterKeyItem[0])
    elif (winterKeyItem[0:1] in controlChars.keys()):
        # Wildcard, -> generate word
        generated = controlChars[winterKeyItem[0:1]](winterKeyItem)
    else:
        # Don't care about this just return it.
        generated = winterKeyItem
    return generated


if (__name__ == "__main__"):
    main()
