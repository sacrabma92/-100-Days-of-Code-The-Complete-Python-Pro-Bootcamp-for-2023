def get_full_name(first_name, last_name):
  full_name = first_name.capitalize() + ' ' + last_name.upper()
  return full_name

print(get_full_name('carlos','Ramirez'))

def get_full_name(first_name:str, last_name:str):
  full_name = first_name.upper() + ' ' + last_name.upper()
  return full_name