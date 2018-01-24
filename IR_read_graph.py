from PIL import Image, ImageTk

'''Change image opened here<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'''
#img = Image.open('90-01-7.bmp')
#img = Image.open('99-05-8.bmp')
img = Image.open('556-18-3.bmp')
'''<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'''
imgdata=list(img.getdata())

Width=1024
Height=768

targetRect=(113,978,29,724)

def copyRect(source,rect):
    left,right,top,bottom=rect
    if left<0: left=0
    if top<0: top=0
    if right>=Width: right=Width-1
    if bottom>=Height: bottom=Height-1

    newImg=[]

    #print(range(top,bottom+1),range(left,right+1))
    
    for y in range(top,bottom+1):
    #for row in range(0,2,1):
        for x in range(left,right+1):
            newImg+=[source[y*Width+x]]
            #print(col,row,y*Width+x)
    return newImg

graph=copyRect(imgdata,targetRect)

Width=targetRect[1]-targetRect[0]+1
Height=targetRect[3]-targetRect[2]+1

img = Image.new('RGB', (Width, Height))
img.putdata(graph)
img.save('graph.png')

data=[]

def pix(x,y):
    if x>=Width or y>=Height or x<0 or y<0:
        print('Out of range!:',x,y,'\n')
    else:
        r,g,b=graph[y*Width+x]
        if r+g+b>=100:
            return False
        else:
            return True

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

f = open("data.txt", "w")
for element in data:
    f.write(str(element) + '\n')
f.close()
