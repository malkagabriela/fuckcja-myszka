
  
def setup(): 
    size(200, 200)
    global pg
    pg = createGraphics(100, 100)

def draw(): 
    if mousePressed:
        line(20,25,40,60)
    else:
        pass  #tu powinno się oddziać, jako że miało się coś dziać tylko gdy mysz wciśnieta


        