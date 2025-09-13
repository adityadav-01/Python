num = int(input("How many students you want to enter: "))

names = []     
averages = []    

for i in range(num):
    name = input(f"Enter name of student {i+1}: ")
    math = int(input("Enter Math score: "))
    science = int(input("Enter Science score: "))
    english = int(input("Enter English score: "))

    avg = (math + science + english) / 3
    
    names.append(name)       
    averages.append(avg)     

    print(f"Average marks of {name}: {avg}\n")


highest_avg = max(averages)  
index = averages.index(highest_avg)   
topper = names[index]

print("Highest average is of:", topper, "with", highest_avg)
