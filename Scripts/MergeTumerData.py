import os
with open (filename.split('.')[0]+"TumarData.txt",'w') as rs:
	for filename in os.listdir(os.getcwd()):
		if(len(filename.split('.'))==2 and filename.split('.')[1]=="fa"):
			 with open (filename) as f:
				 data =f.read().splitlines()
				 for i in range(0,len(data),1):
					 rs.write(data[i]+" " +'0'+'\n')
				 f.close()
	rs.close()
