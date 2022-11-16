import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

mario = Image.new("RGB", (8, 8), "white")

test = Image.open("../images/test.png")
print(test.size[0])
# test.show()

var = 3.5


translation = Image.new("RGB", (int(var*test.size[0])+1, test.size[1]), "white")
rouge = (255, 0, 0)

print(test.getpixel((5, 5)))


for i in range(test.size[0]):
    for j in range(test.size[1]):
        translation.putpixel((int(var*i), j), test.getpixel((i, j)))


translation.show()
test.show()


'''
# Create the red, blue and green color
R = [255, 0, 0]
G = [0, 255, 0]
B = [0, 0, 255]
# Create the RGB first table
RGB = np.array([[G, B, R], [B, R, G], [R, G, B]], dtype=np.uint8)
# Disp the RGB first table
plt.imshow(RGB)
plt.show()
'''
