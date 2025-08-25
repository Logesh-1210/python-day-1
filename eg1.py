print("hello")

## second example :

a = 12
b = 12
print(a+b)


## for indentation error :

x=23
if (x<12):
    print("it is greater than given element")

## finding of the data types :

a=12 
print(type(a))

a="karthi"
print(type(a))

a=9.9
print(type(a))

a= True or False
print(type(a)) 

a= None
print(type(a)) 

## dynamic typing or intellegence 

x=12
x="string"
x=True
x=9.99
print(x)

## local variable function :

def order():
    food = "Thadaladi Briyani"
    print( "Your order food is :" , food)
order()

## Enclosing with nested function :

def addioffer():
   food = "Briyani"
   def discount():
      print("The AAdi offered food is :",food)
   discount()
addioffer()


## global variable function :

user = "Logesh"

def college():
    print("Welcome to our college of Mahendra Institute of Tecnology :", user)

def department():
    print("ECE Department is belongs to :",user)

college()

department()

## test case for the L - E - G - B :

order = "Zomato"

def offer():
    item = "Chilly parrato"

    def place():
        quantity = 4

        print(f"ordering {item} {quantity} using {order}")

    place()
    
offer()