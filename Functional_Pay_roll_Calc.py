hours = input("Enter the number of hours worked: ")
rate = input("Enter the hourly pay rate: ")

try:
    hours = float(hours)
    rate = float(rate)

except:
    print("Enter Numerical Values Only! Try Again")
    exit()

def computepay(hrs, rate):

    if hrs <= 40:
        gpay = hrs * rate
        return gpay
    
    else:
        overtime = hrs - 40
        pay = 40 * rate
        overtime_pay = overtime * (rate * 1.5)
        gpay = pay + overtime_pay
        return gpay

print("Pay", computepay(hours, rate))