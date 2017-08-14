import tkinter as tk

class Settings(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        
        labelSet = tk.Label(self, bg="#fafafa", text="Ensemble :")
        labelSet.grid(padx=5, pady=5)

        entrySetString = tk.StringVar()
        entrySetString.set(self.setting("set"))
        self.entrySet = tk.Entry(self, textvariable=entrySetString)
        self.entrySet.grid(padx=5, pady=5)

        buttonSet = tk.Button(self, text="Générer", command=lambda: self.update("render"))
        buttonSet.grid(padx=5, pady=5)

        labelWidth = tk.Label(self, bg="#fafafa", text="Largeur :")
        labelWidth.grid(padx=5, pady=5)

        entryWidthString = tk.StringVar()
        entryWidthString.set(self.setting("width"))
        self.entryWidth = tk.Entry(self, textvariable=entryWidthString)
        self.entryWidth.grid(padx=5, pady=5)

        labelAccur = tk.Label(self, bg="#fafafa", text="Précision :")
        labelAccur.grid(padx=5, pady=5)

        entryAccurString = tk.StringVar()
        entryAccurString.set(self.setting("accuracy"))
        self.entryAccur = tk.Entry(self, textvariable=entryAccurString)
        self.entryAccur.grid(padx=5, pady=5)

        buttonResize = tk.Button(self, text="Dimensionner", command=lambda: self.update("size"))
        buttonResize.grid(padx=5, pady=5)

    def setting(self, setting, value = None):
        settings = {"set": "random_2d(10000)", "width": "400", "accuracy": "40"}

        file = open("settings.txt")
        for line in file.read().split("\n"):
            splited = line.split(":")
            settings[splited[0]] = splited[1]
        file.close()
        
        if value != None:
            settings[setting] = value
            
            file = open("settings.txt", "w")
            file.write("\n".join([i+":"+j for (i, j) in settings.items()]))
            file.close()
        else:
            return settings[setting]

    def update(self, button):
        if button == "render":
            self.setting("set", self.entrySet.get())
        self.setting("width", self.entryWidth.get())
        self.setting("accuracy", self.entryAccur.get())
        self.callback(button)

class Graph(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.rectangleCount = [1]

        self.canvasGradient = tk.Canvas(self, bg="#778899", highlightthickness=0)
        self.canvasGradient.bind("<B1-Motion>", self.mouse)
        self.canvasGradient.grid(row=0, column=0)

        frameStats = tk.Frame(self, bg="#fafafa", bd=0)
        frameStats.grid(row=1, column=0)

        labelPerTitle = tk.Label(frameStats, bg="#fafafa", text="POURCENTAGE :")
        labelPerTitle.grid(column=0, row=0, padx=20)
        self.labelPer = tk.Label(frameStats, bg="#fafafa", text="")
        self.labelPer.grid(column=0, row=1)

        labelQuantTitle = tk.Label(frameStats, bg="#fafafa", text="QUANTITE :")
        labelQuantTitle.grid(column=1, row=0, padx=20)
        self.labelQuant = tk.Label(frameStats, bg="#fafafa", text="")
        self.labelQuant.grid(column=1, row=1)

        labelIndexTitle = tk.Label(frameStats, bg="#fafafa", text="INDICE :")
        labelIndexTitle.grid(column=2, row=0, padx=20)
        self.labelIndex = tk.Label(frameStats, bg="#fafafa", text="")
        self.labelIndex.grid(column=2, row=1)

        self.canvasPlot = tk.Canvas(self, bg="#778899", highlightthickness=0, bd=0)
        self.canvasPlot.grid(row=2, column=0)

    def size(self, width, divisions):
        self.canvasWidth = width
        self.canvasGradientXDivisions = divisions

    def draw(self, set):
        window = set[:-1]
        values = set[-1]

        depth = len(window)

        xMin = window[0][0]
        xMax = window[0][1]
        self.canvasGradient.delete("all")
        self.canvasGradient["width"] = self.canvasWidth

        if depth == 1:
            yMin = 0
            yMax = 1
            self.canvasGradientHeight = self.canvasWidth/5
            self.canvasGradientYDivisions = 1
        else:
            yMin = window[1][0]
            yMax = window[1][1]
            self.canvasGradientHeight = self.canvasWidth*((yMax - yMin)/(xMax-xMin))
            self.canvasGradientYDivisions = self.canvasGradientXDivisions

        self.canvasGradient["height"] = self.canvasGradientHeight
        self.rectangleCount.append(self.rectangleCount[-1])
	
        xStep = (xMax - xMin)/self.canvasGradientXDivisions
        xPixel = self.canvasWidth/self.canvasGradientXDivisions
        yStep = (yMax - yMin)/self.canvasGradientYDivisions
        yPixel = self.canvasGradientHeight/self.canvasGradientYDivisions

        stats = [0 for i in range(self.canvasGradientXDivisions*self.canvasGradientYDivisions)]

        for i in range(len(values)):
            e = values[i]
            if depth == 1:
                e = [e, 0]
            stats[int(e[0]/xStep) + self.canvasGradientXDivisions*int(e[1]/yStep)] += 1

        statsTotal = len(values)
        statsMax = max(stats)

        for i in range(len(stats)):
            intensityX = int(stats[i]/statsMax * 255)
            intensity = '#%02x%02x%02x' % (intensityX, intensityX, intensityX)
            self.rectangleCount[-1] += 1
            self.canvasGradient.create_rectangle((i%self.canvasGradientXDivisions)*xPixel, int(i/self.canvasGradientXDivisions)*yPixel, (i%self.canvasGradientXDivisions+1)*xPixel, (int(i/self.canvasGradientXDivisions)+1)*yPixel, fill=intensity, width=0)

        self.canvasPlot["width"] = self.canvasWidth
        self.canvasPlot.delete("all")
        self.canvasPlot["height"] = str(int(self.canvasWidth)/2)
        
        xPixel = self.canvasWidth/len(stats)

        statsIntegral = 0

        avg = len(values)/len(stats)
        a, b = 0, 0
        self.canvasPlot.create_line(0, self.canvasPlot["height"], self.canvasPlot["width"], 0, fill="red")
        for i in range(len(stats)):
            a, b = b, b+stats[i]
            statsIntegral += abs(b-(i+1)*statsTotal/len(stats))
            self.canvasPlot.create_line(i*xPixel, (1-a/statsTotal)*int(self.canvasPlot["height"]), (i+1)*xPixel, (1-b/statsTotal)*int(self.canvasPlot["height"]), fill="white")
        statsIntegral /= len(stats)*statsTotal

        self.labelIndex['text'] = statsIntegral

        self.canvasData = {'total': statsTotal, 'max': statsMax, 'index': statsIntegral, 'data': stats}

    def mouse(self, event):
        i = event.widget.find_closest(event.x, event.y)[0] - self.rectangleCount[-2]
        self.labelPer['text'] = str(round(self.canvasData['data'][i]/self.canvasData['max']*100))+"%"
        self.labelQuant['text'] = str(self.canvasData['data'][i])+" / "+str(self.canvasData['max'])
