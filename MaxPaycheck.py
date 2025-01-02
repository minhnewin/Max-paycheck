from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 10

def calculate_paycheck(regular_hours, hourly_wage, overtime_hours, overtime_rate):
    # Convert inputs to Decimal for precise calculations
    regular_hours = Decimal(regular_hours)
    hourly_wage = Decimal(hourly_wage)
    overtime_hours = Decimal(overtime_hours)
    overtime_rate = Decimal(overtime_rate)
    
    # Calculate base and overtime pay
    base_pay = regular_hours * hourly_wage
    overtime_pay = overtime_hours * hourly_wage * overtime_rate
    total_pay = base_pay + overtime_pay

    return base_pay, overtime_pay, total_pay

def calculate_deduction_percentage(total_pay, threshold):
    # Convert inputs to Decimal
    total_pay = Decimal(total_pay)
    threshold = Decimal(threshold)
    
    # Ensure deduction is needed
    if total_pay <= threshold:
        return Decimal(0)
    
    # Calculate the percentage to deduct
    deduction = (total_pay - threshold) / total_pay * 100
    return deduction

# Input values
regular_hours = input("Enter regular hours worked: ")
hourly_wage = input("Enter hourly wage: ")
overtime_hours = input("Enter overtime hours worked: ")
overtime_rate = input("Enter overtime rate multiplier (e.g., 1.5): ")

# Calculate paycheck
base_pay, overtime_pay, total_pay = calculate_paycheck(
    regular_hours, hourly_wage, overtime_hours, overtime_rate
)

# Calculate deduction percentage to bring total below 1965
threshold = 1965  # Target threshold
deduction_percentage = calculate_deduction_percentage(total_pay, threshold)

# Calculate the final paycheck after deduction
deduction_amount = (deduction_percentage / 100) * total_pay
final_paycheck = total_pay - deduction_amount

# Display results
print(f"Base Pay: ${base_pay}")
print(f"Overtime Pay: ${overtime_pay}")
print(f"Total Paycheck Before Deduction: ${total_pay}")
print(f"Deduction Percentage: {deduction_percentage:.2f}%")
print(f"Deduction Amount: ${deduction_amount:.2f}")
print(f"Final Paycheck: ${final_paycheck}")
