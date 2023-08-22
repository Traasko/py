class Chain:
    def __init__(self, content):
        self.content = content
        self.next = None

    def append(self, content):
        current = self
        while current.next is not None:
            current = current.next
        current.next = Chain(content)

    def pop(self):
        if self.next is None:
            raise ValueError("La liste chaînée est vide.")
        
        current = self
        while current.next.next is not None:
            current = current.next
        removed_content = current.next.content
        current.next = None
        return removed_content

    def display(self):
        current = self
        while current is not None:
            print(current.content, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    liste_chaine = Chain("Première cellule")
    liste_chaine.append("Deuxième cellule")
    liste_chaine.append("Troisième cellule")

    print("Liste chaînée initiale :")
    liste_chaine.display()

    liste_chaine.pop()
    print("\nListe chaînée après suppression :")
    liste_chaine.display()
