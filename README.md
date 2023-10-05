# QuickStart Guide

## To Test Object Detection
To get started with testing object detection, follow these steps:

## 1. Clone the Repository
Begin by cloning the Repo.
```
https://github.com/CSUF-CE-TEAM-1/Drone-Modules.git
```
## 2. Set Up Environment
We will primarily use [anaconda](https://www.anaconda.com/download) to manage all packages and dependencies. Create a new conda environment and activate it by running the following commands

```
cd Drone-Modules

conda create -n "drone-env" python=3.8.0

conda activate drone-env

bash get_pi_requirements.sh

```

## 3. Note for macOS and Windows Users
Note: If you attempt to replicate this process on macOS or Windows, the installation of the tflite runtime will not succeed. To resolve this, you will need to manually navigate [here](https://github.com/google-coral/pycoral/releases/) and install the tflite_runtime-2.5.0 package.

## 4. Run Webcam Detection
To run webcam-based object detection, use the following command:
```
python3 ObjectDetection/TFLite_detection_webcam.py --modeldir=Sample_TFLite_model
```
Feel free to explore and modify the repository to suit your needs. -Titan Providence



