# **Scripts**

###### In this ```README.md``` file,the workflow of each script will be mentioned breifly
 ```Install_Tensorflow.sh``` has to be excuted before ```Install_Keras.sh``` but ```install_JellyFish.sh``` may be excuted before both of them or after as it is independant so it is prefered to excute the scripts in the following order.

- ```Install_Ternsoflow.sh``` The first script to be excuted is this one, the content of this script is:                                Here tensorflow is installed with virtual environmentas the following     
  - first of all the virtual environment and PIP should be installed
  - Create the Virtual envionment where you will install the tensorflow,**"targetDirectory"** in the script has to be replaced     with directory name , here it is assumed to be **~/tensorflow**
  - activate the virtual environment to install the tensorflow
  - make sure that pip ≥8.1 is installed
  - install **tensorflow** in the created virtual environment
  - activate **tensorflow** and each time **tensorflow** will be used it will must be activated.
  - to make sure that tensorflow is activated import tensorflow
  
- ```Install_Keras.sh``` The Secound one is this script as keras used the tensorflow as backend, The content of the script
  - virtual environment has to be created to install keras in it
  - work on the created virtual environment
  - install some python dependencies
  - install keras
  - if keras.hson is not exist in the /keras/keras.json Keras has to be imported 
  - import keras to make sure it is successfully installed.
  
- ```install_JellyFish.sh```  this script to install jellyfish 
      just issuing the 2 lines which will install it directly
      
- ```Count_Kmers.sh``` this script for using the jellyfish to count kmers and get the frequencies so it must be excuted in the same order
 - divide the fasta dataset file into k-mers **reads.fasta** shoud be replaced with the name of the datasetfile
 - get the histogram of k-mers frequencies and write the output to file **OutputFile** may be replaced with any file name
 - it is optional and may be commented by **;** or **#**, it is only for search on specific k-mer to make sure that the returned   k-mers is correct

  
  
