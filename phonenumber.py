import phonenumbers
from phonenumbers import geocoder, carrier, timezone


# <------------------------------------------------------------------------------------->







Z = '\033[1;31m'  # Red
X = '\033[1;33m'  # Yellow
Z = '\033[2;31m'  # Red, second shade
F = '\033[2;32m'  # Green
A = '\033[2;34m'  # Blue
C = '\033[2;35m'  # Pink
B = '\033[2;36m'  # Cyan
Y = '\033[1;34m'  # Light blue






# <------------------------------------------------------------------------------------->

# ... (other code)

phonenumber = input(A + "Please Enter Phone Number \n رجائا ادخل رقم الهاتف : \n")

phone = phonenumbers.parse(phonenumber)
print(F + geocoder.description_for_number(phone, "en"))
print(F + carrier.name_for_number(phone, "en"))
print(timezone.time_zones_for_number(phone))  





# ---------------------------------------------------------------------------------------->