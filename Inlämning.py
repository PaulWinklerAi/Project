import json     #Importerar JSON för användning.

class Uppgift:
        def __init__(self, beskrivning, klar=False):
                self.beskrivning = beskrivning  #Beskriver uppgiften du ska ha på checklistan.
                self.klar = klar    #Om uppgiften är klar eller inte.

        def markera_klar(self):
            self.klar = True    #Markerar en uppgift som klar.
        
        def till_dict(self):    #För att spara i JSON så konverteras uppgiften till en ordlista.
            return {'beskrivning': self.beskrivning, 'klar': self.klar}
        
        @classmethod
        def från_dict(cls, data):  #För att skapa en uppgift från ordlistan i JSON.
            return cls(data['beskrivning'], data['klar'])
        
class Uppgiftshanterare:    
    def __init__(self, filnamn='uppgifter.json'):
         self.filnamn = filnamn     #Filen som uppgifterna sparas i.
         self.uppgifter =[]     #Alla uppgifter i en lista.
         self.ladda_uppgifter()     #Uppgifterna från filen kommer ladda när du startar programmet.

    def lägg_till_uppgift(self, beskrivning):       #Lägg till en ny uppgift på din lista.
         uppgift = Uppgift(beskrivning)
         self.uppgifter.append(uppgift)
         self.spara_uppgifter()     #Sparar dina uppgifter.

    def ta_bort_uppgift(self, index):       #Ta bort en uppgift, genom val av index.
         if 0 <= index < len(self.uppgifter):
              del self.uppgifter[index]
              self.spara_uppgifter()        #Sparar ändringarna efter du tagit bort en uppgift.
            
    
    def markera_uppgift_klar(self, index):      #Markera en uppgift som klar, genom val av index.
         if 0 <= index < len(self.uppgifter):
              self.uppgifter[index].markera_klar()
              self.spara_uppgifter()        #Sparar ändringarna efter du markerat en uppgift som klar.

    def ladda_uppgifter(self):      #Om det finns, laddas uppgifterna från JSON.
        try: 
            with open(self.filnamn, 'r') as fil:
                    uppgifter_data =json.load(fil)
                    self.uppgifter = [Uppgift('', '').från_dict(uppgift) for uppgift in uppgifter_data]
        except FileNotFoundError:
             self.uppgifter = []        #Om ingen fil skulle hittas så startar man med en tom lista.

    def spara_uppgifter(self):      #Sparar alla dina uppgifter i JSON.
         with open(self.filnamn, 'w') as fil:
              json.dump([uppgift.till_dict() for uppgift in self.uppgifter], fil, indent=4)

    def visa_uppgifter(self):       #Visar alla uppgifter som inte är genomförda.
         index = 0      #Håller reda på indexet genom att initiera en variabel.
         for uppgift in self.uppgifter:
              status = "Klar" if uppgift.klar else "Ej klar"
              print(f"{index + 1}. {uppgift.beskrivning} - {status}")   #Informerar om beskrivning och status av upgiften.
              index += 1

def main():
        hanterare = Uppgiftshanterare()

        while True:
              print("\n1. Lägg till Uppgift")
              print("2. Ta bort uppgift")
              print("3. Markera uppgift som klar")
              print("4. Visa alla uppgifter")
              print("5. Avsluta")

              val = input("Välj ett alternativ (1-5): ")

              if val == '1':        #Lägger till en ny uppgift.
                   beskrivning = input("Ange beskrivning av uppgiften: ")
                   hanterare.lägg_till_uppgift(beskrivning)
              elif val =='2':       #Tar bort en uppgift
                   hanterare.visa_uppgifter()
                   index = int(input("Ange nummer på uppgiften du vill ta bort: ")) - 1
                   hanterare.ta_bort_uppgift(index)
              elif val == '3':      #Markerar en uppgift som klar
                   hanterare.visa_uppgifter()
                   index = int(input("Ange nummer på uppgiften som är klar: ")) - 1
                   hanterare.markera_uppgift_klar(index)
              elif val =='4':       #Visar alla dina uppgifter
                   hanterare.visa_uppgifter()
              elif val =='5':       #Avslutar uppgiftshanteraren.
                   print("Programmet avslutas...")
                   break
              else:
                   print("Ogiltig siffra, vänligen försök igen.")

if __name__ == '__main__':
        main()