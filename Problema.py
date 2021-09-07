import time
import datetime

class Empresa():
  def __init__(self,dep:list,emp:list,dir:str,tlf:str,rs:str,ruc:str):
    self.emp = Empleado(emp[0],emp[1],emp[2],emp[3]) # empleado; espera una lista con los valores [id,nom,sl,fr]
    self.dep = Departamento(self.emp,dep[0],dep[1]) # departamento; espera una lista con los valores [id,desp]
    self.dir = dir # direccion
    self.tlf = tlf # telefono
    self.rs = rs # razon social
    self.ruc = ruc # ruc
  def __str__(self):
    return f'Empresa\n{self.dep}'

"""## **EMPLEADO**"""

class Empleado():
  def __init__(self,id:int,nom:str,sl:int,fr:str):
    self.id = id # id
    self.nom = nom # nombre
    self.sl = sl # sueldo
    self.fr = fr # fecha de ingreso
  def MostrarEmpleado(self):
    return f'Nombre: {self.nom} Sueldo: {self.sl} Fecha de ingreso: {self.fr}'

"""## **DEPARTAMENTO**"""

class Departamento():
  def __init__(self,emp,id:int,desp:str):
    self.emp = emp # empleado
    self.id = id # id
    self.desp = desp # descripcion
  def __str__(self):
    return f'Departamento:\nid: {self.id} \nEmpleado: {self.emp.MostrarEmpleado()} \nDescripcion: {self.desp}'

"""## **OBRERO**"""

class Obrero(Empleado):
 def __init__(self,sin:bool,con:bool):
    self.sin = sin # sindicato
    self.con = con # contrato colectivo

"""## **ADMINISTRATIVO**"""

class Administrativo(Empleado):
  def __init__(self,com):
    self.com = com # comision

"""## **SOBRETIEMPO**"""

class SobreTiempo():
  def __init__(self,hr:float,he:float,emp,fc:str,id:int,est:bool):
      self.hr = hr # horas recargo
      self.he = he # horas extraordinarias
      self.emp = emp # empleado
      self.fc = fc # fecha
      self.id = id # id
      self.est = est # estado

"""## **PRESTAMO**"""

class Prestamo():
  def __init__(self,fc:str,vl:float,np:int,co:float,id:int,emp,sa:float,est:bool):
    self.fc = fc # fecha
    self.vl = vl # valor
    self.np = np # numero pagos
    self.co = co # cuota
    self.id = id # id
    self.emp = emp # empleado
    self.sa = sa # saldo
    self.est = est # estado

"""## **NOMINA**"""

class Nomina():
  def __init__(self,id:int,emp,fc:str,sb,dec,pres):
    self.id = id # id
    self.emp = emp # empleado
    self.fc = fc # fecha
    self.sl = emp.sl # sueldo
    self.vh = (self.sl/240)
    self.sb = self.vh*(sb.hr*0.5+sb.he*2)  # sobretiempo
    self.com = dec.com*self.sl # comision
    # =======
    form = '%d-%m-%Y'
    d1 = datetime.datetime.strptime(self.fc,form)
    d2 = datetime.datetime.strptime(emp.fr,form)
    dt = d1 - d2
    dt = int(dt.days)
    # =======
    self.ant = dec.ant*(dt)/365*self.sl # antiguedad
    self.iess = dec.iess*(self.sl + self.sb) # iess
    self.pres = pres.co # prestamo
    self.ti = self.sl + self.sb + self.com + self.ant # toting
    self.td = self.iess + self.pres # totdes
    self.lq = self.ti - self.td # liquidoRecibir

  def __str__(self):
    return f'''id: {self.id}\nEmpleado: {self.emp.nom}\nSueldo: {self.sl}
    \nValor por hora: {self.vh}\nSobretiempo: {self.sb}\nComision: {self.com} 
    \nAntiguedad: {self.ant}\nIess: {self.iess}\nPrestamo: {self.pres}
    \nToting: {self.ti}\nTotdes: {self.td}\nLiquidoRecibir: {self.lq}
    '''
  def NewOperation(self):
    pass

"""## **DEDUCCION**"""

class Deduccion():
  def __init__(self,iess:float,com:int,ant:float):
    self.iess = iess # iess
    self.com = com # comision
    self.ant = ant # antiguedad

"""# **FLUJO DEL PROGRAMA**

**DATOS DEL EMPLEADO**
"""

ide = int(input('id empleado: '))
nom = input('Nombre: ')
sueldo = int(input('Sueldo: '))
fi = input('Fecha de ingreso: ')

"""**DATOS DE SOBRETIEMPO**"""

hr = float(input('Horas de recargo: '))
he = float(input('Horas extraordinarias: '))
fs = input('Fecha de sobretiempo: ')
ids = int(input('id sobretiempo: '))
estado = input('Estado(V/F): ')
if estado == 'V':
  estado = True
else:
  estado = False

"""**DATOS DE DEDUCCION**"""

iess = float(input('% iess: '))
com = int(input('Comision: '))
ant = float(input('Antiguedad: '))

"""**DATOS DE PRESTAMO**"""

fp = input('Fecha del prestamo: ')
vp = float(input('Valor del prestamo: ')) 
np = int(input('Numero de pagos: '))
co = float(input('Cuota: '))
idp = int(input('id prestamo: '))
sa = float(input('Saldo: '))
estadop = input('Estado(V/F): ').lower()
if estadop == 'V':
  estadop = True
else:
  estadop = False

"""**DATOS DE NOMINA**"""

idn = int(input('id nomina: '))
fn = input('Fecha de nomina: ')

emp = Empleado(ide,nom,sueldo,fi)
sb = SobreTiempo(hr,he,emp,fs,ids,estado)
dep = Deduccion(iess,com,ant)
pres = Prestamo(fp,vp,np,co,idp,emp,sa,estadop)
n1 = Nomina(idn,emp,fn,sb,dep,pres)
print(n1)