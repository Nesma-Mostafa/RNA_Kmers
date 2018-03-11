import zipfile
import os

str=[]
data_txt = []
c=0
for filename in os.listdir(os.getcwd()):
	if(len(filename.split('.'))==3 and filename.split('.')[2]=="gz"):
		str.append(filename)
                data_txt.append(filename.split('.')[0]+".txt")

c=0
for fn in os.listdir(os.getcwd()):
        if(len(filename.split('.'))==2 and filename.split('.')[2]=="txt"):
	with open(fn, 'r+') as f:
		 content = f.read().splitlines()
		 f.seek(0)
		 f.truncate()
		 for i in content:
			 f.write("> SEQ" + str(c) +" "+ content[c]+'\n' )
			 c+=1
		 f.close()
os.rename(fn, fn.split('.')[0]+".fasta") 
