##Question-1:
#------------------------------------------------------------------------------------------------------------------------------------------#
"""
Create one conditional to find whether “false” is in string str1. If so, assign variable output the string “False. You aren’t you?”. Check to see if “true” is in string str1 and if it is then assign “True! You are you!” to the variable output. If neither are in str1, assign “Neither true nor false!” to output.
"""
#------------------------------------------------------------------------------------------------------------------------------------------#


str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"
if 'false' in str1:
    output="False. You aren’t you?"
elif 'true' in str1:
    output="True! You are you!"
else:
    output="Neither true nor false!"

print(output)
##output: True! You are you!

##=========================================================================================================================================
##Question-2:
#------------------------------------------------------------------------------------------------------------------------------------------#
"""
Create an empty list called resps. Using the list percent_rain, for each percent, if it is above 90, add the string ‘Bring an umbrella.’ to resps, otherwise if it is above 80, add the string ‘Good for the flowers?’ to resps, otherwise if it is above 50, add the string ‘Watch out for clouds!’ to resps, otherwise, add the string ‘Nice day!’ to resps.
"""
#------------------------------------------------------------------------------------------------------------------------------------------#

percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps=[]
for percent in percent_rain:
    if percent > 90:
        resps.append("Bring an umbrella.")
    elif percent > 80:
        resps.append("Good for the flowers?")
    elif percent > 50:
        resps.append("Watch out for clouds!")
    else:
        resps.append("Nice day!")

print(resps)

##output:  ['Bring an umbrella.', 'Nice day!', 'Bring an umbrella.', 'Watch out for clouds!', 'Nice day!', 'Nice day!', 'Watch out for clouds!', 'Good for the flowers?']
##=========================================================================================================================================


food = input("What is your favorite food? ")
drink = input("What is your favorite drink? ")

if food == "pizza" and drink == "juice":
    print("Those are my favorite as well!")
else:
    print("One of those is not my favorite")

##output:
#What is your favorite food? pizza
#What is your favorite drink? juice
#Those are my favorite as well!
