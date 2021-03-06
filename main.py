import streamlit as st
from PIL import Image
from PIL import ImageFont
import requests
from PIL import ImageDraw
import io
from keras.models import Sequential
from keras.layers import Activation, Dense
from keras.layers import Conv2D, MaxPooling2D, Flatten
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from json import load
import sys
from PIL import Image
from keras.models import load_model
import numpy as np

st.title("毒キノコ分類")
st.subheader('椎茸 or 毒キノコ　調べるよ')

upload_file = st.file_uploader('JPG形式の画像を選択してください', type='jpg')
if upload_file is not None:
    image = Image.open(upload_file)
    image = image.resize((64,64))
    image.show()
    model = load_model('model.h5')
    np_image = np.array(image)
    np_image = np_image /255
    np_image = np_image[np.newaxis, :, :, :]
    result = model.predict(np_image)
    
    if result[0][0] > result[0][1]:
        st.write("結果は椎茸")

    else:
        st.write("結果は月夜茸")

    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write('※判断基準はあくまで目安です。誤認識する場合があります。')


    