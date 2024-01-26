import tkinter as tk
import json

dataFile = open('D:\Python\OBS Win Loss Counter\Data.obspt','r+') 
j = json.load(dataFile)

def update():
    #update json
    dataFile.seek(0,0)
    j = json.load(dataFile)
    j['Counter']['Wins'] = wcLabel.cget("text")
    j['Counter']['Losses'] = lcLabel.cget("text")
    j['Counter']['Draws'] = dcLabel.cget("text")
    dataFile.seek(0,0)
    json.dump(j,dataFile)
    dataFile.truncate()

def up(label):
    count = int(label.cget("text"))
    count+=1
    label.config(text = str(count))
    update()
    return


def down(label):
    count = int(label.cget("text"))
    count-=1
    label.config(text = str(count))
    update()
    return


def reset():
    wcLabel.config(text ="0")
    lcLabel.config(text ="0")
    dcLabel.config(text ="0")
    update()
    return

def SubmitRating(start, curr):
    dataFile.seek(0,0)
    j = json.load(dataFile)
    j['Ratings']['Start'] = start
    j['Ratings']['Current'] = curr
    dataFile.seek(0,0)
    json.dump(j,dataFile)
    dataFile.truncate()
    return






window=tk.Tk()

winFrame = tk.Frame(window)
lossFrame = tk.Frame(window)
drawFrame = tk.Frame(window)
ratingFrame = tk.Frame(window)

winFrame.pack()
winLabel =tk.Label(winFrame,text="wins")
wcLabel =tk.Label(winFrame,text="0")
winUp = tk.Button(winFrame,text="+",command = lambda: up(wcLabel))
winDown = tk.Button(winFrame,text="-",command = lambda: down(wcLabel))
winLabel.pack()#side = TOP
wcLabel.pack()
winUp.pack(side = "right")#
winDown.pack(side = "left")#side = LEFT


lossFrame.pack()
lossLabel =tk.Label(lossFrame,text="loss")
lcLabel =tk.Label(lossFrame,text="0")
lossUp = tk.Button(lossFrame,text="+",command = lambda: up(lcLabel))
lossDown = tk.Button(lossFrame,text="-",command = lambda: down(lcLabel))
lossFrame.pack()
lossLabel.pack()#side = TOP
lcLabel.pack()
lossUp.pack(side = "right")#
lossDown.pack(side = "left")#side = LEFT


drawFrame.pack()
drawLabel =tk.Label(drawFrame,text="draw")
dcLabel =tk.Label(drawFrame,text="0")
drawUp = tk.Button(drawFrame,text="+",command = lambda: up(dcLabel))
drawDown = tk.Button(drawFrame,text="-",command = lambda: down(dcLabel))
drawFrame.pack()
drawLabel.pack()#side = TOP
dcLabel.pack()
drawUp.pack(side = "right")#
drawDown.pack(side = "left")#side = LEFT

reset = tk.Button(window, text = "reset",command = reset)
reset.pack()


ratingFrame.pack()
ratingLabel =tk.Label(ratingFrame,text="Ratings",font=(25), pady=20 )
startLabel =tk.Label(ratingFrame,text="Start")
currentLabel =tk.Label(ratingFrame,text="Current")
startEntry = tk.Entry(ratingFrame)
currentEntry = tk.Entry(ratingFrame)
submitRating = tk.Button(ratingFrame,text="Sumbit Rating",command = lambda: SubmitRating(startEntry.get(),currentEntry.get() ) )

ratingLabel.pack()
startLabel.pack()
startEntry.pack()
currentLabel.pack()
currentEntry.pack()
submitRating.pack()


window.title('Stream Deck')
window.geometry("300x450")
window.mainloop()
dataFile.close()