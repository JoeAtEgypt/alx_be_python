monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are: ${monthly_savings}")
yearly_savings = monthly_savings * 12
projected_savings =  yearly_savings + yearly_savings * 0.05 # Annual savings
print(f"Projected savings after one year, with interest, is: ${projected_savings}")
