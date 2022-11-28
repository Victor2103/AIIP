from PIL import Image

def resize():
    test = Image.open("./images/test.png")
    # test.show()

    print("Entrez un rapport d'homothétie verticale puis horizontale !")
    verticale = float(input("Verticale : "))
    horizontale = float(input("Horizontale : "))


    resizing = Image.new(
        "RGB", (int(horizontale*test.size[0])+1, int(verticale*test.size[1])+1), "white")
    resizing2 = Image.new(
        "RGB", (int(horizontale*test.size[0])+1, int(verticale*test.size[1])+1), "white")


    for i in range(test.size[0]):
        for j in range(test.size[1]):
            resizing.putpixel(
                (int(horizontale*i), int(verticale*j)), test.getpixel((i, j)))


    for i in range(resizing.size[0]):
        for j in range(resizing.size[1]):
            if resizing.getpixel((i, j)) == resizing2.getpixel((i, j)):
                resizing.putpixel((i, j), resizing.getpixel((i-1, j-1)))


    resizing.show()
    test.show()


