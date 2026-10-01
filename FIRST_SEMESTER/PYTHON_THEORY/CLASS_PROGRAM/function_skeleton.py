def get_price(item):
    if item == "idli":
        return 30
    elif item == "dosa":
        return 50
    elif item == "tea":
            return 10
    elif item == "golibaje":
                return 40
    else: item == "juice";
    return 100
    
    

    


def item_cost(item, qty):
    # TODO: call get_price() and return the cost
    price=get_price(item)
    return price * qty 



def calculate_gst(amount, rate=0.05):
    # TODO: return the GST rounded to 2 decimals
    gst=amount * rate
    return round (gst,2)  


def generate_bill(subtotal, discount_percent=3):
    discount = subtotal * discount_percent
    amount_after_discount = subtotal-discount
    gst = calculate_gst(amount_after_discount)  
    total = amount_after_discount + gst
    return discount,gst,total

def split_bill(total, people):
    each_pays = total // people
    left_over = total % people
    return total,people


# ---------------- Main program ----------------
# A group of 3 friends orders 2 dosa and 3 coffee, with a 10% coupon.

subtotal1 = item_cost('dosa',2 ) + item_cost('coffee',3) # TODO:  call item_cost() for dosa and coffee and add them
discount1, gst1, total1 = generate_bill(subtotal1,0.02)# TODO: call generate_bill() using a KEYWORD argument
subtotal2= item_cost('coffee',3)
discount2, gst2, total2 = generate_bill(subtotal2,0.02)

each, extra = split_bill(total1 + total2,3) # TODO: call split_bill() , the total (as a whole number) and 3 people

print("-----bill-----")
print("Subtotal :", subtotal1)
print("Discount :", discount1)
print("Subtotal :", subtotal2)
print("Discount :", discount2)
print("GST      :", gst1)
print("Total    :", total1)
print("GST      :", gst2)
print("Total    :", total2)
print("Each pays:", each, "| Left over:", extra)