# Titan Providence

![drone](images/titan-providence-demo.gif)
![drone](images/titan-providence.jpg)

# QuickStart Guide

To get started, follow these steps:

## 1. Clone the Repository

```bash
# Clone Repository
git clone https://github.com/Seena-02/titan-providence
```

## 2. Set Up Environment

We will primarily use [anaconda](https://www.anaconda.com/download) to manage all packages and dependencies. Create a new conda environment and activate it by running the following commands

```bash
# Create Anaconda Env
conda create -n "drone-env" python=3.8.0

# Activate Env
conda activate drone-env
```

## 3. Prerequisites

```bash
# Install Dependencies
bash get_pi_requirements.sh
```

**Note:** If you attempt to replicate this process on macOS or Windows, the installation of the tflite runtime will not succeed. To resolve this, you will need to manually navigate [here](https://github.com/google-coral/pycoral/releases/) and install the tflite_runtime-2.5.0 package.

## 4. Run Webcam Detection

To run webcam-based object detection, use the following command:

```bash
# Navigate to project
cd Drone-Modules

# Run Detection
python3 ObjectDetection/TFLite_detection_webcam.py --modeldir=Sample_TFLite_model
```

## 5. Use the Coral USB Accelerator(Increase TensorFlow Lite FPS!)

If you're working on a desktop or laptop PC, feel free to skip this step. However, if your intention is to deploy this on a Raspberry Pi, please continue below. A Coral USB Accelerator can be purchased [here](https://coral.ai/products/accelerator/). During our testing, we observed a 3x increase in frames per second (FPS).

Begin by issuing the following.

```bash
# Adds the Coral Edge TPU repository to your system's list of package sources.
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list

# Downloads the Google Cloud apt-key and adds it to the system's trusted keyring.
curl packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
```

**Before procceding ensure that the USB Accelerator is NOT plugged into the device.**

You may choose either the **standard** or **max** runtime. **Note** that while the max runtime offers faster frame rates by overclocking the processor, temperatures will increase.

```bash
# Standard
sudo apt get install libedgetpu1-std
```

or

```bash
# Max
sudo apt get install libedgetpu1-max
```

Plug in Edge TPU into the device, and issue the following.

```bash
# Run Detection w/ --edgetpu
python3 TFLite_detection_webcam.py --modeldir=Sample_TFLite_model --edgetpu
```

Feel free to explore and modify the repository to suit your needs. -Titan Providence :)
