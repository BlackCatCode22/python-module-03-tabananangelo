numbers=[]
while True:
    user_input=input("Enter a number or 'done' to finish:")
    if user_input=='done':
        break
    try:
        number=float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'done' to end")
if numbers:
    count=len(numbers)
    total=sum(numbers)
    print("Count:", count)
    print("Total:", total)
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
else:
    print("No numbers were entered.")