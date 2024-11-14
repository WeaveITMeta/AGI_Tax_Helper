def calculate_deductions(income, expenses):
    """Suggests deductions based on expense categories."""
    deductions = {}
    if "Health Expenses" in expenses:
        if expenses["Health Expenses"] > income * 0.075:
            deductions["Health Deduction"] = expenses["Health Expenses"]

    if "Charitable Contributions" in expenses:
        deductions["Charity Deduction"] = expenses["Charitable Contributions"]

    # Additional rules can be added
    return deductions

# Sample call
income = 50000
expenses = {"Health Expenses": 4000, "Charitable Contributions": 3000}
deductions = calculate_deductions(income, expenses)
print("Deductions:", deductions)