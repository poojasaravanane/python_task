##4
percentage = float(input("Enter your percentage: "))
match percentage:
    case p if p >= 90:
        print("Grade A")
    case p if p >= 75:
        print("Grade B")
    case p if p >= 60:
        print("Grade C")
    case p if p >= 50:
        print("Grade D")
    case p if p < 50:
        print("Fail")
##5
month = input("Enter month name: ").lower()
match month:
    case "december" | "january" | "february":
        print("Winter")
    case "march" | "april" | "may":
        print("Spring")
    case "june" | "july" | "august":
        print("Summer")
    case "september" | "october" | "november":
        print("Autumn")
    case _:
        print("Invalid month")

##6
num = int(input("Enter a number: "))
match num:
    case n if n > 0:
        print("Positive")
    case n if n < 0:
        print("Negative")
    case 0:
        print("Zero")     
##7
num = input("Enter a number: ")
match num:
    case n if 1 <= n <= 50:
        print("Number is in range 1–50")
    case _:
        print("Number is out of range")

