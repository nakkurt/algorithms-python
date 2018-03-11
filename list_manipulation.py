# Write a function called list_manipulation. This function should take in three parameters (a list, command, and location), along with an optional fourth parameter (a value).

# If the command is "remove" and the location is "end", the function should remove the last value in the list and return the value removed.
# If the command is "remove" and the location is "beginning", the function should remove the first value in the list and return the value removed.
# If the command is "add" and the location is "beginning", the function should add the value (fourth parameter) to the beginning of the list and return the list.
# If the command is "add" and the location is "end", the function should add the value (fourth parameter) to the end of the list and return the list.


def list_manipulation(l,cmd,loc, val=None):
  if cmd == "remove" and loc == "end":
    return l.pop()
  elif cmd == "remove" and loc == "beginning":
    return l.pop(0)
  elif cmd == "add" and loc == "end":
    l.append(val)
    return l 
  elif cmd == "add" and loc == "beginning":
    l.insert(0,val)
    return l 