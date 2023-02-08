#!/bin/bash

# Get packages required for OpenCV

sudo apt-get -y install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get -y install libxvidcore-dev libx264-dev
sudo apt-get -y install qt4-dev-tools 
sudo apt-get -y install libatlas-base-dev

# Need to get an older version of OpenCV because version 4 has errors
pip3 install opencv-python==3.4.11.41

# Get packages required for TensorFlow
# Using the tflite_runtime packages available at https://www.tensorflow.org/lite/guide/python
# Will change to just 'pip3 install tensorflow' once newer versions of TF are added to piwheels

#pip3 install tensorflow

version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
sys_arch=$(uname -m)


if [ $version == "3.9" ]; then
link="https://github.com/google-coral/pycoral/releases/download/v2.0.0/tflite_runtime-2.5.0.post1-cp39-cp39-linux_${sys_arch}.whl"
wget "${link}"
fi

if [ $version == "3.8" ]; then
link="https://github.com/google-coral/pycoral/releases/download/v2.0.0/tflite_runtime-2.5.0.post1-cp38-cp38-linux_${sys_arch}.whl"
wget "${link}"
fi

if [ $version == "3.7" ]; then
link="https://github.com/google-coral/pycoral/releases/download/v2.0.0/tflite_runtime-2.5.0.post1-cp37-cp37-linux_${sys_arch}.whl"
wget "${link}"
fi

if [ $version == "3.6" ]; then
link="https://github.com/google-coral/pycoral/releases/download/v2.0.0/tflite_runtime-2.5.0.post1-cp36-cp36-linux_${sys_arch}.whl"
wget "${link}"
fi

if [ $version == "3.5" ]; then
link="https://github.com/google-coral/pycoral/releases/download/v2.0.0/tflite_runtime-2.5.0.post1-cp35-cp35-linux_${sys_arch}.whl"
wget "${link}"
fi
