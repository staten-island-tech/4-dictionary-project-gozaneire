MW_Pocket = {
    "Name": "MW Pocket",
    "Description": "Small dictionary that can fit in your hand or pocket",
    "Price": 6.00
}

Merriam_Webster = {
    "Name": "Merriam-Webster",
    "Description": "A complete dictionary made by the most prestigeous company in dictionaries.",
    "Price": 120.00
}

Random_House = {
    "Name": "Random House Webster",
    "Description": "A cheaper version of Merriam-Webster's dictionary but not as prestigious.",
    "Price": 10.00
}

Collins = {
    "Name": "Collins",
    "Description": "A dictionary on paperback for English or French and also thesaurus.",
    "Price": 35.00
}

Oxford = {
    "Name": "Oxford",
    "Description": "A dictionary for British English and named after Oxford University.",
    "Price": 15.00
}

Cambridge = {
    "Name": "Cambridge",
    "Description": "A dictionary for British English and named after Cambridge University.",
    "Price": 40.00
}

MW_Collegiate = {
    "Name": "Merriam-Webster Collegiate",
    "Description": "College dictionary by Merriam-Webster.",
    "Price": 24.95
}

p = 0
pocketcart = 0
mwcart = 0
rhcart = 0
collinscart = 0
oxfordcart = 0
cambridgecart = 0
collegiatecart = 0

bookdictionary = ["MW Pocket","Merriam-Webster","Random House","Collins","Oxford","Cambridge","MW Collegiate"]
print(*bookdictionary, sep="\n")
order_request = input("Which dictionary do you want to buy?")

while order_request != "end":
    if order_request == "MW Pocket":
        print(MW_Pocket["Description"])
        p += 6
        pocketcart += 1
        order_request = input("Which dictionary do you want to buy?")
    elif (order_request == "Merriam-Webster") or (order_request == "MW"):
        print(Merriam_Webster["Description"])
        p += 120
        mwcart += 1
        order_request = input("Which dictionary do you want to buy?")
    elif order_request == "Random House":
        print(Random_House["Description"])
        p += 10
        rhcart += 1
        order_request = input("Which dictionary do you want to buy?")
    elif order_request == "Collins":
        print(Collins["Description"])
        p += 35
        collinscart += 1
        order_request = input("Which dictionary do you want to buy?")
    elif order_request == "Oxford":
        print(Oxford["Description"])
        p += 15
        oxfordcart += 1
        order_request = input("Which dictionary do you want to buy?")
    elif order_request == "Cambridge":
        print(Cambridge["Description"])
        p += 40
        cambridgecart += 1
        order_request = input("Which dictionary do you want to buy?")
    elif order_request == "MW Collegiate":
        print(MW_Collegiate["Description"])
        p += 24.95
        collegiatecart += 1
        order_request = input("Which dictionary do you want to buy?")
    else:
        print("Please enter a valid dictionary listed")
        order_request = input("Which dictionary do you want to buy?")
    if order_request == "end":
        break

def cost(p,t):
    return(p*t)

t = 1.0875

if p != 0:
    if pocketcart != 0:
        print (pocketcart,"MW Pocket")
    if mwcart != 0:
        print(mwcart,"Merriam-Webster(s)")
    if rhcart != 0:
        print(rhcart,"Random House")
    if collinscart != 0:
        print(collinscart,"Collins")
    if oxfordcart != 0:
        print(oxfordcart,"Oxford Dictionary(ies)")
    if cambridgecart != 0:
        print(cambridgecart,"Cambridge(s)")
    if collegiatecart != 0:
        print(collegiatecart,"Merriam-Webster Collegiate(s)")
else:
    print("You've ordered no dictionaries.")


print("Subtotal:", p)
finalprice = round(cost(p,t),2)
print("Final price:", finalprice)