person_health=input("Enter the person health E for excellent and P for poor :")
age=int(input("Enter the person age :"))
gender=input("Enter the person gender M for male and f for female :")
live=input("Enter the person lives in C for city and V for village :")

policy_amount= None
premium_rate= None
should_insured = False

if person_health == "E" and age>=25 and age<=35 and gender == "M" and live == "C"  :
    policy_amount=200000
    premium_rate = 4
    should_insured = True
elif person_health == "E" and age>=25 and age<=35 and gender == "F" and live == "C":
    policy_amount=100000
    premium_rate = 3
    should_insured = True
elif person_health == "P" and age>=25 and age<=35 and gender == "M" and live == "V":
    should_insured = True
    policy_amount=10000
    premium_rate = 6
else:
    should_insured = False


if should_insured: 
    print("Person should be insured")
    print(f"your policy amount cannot be exceed {policy_amount}")
    print(f"your premium rate is Rs.{premium_rate} per thousand")
else: 
    print("Person should be not insured")