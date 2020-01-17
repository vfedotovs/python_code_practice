
"""
Design a new type called payrollT that is capable of holding the data for a list of
employees, each of which is represented using the employeeT type introduced in the
section on “Dynamic records” at the end of the chapter. The type payrollT should
be a pointer type whose underlying value is a record containing the number of
employees and a dynamic array of the actual employeeT values, as illustrated by the
following data diagram

Requirements:
1. app needs to ask how many person records to create
2. in loop itere and ask records fro all persons
3. Print salary 

Write a program that generates the weekly payroll for a company whose employment
records are stored using the type payrollT, as defined in the preceding exercise.
Each employee is paid the salary given in the employee record, after deducting taxes.
Your program should compute taxes as follows:
• Deduct $1 from the salary for each withholding exemption. This figure is the
adjusted income. (If the result of the calculation is less than 0, use 0 as the
adjusted income.)
• Multiply the adjusted income by the tax rate, which you should assume is a flat
25 percent.
For example, Bob Cratchit has a weekly income of $15. Because he has seven
dependents, his adjusted income is $15 – (7 x $1), or $8. Twenty-five percent of $8
is $2, so Mr. Cratchit’s net pay is $15 – $2, or $13.

"""
import employee


def main():

    emp_list = []

    def create_emp_records():
        emp_count = input("How many employee record you need to create?")
        for number in range(int(emp_count)):
            print("Enter detaild for employee #", number + 1)
            n = input("Name:")
            t = input("Title:")
            tax = int(input("Tax ID:"))
            w = int(input("Weekly salary:"))
            k = int(input("Dependent count:"))
            emp_list.append(employee.Employee(n, t, tax, w, k))

    def calculate_salary():
        print("Name         Gross - Tax - Net weekly ")
        print("--------------------------------------------")
        for object in emp_list:
            print_name = object.name
            gross = object.salary
            dep_count = object.child_count
            tax = (gross - (dep_count * 40)) / 4
            net = gross - tax
            print(print_name, "     ", gross, "-",
                  tax, "-", net)  # need to use format

    create_emp_records()
    calculate_salary()


if __name__ == '__main__':
    main()
