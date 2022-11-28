from PIL import Image

test = Image.open("../images/test.png")
# test.show()

print("Entrez un rapport d'homothétie verticale puis horizontale !")
verticale = float(input("Verticale : "))
horizontale = float(input("Horizontale : "))


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


