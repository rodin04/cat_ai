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

- Detects full-body pose (33 landmarks) and face (468 landmarks)  
- Detects left and right hands (21 landmarks each)  
- Recognizes gestures: both hands up 🙌, one hand waving ✋, hands covering face 😿  
- Detects smile 😸  
- Updates GUI images in real-time  
- Optional sound feedback for each status




