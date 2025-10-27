# Cat AI 😸

Your webcam reacts to your face and hand gestures, showing matching cat images and playing sounds.

![Beschreibung des Bildes](example_sad.png)


## Pose recognition

| Emote       | Description            | Img                                     |
|-------------|-----------------------|----------------------------------------|
| Normal      | Keine Bewegung         | <img src="imgs/cat_normal.jpg" width="100"> |
| Laughing 😸 | Lächeln                | <img src="imgs/cat_happy.jpg" width="100"> |
| Crying 😿   | Beide Hände vorm Gesicht | <img src="imgs/cat_sad.jpg" width="100"> |
| One hand ✋  | Winkende Hand          | <img src="imgs/cat_wave.jpg" width="100"> |
| Both 🙌     | Beide Hände oben       | <img src="imgs/cat_both_up.jpg" width="100"> |

## Functions

- Full-body pose detection (33 landmarks)  
- Face detection (468 landmarks)  
- Left and right hand detection (21 landmarks each)  
- Gesture recognition: both hands up 🙌, one hand waving ✋, hands covering face 😿  
- Smile detection 😸  
- Real-time GUI updates with cat images  
- Optional sound feedback for each status

## Installation

1. Open a terminal (Git Bash, PowerShell, or CMD).  
2. Clone the repository:

```bash
git clone https://github.com/rodin04/cat_ai.git
```

3. Navigate to the project folder.
```bash
cd folder path
```

4. Install requirements
```bash
pip install -r requirements.txt
```



## Files / Structure

- `cat_ai.py` – Main Python script
- `requirements.txt` – Python dependencies
- `imgs/` – Images for different states
  - `cat_normal.jpg`
  - `cat_happy.jpg`
  - `cat_sad.jpg`
  - `cat_wave.jpg`
  - `cat_both_up.jpg`
- `sounds/` – Optional sound files
  - `normal.wav`
  - `laughing.wav`
  - `sad.wav`
  - `hello.wav`
  - `yay.wav`
- `example.png` – Example image for README or reference

## Requirements

- Python 3.12+  
- OpenCV 4.8+ (`opencv-python==4.8.1.78`)  
- MediaPipe 0.10+ (`mediapipe==0.10.21`)  
- NumPy 1.24+ (`numpy==1.24.3`)  
- Pygame 2.5+ (`pygame==2.5.2`)  
- Pillow 10+ (`Pillow==10.2.0`)  
- Tkinter (`tk==0.1.0`)  


