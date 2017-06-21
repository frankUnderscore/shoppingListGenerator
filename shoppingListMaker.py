from appJar import gui
import pickle
from fpdf import FPDF

"""
returns list of dictionaries representing
each item that needs to be in the house
"""
def getItemsNeeded():
    with open('listComplete.p', 'rb') as fp:
        return pickle.load(fp)[:-1]

def getUserEntries(itemsNeeded):
    app = gui()
    buildInterface(app, itemsNeeded)
    app.go()

    return getEntries(app)

def buildInterface(app, itemsNeeded):
    nRows = int(len(itemsNeeded)/2)
    for i in range(len(itemsNeeded)):
        name = itemsNeeded[i]["name"]

        row = i % nRows
        column = int(i / nRows)
        app.addLabelNumericEntry(name, row, column)
        app.setEntryDefault(name, 0)
        app.setEntryWidth(name, 3)

    app.addButton("Enter", lambda x: closeApp(app), nRows + 2, 1)
    app.setButtonWidth("Enter", 20)


    app.enableEnter(lambda x: closeApp(app))

#for when it's time to stop
def closeApp(app):
    app.stop()

def getEntries(app):
    entries = app.getAllEntries()
    for key in entries.keys():
        entries[key] = int(entries[key])
    return entries

def generatePDF(entries):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 16)

if __name__ == "__main__":
    itemsNeeded = getItemsNeeded()
    userEntries = getUserEntries(itemsNeeded)
    print(userEntries)
