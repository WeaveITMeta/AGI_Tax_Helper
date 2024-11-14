def suggest_deductions(income, expenses):
    """Suggests potential deductions based on income and expenses."""
    suggestions = []
    if income < 40000:
        suggestions.append("Consider standard deduction.")
    if "Charitable Contributions" in expenses:
        suggestions.append("You may be eligible for charitable deduction.")
    if "Health Expenses" in expenses and expenses["Health Expenses"] > income * 0.075:
        suggestions.append("Medical expenses exceeding 7.5% of income can be deductible.")
    return suggestions

# Sample income and expenses
income = 50000
expenses = {
    "Charitable Contributions": 3000,
    "Health Expenses": 5000,
}

deduction_suggestions = suggest_deductions(income, expenses)
print("Suggested Deductions:", deduction_suggestions)