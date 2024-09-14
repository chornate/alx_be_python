monthlyIncome=int(input("Enter your monthly income: "))
monthlyExpense=int(input("Enter your monthly expenses: "))
monthlySavings=monthlyIncome-monthlyExpense

print(f"Your monthly savings are {monthlySavings}")
print(f"Projected savings after one year, with interest, is: {monthlySavings*12+(monthlySavings*12*0.05)}")