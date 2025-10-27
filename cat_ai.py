import cv2
import mediapipe as mp
import time
import tkinter as tk
from PIL import Image, ImageTk
import os
import threading

# === Optional: pygame nur laden, wenn verfügbar ===
try:
    import pygame
    pygame.mixer.init()
    SOUND_AVAILABLE = True
except Exception as e:
    print("⚠️ Kein Lautsprecher oder Soundgerät verfügbar:", e)
    SOUND_AVAILABLE = False

# === Settings ===
IMG_DIR = "imgs"
SOUND_DIR = "sounds"

status_data = {
    "Keine Bewegung": ("cat_normal.jpg", "normal.wav"),
    "Beide Hände oben 🙌": ("cat_both_up.jpg", "yay.wav"),
    "Winkende Hand ✋": ("cat_wave.jpg", "hello.wav"),
    "Beide Hände vorm Gesicht 😿": ("cat_sad.jpg", "sad.wav"),
    "Lächeln 😸": ("cat_happy.jpg", "laughing.wav")
}

current_sound = None

# === Tkinter GUI ===
root = tk.Tk()
root.title("Status Anzeige")
label_img = tk.Label(root)
label_img.pack()
label_text = tk.Label(root, text="", font=("Arial", 24))
label_text.pack()
current_state = None

def update_gui(status):
    global current_state, current_sound
    if status != current_state:
        current_state = status

        # Bild aktualisieren
        img_path = os.path.join(IMG_DIR, status_data[status][0])
        if os.path.exists(img_path):
            img = Image.open(img_path).resize((600, 600))
            photo = ImageTk.PhotoImage(img)
            label_img.config(image=photo)
            label_img.image = photo
        label_text.config(text=status)

        # Sound abspielen (nur wenn Lautsprecher verfügbar)
        if SOUND_AVAILABLE:
            try:
                if current_sound:
                    current_sound.stop()
                sound_path = os.path.join(SOUND_DIR, status_data[status][1])
                if os.path.exists(sound_path):
                    current_sound = pygame.mixer.Sound(sound_path)
                    current_sound.play(loops=-1)  # Endlosschleife
            except Exception as e:
                print("⚠️ Fehler beim Abspielen des Sounds:", e)

# === Kamera + Status Detection Thread ===
def detection_loop():
    mp_pose = mp.solutions.pose
    mp_face = mp.solutions.face_mesh
    pose = mp_pose.Pose()
    face = mp_face.FaceMesh(refine_landmarks=True)
    mp_drawing = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    current_text = "Keine Bewegung"
    last_change_time = 0
    change_delay = 0.5

    stable_state = None
    stable_counter = 0
    stable_threshold = 5  # Anzahl der Frames für stabilen Zustand

    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results_pose = pose.process(rgb)
        results_face = face.process(rgb)

        detected_text = "Keine Bewegung"
        left_hand_above = right_hand_above = False
        left_hand_near_face = right_hand_near_face = False

        # --- Pose check ---
        if results_pose.pose_landmarks:
            mp_drawing.draw_landmarks(frame, results_pose.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            landmarks = results_pose.pose_landmarks.landmark
            nose = landmarks[mp_pose.PoseLandmark.NOSE]
            left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST]
            right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST]
            left_index = landmarks[mp_pose.PoseLandmark.LEFT_INDEX]
            right_index = landmarks[mp_pose.PoseLandmark.RIGHT_INDEX]

            face_height = 0.15
            if results_face.multi_face_landmarks:
                face_landmarks = results_face.multi_face_landmarks[0].landmark
                nose_y = face_landmarks[1].y
                chin_y = face_landmarks[152].y
                face_height = abs(chin_y - nose_y)

            hand_threshold = face_height * 0.7
            hands_above_head = 0.3

            left_hand_near_face = abs(left_index.y - nose.y) < hand_threshold
            right_hand_near_face = abs(right_index.y - nose.y) < hand_threshold
            left_hand_above = left_wrist.y < nose.y - hands_above_head
            right_hand_above = right_wrist.y < nose.y - hands_above_head

            if left_hand_above and right_hand_above:
                detected_text = "Beide Hände oben 🙌"
            elif left_hand_above or right_hand_above:
                detected_text = "Winkende Hand ✋"
            elif left_hand_near_face and right_hand_near_face:
                detected_text = "Beide Hände vorm Gesicht 😿"

        # --- Lächeln check ---
        if results_face.multi_face_landmarks and not (left_hand_above or right_hand_above):
            face_landmarks = results_face.multi_face_landmarks[0].landmark
            left_mouth = face_landmarks[61]
            right_mouth = face_landmarks[291]
            top_lip = face_landmarks[13]
            bottom_lip = face_landmarks[14]

            mouth_open = bottom_lip.y - top_lip.y
            mouth_width = right_mouth.x - left_mouth.x
            nose_y = face_landmarks[1].y
            chin_y = face_landmarks[152].y
            face_height = chin_y - nose_y

            smile_score = (mouth_width / face_height) + (mouth_open / face_height)
            if smile_score > 0.5:
                detected_text = "Lächeln 😸"

        # --- Stabilitäts-Logik ---
        if detected_text == stable_state:
            stable_counter += 1
        else:
            stable_state = detected_text
            stable_counter = 0

        if stable_counter >= stable_threshold:
            now = time.time()
            if detected_text != current_text and now - last_change_time > change_delay:
                current_text = detected_text
                last_change_time = now
                root.after(0, update_gui, detected_text)
                stable_counter = 0

        # --- Frame anzeigen ---
        cv2.putText(frame, current_text, (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Pose Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    root.quit()

# === Startmeldung ===
def show_start_message():
    if SOUND_AVAILABLE:
        label_text.config(text="✅ Sound funktioniert 🎵")
    else:
        label_text.config(text="❌ Kein Sound verfügbar 🔇")

    # Bild passend anzeigen (z. B. neutrale Katze)
    img_path = os.path.join(IMG_DIR, "cat_normal.jpg")
    if os.path.exists(img_path):
        img = Image.open(img_path).resize((400, 400))
        photo = ImageTk.PhotoImage(img)
        label_img.config(image=photo)
        label_img.image = photo

    # Nach 2 Sekunden Detection starten
    root.after(2000, lambda: threading.Thread(target=detection_loop, daemon=True).start())

# === Start GUI mit Soundmeldung ===
show_start_message()
root.mainloop()
