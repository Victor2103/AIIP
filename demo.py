import numpy as np
from PIL import Image
import math


test = Image.open("images/test.png")

horizontale=1
verticale=2

translation = Image.new(
    "RGB", (int(horizontale*test.size[0])+1, int(verticale*test.size[1])+1), "white")
translation2 = Image.new(
    "RGB", (int(horizontale*test.size[0])+1, int(verticale*test.size[1])+1), "white")


for i in range(test.size[0]):
    for j in range(test.size[1]):
        translation.putpixel(
            (int(horizontale*i), int(verticale*j)), test.getpixel((i, j)))


for i in range(translation.size[0]):
    for j in range(translation.size[1]):
        if translation.getpixel((i, j)) == translation2.getpixel((i, j)):
            translation.putpixel((i, j), translation.getpixel((i-1, j-1)))


translation.show()
test.show()


degre=30
im_array = np.array(test)

# Calcul the matrix of the rotation
R = np.zeros((2, 2))
radian = degre*3.1415/180
R[0, 0] = math.cos(radian)
R[1, 1] = math.cos(radian)
R[0, 1] = -math.sin(radian)
R[1, 0] = math.sin(radian)
# Calcul the new coordinates
new_coord = np.zeros((im_array.shape[0], im_array.shape[1], 2))
coord = np.zeros((2, 1))

centrex = im_array.shape[0]/2
centrey = im_array.shape[1]/2

for i in range(im_array.shape[0]):
    for j in range(im_array.shape[1]):
        coord[0, 0] = i-centrex
        coord[1, 0] = j-centrey
        prod = np.dot(R, coord)
        new_coord[i, j] = (int(prod[0, 0])+centrex, int(prod[1, 0])+centrey)

rotation = Image.new("RGBA", (im_array.shape[0], im_array.shape[1]), "white")

rotation_arr = np.array(rotation)


for i in range(new_coord.shape[0]):
    for j in range(new_coord.shape[1]):
        if (new_coord[i, j, 0] < rotation_arr.shape[0] and new_coord[i, j, 0] > 0 and new_coord[i, j, 1] < rotation_arr.shape[1] and new_coord[i, j, 1] > 0):
            rotation_arr[int(new_coord[i, j, 0]), int(
                new_coord[i, j, 1])] = im_array[i, j]

rotation = Image.fromarray(rotation_arr)

rotation.show()

gauche=50
droite=0
translation=Image.new("RGBA", (im_array.shape[0]+gauche, im_array.shape[1]+droite), "white")
translation_arr=np.array(translation)
for i in range(im_array.shape[0]):
    for j in range(im_array.shape[1]):
        if (i+gauche<translation_arr.shape[0]) and (j+droite<translation_arr.shape[1]):
            translation_arr[i+gauche,j+droite]=im_array[i,j]

translation=Image.fromarray(translation_arr)

translation.show()