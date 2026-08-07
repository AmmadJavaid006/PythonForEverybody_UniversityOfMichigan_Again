hrs = float(input("Enter the number of hours worked: "))
rate = float(input("Enter the hourly pay rate: "))

if hrs <= 40:
    gpay = hrs * rate

else:
    overtime = hrs - 40
    pay = 40 * rate
    overtime_pay = overtime * (rate * 1.5)
    gpay = pay + overtime_pay

print(gpay)