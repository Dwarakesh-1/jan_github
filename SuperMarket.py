from datetime import datetime #for date

name = input("Enter your name:")

#List of items
lists = '''
Rice        Rs 35/kg
Sugar       Rs 25/kg
Salt        Rs 15/kg
Oil         Rs 100/liter
Paneer      Rs 150/kg
Noodles     Rs 75/kg
Bournvita   Rs 120/each
Toothpaste  Rs 95/each
Soaps       Rs 45/each
'''
#declaration
price = 0
pricelist = []
totalprice = 0
finalprice = 0
ilist = []
qlist = []
plist = []

#Rate of items
items = {'rice':35, 
'sugar':25, 
'salt':15, 
'oil':100, 
'paneer':150, 
'noodles':75, 
'bournvita':120,
'toothpaste':95,
'soaps':45}

option = int(input("For list of items press 1: "))
if(option == 1):
    print(lists)
for i in range(len(items)):
    inp1 = int(input("If you want to buy press 1 or press 2 to exist:"))
    if (inp1 == 2):
        break
    if (inp1 == 1):
        item = input("Enter your items:")
        quantity = int(input("Enter the required quantity:"))
        if (item in items.keys()):
            price = quantity * (items[item])
            pricelist.append((item,quantity,items,price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (totalprice * 5)/100
            finalprice = gst + totalprice
        else:
            print("Sorry! Entered item is not available")
    else:
        print("Sorry! You entered the wrong number")
    inp = input("Can I bill the items yes or no:")
    if (inp == 'yes'):
        pass
        if (finalprice != 0):
            print(30*"=", "People Mart", 30*"=")
            print(32*" ", "Tirupati")
            print("Name:", name, 34*" ", "Date:", datetime.now())
            print(75*"-")
            print("S.No", 5*" ", 'items', 10*" ", "quantity", 8*" ", "price")
            for i in range(len(pricelist)):
                print(i, 8*' ', 1*' ', ilist[i], 5*' ', qlist[i], 10*" ", plist[i])
            print(75*"-")
            print(50*" ", 'Total Amount:', 'Rs', totalprice)
            print('GST Amount:', 50*" ", 'Rs', gst)
            print(75*"-")
            print(50*" ", 'Final Price:', 'Rs', finalprice)
            print(75*"-")
            print(25*" ", "Thanks for visiting the mart")
            print(75*"-")