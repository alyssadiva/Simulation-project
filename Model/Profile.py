#!/usr/bin/env python
# coding: utf-8

# In[7]:


"""
This module makes it possible to establish the different classes that bring together our profiles.
We will have the classes Home (for Home profiles) and Community (for profiles from the public or private community)/
which are daughter classes of User.
"""
import Model.Location
from Model.Location import *
from Model.Enum_profile import *


# class User:
#     def __init__(self, supplier, local, load_curve):
#         self.supplier = supplier
#         # self.pays = location.get_pays()
#         # self.situation = location.get_situation()
#         self.location = local
#         self.load_curve = load_curve
#
#     # Getters (obtenir une information)
#     def get_supplier(self):
#         return self.supplier
#
#     def get_location(self):
#         return self.location
#
#     def get_curve(self):
#         return self.load_curve
#
#     # setters (modifier une information)
#     def set_supplier(self, supplier):
#         self.supplier = supplier


class Foyer():
    def __init__(self, supplier, location, load_curve, number_Person, profil):
        self.number_Person = number_Person
        self.profil_foyer = profil
        self.supplier = supplier
        # self.pays = location.get_pays()
        # self.situation = location.get_situation()
        self.location = location
        self.load_curve = load_curve
        # Getters (obtenir une information)

    def get_supplier(self):
        return self.supplier

    def get_location(self):
        return self.location

    def get_curve(self):
        return self.load_curve

        # setters (modifier une information)

    def set_supplier(self, supplier):
        self.supplier = supplier

    def get_number_Person(self):
        return self.number_Person

    def get_profil_foyer(self):
        return self.profil_foyer

    def goto(self):
        return self.location.get_pays

    @property
    def coupleMultiplier(self):
        if self.number_Person == 2:
            return 0.75
        else:
            return 0

    def Iscouple(self):
        if self.number_Person == 2:
            return "couple"
        else:
            return "Famille"


class Community(Foyer):
    def __init__(self, supplier, location, load_curve, number_Person, profil):
        super().__init__(supplier, location, load_curve)
        self.profil_coll = profil

# user1 = Localisation( "Chine", " North")
# user = Foyer("ED", user1,"Oui" ,3, Foyer_profil(3).name)

# print(user.location.situation)

# col_profil = Collectivite_profil(2).name
# user = Collectivité("ED", "n", col_profil)
# print(user.profil_coll)


# In[ ]:
