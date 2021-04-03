from PIL import Image
import time,math
###Constantes
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)
###creation de l image
output=Image.new("RGB",(1366,766))
###fonction mandelbrot
def mandelset(x,y,iteration):
    value=complex(x,y)
    for x in range (0,iteration):
        value=value*value-1.3
    try:
        if abs(value)>1500000:
            return 2
        if abs(value)>150:
            return 1
    except Exception:
        return 0
    return False
###iteration pixel par pixel
for y in range (0,output.size[1]):
        for x in range (0,output.size[0]):
            xaxis=float(x-output.size[0]/2)
            yaxis=float(output.size[1]/2-y)
            coords=(x,y)
            radius=math.sqrt(xaxis*xaxis+yaxis*yaxis)
            output.putpixel(coords,black)
            if mandelset(xaxis/100,yaxis/100,10)==1:
                output.putpixel(coords,red)
            if mandelset(xaxis/100,yaxis/100,10)==2:
                output.putpixel(coords,green)
            if(xaxis%40==0 or yaxis%40==0):
                output.putpixel(coords,white)
            if((xaxis==0 or yaxis==0)):
                output.putpixel(coords,blue)
###affichage et enregistrement
output.show()
output.save(str(str(time.gmtime())+".png"))
