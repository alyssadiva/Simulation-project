"""
This module allows you to perform operations from each Calculation Class (for the network)/
and Beoga Class (for the beoga offer)which is a daughter class.
"""
from Data import *
import Model.Profile as Profile
import matplotlib.pyplot as plt
from matplotlib import pyplot


class Calculation:
    def __init__(self, cout_by_kwh, capa_pv, p: Profile.Foyer):
        self.cout_by_kwh = cout_by_kwh
        self.capa_pv = capa_pv
        self.profile = p

    # Getters 
    def get_p(self):
        return self.profile

    def get_cout_by_kwh(self):
        return self.cout_by_kwh

    def resultat_profil_A(self):
        """
        This function determines the results (consumption, bill) of a profile A /
        (does not produce any electricity and does not store either/it is a standard profile) /
        that is on the grid.
        """
        conso = data['Conso_inactif'] * self.profile.coupleMultiplier
        conso_total = sum(conso)

        bill = self.cout_by_kwh * conso_total

        # Curve
        pyplot.figure(figsize=(12, 6))
        pyplot.title("semaine d'hiver")
        pyplot.xlabel('Date', fontsize=18)
        pyplot.ylabel('consommation (kWh)', fontsize=18)
        g = data['Conso_inactif']
        d = g['1 jan 2020': '15 jan 2020']
        pyplot.plot(d, lw=1)

        return conso, conso_total, bill

    # Valeur monétaire énergétique
    def total_energy_value_sale(self, sale, bill, subscription, production_Total, production_price):
        """
        Function that calculates the financial energy value that could be won or lost by the consumer.
        """
        cout_production = production_Total * production_price
        val = sale - (bill + cout_production + subscription)
        return val

    def energy_value_injection(self, bill, subscription, surplus_Total, injection_price):
        """
        Function that calculates the financial energy value that could be won or lost by the consumer.
        """
        cout_injection = surplus_Total * injection_price
        val = cout_injection - (bill + cout_injection + subscription)
        return val


class Beoga(Calculation):
    """
    Daughter class of the Calculation class/
    which is differentiated by the different costs on the market.
    """

    def __init__(self, cout_by_kwh, capa_pv, p: Profile.Foyer):
        super().__init__(cout_by_kwh, capa_pv, p)


"""
user1 = Localisation( "France", "Southeast")
p = Foyer("EDF", user1,"Actif", 2, "profil_foyer")      
calcul = Calculation(0.157,6,p)  
x = 0.08 
prix_production = 0.1
prix_injection = 0.09
abonnement = 120
print(calcul.resultat_profil_B(x, abonnement))
"""
