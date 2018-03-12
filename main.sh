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

#Get The Dataset file
wget -O GSE20592_RAW.tar 'https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE20592&format=file' 

#unzip all files
gunzip *.gz

python ConvertToFasta.py

#catch kmers
for n in *.fasta; do 
#printf '%s\n' "$n";
jellyfish count -m 21 -s 100M -t 10 -C  $n;
jellyfish dump mer_counts.jf > ${n%.*}.fa;
done

#repeate each kmer by its frequency
python repeatKmers.py

python MergeNormalData.py

python MergeTumerData.py

python MergeAllFiles

