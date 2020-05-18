How to setup Tensorflow-GPU ?
=========================
There are 2 options to setup Tensorflow GPU Version by either installing Tensorflow Container or Tensorflow GPU with GPU Driver enabled.



1) Setup Tensorflow Container is pretty straight forward but Tensorflow libaries/python/jupyter are a bit old.

https://docs.docker.com/toolbox/toolbox_install_windows/

a) Install Docker ToolBox Community Edition since my computer install with Win10 HOME Edition.

b) Run "Docker QuickStart Terminal' icon.

c) Navigate to your bash.exe location.

d) It will create docker machine when first time running this command.

e) To test installation, "docker run hello-world"

f) docker pull tensorflow/tensorflow/t

g) docker run -it tensorflow/tensorflow bash




2) Setup Tensorflow GPU with GPU Driver enabled.

a) Download and install Anaconda and select Python 3.7

b) Open Anaconda Prompt and open "Base" anaconda

c) The latest Tensorflow GPU version is 1.13.1, which I found the installation does not work on 1st trail.

After checking, this Tensorflow version only works with Python v3.6.

d) Download Python version to 3.6 in 2nd trail

conda install python=3.6

e) Create a new conda environment to buld all modules using GPU.

mkdir tensorflow

cd tensorflow

conda create --name PythonGPU36 python=3.6


f) Activate pythongpu36

g) To install Keras & Tensorflow GPU related modules by :

conda install -c anaconda keras-gpu

conda install spyder

conda install -c anaconda pandas

conda install -c anaconda xlrd

conda install -c anaconda xlwt

conda install -c anaconda seaborn

conda install -c anaconda scikit-learn

conda install ipykernel

conda install juypter notebook (otherwise, it will use python3.7 Jupyter Notebook by default)

h) Add new Python kernal in Jupyter Notebook

python -m ipykernal install --user --name pythongpu36 --display-name "TensorFlow-GPU"

i) Execute DirectX Diagnosis "dxdiag" to check your Display Card supports driver model "WDDM".
 "
(I am using NVIDA Geoforce MX150)

j) Install the latest NVIDIA Device Driver by "Geforce Experience" 

https://www.geforce.com/drivers

k) Check Device Manager that your device driver works properly.

l) Install CUDA Toolkit by checking which CUDA version compatiale with TensorFlow GPU version.

https://www.tensorflow.org/install/source#linux

https://developer.nvidia.com/cuda-downloads

Install CUDA v10.1


m) Install cuDNN by checking wich cuDNN version compatiable with Tensorflow GPU version

Install cuDNN v7.5.1

n) Use Task Manager => Performance to check GPU work properly.

o) Run TestGPU.ipynb by setting "cpu:0" or "gpu:0" device to test the processing time difference.
