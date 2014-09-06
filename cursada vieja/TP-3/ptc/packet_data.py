# -*- coding: utf-8 -*- 
# # # # # # # # # # # # # # # # # # # # #
#                                       #                                       
#    Trabajo Práctico 3 - Conexiones    # 
#                                       #
#     Teoría de las Comunicaciones      #
#      Departamento de Computación      #
#              FCEN - UBA               #
#            junio de 2013              #
#                                       #
# # # # # # # # # # # # # # # # # # # # #
class DataPacket(object):
    
    KB = 1000
    
    def __init__(self, size = 0):
        self.data = ""
        self.__build(size)
            
    def __build(self, size):
        if (size > 0):
            i = 0
            for i in range(size * self.KB):
                new_data = "x"
                if (i % 100 == 0):
                    new_data = "\n"
                    i = i + 1
                self.data = self.data + new_data
                i = i + 1
        else:
            self.data = ""
        
    def get_data(self):
        return self.data
    
    def size(self):
        return len(self.data)
    
    def sizeKb(self):
        return self.size() / 1000
    
if __name__ == "__main__":
    #data = DataPacket(5)
    #print data.size()
    #print "data: " + data.get_data()
    #data = DataPacket()
    #print data.size()
    #print "data: " + data.get_data()
    data = DataPacket(1)
    print data.size()
    print "data: " + data.get_data()
    