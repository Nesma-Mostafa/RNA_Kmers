#install tensorFlow
sudo apt-get install python3-pip python3-dev python-virtualenv
virtualenv --system-site-packages -p python3  tensorflow
source ~/tensorflow/bin/activate
easy_install -U pip
pip3 install --upgrade tensorflow
source ~/tensorflow/bin/activate 
 python
>>> import tensorflow as tf
>>> quit()

#install Keras
 mkvirtualenv keras_tf
 workon <keras_tf>
 pip install numpy scipy
 pip install scikit-learn
 pip install pillow
 pip install h5py
 pip install keras
 workon keras_tf
 python
>>> import keras
>>> quit()

#install jellyFish
sudo apt-get update
sudo apt-get install jellyfish
