class Dom:
    def __init__(self):
        self.elementy = []
    
    def __str__(self):
        return f"posiada: {', '.join(self.elementy)}"

class BudowniczyDomu:
    def __init__(self):
        self.dom = Dom()

    def Zbuduj_Sciany(self):
        self.dom.elementy.append("Proste sciany")
        return self

    def Zbuduj_Drewniane_Drzwi(self):
        self.dom.elementy.append("Drewniane drzwi")
        return self    

    def Zbuduj_Metalowe_Drzwi(self):
        self.dom.elementy.append("Metalowe drzwi")
        return self

    def Wstaw_Zwykle_Okna(self):
        self.dom.elementy.append("Zwykle okna")
        return self

    def Wstaw_Duze_Okna(self):
        self.dom.elementy.append("Duze okna")
        return self

    def Buduj_Dach(self):
        self.dom.elementy.append("Dachówki z bakelitu")
        return self

    def Buduj_Dach_Premium(self):
        self.dom.elementy.append("Dachówki premium")
        return self
    
    def Wykop_Basen(self):
        self.dom.elementy.append("Basen olimpijski")
        return self
    
    def Buduj_Garaz(self): 
        self.dom.elementy.append("Garaż")
        return self

    def Wychoduj_Ogrod(self): 
        self.dom.elementy.append("Ogród")
        return self

    def Pobierz_Dom(self):
        return self.dom

domek = (BudowniczyDomu()
         .Zbuduj_Sciany()
         .Zbuduj_Drewniane_Drzwi()
         .Wstaw_Zwykle_Okna()
         .Buduj_Dach()
         .Pobierz_Dom())

willa = (BudowniczyDomu()
         .Zbuduj_Sciany()
         .Zbuduj_Metalowe_Drzwi()
         .Wstaw_Duze_Okna()
         .Buduj_Dach_Premium()
         .Wykop_Basen()
         .Buduj_Garaz()
         .Wychoduj_Ogrod()
         .Pobierz_Dom())

print("Wyposażenie domku:", domek)
print("Wyposażenie willi:", willa)