
import PrintList

"""
Prioritize an item in the to-do list.

Parameters:
to_do (list): The list of tasks to be prioritized

"""


def prioritize(to_Do):

  print("""
  ------------------------------
  Prioritize an item
  ------------------------------
  """)

  # Print list

  PrintList.print_list(to_Do)

  #Exit screen
  X = input("[Respond with X to exit this screen]").upper()

  if X == "X":

    return

  for user_input in range(3):

    user_input = input('Which items would you like to prioritize? ')

    if user_input.upper() == 'X':
      return
    
    try:
      task = int(user_input) - 1
      if 0 <= task <= len(to_Do):
        user_choice = to_Do[task]
        to_Do.remove(user_choice)
        to_Do.insert(0, user_choice)
        PrintList.print_list(to_Do)
        return

      else: 
        print("Please enter a valid number within range!")

    except ValueError:
      print("Enter a valid number!")

  PrintList.print_list(to_Do)
