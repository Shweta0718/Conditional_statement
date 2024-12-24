# Input the basic salary
basic_salary = float(input("Enter the basic salary: "))

# Initialize DA and HRA
DA = 0  # Dearness Allowance
HRA = 0  # House Rent Allowance

# Calculate DA and HRA if basic salary is more than 50000
if basic_salary > 50000:
    DA = 0.10 * basic_salary  # 10% of basic salary
    HRA = 0.12 * basic_salary  # 12% of basic salary

# Calculate total salary
total_salary = basic_salary + DA + HRA

# Display the results
print(f"Basic Salary: {basic_salary}")
print(f"DA (10%): {DA}")
print(f"HRA (12%): {HRA}")
print(f"Total Salary: {total_salary}")
