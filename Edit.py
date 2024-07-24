import PrintList

def edit(to_Do):
  # Print List
  PrintList.print_list(to_Do)

  X = input("[Press X if you want to exit]")

  if X.upper() == 'X':
    return

  while True:
    user_input = input("What item would you like to edit? ")
    
    if user_input == "X":
      return

    try:
      task = int(user_input) - 1
      if 0 <= task <= len(to_Do):
        user_choice = to_Do[task]
        print(f"Update: {user_choice}")
        update = input("update item to: ")
        to_Do[task] = update
        PrintList.print_list(to_Do)
        return

      else: 
        print("Enter a number within range!")

    except ValueError:
      print("Please enter a valid number!")
      
      

    