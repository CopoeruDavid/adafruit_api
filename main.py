from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from fastapi.responses import FileResponse
import os
from os import path
from random import randint
import uuid
from PIL import Image
import imagehash
import speech_recognition as sr
from fastapi.middleware.cors import CORSMiddleware
from Adafruit_IO import Client, RequestError, Feed


app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



ADAFRUIT_IO_KEY = 'aio_Selm30Gb4hBqOYhrbmpCjsGlb7Wf'

ADAFRUIT_IO_USERNAME = 'DavidCop'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

@app.get("/windowdown")
async def window_down():
    test = aio.feeds('windowdown')
    print("window going down")
    aio.send_data(test.key, 1)

@app.get("/windowup")
async def window_down():
    test = aio.feeds('windowup')
    print("window going up")
    aio.send_data(test.key, 1)