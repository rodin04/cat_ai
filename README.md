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

## Files / Structure

cat_ai/
├── cat_ai.py # Main script
├── requirements.txt # Python dependencies
├── imgs/ # Images for different states
│ ├── cat_normal.jpg
│ ├── cat_happy.jpg
│ ├── cat_sad.jpg
│ ├── cat_wave.jpg
│ └── cat_both_up.jpg
├── sounds/ # Optional sound files
│ ├── normal.wav
│ ├── laughing.wav
│ ├── sad.wav
│ ├── hello.wav
│ └── yay.wav
└── example.png # Example image for README or reference


