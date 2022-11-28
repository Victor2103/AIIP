from Resizing.resizing import resize
from Resizing.aliasing import aliasing
from Cisaillement.cisaillement import cisaille
from Rotation.rotation import rotatation
from Translation.translation import translation

def switch():
    img_path = 'images/test.png'

def switch():
    print("Press 1 for Translation \nPress 2 for Resizing \nPress 3 for Rotation \nPress 4 for Sheared images \n Press 5 for Aliasing demonstration")
 
    option = int(input("your option : "))
    print("\n")
 
 
    if option == 1:
        translation()
 
    elif option == 2:
        resize()
 
    elif option == 3:
        rotatation()
    
    elif option == 4:
        cisaille()

    elif option == 5:
        aliasing()
 
    else:
        print("Incorrect option")


"""Exécution du script"""
if __name__ == "__main__":
    switch()