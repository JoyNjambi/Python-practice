#hello function
def hello():
    print("This is my first function")
hello()


#calculating function
def calculate():
    x=5
    y=9
    print(x*y)
calculate()


#names function
def majina(fname,lname):
    print(fname+"  "+lname)
majina("Joyangel","Njambi")
majina("Carol","Ndeti")
majina("Kidani","Kinoti")


#greetins function
def greetings(name,greeting="Hello"):
    print(greeting+"  "+name)
greetings("Martha")
greetings("Niaje","Stacy")
greetings("Joan","Niaje")




def jaribio(name,jina):
    print(name+" "+jina)
jaribio("Bata" ,"mzinga")
jaribio("Komba" ,"mwiko")



#maximun function
def maxvalue(a,b,c,d,e,f):
    return max(a,b,c,d,e,f)
result=maxvalue(7,9,1,8,19,45)
print(result)



#minimun function
def minvalue(a,b,c,d,e,f):
    return min(a,b,c,d,e,f)
result=minvalue(15,76,89,26,2,90)
print(result)


#sorting function
def sort_list(lst):
    return sorted(lst)
answer=sort_list([3,9,0,2,7,1,5,4,2])
print(answer)


def print_numbers(n):
    for i in range(n):
        print(i)
    print_numbers(5)