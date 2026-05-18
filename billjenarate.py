#Bill Genarator

products = {

            "rice"  :"52",
            "sugar" :"110",
            "oil"   :"200",
            "moyda" :"40",
            "salt"  :"20",
            "khud"  :"40",
            "vushi" :"50"

            }

product_name = input("Enter the name of product you want: ")

price = float(products[product_name])

quantity = float(input("Enter quantity(kg): "))

total = price * quantity

print("The price of your all product: ",total)



               