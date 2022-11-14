#import matplotlib.pyplot as plt

def switch():
    img_path = 'images/test.png'

def switch():
    print("Press 1 for Translation \nPress 2 for Resizing \nPress 3 for Rotation \nPress 4 for Sheared images \n")
 
    option = int(input("your option : "))
    print("\n")
 
 
    if option == 1:
        print("Translation")
 
    elif option == 2:
        print("Resizing")
 
    elif option == 3:
        print("Rotation")
    
    elif option == 4:
        print("Sheard images")
 
    else:
        print("Incorrect option")


"""Exécution du script"""
if __name__ == "__main__":
    switch()