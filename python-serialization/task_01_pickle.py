#!/usr/bin/python3
"""contains the Pickling Custom Classes"""


import pickle


class CustomObject:
    """custom class"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """ method display """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("Is Student: {self.is_student}")

    def serialize(self, filename):
        """method ser"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"An error serializing {e}")

    @classmethod
    def deserialize(cls, filename):
        """class method """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                else:
                    print("Deserialized object is not of type CustomObject.")
                    return None
        except Exception as e:
            print(f"An error occurred while deserializing the object: {e}")
            return None
