class Country:
    def __init__(self,cName="",cPopulation=0,sqMile=0,cDensity=0):
        self.cName=cName
        self.cPopulation=cPopulation
        self.sqMile=sqMile
        self.cDensity=cDensity
    def Destiny(self):
        return self.cPopulation/self.sqMile
    def Record(self, cName,cPopulation,sqMile):
        self.cName=cName
        self.cPopulation=cPopulation
        self.sqMile=sqMile
        self.cDensity=self.Destiny()
    def prints(self):
        print("Country Name:",self.cName)
        print("Population Number:",self.cPopulation)
        print("Miles:",self.sqMile)
        print("Density:",self.cDensity)
call=Country()
call.Record("Canada", 1000,10)
call.prints()


