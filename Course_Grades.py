def convert_round(score):
    score_dec = round(score - int(score),2) # get the digits after the decimal point and round them to 2 numbers
    if score_dec >= 0.5:
        score = int(score) + 1
    else:
        score = int(score)
    return score

def highest(s1,s2,s3): # This function was done this way to find not just the number of the highest score but also the subject
    if s1 >= s2 and s1 >= s3: # Python
        return 1
    elif s2 >= s1 and s2 >= s3: # Linux
        return 2
    else: # Networking
        return 3
    
 

# this part will read the input from the user, then will convert to float and finially will round to 2 numbers after the decimal point
python = round(float(input("Enter the mark in python: ")),2)
python = convert_round(python)

linux = round(float(input("Enter the mark in linux: ")),2)
linux = convert_round(linux)

networking = round(float(input("Enter the mark in networking: ")),2)
networking = convert_round(networking)

average_score = (python + linux + networking)/3
highest_score = highest(python,linux,networking)

print("Python score = " + str(python))
print("Linux score = " + str(linux))
print("Networking score = " + str(networking))
print("Average score = " + str(average_score))

if highest_score == 1:
    print("Python is the highest score")
    print("The Highest score = " + str(python))
elif highest_score == 2:
    print("Linux is the highest score")
    print("Highest score = " + str(linux))
else:
    print("Networking is the highest score")
    print("Highest score = " + str(networking))

