class Pizza:
   
    precio = 10000
    tipos_masa = ['tradicional','delgada']
    vegetales  = ['tomate', 'aceitunas', 'champiñones']
    proteicos  = ['pollo', 'vacuno', 'carne vegetal']
    
    @staticmethod
    def validar(texto,valores_posibles ):
        return texto in valores_posibles
    
    def pedido(self):
        
        self.masa = str(input("Ingrese el tipo de masa ( tradicional o delgada) : ")).lower()             
        self.proteico_1  = str(input("Ingrese el ingrediente proteico (pollo,vacuno o carne vegetal ) : ")).lower()
        self.vegetal_1 = str(input("Ingrese el 1° ingrediente vegetal (tomate, aceitunas, champiñones) : ")).lower()                        
        self.vegetal_2 = str(input("Ingrese el 2° ingrediente vegetal (tomate, aceitunas, champiñones) : ")).lower()
        
        if self.validar(self.masa,self.tipos_masa) and self.validar(self.proteico_1,self.proteicos) and self.validar(self.vegetal_1,self.vegetales) and self.validar(self.vegetal_2,self.vegetales):
            self.validacion = True
        else:
            self.validacion = False
        
    
        
        
        