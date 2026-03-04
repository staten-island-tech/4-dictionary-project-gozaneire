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

bookdictionary = ["MW Pocket","Merriam-Webster","Random House","Collins","Oxford","Cambridge","MW Collegiate"]
print(*bookdictionary, sep="\n")
order_request = input("Which dictionary do you want to buy?")

while order_request != "end":
    if order_request == "MW Pocket":
        print(MW_Pocket)
        p += 6
        order_request = input("Which dictionary do you want to buy?")
    elif order_request == "Merriam-Webster":
        print(Merriam_Webster)
        p += 120
        order_request = input("Which dictionary do you want to buy?")
    elif order_request == "Random House":
        print(Random_House)
        p += 10
        order_request = input("Which dictionary do you want to buy?")
    elif order_request == "Collins":
        print(Collins)
        p += 35
        order_request = input("Which dictionary do you want to buy?")
    elif order_request == "Oxford":
        print(Oxford)
        p += 15
        order_request = input("Which dictionary do you want to buy?")
    elif order_request == "Cambridge":
        print(Cambridge)
        p += 40
        order_request = input("Which dictionary do you want to buy?")
    elif order_request == "MW Collegiate":
        print(MW_Collegiate)
        p += 24.95
        order_request = input("Which dictionary do you want to buy?")
    else:
        print("Please enter a valid dictionary listed")
        order_request = input("Which dictionary do you want to buy?")
    if order_request == "end":
        break

def cost(p,t):
    return(p*t)

t = 1.0875

finalprice = round(cost(p,t),2)
print(finalprice)