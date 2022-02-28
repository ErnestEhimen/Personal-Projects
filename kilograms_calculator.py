


from tkinter import*
root = Tk()
root.title("Conversion Calculator")
root.minsize (350,250)
root.configure(bg = "lightgrey")

L1 = Label(root, text = "Enter kilograms: ", bg = "lightgrey", fg = "black", font = "arial 10")
L1.place(x = 3, y = 25)
L2 = Label(root, text = "Choose a mass/weight: ", bg = "lightgrey", fg = "black", font = "arial 10")
L2.place(x = 25, y = 70)
L3 = Label(root, text= "Answer = ", bg = "lightgrey", fg = "black", font = "arial 10")
L3.place(x = 25, y = 150)

E1 = Entry(root, bg = "white", fg = "black", bd = 3)
E1.place(x = 100, y = 25)

def gramsconversion():
    kilograms = int(E1.get())
    a1 = "{:3f}".format(kilograms * 1000)
    L4.config(text = str(a1) + " " + "grams")
def ouncesconversion():
    kilograms = int(E1.get())
    a2 = kilograms * 35.27396
    L4.config(text = str(a2) + " " + "ounces")
def poundsconversion():
    kilograms = int(E1.get())
    a3 = kilograms * 2.2046
    L4.config(text = str(a3) + " " + "pounds")

B1 = Button(root, text = "grams", bg = "white", fg = "black", font = "arial 10", command = gramsconversion, bd = 3)
B1.place(x = 25, y = 110)
B2 = Button(root, text = "ounces", bg = "white", fg = "black", font = "arial 10", command = ouncesconversion, bd = 3)
B2.place(x = 100, y = 110)
B3 = Button(root, text = "pounds", bg = "white", fg = "black", font = "arial 10", command = poundsconversion, bd = 3)
B3.place(x = 190, y = 110)


L4 = Label(text = "", bg = "white", fg = "black", font = "arial 10")
L4.place(x = 100, y = 150)

#NEXT CONVERSION CODE


L21 = Label(root, text = "Enter grams: ", bg = "lightgrey", fg = "black", font = "arial 10")
L21.place(x = 3, y = 205)
L22 = Label(root, text = "Choose a mass/weight: ", bg = "lightgrey", fg = "black", font = "arial 10")
L22.place(x = 25, y = 250)
L23 = Label(root, text= "Answer = ", bg = "lightgrey", fg = "black", font = "arial 10")
L23.place(x = 25, y = 360)

E21 = Entry(root, bg = "white", fg = "black", bd = 3)
E21.place(x = 95, y = 205)

def kilogramsconversion():
    grams = int(E21.get())
    a11 = "{:3f}".format(grams / 1000)
    L41.config(text = str(a11) + " " + "kilograms")
def ouncesconversion2():
    grams = int(E21.get())
    a21 = grams / 28.35
    L41.config(text = str(a21) + " " + "ounces")
def poundsconversion2():
    grams = int(E21.get())
    a31 = grams / 454
    L41.config(text = str(a31) + " " + "pounds")

B11 = Button(root, text = "kilograms", bg = "white", fg = "black", font = "arial 10", command = kilogramsconversion, bd = 3)
B11.place(x = 25, y = 310)
B21 = Button(root, text = "ounces", bg = "white", fg = "black", font = "arial 10", command = ouncesconversion2, bd = 3)
B21.place(x = 120, y = 310)
B31 = Button(root, text = "pounds", bg = "white", fg = "black", font = "arial 10", command = poundsconversion2, bd = 3)
B31.place(x = 190, y = 310)


L41 = Label(text = "", bg = "white", fg = "black", font = "arial 10")
L41.place(x = 95, y = 360)



##NEXT CONVERSION CODE

L221 = Label(root, text = "Enter pounds: ", bg = "lightgrey", fg = "black", font = "arial 10")
L221.place(x = 470, y = 25)
L222 = Label(root, text = "Choose a mass/weight: ", bg = "lightgrey", fg = "black", font = "arial 10")
L222.place(x = 495, y = 70)
L223 = Label(root, text= "Answer = ", bg = "lightgrey", fg = "black", font = "arial 10")
L223.place(x = 495, y = 150)

