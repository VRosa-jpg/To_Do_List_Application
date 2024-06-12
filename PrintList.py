
def print_list(to_Do):
  print("Your current ToDo list: ")
  for y, x in enumerate(to_Do, start=1):
    print(f"{y}. {x}")