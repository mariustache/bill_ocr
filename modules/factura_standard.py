#!/usr/local/bin/python3


class FacturaStandard(object):

    def __init__(self):
        self._furnizor = ""
        self._numar = ""
        self._data = ""
        self._delegat = ""
        self._auto = ""
        self._lista_produse = list()
        self._cota_tva = ""
        self._total = ""

    def set_furnizor(self, furnizor):
        self._furnizor = furnizor
    
    def set_numar(self, numar):
        self._numar = numar
    
    def set_data(self, data):
        self._data = data
    
    def set_delegat(self, delegat):
        self._delegat = delegat

    def set_auto(self, auto):
        self._auto = auto
    
    def set_cota_tva(self, cota_tva):
        self._cota_tva = cota_tva
    
    def set_total(self, total):
        self._total = total



