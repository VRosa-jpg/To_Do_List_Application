import PrintList


def remove_1(to_Do, removed):

  print("""
  ------------------------------
  Remove an item
  ------------------------------
  """)
  
  PrintList.print_list(to_Do)

  X = input("[Enter X to exit this screen]")

  item_to_remove = int(input("What item would you like to remove?")) - 1

  
  # Calling the item by index and not by name
  if item_to_remove <= len(to_Do):

    user_choice = to_Do[item_to_remove]

    to_Do.remove(user_choice)
    removed.append(user_choice)

  elif X == "X":
    return

  else:

      print("Item not listed")
      
  PrintList.print_list(to_Do)

