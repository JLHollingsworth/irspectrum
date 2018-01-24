from PIL import Image, ImageTk
import sys

img = Image.open(sys.argv[1])
imgdata=list(img.getdata())#the pixels from the image

#this with and height seems to be standard for all IR samples
Width=1024
Height=768

#the area of each image that we want (the graph)
        #(left,right,top,bottom)
targetRect=(113,978,29,724)

def copyRect(source,rect):#copies pixels from the source image within the targetRect
    left,right,top,bottom=rect
    if left<0: left=0
    if top<0: top=0
    if right>=Width: right=Width-1
    if bottom>=Height: bottom=Height-1

    newImg=[]
    
    for y in range(top,bottom+1):
        for x in range(left,right+1):
            newImg+=[source[y*Width+x]]
    return newImg

#the graph cut out of the larger image
graph=copyRect(imgdata,targetRect)

#width and height of out cropped graph
Width=targetRect[1]-targetRect[0]+1
Height=targetRect[3]-targetRect[2]+1

#save the graph image
img = Image.new('RGB', (Width, Height))
img.putdata(graph)
img.save('graph.png')

data=[]

def pix(x,y):#checks if the pixel at x,y is black
    if x>=Width or y>=Height or x<0 or y<0:
        print('Out of range!:',x,y,'\n')
    else:
        r,g,b=graph[y*Width+x]
        if r+g+b>=100:
            return False
        else:
            return True

#for each x get the range over which the graph is drawn (has black pixels)
    # or None if the graph is empty at that x value
for x in range(0,Width):
    data+=[None]
    foundPix=False
    for y in range(0,Height):
        p=pix(x,y)
        if p and not foundPix:
            foundPix=True
            maxVal=y
        elif not p and foundPix:
            minVal=y
            data[-1]=(minVal,maxVal)
            break

#save data
f = open("data.txt", "w")
for element in data:
    f.write(str(element) + '\n')
f.close()

print('done')
            
