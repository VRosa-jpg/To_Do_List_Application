
import PrintList


def prioritize(to_Do):

  print("""
  ------------------------------
  Prioritize an item
  ------------------------------
  """)

  # Print list

  PrintList.print_list(to_Do)

  #Exit screen

  X = input("[Respond with X to exit this screen]")

  #Prompt user for task number
  task_number = input('Which items would you like to prioritize?')

  # This code will be reusable for Remove Function as well
  def is_tasknumber_an_actaul_number():
    task_number_input = int(task_number) - 1
    if 0 <= task_number_input < len(to_Do):
      user_choice = to_Do[task_number]
      to_Do.remove(user_choice)
      to_Do.insert(0, user_choice)
    return task_number_input
  
  try:
    is_tasknumber_an_actaul_number()
    

  except ValueError:
    print("Please enter a valid number.")
    task_number = input('Which items would you like to prioritize?')
    


  

  if X == 'X' and task_number == 'X':
    return
        
  else:
    print("Item not listed")

  #Print LIST

  PrintList.print_list(to_Do)




  