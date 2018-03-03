import os
for filename in os.listdir(os.getcwd()):
	if(len(filename.split('.'))==2 and filename.split('.')[1]=="fa"):
		 with open (filename) as f:
			 data =f.read().splitlines()
			 with open (filename.split('.')[0]+"1.fa",'w') as rs:
				 for i in range(0,len(data),2):
					 if(int(data[i].split('>')[1])>1):
						 for number in range(int(data[i].split('>')[1])):
							 rs.write(data[i+1]+'\n')
				 rs.close()
