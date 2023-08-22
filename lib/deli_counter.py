katz_deli = []
def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        message = "The line is currently:"
        for i in range(len(katz_deli)):
            message += f' {i + 1}. {katz_deli[i]}'
        print(message)
# print(line(["Gloria","kelvin","Somiyan"]))

    
def take_a_number(katz_deli,name):
    # if len(katz_deli)== 0 :
       katz_deli.append(name)
    # print(f'Welcome, {name}. You are number {1} in line.')
    # if len(katz_deli) > 1:
    #     for i in range(len(katz_deli)):
       print(f'Welcome, {name}. You are number {len(katz_deli)} in line.')
    #     return f'Welcome, {katz_deli[i]}. You are number {i + 1} in line.'
    # print(message
    #  for i in range(len(katz_deli)):
         
    #      print(f'Welcome, {katz_deli[i]}. You are number {i + 1} in line.')
    #      return katz_deli.append(name)
# def take_a_number(katz_deli, new_customer):
#     katz_deli.append(new_customer)
#     print(f'Welcome, {new_customer}. ' +\
#         f'You are number {len(katz_deli)} in line.')
     
# print(take_a_number(["Gloria","kelvin","Somiyan"],'Justo'))
    #  message = "The line is currently:"
    #     for i in range(len(katz_deli)):
    #         message += f' {i + 1}. {katz_deli[i]}'
    #     print(message)
def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        del(katz_deli[0])
        # else:
        #      print("There is nobody waiting to be served!")
        # elif  
# print(now_serving(["Gloria","kelvin","Somiyan"]))
        
        