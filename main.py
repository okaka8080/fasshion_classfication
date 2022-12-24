from keras.models import load_model
import numpy as np
import sys
from PIL import Image

image_path = "./Images/parker.jpg" #画像パス
#画像のグレースケール化
im = Image.open(image_path)
if im.mode != "RGB":
    im = im.convert("RGB") # any format to RGB
rgb = np.array(im, dtype="float32")

rgbL = pow(rgb/255.0, 2.2)
r, g, b = rgbL[:,:,0], rgbL[:,:,1], rgbL[:,:,2]
grayL = 0.299 * r + 0.587 * g + 0.114 * b  # BT.601
gray = pow(grayL, 1.0/2.2)*255

im_gray = Image.fromarray(gray.astype("uint8"))

model = load_model('./model/fashion-classification.h5') # 保存したモデルから読み込む

gray_img = np.array(im_gray.resize((28, 28))) / 255 #画像のリサイズ

# Add the image to a batch where it's the only member.
gray_img = (np.expand_dims(gray_img,0))

#print(sumpleimg.shape)

predictions_single = model.predict(gray_img) #機械学習での予測(約88%) 0.8866999745368958

print(predictions_single)

print("結果")
print(np.argmax(predictions_single[0])) #ラベル表記