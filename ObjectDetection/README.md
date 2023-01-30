# Quick Start Guide

## Here

## To add support for Coral Accelerator

### 1. Issue the following

```
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
curl packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

sudo apt get update
```
### 2. Ensure coral is unplugged
```
## sudo apt-get install libedgetpu1-std
```

