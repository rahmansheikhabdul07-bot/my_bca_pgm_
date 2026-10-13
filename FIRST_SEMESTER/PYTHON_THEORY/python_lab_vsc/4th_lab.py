raw_data = """
 naveen KUMAR
 naveen.kumar@COMPANY.com
 +91-98765-43210
"""

first, last, email, phone = raw_data.split()

first, last = first.capitalize(), last.capitalize()
email = email.lower()
domain = email.split("@")[1]
digits = "".join(c for c in phone if c.isdigit())
masked = "*" * (len(digits) + 1 - 4) + digits[-4:]

valid = (first.isalpha() and last.isalpha()
         and email.count("@") == 1 and "." in domain
         and len(digits) == 12)

print("Name     :", first, last)
print("Initials :", first[0] + last[0])
print("Email    :", email)
print("Domain   :", domain)
print("Phone    :", masked)
print("Valid    :", valid)