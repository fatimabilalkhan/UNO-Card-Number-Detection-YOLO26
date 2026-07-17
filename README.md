# 🃏 UNO Card Number Detection using YOLO26

## 📌 Project Overview

This project implements a **Real-Time UNO Card Number Detection System** using the **YOLO26** object detection model. The model is trained to accurately detect and classify **15 different UNO card number classes** from images and video streams.

Developed using Python and the Ultralytics framework, this project demonstrates the complete computer vision workflow, including dataset preparation, model training, validation, and real-time inference.

---

## ✨ Features

- 🃏 Real-time UNO card number detection
- 🎯 Custom-trained YOLO26 model
- 📷 Image inference
- 🎥 Video inference
- ⚡ Fast and accurate detection
- 📊 Performance evaluation using mAP metrics
- 🤖 Computer Vision and Deep Learning application

---

## 📂 Dataset Information

- **Number of Classes:** 15

| Class ID | Card Number |
|----------|-------------|
| 0 | 0 |
| 1 | 1 |
| 2 | 10 |
| 3 | 11 |
| 4 | 12 |
| 5 | 13 |
| 6 | 14 |
| 7 | 2 |
| 8 | 3 |
| 9 | 4 |
| 10 | 5 |
| 11 | 6 |
| 12 | 7 |
| 13 | 8 |
| 14 | 9 |

---

## 🛠️ Tech Stack

- Python
- YOLO26
- Ultralytics
- OpenCV
- NumPy

---

## 📁 Project Structure

```text
UNO-Card-Number-Detection-YOLO26
│
├── dataset/
│   ├── images/
│   ├── labels/
│   └── dataset.yaml
│
├── train.py
├── main.py
├── README.md
└── .gitignore
```

---

## 🚀 Applications

- 🤖 Robotics
- 🃏 Smart Card Recognition Systems
- 🎮 AI-Based Gaming Systems
- 📷 Computer Vision Research
- 🧠 Deep Learning Projects
- 📚 Educational AI Applications

---

## 📈 Model Performance

The YOLO26 model was trained on a custom dataset containing 15 UNO card number classes.

Performance was evaluated using standard object detection metrics:

- Precision
- Recall
- mAP@50
- mAP@50-95

---

## 📷 Sample Results

*(Add screenshots of your detection results here.)*

---

## ⚙️ Installation

```bash
git clone https://github.com/fatimabilalkhan/UNO-Card-Number-Detection-YOLO26.git

cd UNO-Card-Number-Detection-YOLO26

pip install ultralytics opencv-python
```

---

## ▶️ Training

```python
python train.py
```

---

## ▶️ Prediction

```python
python main.py
```

---

## 💡 Future Improvements

- Detect action cards (Skip, Reverse, Draw Two, Wild, Wild Draw Four)
- Real-time webcam detection
- Mobile deployment
- ROS integration for robotics
- AI-powered UNO game assistant

---

## 👩‍💻 Author

**Fatima Bilal Khan**

BS Robotics Student

Computer Vision & AI Enthusiast

---

⭐ If you found this project useful, consider giving it a star on GitHub!
