#!/usr/bin/python3
"""Module contenant la classe Square."""


class Square:
    """Classe représentant un carré."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise un carré avec une taille optionnelle."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Obtient la taille du carré."""
        return self._size

    @size.setter
    def size(self, value):
        """Définit la taille du carré avec des vérifications."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """obtient la position du carre"""
        return self._position

    @position.setter
    def position(self, value):
        """Définit la position du carré avec des vérifications."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Calcule et retourne l'aire du carré."""
        return (self._size ** 2)

    def my_print(self):
        """imprimer la valeur de la taille"""
        if self._size == 0:
            print("")
            return
        for _ in range(self._position[1]):
            print("")
        for _ in range(self._size):
            print(" " * self._position[0] + "#" * self._size)
