import numpy as np
import argparse
import string
import numpy as np
from PIL import Image
import os
from pickle import dump, load
import numpy as np
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model,load_model
import cv2
from tensorflow import saved_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
def extract_features(img, model):
    img_resize=cv2.resize(img,(224,224))
    img=img_resize.reshape(-1,224,224,3)  
    pred=model.predict(img).reshape(2048,)
    return pred

def word_for_id(integer, tokenizer):
    for word, index in tokenizer.word_index.items():
        if index == integer:
            return word
    return None

def generate_desc(model, tokenizer, photo, max_length):
    in_text = '<start>'
    for i in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)
        pred = model([photo.reshape(1,-1),sequence])
        pred = np.argmax(pred,axis=1)
        word = word_for_id(pred, tokenizer)
        if word is None:
            break
        
        if word == 'end':
            break
        in_text += ' ' + word
    return in_text[7:]


def predict(uploaded_file):
    max_length = 29
    tokenizer = load(open("tokenizer.p","rb"))
    model_res = load_model('model_res.h5')
    model = load_model('img_cap_model.h5',compile=False)
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    
    photo = extract_features(uploaded_file, model_res)
    description = generate_desc(model, tokenizer, photo, max_length)
    return description

model_res=ResNet50(include_top=True)
last=model_res.layers[-2].output
model_res=Model(inputs=model_res.input,outputs=last)
model_res.save("model_res.h5")
