
import cv2
img=cv2.imread("images/val2017/000397.jpg")
data=open("labels/val2017/000397.txt","r")
data2=open("landmark_align.txt","r")
lines2=data2.readlines()
line=lines2[396]
print(line)
line=line.split(" ")
for i in range(1,len(line)):
    line[i]=int(line[i])


lines=data.readlines()
print(len(lines[0].split(" ")))
lines=lines[0].split(" ")
print(len(lines))
for i in range(len(lines)):
    lines[i]=float(lines[i])
height=img.shape[0]
width=img.shape[1]
bbox=[]
bbox.append(int(width*lines[1]))
bbox.append(int(height*lines[2]))
bbox.append(int(width*lines[3]))
bbox.append(int(height*lines[4]))
print(bbox)
img=cv2.rectangle(img, (bbox[0]-bbox[2]//2, bbox[1]-bbox[3]//2), (bbox[0]+bbox[2]//2, bbox[1]+bbox[3]//2), (255,255,255), 2)
for i in range(5,len(lines),3):
    img = cv2.circle(img, (int(lines[i]*width),int(lines[i+1]*height)), radius=0, color=(0, 0, 255), thickness=2)

imS = cv2.resize(img, (1024, 768))                # Resize image
cv2.imshow("output", imS)                       # Show image
k = cv2.waitKey(0)

