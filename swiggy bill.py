#bill for zomato 
item = input("item name: ").strip().upper()
price = float(input("price: "))
quantity = int(input("quantity: "))
distance = int(input("enter delivery distance: "))

dis = 10
tax = 20

discount = (price*dis/100)
prices = price-discount
final_price = prices*quantity
tax_amount= final_price+(final_price*20/100)

if distance <= 3:
    print(f"please pay {tax_amount} and\n no delivery charge")
elif distance <= 6:
    n1 = (distance-3)*5
    print(f"total amount for {item} is :{tax_amount+n1}")
elif distance <= 9:
    n1 = (distance-3)*5
    n2 = (distance-6)*10+n1
    print(f"total amount for {item} and \n quantity {quantity} is {tax_amount+n2} ")
else:
        
        n3 = (distance-9)*20+45
        print(f"total amount for {item} and \n quantity {quantity} is {tax_amount+n3}" )