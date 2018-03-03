import os
with open (filename.split('.')[0]+"NormalData.txt",'w') as rs:
	for filename in os.listdir(os.getcwd()):
		if(len(filename.split('.'))==2 and filename.split('.')[1]=="txt"):
			 with open (filename) as f:
				 data =f.read().splitlines()
				 for i in range(0,len(data),1):
					 rs.write(data[i]+'\n')
				 f.close()
	rs.close()
