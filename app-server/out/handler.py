import sys
import json

dirC = None
dirH = None
dirL = None
jsonData = None

def setFilePaths(readData):
    global dirC
    global dirH
    global dirL

    dirC = readData[0][12:]
    dirH = readData[1][10:]
    dirL = readData[2][8:]
    
    return

def readConfigFile():
    readData = []
    linesToRead = [1, 2, 3]

    with open("config.conf") as f:
        for position, line in enumerate(f):
            if position in linesToRead:
                readData.append(str.rstrip(line))
        f.close()

    return setFilePaths(readData)

def readJson():
    global jsonData

    with open("images.json") as f:
        jsonData = json.load(f)
        f.close()
    print(jsonData["client"])
    if not (jsonData["images"]):
        print("Error, there are no images to handle")
        sys.exit()

    return

def main():
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    readJson()
    readConfigFile()
    sys.exit()

if __name__ == "__main__":
    main()