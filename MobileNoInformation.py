#importing packages
import phonenumbers
from phonenumbers import carrier,geocoder,timezone

#Getting input
mobno=input("Enter The Mobile No:-")
mobno=phonenumbers.parse(mobno)

#Getting Validation of Mobile no
print("\n\nValid Mobile No:-",phonenumbers.is_valid_number(mobno))

#Checking Possibility of Mobile no
print("\n\nChecking Possibility of Mobile Number:-",phonenumbers.is_possible_number(mobno))


#get the timezone of Mobile no
print("\n\n")
print(timezone.time_zones_for_number(mobno))

#getting carrier of Mobile no
print("\n\n")
print(carrier.name_for_number(mobno,"en"))

#Getting Region
print("\n\n")
print(geocoder.description_for_number(mobno,"en"))

