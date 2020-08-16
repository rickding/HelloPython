import face_recognition
import cv2
from PIL import Image, ImageDraw

image = face_recognition.load_image_file("test.jpg")
face_locations = face_recognition.face_locations(image)
print("found %d faces" % len(face_locations))

# mark face
for face in face_locations:
    y0, x1, y1, x0 = face
    cv2.rectangle(image, pt1=(x0, y0), pt2=(x1, y1), color=(0, 0, 255), thickness=3)

cv2.imwrite("./marked.jpg", image)

# crop face
for i in range(len(face_locations)):
    y0, x1, y1, x0 = face_locations[i]
    cropped = image[y0:y1, x0:x1]
    cv2.imwrite("./face_" + str(i) + ".jpg", cropped)

# encoding and compare
face_encodings = face_recognition.face_encodings(image, face_locations)
is_same = face_recognition.compare_faces([face_encodings[0]], face_encodings[1])

print("Is same face: ", is_same)

# landmarks
face_landmarks = face_recognition.face_landmarks(image, face_locations)

pil_image = Image.fromarray(image)
draw = ImageDraw.Draw(pil_image)

for face_landmark in face_landmarks:
        for facial_feature in face_landmark.keys():
            draw.line(face_landmark[facial_feature], width=3)

pil_image.save("./landmark.jpg")

# decoration
for face_landmark in face_landmarks:
    face = ImageDraw.Draw(pil_image, "RGBA")
    face.polygon(face_landmark['top_lip'], fill=(150, 0, 0, 128))
    face.polygon(face_landmark['bottom_lip'], fill=(150, 0, 0, 128))
    face.line(face_landmark['top_lip'], fill=(150, 0, 0, 64), width=2)
    face.line(face_landmark['bottom_lip'], fill=(150, 0, 0, 64), width=2)

pil_image.save("./decoration.jpg")