#!/usr/local/bin/python3


class Produs(object):
    
    def __init__(self):
        self._nume = ""
        self._um = ""
        self._cantitate = ""
        self._pret_unitar = ""
        self._valoare = ""
        self._valoare_tva = ""

    def __str__(self):
        return ' | '.join(self.__dict__.values()[::-1])

    def set_nume(self, nume):
        self._nume = nume

    def set_um(self, um):
        self._um = um

    def set_cantitate(self, cantitate):
        self._cantitate = cantitate

    def set_pret_unitar(self, pret_unitar):
        self._pret_unitar = pret_unitar

    def set_valoare(self):
        assert self._cantitate != ""
        assert self._pret_unitar != ""
        
        self._valoare = str(float(self._cantitate) * float(self._pret_unitar))
    
    def set_valoare_tva(self, cota_tva):
        assert self._valoare != ""
        assert cota_tva[-1] == "%"
        
        self._valoare_tva = str(float(self._valoare) * int(cota_tva[:-1]) / 100)


if __name__ == "__main__":
    prod = Produs()
    prod.set_nume("Test")
    prod.set_um("BUC")
    prod.set_cantitate("0.15")
    prod.set_pret_unitar("10")
    prod.set_valoare()
    prod.set_valoare_tva("19%")

    print(prod)
