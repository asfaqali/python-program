book = input("Hello! I have English,Math and Hindi \n")
if book == "English":
    a = input("this avalible english book : class1 and class2 \n")
    if a == "class1":
        print("ok done")
    elif a == "class2":
        print("Not Avilable")
    else: 
        print("invalid book! ")    
elif book == "Math":
    b = input("Math book avilable Basic and Advance \n")
    if b == "Basic":
        print("Done")
    elif b == "Advance":
        print("Not Avilable")
    else:
        print("Thanks Serching")
elif book == "Hindi":
    c = input("Hindi book is avilable : Basic and Advance  \n")
    if c == "Basic":
        print("Done")
    elif c == "Advance":
        print("Not Avilable")
    else:
        print("thanks \n")
else:
    print("Thank You ! ")
