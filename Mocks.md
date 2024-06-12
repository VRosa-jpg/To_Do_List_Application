# ToDo App Mocks

## Menu screen

Provide user with list of possible actions and take the item number as input and then trigger the selected workflow. If the user enters an invalid number, respond with "Invalid selection" and reprint the "Please enter action number: " line.


```console
-------------------------------------------
MAIN MENU
-------------------------------------------
What action do you want to take?

1. Add an item
2. Remove an item
3. Prioritize an item
4. Print list
5. End program

Please enter action number: 
```

## "Add an item" action

```console
-------------------------------------------
Add an item
-------------------------------------------
What do we need to get done today? 
```

- Gather task as input
- Add task to end of ToDo list
- Ask if user wants to add another item.

```console
Do you want to add another task? Y/N: 
```

- If user enters Y, repeat the above workflow where we ask for the item, store it, then ask if they want to add another item.
- If user enters N, return to menu screen.

## "Remove an item" action

Print the current todo list as a numbered list and ask user which item they want to remove.

```console
-------------------------------------------
Remove an item
-------------------------------------------
Your current ToDo list:
1. run
2. laundry
3. eat lots of ice cream

[Respond with X to exit this screen]

Which item would you like to remove? 
```

- If the user enters a valid number, remove that item from the list and then reprint the above lines.
- If the user enters an invalid number, respond with "Invalid selection" and reprint the "Which item would you like to remove? " line.
- If the user enters X, return to menu screen.

## "Prioritize an item" action

Print the current todo list as a numbered list and ask user which item they want to prioritize.

```console
-------------------------------------------
Prioritize an item
-------------------------------------------
Your current ToDo list:
1. run
2. laundry
3. eat lots of ice cream

[Respond with X to exit this screen]

Which item would you like to prioritize? 
```

- If the user enters a valid number, move that item to the top of the list and then reprint the above lines.
- If the user enters an invalid number, respond with "Invalid selection" and reprint the "Which item would you like to prioritize? " line.
- If the user enters X, return to menu screen

## "Show my list" action

Print the current todo list as a numbered list and ask user to enter X to return to the menu screen.

```console
-------------------------------------------
Show my list
-------------------------------------------
Your current ToDo list:
1. run
2. laundry
3. eat lots of ice cream

[Respond with X to exit this screen]
```

## "End program" action

Print a list of all actions accomplished / completed as a bulleted list and the current todo list as a numbered list then end the program.

```console
The tasks completed were:
- study programming
- water plants
- walk dog

Your current ToDo list:
1. run
2. laundry
3. eat lots of ice cream

<Program terminated>
```