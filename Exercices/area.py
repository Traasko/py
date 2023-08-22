def square_area(length, width):
    return length * width

width = float(input("Entrez la largeur du rectangle : "))
length = float(input("Entrez la hauteur du rectangle : "))

area = square_area(length, width)

print("L'aire du rectangle est :", area)
