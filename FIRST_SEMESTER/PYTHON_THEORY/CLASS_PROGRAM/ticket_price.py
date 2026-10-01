# Display pricing details
print("------------- ticket price: -------------")
print("per ticket price:- child:150 adult:300 senior citizen:200")
print("Monday-FRIDAY (NO DISCOUNT)")
print("SATURDAY & SUNDAY (50% DISCOUNT)\n")

# Get user input for age and weekday
age = int(input("ENTER YOUR AGE: "))
day = input("ENTER THE WEEK DAY: ").strip().lower()

# Determine base price based on age group using if-elif-else
if age < 5:
    base_price = 150  # Child
elif age >= 6 and age <= 59:
    base_price = 300  # Adult
else:
    base_price = 200  # Senior citizen (age > 60 or 60+)

# Determine day-of-week discount using logical operators
if day == "saturday" or day == "sunday":
    final_price = base_price * 0.5  # 50% weekend discount
else:
    final_price = base_price  # Weekday (no discount)

# Display final ticket price
print(f"TICKET PRICE: {int(final_price)}")


 

  