print(2+2)
intVar = 1
floatVar = 3.14
booleanVar = False
stringVar = "slowo"
pustyVar = None

print('To sa nasze zmienne: {} , {} , {} , {} , {} ').format( type(intVar) ,type(floatVar), type(booleanVar), type(stringVar), type(pustyVar))
print(type(intVar))
print (type(2+2.0))
print(stringVar*2)

if (2 is not 2) and (2 is not 3):
    print("warunek jest spelniony") 
elif 2 < 3:
    print("inny warunek")
else:
    print("warunek nie jest spelniony")

def setup():
    pass    

def draw():
    print(mousePressed)
    line(20,50,100,150)