# **Scripts**

###### In this ```README.md``` file,the workflow of each script will be mentioned breifly
hear tensorflow has to be installed before keras but u may install jellyfish before both of them as it is independant.

- ```Install_Ternsoflow.sh``` The first script to be excuted is this one, the content of this script is:                                Here tensorflow is installed with virtual environmentas the following     
  - first of all the virtual environment and PIP should be installed
  - Create the Virtual envionment where you will install the tensorflow,**"targetDirectory"** in the script has to be replaced     with directory name , here it is assumed to be **~/tensorflow**
  - activate the virtual environment to install the tensorflow
  - make sure that pip ≥8.1 is installed
  - install **tensorflow** in the created virtual environment
  - activate **tensorflow** and each time **tensorflow** will be used it will must be activated.
  - to make sure that tensorflow is activated import tensorflow
  
-```Install_Keras.sh``` The Secound one is this script as keras used the tensorflow as backend, The content of the script
  - virtual environment has to be created to install keras in it
  - work on the created virtual environment
  - install some python dependencies
  - install keras
  - if keras.hson is not exist in the /keras/keras.json Keras has to be imported 
  - import keras to make sure it is successfully installed.
  
  
