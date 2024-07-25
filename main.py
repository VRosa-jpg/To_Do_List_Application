import Add
import Edit
import Prioritize
import PrintList
import Remove

to_Do = []


def main():
    while True:

      print("""
----------------------------
MAIN MENU
----------------------------
1. Add an Item
2. Remove an item
3. Prioritize an Item
4. Print list 
5. End Program
""")
      
      action = input("What action do you want to take? ")

      
      # Adding items to a list
      if action == '1':
        Add.add(to_Do)
      
      # Removing Items from the list
      elif action == '2':
        Remove.remove(to_Do)

      # Putting items at the top of the list
      elif action == '3':
          Prioritize.prioritize(to_Do)
      # Edit an item on a list
      elif action == '4':
        Edit.edit(to_Do)
        
      # Print list
      elif action == '5':
        PrintList.print_list(to_Do)

      # End Program
      elif action == '6':
        break
 
      else:
          print("Action not recognized")

main()