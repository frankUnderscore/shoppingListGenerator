from appJar import gui

import pickle

with open('listComplete.p', 'rb') as fp:
    data = pickle.load(fp)[:-1]


app = gui()

nRows = int(len(data)/2)
for i in range(len(data)):
    name = data[i]["name"]

    row = i % nRows
    column = int(i / nRows)
    app.addLabelNumericEntry(name, row, column)
    app.setEntryDefault(name, 0)
    app.setEntryWidth(name, 3)

app.go()
