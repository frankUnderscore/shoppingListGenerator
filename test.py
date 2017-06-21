import pickle

def replaceUmlauts(inputString):
    return inputString.replace("Ã¼", "ü").replace("Ã¤", "ä").replace("Ã–", "Ö")

with open('list.p', 'rb') as fp:
    data = pickle.load(fp)[:-1]

data.append({"name" : "Obst & Gemüse je nach Saison", "homeLocation" : "andere"})


for item in data:
    for key in item.keys():
        item[key] = replaceUmlauts(item[key])
"""
for l in data:
    print(l)
    """

locationChunks = [chunk.split("\n") for chunk in open("shoppingItemsByStoreLocation.txt").read().split("\n\n")]
for locationChunk in locationChunks:
    location = locationChunk[0]
    location = replaceUmlauts(location)
    print(location)
    for item in locationChunk[1:]:
        if not item == "":
            item = replaceUmlauts(item)
            dictItem = [dictItem for dictItem in data if dictItem["name"]== item][0]
            for key in dictItem.keys():
                dictItem[key] = replaceUmlauts(dictItem[key])
            dictItem["storeLocation"] = location



for item in data:
    print(item)

pickle.dump(data , open( "listComplete.p", "wb" ) )
