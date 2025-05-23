print("Leap Year Calculator")
try :
  user_input = int(input("Enter a Year[yyyy]: "))
  if user_input < 1000 or user_input > 9000 :
    print("Please enter a valid 4-didgt code.")
  elif (user_input % 4 == 0 and user_input % 100 != 0) or (user_input % 400 ==0):
    print(f"The year {user_input} is a leap year")
  else : 
    print(f"This year {user_input} is not a leap year.")
except ValueError:
  print("Please enter a valid 4-didgt code.")