

train=open("train2017.txt","w")
val=open("val2017.txt","w")
for i in range(1,201):
    name=str(i).zfill(6)
    train.write("./images/train2017/{}.jpg\n".format(name))
for i in range(201,401):
    name=str(i).zfill(6)
    val.write("./images/val2017/{}.jpg\n".format(name))
train.close()
val.close()
