import cv2
import face_recognition
import os
import numpy as np

  # Image Path Contant
IMAGES_PATH = f'{os.getcwd()}{os.sep}images'
SOURCE_PATH = f'{os.getcwd()}{os.sep}source{os.sep}source_dataset.png'

def detect_face_id():
    # List all trained images for verification
    image_list = os.listdir(IMAGES_PATH)
    images = []
    source = cv2.imread(SOURCE_PATH)
    image_ids = []

    # Read all images using opencv
    # for image in image_list:
    #     images.append(cv2.imread(f'{IMAGES_PATH}{os.sep}{image}'))

    #     # Format of the image name is image_{id}_dataset.png
    #     # so we need to get the second value of list to get the id
    #     image_ids.append(image.split('_')[1])

    # Encode the images
    def encode_images(images):
        encoded_list = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encoded = face_recognition.face_encodings(img)[0]
            encoded_list.append(encoded)
        return encoded_list

    # Get the list of images encoded
    #encoded_images_list = encode_images(images)

    # if len(encoded_images_list) < 1:
    #     return None

    # # Check if the source id is fill and source image
    # if source is not None:
    #     try:
    #         faces_frame_location = face_recognition.face_locations(source)
    #         encoded_face_frame = face_recognition.face_encodings(source, faces_frame_location)

    #         for face in encoded_face_frame:
    #             matches = face_recognition.compare_faces(encoded_images_list, face)
    #             face_distance = face_recognition.face_distance(encoded_images_list, face)
    #             # Find the lowest index so that is the best match
    #             bestMatchIndex = np.argmin(face_distance)
    #             # Check if the index is the best match of the face
                
    #             if matches[bestMatchIndex] and image_ids[bestMatchIndex]:
    #                 return image_ids[bestMatchIndex]
    #     except IndexError:
    #         return None
    return None
                