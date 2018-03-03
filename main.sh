#install tensorFlow
sudo apt-get install python3-pip python3-dev python-virtualenv
virtualenv --system-site-packages -p python3  tensorflow
source ~/tensorflow/bin/activate
easy_install -U pip
pip3 install --upgrade tensorflow
source ~/tensorflow/bin/activate 

#install Keras
 mkvirtualenv keras_tf
 workon <keras_tf>
 pip3 install numpy scipy
 pip3 install scikit-learn
 pip3 install pillow
 pip3 install h5py
 pip3 install keras
 workon keras_tf
 
#install jellyFish
sudo apt-get update
sudo apt-get install jellyfish