E221 = Entry(root, bg = "white", fg = "black", bd = 3)
E221.place(x = 570, y = 25)

def kilogramsconversion3():
    pounds = int(E221.get())
    a111 = "{:3f}".format(pounds / 2.205)
    L441.config(text = str(a111) + " " + "kilograms")
def ouncesconversion3():
    pounds = int(E221.get())
    a221 = pounds * 16
    L441.config(text = str(a221) + " " + "ounces")
def gramsconversion3():
    pounds = int(E221.get())
    a331 = pounds * 454
    L441.config(text = str(a331) + " " + "grams")

B111 = Button(root, text = "kilograms", bg = "white", fg = "black", font = "arial 10", command = kilogramsconversion3, bd = 3)
B111.place(x = 490, y = 110)
B221 = Button(root, text = "ounces", bg = "white", fg = "black", font = "arial 10", command = ouncesconversion3, bd = 3)
B221.place(x = 590, y = 110)
B331 = Button(root, text = "grams", bg = "white", fg = "black", font = "arial 10", command = gramsconversion3, bd = 3)
B331.place(x = 680, y = 110)


L441 = Label(text = "", bg = "white", fg = "black", font = "arial 10")
L441.place(x = 590, y = 150)




###NEXT CONVERSION CODE


L2221 = Label(root, text = "Enter ounces: ", bg = "lightgrey", fg = "black", font = "arial 10")
L2221.place(x = 470, y = 205)
L2222 = Label(root, text = "Choose a mass/weight: ", bg = "lightgrey", fg = "black", font = "arial 10")
L2222.place(x = 495, y = 250)
L2223 = Label(root, text= "Answer = ", bg = "lightgrey", fg = "black", font = "arial 10")
L2223.place(x = 495, y = 360)

E2221 = Entry(root, bg = "white", fg = "black", bd = 3)
E2221.place(x = 570, y = 205)

def kilogramsconversion4():
    ounces = int(E2221.get())
    a1111 = "{:3f}".format(ounces / 35.274)
    L4441.config(text = str(a1111) + " " + "kilograms")
def poundsconversion4():
    ounces = int(E2221.get())
    a2221 = ounces / 16
    L4441.config(text = str(a2221) + " " + "pounds")
def gramsconversion4():
    ounces = int(E2221.get())
    a3331 = ounces * 28.35
    L4441.config(text = str(a3331) + " " + "grams")

B1111 = Button(root, text = "kilograms", bg = "white", fg = "black", font = "arial 10", command = kilogramsconversion4, bd = 3)
B1111.place(x = 490, y = 310)
B2221 = Button(root, text = "pounds", bg = "white", fg = "black", font = "arial 10", command = poundsconversion4, bd = 3)
B2221.place(x = 590, y = 310)
B3331 = Button(root, text = "grams", bg = "white", fg = "black", font = "arial 10", command = gramsconversion4, bd = 3)
B3331.place(x = 680, y = 310)


L4441 = Label(text = "", bg = "white", fg = "black", font = "arial 10")
L4441.place(x = 590, y = 360)



####NEXT CODE CONVERSION

L22221 = Label(root, text = "Enter centimetres: ", bg = "lightgrey", fg = "black", font = "arial 10")
L22221.place(x = 3, y = 410)
L22222 = Label(root, text = "Choose a length: ", bg = "lightgrey", fg = "black", font = "arial 10")
L22222.place(x = 25, y = 455)
L22223 = Label(root, text= "Answer = ", bg = "lightgrey", fg = "black", font = "arial 10")
L22223.place(x = 25, y = 560)

E22221 = Entry(root, bg = "white", fg = "black", bd = 3)
E22221.place(x = 115, y = 410)

def metres5():
    centimetres = int(E22221.get())
    a11111 = "{:3f}".format(centimetres / 100)
    L44441.config(text = str(a11111) + " " + "metres")
def millimetres5():
    centimeters = int(E22221.get())
    a22221 = "{:3f}".format(centimeters * 10)
    L44441.config(text = str(a22221) + " " + "millimetres")
def inches5():
    centimeters = int(E22221.get())
    a33331 = "{:3f}".format(centimeters / 2.54)
    L44441.config(text = str(a33331) + " " + "inches")

B11111 = Button(root, text = "metres", bg = "white", fg = "black", font = "arial 10", command = metres5, bd = 3)
B11111.place(x = 35, y = 510)
B22221 = Button(root, text = "millimetres", bg = "white", fg = "black", font = "arial 10", command = millimetres5, bd = 3)
B22221.place(x = 120, y = 510)
B33331 = Button(root, text = "inches", bg = "white", fg = "black", font = "arial 10", command = inches5, bd = 3)
B33331.place(x = 210, y = 510)


L44441 = Label(text = "", bg = "white", fg = "black", font = "arial 10")
L44441.place(x = 95, y = 560)



#######NEXT CONVERSION CODE

LL21 = Label(root, text = "Enter metres: ", bg = "lightgrey", fg = "black", font = "arial 10")
LL21.place(x = 470, y = 410)
LL22 = Label(root, text = "Choose a length: ", bg = "lightgrey", fg = "black", font = "arial 10")
LL22.place(x = 495, y = 455)
LL23 = Label(root, text= "Answer = ", bg = "lightgrey", fg = "black", font = "arial 10")
LL23.place(x = 495, y = 560)

EE21 = Entry(root, bg = "white", fg = "black", bd = 3)
EE21.place(x = 570, y = 410)

def centimetres6():
    metres = int(EE21.get())
    aa11 = "{:2f}".format(metres * 100)
    LL41.config(text = str(aa11) + " " + "metres")
def millimetres6():
    metres = int(EE21.get())
    aa21 = "{:2f}".format(metres * 1000)
    LL41.config(text = str(aa21) + " " + "millimetres")
def inches6():
    metres = int(EE21.get())
    aa31 = "{:2f}".format(metres * 39.37)
    LL41.config(text = str(aa31) + " " + "inches")

BB11 = Button(root, text = "centimetres", bg = "white", fg = "black", font = "arial 10", command = centimetres6, bd = 3)
BB11.place(x = 490, y = 510)
BB21 = Button(root, text = "millimetres", bg = "white", fg = "black", font = "arial 10", command = millimetres6, bd = 3)
BB21.place(x = 590, y = 510)
BB31 = Button(root, text = "inches", bg = "white", fg = "black", font = "arial 10", command = inches6, bd = 3)
BB31.place(x = 680, y = 510)


LL41 = Label(text = "", bg = "white", fg = "black", font = "arial 10")
LL41.place(x = 590, y = 560)



################NEXT CODE CONVERSION##################

L2210 = Label(root, text = "Enter inches: ", bg = "lightgrey", fg = "black", font = "arial 10")
L2210.place(x = 920, y = 25)
L2220 = Label(root, text = "Choose a length: ", bg = "lightgrey", fg = "black", font = "arial 10")
L2220.place(x = 940, y = 70)
L2230 = Label(root, text= "Answer = ", bg = "lightgrey", fg = "black", font = "arial 10")
L2230.place(x = 940, y = 150)

E2210 = Entry(root, bg = "white", fg = "black", bd = 3)
E2210.place(x = 1010, y = 25)

def centimetres7():
    inches = int(E2210.get())
    a1110 = "{:3f}".format(inches * 2.54)
    L4410.config(text = str(a1110) + " " + "centimetres")
def millimetres7():
    inches = int(E2210.get())
    a2210 = inches * 25.4
    L4410.config(text = str(a2210) + " " + "millimetres")
def metres7():
    inches = int(E2210.get())
    a3310 = inches / 39.37
    L4410.config(text = str(a3310) + " " + "metres")

B1110 = Button(root, text = "centimetres", bg = "white", fg = "black", font = "arial 10", command = centimetres7, bd = 3)
B1110.place(x = 940, y = 110)
B2210 = Button(root, text = "millimetres", bg = "white", fg = "black", font = "arial 10", command = millimetres7, bd = 3)
B2210.place(x = 1040, y = 110)
B3310 = Button(root, text = "metres", bg = "white", fg = "black", font = "arial 10", command = metres7, bd = 3)
B3310.place(x = 1130, y = 110)


