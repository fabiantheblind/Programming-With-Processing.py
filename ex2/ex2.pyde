#add some color
#this is the bg of the canvas
background(255)
#we dont want a stroke for now
noStroke()
#create a color
myColor = color(100) #greyscale
#set the fill for all following elements
fill(myColor)
#draw the element
rect(0, 0, width/4, height)
#update the color
myColor = color(100, 200) #greyscale with alpha
#set fill...
fill(myColor)
#draw ..
rect(width/4, 0, (width/4)*2, height)
#update...
myColor = color(100, 200, 100)#RGB color
#set...
fill(myColor)
#draw...
rect((width/4)*2, 0, (width/4)*3, height)
#and
myColor = color(10, 20, 100, 100) #RGB with alpha
#so
fill(myColor)
#on
rect((width/4)*3, 0, width, height)
#the same thing goes for stroke
#take a look at
colorMode(HSB, 360, 100, 100, 100)

