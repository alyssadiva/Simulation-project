#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Location:

    def __init__(self, country, situation):
        self.country = country
        self.situation = situation

    # Getters
    def get_pays(self):
        return self.country

    def get_situation(self):
        return self.situation

    # setters
    def set_pays(self, country):
        self.country = country

    def habiter(self):
        print("Live in ", self.situation)

    @property
    def multiplier(self):
        return {
            'Northeast': {
                'production': 0.87
            },
            'Southeast': {
                'production': 1
            },
            'Southwest': {
                'production': 0.94
            },
            'Diagonale': {
                'production': 0.90
            },
        }[self.situation]


# In[ ]:

print('TEST')
l = Location('France', 'Northeast')
print(l.multiplier['production'])
