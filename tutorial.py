from appJar import gui

testDict = {"a":False, "b":False}

app=gui()
app.setBg("lightBlue")
app.setFont(20)
app.addProperties("test", testDict)
app.setProperty("test", "Pepper")
app.go()

print(app.getProperties("test"))
