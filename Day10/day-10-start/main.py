# function with outputs

def format_name(f_name,l_name):
  """Take first and last name and format it to title format""" #docstring
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs"
  title_name = f_name.title() + " "+l_name.title()
  return title_name #return tells the computer the function ends

formated_string = format_name(input("What is your first name ? "),input("What is your last name ? "))
print(formated_string)