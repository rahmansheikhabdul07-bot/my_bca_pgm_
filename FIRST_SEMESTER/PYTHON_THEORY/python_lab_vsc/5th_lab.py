menu = {"idli": 40, "dosa": 60, "biriyani": 180, "coffee": 25, "juice": 50}


def item_cost(item, qty):
    return menu.get(item, 0) * qty


def generate_bill(subtotal, discount_percent=0, gst_rate=0.05):
    discount = subtotal * discount_percent / 100
    gst = (subtotal - discount) * gst_rate
    return discount, gst, subtotal - discount + gst


def split_bill(total, people):
    return divmod(int(total), people)


print("========== RESTAURANT MENU ==========")
for item, price in menu.items():
    print(item.capitalize(), ": Rs.", price)
print("=====================================")

subtotal = 0
for _ in range(int(input("\nEnter number of items ordered: "))):
    item = input("\nEnter item name: ").lower()
    qty = int(input("Enter quantity: "))
    cost = item_cost(item, qty)
    if cost == 0:
        print("Sorry,", item, "is not on the menu. Item skipped.")
    else:
        print(item.capitalize(), "x", qty, "= Rs.", cost)
        subtotal += cost

discount_percent = float(input("\nEnter discount percentage (0 for none): "))
people = int(input("Enter number of people sharing the bill: "))

discount, gst, total = generate_bill(subtotal, discount_percent)
each, left = split_bill(total, people)

print("\n============== BILL ==============")
print("Subtotal      : Rs.", round(subtotal, 2))
print("Discount      : Rs.", round(discount, 2))
print("GST (5%)      : Rs.", round(gst, 2))
print("Final Total   : Rs.", round(total, 2))
print("----------------------------------")
print("Each person pays : Rs.", each)
print("Rupees left over : Rs.", left)
print("==================================")