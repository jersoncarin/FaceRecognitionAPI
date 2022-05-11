from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import base64
import face
import os

if not os.path.exists(face.IMAGES_PATH):
    os.mkdir(face.IMAGES_PATH)

if(os.getenv('APP_ENV') == 'production'):
    app = FastAPI(docs_url=None)
else:
    app = FastAPI()

app.mount("/static", StaticFiles(directory=face.IMAGES_PATH), name="static")

class Data(BaseModel):
    image: str

class FaceData(BaseModel):
    image_string: str
    user_id: int

@app.post("/face_verify")
def verify_face(image: Data):
    try:
        with open(f'{face.SOURCE_PATH}', "wb") as f:
            image_data = image.image.replace('data:image/png;base64','').replace('data:image/jpeg;base64','')
            f.write(base64.b64decode(image_data))
            face_id = face.detect_face_id()

            if face_id is None:
                return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"status": 404, "message": "Face ID not found in the server."})

            return JSONResponse(status_code=status.HTTP_200_OK, content={"face_id": face_id})
    except BaseException  as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"status": 500, "message": str(e)})

@app.post("/register_face")
def register_face(image: FaceData):
    try:
        image_name = f'image_{image.user_id}_dataset.png'

        # If images path not exist then create
        if not os.path.exists(face.IMAGES_PATH):
            os.mkdir(face.IMAGES_PATH)

        with open(f'{face.IMAGES_PATH}/{image_name}', "wb") as f:
            image_data = image.image_string.replace('data:image/png;base64','').replace('data:image/jpeg;base64','')
            f.write(base64.b64decode(image_data))

            if not os.path.exists(f'{face.IMAGES_PATH}/{image_name}'):
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"status": 400, "message": "Face has not been register in the server."})

            return JSONResponse(status_code=status.HTTP_200_OK, content={"image_name": image_name, "face_id": image.user_id, "image_path": f'static/{image_name}'})
    except BaseException  as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"status": 500, "message": str(e)})