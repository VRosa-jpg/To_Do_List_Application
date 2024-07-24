import PrintList


def remove_1(to_Do):

  print("""
  ------------------------------
  Remove an item
  ------------------------------
  """)

  # Print current list
  PrintList.print_list(to_Do)

  #User presses X to exit screen
  X = input("[Enter X to exit this screen]").upper()

  if X == "X":
    return

  for user_attempt in range(3):
    
    user_attempt = input("What item would you like to remove?").upper()

    if user_attempt == "X":
      return

    try:
      task = int(user_attempt) - 1
      if 0 <= task <= len(to_Do):
        user_choice = to_Do[task]
        to_Do.remove(user_choice)
        PrintList.print_list(to_Do)
        return

      else:
        print("Enter a number within range!")
        

    except ValueError:
      print("Please enter a valid number!")

    else:
      print("Enter number within range!")

      