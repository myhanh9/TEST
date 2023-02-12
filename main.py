import pandas as pd
data = pd.read_excel('Ex1.xlsx')
dataDict = data.to_dict('list')
print('Welcome to the birthday dictionary. We know the birthdays of:')
name = dataDict.get("Name")
bDate = dataDict.get("Birthday")
for i in name:
    print(i)
flag = True
while(flag):
    name_input = input("Who's birthday do you want to look up?, Type 'ESC' to exit")
    if name_input not in name and name_input.lower() != 'esc':
        print("Sorry, we do not know this person")
    for i,v in enumerate(name):
        if name_input.isnumeric() == True:
            name_input = input("Please type a string")
        elif name_input.lower() == v.lower():
            print(f"{name_input}"+"'s birthday is "+ str(bDate[i]))
        elif name_input.lower() == "esc":
            flag = False


