class EmobilisStudent:
    def __init__(self , name, age):
        self.name= name
        self.age= age
    def hello_me(self):
        print(f"My name is {self.name} and i'm {self.age}years old")


#creating an object
myobj=EmobilisStudent("Joy",18)
myobj.hello_me()

myobj=EmobilisStudent("Carol",18)
myobj.hello_me()

class magari:
    def __init__(self,mode,make,year,properties):
        self.mode=mode
        self.make=make
        self.year=year
        self.properties=properties
    def hello_me(self):
        print(f"I bought a{self.mode} car, a {self.make}, in {self.year} that is {self.properties}")


myobj=magari(" nautomatic drive","ferrari",2016,"the fastest thing i own")
myobj.hello_me()
myobj=magari("manual drive","volvo","2005","blue in color")
myobj.hello_me()
myobj=magari("nautomatic drive","nissan","2015","that is very reliable")
myobj.hello_me()


class nguo:
    def __init__(self,type,size):
        self.type=type
        self.size=size
    def hello_me(self):

        print( f"clothes:{self.type}.are available at a size {self.size} in all leading boutique outlets")

myobj=nguo("crotchet tops",38)
myobj.hello_me()

myobj=nguo("backless dresses","32")
myobj.hello_me()