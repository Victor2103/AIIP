import numpy as np
from PIL import Image

def translation():
    test = Image.open("./images/test.png")
    # test.show()

    print("Entrez la translation horizontale puis verticale !")
    droite = float(input("Horizontale : "))
    gauche = float(input("Verticale : "))


    im_array = np.array(test)


    translation=Image.new("RGBA", (im_array.shape[0]+int(gauche), im_array.shape[1]+int(droite)), "white")
    translation_arr=np.array(translation)
    for i in range(im_array.shape[0]):
        for j in range(im_array.shape[1]):
            if (i+gauche<translation_arr.shape[0]) and (j+droite<translation_arr.shape[1]):
                translation_arr[i+int(gauche),j+int(droite)]=im_array[i,j]

    translation=Image.fromarray(translation_arr)

    translation.show()
    test.show()