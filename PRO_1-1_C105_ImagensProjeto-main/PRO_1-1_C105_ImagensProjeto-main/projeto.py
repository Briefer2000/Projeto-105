import os
import cv2

path = "C:/Users/marcy/Downloads/PRO_1-1_C105_ImagensProjeto-main/PRO_1-1_C105_ImagensProjeto-main/Imagems"
Images = []

for file in os.listdir(path):
    filename, file_extension = os.path.splitext(file)
    if file_extension.lower() in ['.jpg', '.jpeg', '.png']:
        file_name = path + "/" + file
        print(file_name)
        Images.append(file_name)

count = len(Images)
frame = cv2.imread(Images[0])
width, height, channels = frame.shape
size = (width, height)
print(size)

out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count):
    image = cv2.imread(Images[i])
    out.write(image)

out.release()
print("Concluído")