
class bank:
    bank_name = "State Bank of India"
    branch = "Chennai"
    rate_of_interest = 4.5
    minimum_balance = 500
    bank_balance=600


bindhu_account = bank()
print(bindhu_account.bank_name)
bindhu_account.rate_of_interest=5
print(bindhu_account.rate_of_interest)

devan_account=bank()
print(bank.rate_of_interest)


moni_account=bank()
print(bindhu_account.rate_of_interest)
print(bank.minimum_balance)
print(bank.bank_balance)



