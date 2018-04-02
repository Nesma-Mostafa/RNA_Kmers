import os
X = os.getcwd()+"/N"
with open (X+'/'+"NormalData.txt",'w+') as rs:
	for filename in os.listdir(X):
		if(len(filename.split('.'))==2 and filename.split('.')[1]=="fa"):
			 with open (X+'/'+filename) as f:
				 data =f.read().splitlines()
				 for i in range(0,len(data),1):
					 rs.write(data[i]+" " +'0'+'\n')
				 f.close()
	rs.close()
