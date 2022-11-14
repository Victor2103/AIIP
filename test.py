import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

mario=Image.new("RGB",(8,8),"white")  

translation=Image.new("RGB",(10,10),"white")

for i in range


# Create the red, blue and green color
R = [255, 0, 0]
G = [0, 255, 0]
B = [0, 0, 255]
# Create the RGB first table
RGB = np.array([[G, B, R], [B, R, G], [R, G, B]], dtype=np.uint8)
# Disp the RGB first table
plt.imshow(RGB)
plt.show()