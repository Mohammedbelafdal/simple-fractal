###created by mohammed belafdal on 04/03/2021
    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.
from PIL import Image
import time,math
###Constantes
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
green=(0,255,0)
red=(255,0,0)
constant=-1.3
threshold1=1500000
threshold2=150
###image creation
output=Image.new("RGB",(1366,766))
###fractal function
def mandelset(x,y,iteration):
    value=complex(x,y)
    for x in range (0,iteration):
        value=value*value+constant
    try:
        if abs(value)>threshold1:
            return 2
        if abs(value)>threshold2:
            return 1
    except Exception:##in case of overflow
        return 0
    return False
###pixel by pixel editing
def main():
    for y in range (0,output.size[1]):
            for x in range (0,output.size[0]):
                ###positionning the origin
                xaxis=float(x-output.size[0]/2)
                yaxis=float(output.size[1]/2-y)
                coords=(x,y)
                ###filling the background
                output.putpixel(coords,black)
                ###drawing the set
                if mandelset(xaxis/100,yaxis/100,10)==1:
                    output.putpixel(coords,red)
                if mandelset(xaxis/100,yaxis/100,10)==2:
                    output.putpixel(coords,green)
                ###drawing the axis
                if(xaxis%40==0 or yaxis%40==0):
                    output.putpixel(coords,white)
                if((xaxis==0 or yaxis==0)):
                    output.putpixel(coords,blue)
    ###display and save
    output.show()
    output.save(str(str(constant)+"&"+str(threshold1)+"&"+str(threshold2)+".png"))


if __name__=="__main__":
    main()