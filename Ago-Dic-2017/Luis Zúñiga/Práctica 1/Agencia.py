
class Agencia:
    """Class Agencia
    """
    # Campos:
    __nombre = ""  # (String)
    __direccion = ""  # (String)
    __numeroDeEmpleados = 0  # (int)
    __numeroDeClientes = 0  # (int)
    __empleados = []
    __clientes = []
    __autos = []
    __camiones = []
    __motos = []
    __dict_ventas = {'vendedor': 0, 'comprador':0, 'sku': 'valor'}
    __lista_ventas = []
    __totalCamiones = 0
    __totalAutos = 0
    __totalMotos = 0

    # Operations
    #Constructor
    def __init__(self, nombre='', direccion='', numeroDeEmpleados =0, numeroDeClientes=0):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__numeroDeEmpleados = numeroDeEmpleados
        self.__numeroDeClientes = numeroDeClientes
    
    #Métodos
    
    #Operaciones para Agencia
    
    def setNombre(self, nombre):       
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre
    
    def setDireccion(self,direccion):
        self.__direccion = direccion

    def getDireccion(self):
        return self.__direccion
    
    #Operaciones de compra y venta
    
    def ventaCamion(self,vendedor,comprador,sku):
        if self.buscaCamion(sku).getExistencias() > 0:
            self.__dict_ventas={'vendedor': vendedor, 'comprador': comprador, 'sku': sku}
            self.__lista_ventas.append(self.__dict_ventas)        
            self.bajaCamion(self.buscaCamion(sku))
            print('Un camion con sku ' + sku + ' ha sido vendido')
        else:
            print('Existencias agotadas.\nPor favor consulte el catálogo de existencias.')
    
    
    def ventaAuto(self,vendedor,comprador,sku):
        if self.buscaAuto(sku).getExistencias() > 0:
            self.__dict_ventas={'vendedor': vendedor, 'comprador': comprador, 'sku': sku}
            self.__lista_ventas.append(self.__dict_ventas)
            self.bajaAuto(self.buscaAuto(sku))
            print('Un automóvil con sku ' + sku + ' ha sido vendido')
        else:
           print('Existencias agotadas.\n Por favor consulte el catálogo de existencias.')
        
    
    
    def ventaMoto(self,vendedor,comprador,sku):
        
        if self.buscaMoto(sku).getExistencias() > 0:
            self.__dict_ventas={'vendedor': vendedor, 'comprador': comprador, 'sku': sku}
            self.__lista_ventas.append(self.__dict_ventas)
            self.bajaMoto(self.buscaMoto(sku))
            print('Una motocicleta con sku ' + sku + ' ha sido vendida')
        else:
            print('Existencias agotadas.\n Por favor consulte el catálogo de existencias.')
            
    def imprimeVentas(self):
        for i in self.__lista_ventas:
            print (i) 
   
    #operaciones para camiones    
    def altaCamion(self,camion):
        self.__camiones.append(camion)
        self.__totalCamiones = camion.getExistencias()
                
    def bajaCamion(self,camion):
        camion.reduceExistencias()
        self.__totalCamiones-=1
    
    def imprimeCamiones(self):
        for i in self.__camiones:
            print(i.datosDeCamion())

    def agregaCamion(self, sku, cantidad):
       if sku == self.buscaCamion(sku).getSku():
               self.buscaCamion(sku).aumentaExistencias(int(cantidad))
               self.__totalCamiones += int(cantidad)
               
    def buscaCamion(self,sku):
        for i in self.__camiones:
            if sku == i.getSku():
                return i
                break
                
    #operaciones para autos                    
    def altaAuto(self,auto):
        self.__autos.append(auto)
        self.__totalAutos = auto.getExistencias()
    
    def imprimeAutos(self):
        for i in self.__autos:
            print(i.datosDeAuto())
    
    
    def bajaAuto(self,auto):
        auto.reduceExistencias()
        self.__totalAutos-=1      
    
    def agregaAuto(self,sku,cantidad):
        if sku == self.buscaAuto(sku).getSku():
               self.buscaAuto(sku).aumentaExistencias(int(cantidad))
               self.__totalAutos += int(cantidad)           
            
    def buscaAuto(self,sku):
        for i in self.__autos:
            if sku == i.getSku():
                return i
                break
    
    #Operaciones para motos
    def altaMoto(self,moto):
        self.__motos.append(moto)
        self.__totalMotos = moto.getExistencias()
        
    def agregaMoto(self, sku, cantidad):
        if sku == self.buscaMoto(sku).getSku():
               self.buscaMoto(sku).aumentaExistencias(int(cantidad))
               self.__totalMotos += int(cantidad)
               
    def imprimeMotocicletas(self):
        for i in self.__motos:
            print(i.datosDeMoto())
                
    def bajaMoto(self, moto):
        moto.reduceExistencias()
        self.__totalMotos-=1
        
    def buscaMoto(self, sku):
        for i in self.__motos:
            if sku == i.getSku():
                return i
                break
                
    #Operaciones sobre clientes y empleados
    #Empleados   
    
        
    def bajaEmpleado(self, numeroDeEmpleado):
        self.__empleados.pop(numeroDeEmpleado-1)
        self.__numeroDeEmpleados-=1

    def aumentaEmpleados(self,empleado):
        self.__empleados.append(empleado)        
        self.__numeroDeEmpleados+=1        

    def getEmpleado(self,cant):
        print(cant)
        return self.__empleados[int(cant)-1].datosDeEmpleado()

    def getEmpleados(self):
        return self.__numeroDeEmpleados

    def imprimeEmpleados(self):
        for i in self.__empleados:
            print(i.datosDeEmpleado())
            
    def buscaEmpleados(self, numEmpleado):
        for i in self.__empleados:
            if i.getEmpleado() == numEmpleado:
                return True
                break
            else: return False            

    #clientes
    def bajaCliente(self, numeroDeCliente):
        self.__clientes[int(numeroDeCliente)-1] = None
    
    def getCliente(self, cant):
        return self.__clientes[int(cant)-1].datosDeCliente()

    def aumentaClientes(self,cliente):
        self.__clientes.append(cliente)
        self.__numeroDeClientes+=1

    def imprimeClientes(self):
        for i in self.__clientes:
            print(i.datosDeCliente())

    def getClientes(self):
        return self.__numeroDeClientes
 
            
    
   
    
    
         
            
   

