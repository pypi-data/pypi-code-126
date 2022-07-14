"""
    Filename    :   conversions.py
    Description :   Part of EtherChainPy
    By          :   Emmanuel Adigun (emmanuel@zignal.net)
    Date        :   10 May 2022
"""
import json

class Conversions(object):
    """
    Conversion Module ...
    """
    def __init__(self):
        self.math_base = 10
        self.response = None

    def to(self, what):
        w = what.upper()
        if w   == "WEI": return self.toWEI()
        elif w == "GWEI": return self.toGWEI()
        elif w == "ETH": return self.toETH()
        elif w == "ZAR": return self.toZAR()
        elif w == "USD": return self.toUSD()
        elif w == "EUR": return self.toEUR()
        else: return self.toJSON()

    def toJSON(self):
        if self.response: return self.response.json()
        else: return None

    def toWEI(self):
        wei = None
        if self.response:
            data = self.response.json()
            if "result" in data: 
                rd = data["result"]
                if isinstance(rd,str):
                    wei = int(data["result"],self.math_base)
                elif isinstance(rd,list):
                    wei = []
                    for r in rd: 
                        r.update({"wei": int(r["balance"],self.math_base) })
                        wei.append(r)

        return wei

    def toGWEI(self):
        gwei = None
        if self.response:
            data = self.response.json()
            if "result" in data: 
                rd = data["result"]
                if isinstance(rd,str):
                    gwei = int(data["result"],self.math_base)/(10**9)
                elif isinstance(rd,list):
                    gwei = []
                    for r in rd: 
                        r.update({"gwei": int(r["balance"],self.math_base)/(10**9) })
                        gwei.append(r)
        return gwei

    def toETH(self):
        eth = None
        if self.response:
            data = self.response.json()
            if "result" in data: 
                rd = data["result"]
                if isinstance(rd,str):
                    eth = int(data["result"],self.math_base) / (10**18)
                elif isinstance(rd,list):
                    eth = []
                    for r in rd: 
                        r.update({"eth": int(r["balance"],self.math_base)/(10**18) })
                        eth.append(r)
        
        return eth

    def toFIAT(self, currency="ZAR"):
        pass


    def toZAR(self):
        return self.toFIAT("ZAR")


    def toUSD(self):
        return self.toFIAT("USD")

    def toEUR(self):
        return self.toFIAT("EUR")






