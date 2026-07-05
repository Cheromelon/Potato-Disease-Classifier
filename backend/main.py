from fastapi import FastAPI,File,UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # During development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
MODEL=tf.keras.models.load_model("models/1.keras")
CLASS_NAMES=['Early Blight', 'Late Blight', 'Healthy']
@app.get("/ping")
async def ping():
    return "hello,there"

def read_file_as_image(data)->np.ndarray:
    image=np.array(Image.open(BytesIO(data)))
    return image

@app.post('/predict')
async def predict(file:UploadFile=File(...)):
    image=read_file_as_image(await file.read())
    image_batch=np.expand_dims(image,0)
    predictions=MODEL.predict(image_batch,verbose=0)
    predicted_class=CLASS_NAMES[np.argmax(predictions[0])]
    confidence = round(float(np.max(predictions[0]) * 100),2)
    return {'class':predicted_class,'confidence':confidence}

if __name__=="__main__":
    uvicorn.run(app,host='localhost',port=8000)