from tkinter import *

def retrieve():

    # get the data 
    kg1 = kg.get()
    gal1 = gal.get()
    
    # make it float
    kg1 = float(kg1)
    gal1 = float(gal1)
    
    
    if Var1.get() == 1: #check 100LL
        # check for data to display and do corresponding math
        if gal1 != 0 and kg1 == 0 :
            outputKg = gal1 * 2.68735
            Output.set("%.3f kg " % ( outputKg ))

        elif kg1 != 0 and gal1 == 0 :

            outputGal = kg1 / 2.68735
            Output.set(" %.3f gal" % ( outputGal))

        else     :

            outputKg = gal1 * 2.68735
            outputGal = kg1 / 2.68735
            Output.set(" %.3f gal      %.3f kg " % ( outputGal, outputKg ))
        
    elif Var1.get() == 2: #check JetA
        #do the math
        outputKg = gal1 * 3.08447722
        outputGal = kg1 / 3.08447722
        # check for data to display        
        if gal1 != 0 and kg1 == 0 :
            Output.set("%.3f kg " % ( outputKg ))

        elif kg1 != 0 and gal1 == 0 :

             Output.set(" %.3f gal" % ( outputGal))

        else     :

            Output.set(" %.3f gal      %.3f kg " % ( outputGal, outputKg ))
    else: #if user did not specify fueltype

        Output.set("Please choose fuel type.")

def reset(): #clear the form and enter zeros

    kg.delete(0,'end')
    gal.delete(0, 'end')
    kg.insert(0,"0")
    gal.insert(0,"0")
    Output.set(" ")
   
root = Tk()
root.geometry("350x400")
frame = Frame(root)
frame.pack()
 
leftframe = Frame(root)
leftframe.pack(side=LEFT)
 
rightframe = Frame(root)
rightframe.pack(side=RIGHT)

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

label1 = Label(frame, text = "\n\nThis is the FSE Fuel converter")
label1.pack()

Var1 = IntVar()
 
RBttn = Radiobutton(frame, text = "100LL", variable = Var1,
                    value = 1)
RBttn.pack(padx = 5, pady = 5)
 
RBttn2 = Radiobutton(frame, text = "JetA", variable = Var1,
                     value = 2)
RBttn2.pack(padx = 5, pady = 5)

lable2 = Label(frame, text = "KG:")
lable2.pack()
kg = Entry(frame, width = 20)
kg.insert(0,'0')
kg.pack( padx = 5, pady = 5)

label3 = Label(frame, text = "GAL:")
label3.pack()
gal = Entry(frame, width = 15)
gal.insert(0,'0')
gal.pack( padx = 5, pady = 5)

button = Button(leftframe, text = "Convert", command = retrieve)
button.pack( padx = 60, pady = 5)

button = Button(rightframe, text = "Reset", command = reset)
button.pack( padx = 60, pady = 5)

Output = StringVar()
Output.set(" ")

labelOutput = Label(frame, textvariable = Output )
labelOutput.pack(pady = 10 )

 

root.title("FSE Fuel Converter 1.0 by cad01")
root.mainloop()
