# 1.1, 2.1, 2.2 and 2.3

SALOON_DAILY_RATE = 22.50
HIGH_PERFORMANCE_DAILY_RATE = 28.00
VAN_DAILY_RATE = 35.00
MAX_DAYS = 10 # THIS NEVER CHANGES + CONST ARE ALWAYS CAPS
LONG_HIRE_THRESHOLD = 7 # The amount of days before it becomes a long hire
LONG_HIRE_DISCOUNT = 0.10 # x0.10
GOLD_HP_PROMO = 18.00 #HIGH_PERFORMANCE_PROMO
INSURANCE_PREMIUM = 15.50
DEPOSIT = 50.00

# BOX 1


vehicle_type = input("Which type of vehicle do you require: (S = Saloon) (HP = High Performance) (V = Van) ").upper().strip()
while vehicle_type not in ("S", "HP", "V"):
    print("Please pick a valid option: (S = Saloon) (HP = High Performance) (V = Van): ")

    vehicle_type = input("Which type of vehicle do you require: (S = Saloon) (HP = High Performance) (V = Van) ").upper().strip()


# ASK THE AMOUNT OF DAYS NEEDED AND LOOP IT 3.3

number_of_days = int(input("How Many days do you need: 1 to 10: " ))
while number_of_days < 1 or number_of_days > MAX_DAYS:

    if number_of_days < 1:
        print("Value too low")

    elif number_of_days > MAX_DAYS:
        print("Value too high")

    number_of_days = int(input("How Many days do you need: 1 to 10: "))


# insurance loop 3.3



insurance_requirement = input("Do you require insurance: (Y = YES), (N = NO): ").upper().strip()
while insurance_requirement not in ("Y", "N" ):
    print("Please pick a valid option, Do you require insurance : (Y = YES), (N = NO) ")

    insurance_requirement = input("Do you require insurance : (Y = YES), (N = NO): ").upper().strip()

# new or old customer and membership type

membership_type = "no card"

returning_customer = input("Are you a returning customer: (NEW), (EXISTING): ").upper().strip()
while returning_customer not in ("NEW", "EXISTING" ):
    print("Please pick a valid option, Are you a returning customer: (NEW), (EXISTING): ")

    returning_customer = input("Are you a returning customer: (NEW), (EXISTING): ").upper().strip()

if returning_customer == "existing".upper().strip():
    membership_type = input("Which Loyalty Card do you have?:(BRONZE), (SILVER) and (GOLD): ") .upper().strip()

    while membership_type not in ( "BRONZE", "SILVER", "GOLD" ):
        print("Please pick a valid option, Which Loyalty Card do you have?: (BRONZE), (SILVER) and (GOLD): ")

        membership_type = input("Which Loyalty Card do you have?:(BRONZE), (SILVER), (GOLD): ").upper().strip()


# box 2 - rate picking

if vehicle_type == ("V"):
    daily_rate = VAN_DAILY_RATE
    vehicle_name = "VAN"

elif vehicle_type == ("HP"):
    daily_rate = HIGH_PERFORMANCE_DAILY_RATE
    vehicle_name = "HIGH PERFORMANCE"

else:
    daily_rate = SALOON_DAILY_RATE
    vehicle_name = "SALOON"


# BOX 3  THE SUMS

base_cost = daily_rate * number_of_days
total_cost = base_cost

promo_saving=0
long_hire_savings = 0

if number_of_days > LONG_HIRE_THRESHOLD:
    long_hire_savings = total_cost * LONG_HIRE_DISCOUNT # Store insurance premium inside new variable insurance
    total_cost = total_cost - long_hire_savings

if membership_type == "GOLD" and vehicle_type == "HP":
    promo_saving = GOLD_HP_PROMO # Store £18 inside promo_saving
    total_cost = total_cost - promo_saving

if insurance_requirement == "Y":
    insurance = INSURANCE_PREMIUM # Store insurance premium inside new variable insurance
    total_cost = total_cost + insurance

deposit = DEPOSIT
total_cost = total_cost + deposit

#BOX 4


print("\n===== VEHICLE HIRE QUOTE =====")
print(f"Vehicle:         {vehicle_name}")
print(f"Days hired:      {number_of_days}")
print(f"Customer type:   {returning_customer}")
print(f"Loyalty card:    {membership_type}")
print(f"Hire cost:       £{base_cost:.2f}")
print(f"Long hire discount:   -£{long_hire_savings:.2f}")
print(f"Gold promotion:       -£{promo_saving:.2f}")

if insurance_requirement == "Y":
    print(f"Insurance:            Yes (£{insurance:.2f})")
else:
    print("Insurance:            No")

print(f"Deposit (returnable): £{deposit:.2f}")
print(f"TOTAL DUE:            £{total_cost:.2f}")