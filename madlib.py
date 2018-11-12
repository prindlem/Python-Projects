from pathlib import Path
import re
import sys

def main():

    i = open(sys.argv[1], 'r+')
    o = open(sys.argv[2], 'r+')

    inputStr = i.read()
    outputStr = o.read()

    m = re.findall("(?<=\[)(.*?)(?=\])", inputStr)

    for oldInput in m:
        newInput = input("Please provide a " + oldInput + ": ")
        oldInputIndex = m.index(oldInput)
        m[oldInputIndex] = newInput

    newStr = inputStr
    k = 0
    while k < len(m):
        n = re.search("\[.*?\]", newStr)[0]
        newStr = newStr.replace(n, m[k])
        k += 1

    print(newStr)

    o.write(newStr+"\n")

    i.close()
    o.close()

if __name__ == "__main__":
    main()
