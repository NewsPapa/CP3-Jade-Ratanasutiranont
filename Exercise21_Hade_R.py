from tkinter import *
import math

def leftClickButton(event):
  Result_1 = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
  labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
  if Result_1 >= 30.0:
    labelResults.configure(text="Extreme Obesity")
  elif Result_1 >= 25.0:
    labelResults.configure(text="Obesity")
  elif Result_1 >= 23.0:
    labelResults.configure(text="Over Weight")
  elif Result_1 >= 18.6:
    labelResults.configure(text="Normal")
  else:
    labelResults.configure(text="Thin")

MainWindow = Tk()
labelHeight = Label(MainWindow, text="Tall (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="Fat (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow, text = "Evaluation")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2)
labelResult = Label(MainWindow,text="Result_1")
labelResult.grid(row=2,column=1)
labelResults = Label(MainWindow,text = "Result_Mean")
labelResults.grid(row=3,column=1)
MainWindow.mainloop()
