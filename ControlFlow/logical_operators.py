high_income = True
good_credit = True
student = True

if high_income and good_credit:
    message = "Eligible"
else:
    message = "Not eligible"

message = "Eligible" if high_income and good_credit else "Not eligible"
print(message)

message = "Eligible" if not student and (high_income or good_credit) else "Not eligible"
print(message)


