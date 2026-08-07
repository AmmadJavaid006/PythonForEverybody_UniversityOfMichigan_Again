score = input("Enter Score: ")

try:
   score = float(score)

except:
    print("Enter value between 0.0 to 1.0! Try Again")
    exit()

if score >= 0.9:
    print("A")

elif score >= 0.8:
    print("B")

elif score >= 0.7:
    print("C")

elif score >= 0.6:
    print("D")

elif score < 0.6:
    print("F")
