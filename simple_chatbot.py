patterns = {"Plan a new holiday.":{"International":" Visit: https://internationalpackages.com","Domestic":"Visit: https://domesticpackages.com"},"Bookings related queries.":{"greetings":{"hi":"xyz","hey":"abc","hello":"qwe"},"end":{"bye":"abc","goodbye":"xyz"}}}
temp = patterns
# l1=[]
# sc=['?','.',':','!']
# for s in patterns:
#     l1.append(s)
    # for c in s:
    #     if c in sc:
    #         s = s.replace(c, "")
    # for x in s.split():
    #     l1.append(x.lower())
    # l1.append(s.split())
# print(l1)
# print(set(l1))
print("Hello, I am Alex. How may I help you?")
while True:
    c = 1
    l1 = []
    if type(temp) != str:
        for i in temp:
            print(f"{c}. {i}")
            c += 1
            l1.append(i)
        print(f"{c}. Quit")
        x = int(input("\nEnter number: "))
        if x in range(1,c):
            temp = temp[l1[x-1]]
        elif x == c:
            print("Have a nice day.")
            break
    
        else:
            print("Invalid Input")
        
    else:
        print("\nAlex:",temp,"\n")
        
        print("Do you wish to continue?\n1. Yes \t2. No")
        y = int(input("\nEnter number: "))
        if y == 1:
            temp = patterns
        elif y==2:
            print("Have a nice day.")
            break
        else:
            print("Invalid Input")