import pandas as pd
import cv2
data=open("bbox_align.txt","r")
lines=data.readlines()
data2=open("landmark_align.txt","r")
lines2=data2.readlines()
for i in range(0,400):
    line2=lines2[396]
    line2=line2.split(" ")
    for j in range(1,len(line2)):
        line2[j]=int(line2[j])

    line=lines[i].split(" ")
    print(line)
    name=line[0]
    number=name.split(".")
    number=int(number[0])
    print(number)
    if(number<201):
        print("train"+name)
        img=cv2.imread("images/train2017/"+name)
    else:
        print("val"+name)
        img=cv2.imread("images/val2017/"+name)
    img_height=img.shape[0]
    img_width=img.shape[1]
    name=name.split('.')[0]+".txt"
    x_center=(float(line[1])+float(line[3]))//2
    y_center=(float(line[2])+float(line[4]))//2

    width=(float(line[3])-float(line[1]))
    height=(float(line[4])-float(line[2]))
    if(number<201):
        file=open("labels/train2017/"+name,"w")
    else:
        file=open("labels/val2017/"+name,"w")
    file.write("0 "+str(x_center/img_width)+" "+str(y_center/img_height)+" "+str(width/img_width)+" "+str(height/img_height)+" "+str(line2[37*2-1]/img_width)+" "+str(line2[37*2]/img_height)+" "+"2.00000000"+" "+str(line2[34*2-1]/img_width)+" "+str(line2[34*2]/img_height)+" "+"2.00000000"+" "+str(line2[46*2-1]/img_width)+" "+str(line2[46*2]/img_height)+" "+"2.00000000"+" "+str(line2[49*2-1]/img_width)+" "+str(line2[49*2]/img_height)+" "+"2.00000000"+" "+str(line2[55*2-1]/img_width)+" "+str(line2[55*2]/img_height)+" "+"2.00000000\n")
    file.close()
