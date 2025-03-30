import cv2
import mediapipe as mp

# Mediapipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Ruta del vídeo
video_path = "/home/h4ckxel/Desktop/KO-Analysis-AI/Videos/Sparring.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error en: {video_path}")
    exit()

# Muestra fotograma por fotograma
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Imagen a RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detector de pose
    results = pose.process(rgb_frame)

    # Se dibuja pose si se detecta
    if results.pose_landmarks:
        # Marcas de los puntos de referencia
        mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Imagen con las marcas de los puntos de referencia
    cv2.imshow('Pose Estimation', frame)

    # Tecla "q" para salir
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
