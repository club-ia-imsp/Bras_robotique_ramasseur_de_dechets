import cv2
import serial 
import mediapipe as mp
from pyfirmata import Arduino, util
# Configurations
cam_source = 0
x_min, x_mid, x_max = 0, 75, 180
palm_angle_min, palm_angle_mid = -50, 20
y1_min, y1_mid, y1_max = 170, 75, 0
y2_min, y2_mid, y2_max = 60, 120, 180
y3_min, y3_mid, y3_max = 200, 50, 50
z_min, z_mid, z_max = 0, 40, 180
claw_open_angle = 180
claw_close_angle = 0

clamp = lambda n, minn, maxn: max(min(maxn, n), minn)
map_range = lambda val, in_min, in_max, out_min, out_max: abs(
    (val - in_min) * (out_max - out_min) // (in_max - in_min) + out_min)


# Angles initiaux pour les servos
servo_angle = [x_mid, y1_mid, y2_mid, y3_mid, z_mid, claw_open_angle]
prev_servo_angle = servo_angle[:]

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


# Initialisation de la caméra et de la carte Arduino
cap = cv2.VideoCapture(cam_source)
board = Arduino('COM3')
ser=board.sp
servo_x_pin = board.get_pin('d:3:s')
servo_y1_pin = board.get_pin('d:5:s')
servo_y2_pin = board.get_pin('d:6:s')
servo_y3_pin = board.get_pin('d:9:s')
servo_z_pin  = board.get_pin('d:10:s')
servo_claw_pin = board.get_pin('d:11:s')

arduino_serial=serial.Serial(port="COM3",baudrate=57600,timeout=1)

def wait_for_confirmation():
    while True:
        if arduino_serial.in_waiting > 0:
            response=arduino_serial.readline().decode().strip()

            if response =="done":
                break


# Fonction pour calculer la distance entre deux points
def calculate_distance(point1, point2):
    return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2 + (point1.z - point2.z) ** 2) ** 0.5
   
# Fonction pour vérifier si les doigts sont levés ou baissés
def check_finger_positions(hand_landmarks):
    WRIST = hand_landmarks.landmark[0]
    INDEX_FINGER_TIP = hand_landmarks.landmark[8]
    INDEX_FINGER_MCP = hand_landmarks.landmark[5]
    MIDDLE_FINGER_TIP = hand_landmarks.landmark[12]
    MIDDLE_FINGER_MCP = hand_landmarks.landmark[9]
    PINKY_TIP = hand_landmarks.landmark[20]
    PINKY_MCP = hand_landmarks.landmark[17]
    THUMB_BASE = hand_landmarks.landmark[1]
    INDEX_BASE = hand_landmarks.landmark[5]
    THUMB_TIP = hand_landmarks.landmark[4]
    RING_TIP=hand_landmarks.landmark[16]
    RING_MCP=hand_landmarks.landmark[13]

    distances = {
        "index": calculate_distance(WRIST, INDEX_FINGER_TIP) > calculate_distance(WRIST, INDEX_FINGER_MCP),
        "middle": calculate_distance(WRIST, MIDDLE_FINGER_TIP) > calculate_distance(WRIST, MIDDLE_FINGER_MCP),
        "pinky": calculate_distance(WRIST, PINKY_TIP) > calculate_distance(WRIST, PINKY_MCP),
        "thumb": calculate_distance(THUMB_TIP, INDEX_BASE) > calculate_distance(THUMB_BASE, INDEX_BASE),
        "ring": calculate_distance(WRIST, RING_TIP) > calculate_distance(WRIST, RING_MCP)
    }
    return distances

# Convertir les positions des doigts en angles pour les servos
def landmark_to_servo_angle(hand_landmarks_right, hand_landmarks_left, prev_servo_angle):
    
    servo_angle = prev_servo_angle[:]
    distances_right = check_finger_positions(hand_landmarks_right)
    distances_left = check_finger_positions(hand_landmarks_left)

    WRIST_RIGHT = hand_landmarks_right.landmark[0]
    INDEX_FINGER_MCP_RIGHT = hand_landmarks_right.landmark[5]
    palm_size = ((WRIST_RIGHT.x - INDEX_FINGER_MCP_RIGHT.x) ** 2 + (WRIST_RIGHT.y - INDEX_FINGER_MCP_RIGHT.y) ** 2 + \
                (WRIST_RIGHT.z - INDEX_FINGER_MCP_RIGHT.z) ** 2) ** 0.5
    
    # Calculate x angle
    angle = int(((WRIST_RIGHT.x - INDEX_FINGER_MCP_RIGHT.x) /palm_size) * 180 / 3.1415926)
    angle = clamp(angle, palm_angle_min, palm_angle_mid)
    servo_angle0= map_range(angle, palm_angle_min, palm_angle_mid, x_max, x_min)
    #espace_autorisation=[int(i) for i in range (70,150) ]
    if palm_size>=0.2068279321240721:
        servo_angle[0]=x_min if 90>=servo_angle0>=0 else x_max
    else:
        servo_angle[0]=prev_servo_angle[0]
        
    if distances_left.get("index"):
        servo_angle[1] = y1_max if distances_right["index"] else y1_min

    if distances_left.get("middle"):
        servo_angle[2] = y2_max if distances_right["middle"] else y2_min

    if distances_left.get("ring"):
        servo_angle[3] = y3_max if distances_right["ring"] else y3_min

    if distances_left.get("thumb"):
        servo_angle[5] = claw_open_angle if distances_right["thumb"] else claw_close_angle

    if distances_left.get("pinky"):
        servo_angle[4] = z_max if distances_right["pinky"] else z_min

    prev_servo_angle[:] = servo_angle
    return [int(i) for i in servo_angle]

with mp_hands.Hands(model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        right_hand_landmarks = None
        left_hand_landmarks = None

        if results.multi_hand_landmarks and results.multi_handedness:
            for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
                hand_label = results.multi_handedness[idx].classification[0].label
                if hand_label == "Left":
                    right_hand_landmarks = hand_landmarks
                elif hand_label == "Right":
                    left_hand_landmarks = hand_landmarks

                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

            if right_hand_landmarks and left_hand_landmarks:
                distances_left = check_finger_positions(left_hand_landmarks)
                servo_angle = landmark_to_servo_angle(right_hand_landmarks, left_hand_landmarks, prev_servo_angle)

                # Vérification que distances_left est non vide avant d'utiliser ses clés

                wait_for_confirmation()
                servo_x_pin.write(servo_angle[0])
                if distances_left.get("index"):
                    servo_y1_pin.write(servo_angle[1])
                if distances_left.get("middle"):
                    servo_y2_pin.write(servo_angle[2])
                if distances_left.get("ring"):
                    servo_y3_pin.write(servo_angle[3])
                if distances_left.get("thumb"):
                    servo_claw_pin.write(servo_angle[5])
                if distances_left.get("pinky"):
                    servo_z_pin.write(servo_angle[4])
                

                print("Servo angles:", servo_angle)

        cv2.putText(image, str(servo_angle), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('MediaPipe Hands', image)

        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()

