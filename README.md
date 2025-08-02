# YOLO Segmentation & Pose Detection in Python

This project demonstrates how to perform real-time object segmentation and human pose detection using YOLOv8 models in Python. It uses the [Ultralytics](https://github.com/ultralytics/ultralytics) library to simplify model loading and inference.

---

## 🚀 Features

- ✅ Real-time object segmentation
- ✅ Real-time human pose detection
- ✅ Works with images, videos, or webcam
- ✅ Minimal setup using Python
- ✅ Lightweight and scalable code

---

## 📦 Installation

Install the required dependencies:

```bash
pip install ultralytics opencv-python numpy
```

## Supported Models
You can download YOLOv8 pretrained models from the Ultralytics release page.

Recommended models:

yolov8n-seg.pt – for segmentation (nano)

yolov8m-seg.pt – for segmentation (medium)

yolov8n-pose.pt – for pose estimation (nano)

yolov8m-pose.pt – for pose estimation (medium)


## Project Structure
.
├── segment.py         # Script for object segmentation
├── pose_detect.py     # Script for human pose detection
├── utils.py           # Helper functions (optional)
├── assets/            # Sample images/videos (optional)
├── requirements.txt   # List of dependencies
└── README.md


Made with ❤️ by combining YOLOv8, Python, and OpenCV





