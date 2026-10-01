

def calculate_bill(units, category, peak_threshold, paid_before_due):
    category = category.strip().lower()

    # ---------- 1. Slab-wise rate calculation using if-elif-else ----------
    if category == "commercial":
        if units <= 100:
            base_bill = units * 10
        elif units <= 300:
            base_bill = (100 * 10) + (units - 100) * 12
        else:
            base_bill = (100 * 10) + (200 * 12) + (units - 300) * 15
    elif category == "non-commercial":
        if units <= 100:
            base_bill = units * 5
        elif units <= 300:
            base_bill = (100 * 5) + (units - 100) * 6
        else:
            base_bill = (100 * 5) + (200 * 6) + (units - 300) * 8
    else:
        print("Invalid category entered. Please enter 'commercial' or 'non-commercial'.")
        return

    print(f"\nBase Bill (before surcharge/discount/penalty): Rs {base_bill:.2f}")

    # ---------- 2. Peak surcharge using logical operators (and) ----------
    peak_exceeded = (category == "commercial") and (units > peak_threshold)

    surcharge = 0
    if peak_exceeded:
        surcharge = 0.10 * base_bill   # 10% surcharge on base bill
        base_bill += surcharge
        print(f"Peak Surcharge Applied (10%): Rs {surcharge:.2f}")

    print(f"Is peak threshold exceeded? {'Yes' if peak_exceeded else 'No'}")

    # ---------- 3. Discount (early payment) OR Penalty (late payment) ----------
    # Using logical operator 'or' style condition through if-else
    if paid_before_due:
        discount = 0.05 * base_bill    # 5% discount for early payment
        base_bill -= discount
        print(f"Early Payment Discount (5%): Rs {discount:.2f}")
    else:
        penalty = 100 if category == "commercial" else 50
        base_bill += penalty
        print(f"Late Payment Penalty: Rs {penalty:.2f}")

    # ---------- 4. Final Bill ----------
    print(f"\nFinal Electricity Bill: Rs {base_bill:.2f}")
    return base_bill


# --------------------- Driver / Input Section ---------------------
if __name__ == "__main__":
    print("===== Electricity Bill Calculator =====")

    units = float(input("Enter units consumed: "))
    category = input("Enter category (Commercial/Non-Commercial): ")
    peak_threshold = float(input("Enter peak threshold units (for commercial category): "))

    paid_input = input("Was the bill paid before the due date? (yes/no): ").strip().lower()
    paid_before_due = paid_input == "yes"

    calculate_bill(units, category, peak_threshold, paid_before_due)

