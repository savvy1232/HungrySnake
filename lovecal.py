print("Welcome to the love calculator!")

name1=input("What is your name?\n")
name2=input("What is your Partner name?\n")

combined_string=name1+name2
lower_case_string=combined_string.lower()

t=lower_case_string.count("t") 
r=lower_case_string.count("r") 
u=lower_case_string.count("u") 
e=lower_case_string.count("e") 
true = t+r+u+e 

l=lower_case_string.count("l") 
o=lower_case_string.count("o") 
v=lower_case_string.count("v") 
e=lower_case_string.count("e")
love = l+o+v+e

love_score = int((true+love))
print(love_score)

if (love_score==int)  or (love_score>90):
    print(f"Your Love Score is{love_score} You should Go like Coke and Mentos")
elif(love_score>=40) or (love_score<=50):
    print(f"Your Love Score is{love_score} You should go like Chai and Gulab jamun")
else:
    printf("Your Love score is{love_score}")
