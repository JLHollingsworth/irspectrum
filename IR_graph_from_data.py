from PIL import Image, ImageTk

Width=866
Height=696

f = open("data.txt", "r")
lines=f.readlines()

def str2Tuple(s):#convert strings to 2 element tuples (int, int)
    
    if s=='None':
        return None
    
    l,r =s. split(',')
    return ( int( l[1:len(l)+1] ) , int( r[1:len(r)-1] ) )

#convert data from text file
data=[str2Tuple(s.strip()) for s in lines]

graph=[]

for x in range(Width):#white blank image
    for y in range(Height):
        graph+=[(255,255,255)]

for x in range(0,Width):#draw lines in graph from data
    if data[x]:
        for y in range(data[x][1],data[x][0]):
            graph[y*Width+x]=(0,0,0)

#save graph
img = Image.new('RGB', (Width, Height))
img.putdata(graph)
img.save('regraph.png')
print('done')
