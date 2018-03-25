import os
for fn in os.listdir(os.getcwd()):
	c=0
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
