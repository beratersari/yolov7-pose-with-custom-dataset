data=open("cars_train/files.txt","r")

lines=data.readlines()

out=open("train_labels.txt","w")
for i in lines:
	line="./images/cars_train/"+i
	out.write(line)
out.close()
	

