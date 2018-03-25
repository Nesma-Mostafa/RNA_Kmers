file_ =[]
file_.append("NormalData.txt")
file_.append("TumarData..txt")

with open ("dataset.txt" , "w+") as rs:
	for i in file_:
		with open (i) as f:
			data =f.read().splitlines()
			for i in range(0,len(data),1):
				 rs.write(data[i]+'\n')
		f.close()
	rs.close()
