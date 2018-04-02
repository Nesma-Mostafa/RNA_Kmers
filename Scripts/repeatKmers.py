import os
X = os.getcwd()+"/N"
for filename in os.listdir(X):
	if(len(filename.split('.'))==2 and filename.split('.')[1]=="fa"):
		 with open (X+'/'+filename) as f:
			 data =f.read().splitlines()
			 with open (X+'/'+filename.split('.')[0]+"1.fa",'w') as rs:
				 for i in range(0,len(data),2):
					 if(int(data[i].split('>')[1])>1):
						 for number in range(int(data[i].split('>')[1])):
							 rs.write(data[i+1]+'\n')
				 rs.close()

X = os.getcwd()+"/T"
for filename in os.listdir(X):
	if(len(filename.split('.'))==2 and filename.split('.')[1]=="fa"):
		 with open (X+'/'+filename) as f:
			 data =f.read().splitlines()
			 with open (X+'/'+filename.split('.')[0]+"1.fa",'w') as rs:
				 for i in range(0,len(data),2):
					 if(int(data[i].split('>')[1])>1):
						 for number in range(int(data[i].split('>')[1])):
							 rs.write(data[i+1]+'\n')
				 rs.close()
