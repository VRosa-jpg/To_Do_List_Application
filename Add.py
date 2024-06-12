
def add(to_Do):

  print("""
--------------------------
Item
--------------------------""")
  """
  Nested function to recycle task input if user wants to repeatedly add tasks 
  and append tasks to the list so we dont have to repeatedly use the the 
  to_Do.append() method
  """
  def add_task():
    task = input("What do we need to get done today? ")
    to_Do.append(task)

  # Intialized variable loop 
  add_task()

  """
  This while loop represents the user repeatedly asking to add items to their
  to-do list
  """
  while True:
    add_another_item = input("Do you want to add another item? Y/N: ")

    if add_another_item == "Y":
      add_task()
    
    elif add_another_item == "N":
      print(to_Do)
      break
      
    else:
      print("Options are Y or N")

    