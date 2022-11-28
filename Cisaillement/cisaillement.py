import numpy as np
from PIL import Image


test = Image.open("../images/test.png")
# test.show()

print("Entrez le vecteur de cisaillement de l'image !")
vecteur = float(input("Vecteur : "))


im_array = np.array(test)

# Calcul the matrix of the rotation
R = np.zeros((2, 2))
R[0, 0] = 1
R[1, 1] = 1
R[0, 1] = vecteur
R[1, 0] = 0
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

cisaillement = Image.new("RGBA", (im_array.shape[0], im_array.shape[1]), "white")

cisaillement_arr = np.array(cisaillement)


for i in range(new_coord.shape[0]):
    for j in range(new_coord.shape[1]):
        if (new_coord[i, j, 0] < cisaillement_arr.shape[0] and new_coord[i, j, 0] > 0 and new_coord[i, j, 1] < cisaillement_arr.shape[1] and new_coord[i, j, 1] > 0):
            cisaillement_arr[int(new_coord[i, j, 0]), int(
                new_coord[i, j, 1])] = im_array[i, j]

rotation = Image.fromarray(cisaillement_arr)

rotation.show()
