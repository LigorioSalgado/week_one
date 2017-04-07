class Robot:
  
    
    def __init__(self,name=None,lastname=None,age=None,*args,**kargs):
        self.name = name
        self._lastname = lastname
        self.__age = age
    

    def getAge(self):
        return self.__age
    
    
    def setAge(self,age):
        self.__age = age
    
    def Saluda(self):
        return "Hola mi nombre es %s y tengo %s años" % (self.name,str(self.__age))

    def __str__(self):
        return "Este es un objeto robot llamado : %s" % self.name

    def __repr__(self):
        
        return "Robot(name=%s, lastname=%s, age=%s) " % (self.name,self._lastname,self.__age)

    def __del__(self):
        texto = "Objeto Destruido llamado:%s" % (self.name)
        print(texto)

if __name__ == '__main__':
     
     robot = Robot("Edwin","Salgado",23)
     robot1 = Robot("Luis","Torres",29)
     age = robot.getAge()
     robot.setAge(12)
     print(str(robot))
     print(robot1)
     print(repr(robot1))
     '''
     print(robot.__dict__)
     dic = robot.__dict__.copy()
     dic['Saludo'] = "Hola a todos"
     print(dic)
     print(robot.__dict__)
     print(robot.Saludo)
     print(robot._lastname)
     '''