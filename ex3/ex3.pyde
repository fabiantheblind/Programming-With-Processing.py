#to have some interaction
#we need an loop to look for actions

def setup():
    size(400, 400)
    #executed once
    println("This is the setup. Executed once. Initiate things here")

#executed all the time waiting for infos
def draw():
    #do the bakcground color transformation
    noStroke()
    fill(map(mouseX, width, 0, 0, width), 100)
    rect(0, 0, width, height)
    #do the circle color transformation
    fill(mouseX)
    #draw an ellipse
    ellipse(mouseX, mouseY, 10, 10)

    #print some infos
    println("Frame number: " + frameCount)
    print("mouse x: " + mouseX )
    println(" mouse y: " + mouseY )

