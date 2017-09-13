#Schrijf functie standaardprijs(afstandKM).
#  Iedere treinrit kost 80 cent per kilometer, maar als de rit langer is dan 50 kilometer betaal je een vast bedrag
#  van €15,- plus 60 cent per kilometer. Ga bij invoer van negatieve afstanden uit van een afstand van 0 kilometer (prijs is dan dus 0 Euro).

def standaardprijs(afstandKM):

    if afstandKM >= 50 :
        Prijs = (afstandKM * 0.60) + 15
    else :
        Prijs = (0.80 * afstandKM)
    return Prijs



#Op werkdagen reizen kinderen (onder 12 jaar) en ouderen (65 en ouder) met 30% korting. In het weekend reist deze
# groep met 35% korting. De overige leeftijdsgroepen reizen betalen de gewone prijs, behalve in het weekend, dan reist deze leeftijdsgroep met 40% korting.

def ritprijs(leeftijd, weekendrit, afstandKM):
    Varprijs = standaardprijs(afstandKM)
    weekendkortinggroepOUD = 0.65
    weekendkortingGroepNormaal = 0.60
    Weekdagengroep = 0.70
    if weekendrit == True:
        if leeftijd < 12 or leeftijd > 65 :
            VastPrijs1 = (Varprijs * weekendkortinggroepOUD)
            print (VastPrijs1)

        else:
            Vastprijs2 = (Varprijs * weekendkortingGroepNormaal)
            print(Vastprijs2)

    elif weekendrit == False :
        if leeftijd < 12 or leeftijd > 65 :
            VastPrijs3 = (Varprijs * weekendrit)
            print(VastPrijs3)
        else :
            print(Varprijs)


ritprijs(15,True,150)




