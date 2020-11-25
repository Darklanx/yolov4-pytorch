#-------------------------------------#
#       对单张图片进行预测
#-------------------------------------#
import glob
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from yolo import YOLO
from PIL import Image
import os
import json
TEST_DIR = "./dataset/test"
yolo = YOLO()


answer = []
for i, f in enumerate(sorted(glob.glob(os.path.join(TEST_DIR, "*.png")), key=lambda x: int(x.split('/')[-1].split('.')[0]))):
    image = Image.open(f)
    r_image, prediction = yolo.detect_image(image)
    prediction['id'] = i+1
    # print(f)
    # print(prediction)
    answer.append(prediction)
    if i < 10:
        r_image.save("./result/{}.jpg".format(i+1))
    if i % 100 == 0:
        print(i)
with open('0616215.json', 'w') as outfile:
    json.dump(answer, outfile)
exit()


# img = 
# while True:
    # img = input('Input image filename:')
img = 'dataset/test/1.png'
try:
    image = Image.open(img)
except:
    print('Open Error! Try again!')
else:
    r_image = yolo.detect_image(image)
    # print(type(r_image))
    r_image.save("a.jpg")
    # r_image.show()
