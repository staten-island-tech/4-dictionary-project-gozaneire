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


bookdictionary = ["MW Pocket","Merriam-Webster","Random House","Collins","Oxford","Cambridge","MW Collegiate"]
print(*bookdictionary, sep="\n")
order_request = input("Which dictionary do you want to buy?")

x = bookdictionary.index([order_request])
print(x)


"def cost(p,t)"
"return(p*t)"

"p = price"
"t = 8.875"

"finalprice = cost(p,t)"
"print[finalprice]"