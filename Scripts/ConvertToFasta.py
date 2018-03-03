import zipfile
import os

def fixBadZipfile(zipFile):  
 f = open(zipFile, 'r+b')  
 data = f.read()  
 pos = data.find('\x50\x4b\x05\x06') # End of central directory signature  
 if (pos > 0):  
     self._log("Trancating file at location " + str(pos + 22)+ ".")  
     f.seek(pos + 22)   # size of 'ZIP end of central directory record' 
     f.truncate()  
     f.close()   

str=[]
data_txt = []
c=0
for filename in os.listdir(os.getcwd()):
	if(len(filename.split('.'))==3 and filename.split('.')[2]=="gz"):
		str.append(filename)
                data_txt.append(filename.split('.')[0]+".txt")
                
#print(data_txt)
                
#for i in str:
	#fantasy_zip = zipfile.ZipFile(str[c],r)
        #fantasy_zip.extract(data_txt[c], os.getcwd())
        #fantasy_zip.close()
        #c+=1 
fn = "/home/nesma/Documents/Dataset_original/xx/GSM532872_G652T.txt"
c=0
for fn in data_txt:
	with open(fn, 'r+') as f:
		 content = f.read().splitlines()
		 f.truncate()
		 for i in content:
			 f.write("> SEQ" + str(c) +" "+ content[c]+'\n' )
			 c+=1
		 f.close()
		 os.rename(fn, fn.split('.')[0]+".fasta")      
               