L4410 = Label(text = "", bg = "white", fg = "black", font = "arial 10")
L4410.place(x = 1040, y = 150)



#NEXT CONVERSION CODE

L2221_ = Label(root, text = "Enter millimetres: ", bg = "lightgrey", fg = "black", font = "arial 10")
L2221_.place(x = 920, y = 205)
L2222_ = Label(root, text = "Choose a length: ", bg = "lightgrey", fg = "black", font = "arial 10")
L2222_.place(x = 940, y = 250)
L2223_ = Label(root, text= "Answer = ", bg = "lightgrey", fg = "black", font = "arial 10")
L2223_.place(x = 940, y = 360)

E2221_ = Entry(root, bg = "white", fg = "black", bd = 3)
E2221_.place(x = 1040, y = 205)

def centimetres8():
    millimetres = int(E2221_.get())
    a1111_ = "{:3f}".format(millimetres / 10)
    L4441_.config(text = str(a1111_) + " " + "centimetres")
def metres8():
    millimetres = int(E2221_.get())
    a2221_ = millimetres / 1000
    L4441_.config(text = str(a2221_) + " " + "metres")
def inches8():
    millimetres = int(E2221_.get())
    a3331_ = millimetres / 25.4
    L4441_.config(text = str(a3331_) + " " + "inches")

B1111_ = Button(root, text = "centimetres", bg = "white", fg = "black", font = "arial 10", command = centimetres8, bd = 3)
B1111_.place(x = 940, y = 310)
B2221_ = Button(root, text = "metres", bg = "white", fg = "black", font = "arial 10", command = metres8, bd = 3)
B2221_.place(x = 1040, y = 310)
B3331_ = Button(root, text = "inches", bg = "white", fg = "black", font = "arial 10", command = inches8, bd = 3)
B3331_.place(x = 1130, y = 310)


L4441_ = Label(text = "", bg = "white", fg = "black", font = "arial 10")
L4441_.place(x = 1040, y = 360)


#*#*#*#*#*#*##*#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*#*#*##*#*#*#*#**#*#*#*#*#*#**#*##*#*#*#*#*#*#*#*#*#*#*#*#
#FINAL CONVERSION CODE

LL21_1 = Label(root, text = "Enter kilometres: ", bg = "lightgrey", fg = "black", font = "arial 10")
LL21_1.place(x = 920, y = 410)
LL22_1 = Label(root, text = "Choose a length: ", bg = "lightgrey", fg = "black", font = "arial 10")
LL22_1.place(x = 940, y = 455)
LL23_1 = Label(root, text= "Answer = ", bg = "lightgrey", fg = "black", font = "arial 10")
LL23_1.place(x = 940, y = 560)

EE21_1 = Entry(root, bg = "white", fg = "black", bd = 3)
EE21_1.place(x = 1040, y = 410)

def metres9():
    kilometres = int(EE21_1.get())
    aa11_1 = "{:2f}".format(kilometres * 1000)
    LL41_1.config(text = str(aa11_1) + " " + "metres")
def miles9():
    kilometres = int(EE21_1.get())
    aa21_1 = "{:2f}".format(kilometres / 1.609)
    LL41_1.config(text = str(aa21_1) + " " + "miles")
def kph9():
    kilometres = int(EE21_1.get())
    aa31_1 = "{:2f}".format(kilometres / 60)
    LL41_1.config(text = str(aa31_1) + " " + "kph")

BB11_1 = Button(root, text = "metres", bg = "white", fg = "black", font = "arial 10", command = metres9, bd = 3)
BB11_1.place(x = 940, y = 510)
BB21_1 = Button(root, text = "miles", bg = "white", fg = "black", font = "arial 10", command = miles9, bd = 3)
BB21_1.place(x = 1040, y = 510)
BB31_1 = Button(root, text = "kph", bg = "white", fg = "black", font = "arial 10", command = kph9, bd = 3)
BB31_1.place(x = 1130, y = 510)


LL41_1 = Label(text = "", bg = "white", fg = "black", font = "arial 10")
LL41_1.place(x = 1040, y = 560)

root.mainloop()