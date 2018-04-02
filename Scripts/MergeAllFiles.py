import os


X1= os.getcwd()+"/N"
X2= os.getcwd()+"/T"

file_ =[]
file_.append(X1+'/'+"NormalData.txt")
file_.append(X2+'/'+"TumarData.txt")
X = os.getcwd()+"/DataSet"

with open (X+'/'+"dataset.txt" , "w+") as rs:
	for i in file_:
		with open (i) as f:
			data =f.read().splitlines()
			for i in range(0,len(data),1):
				 rs.write(data[i]+'\n')
		f.close()
	rs.close()
