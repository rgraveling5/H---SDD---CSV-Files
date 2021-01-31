"""
Reading CSV
"""
# Lists for storing data
name    = []
height  = []
age     = []
gender  = []

file = open('input_data.csv','r')

for line in file:
    # Replace quotation marks, strip extra whitespace and split into a list
    data = line.replace('"','').strip().split(',')

    # Move temp data into lists
    name.append     (data[0])
    height.append   (float(data[1]))
    age.append      (int(data[2]))
    gender.append   (data[3])

file.close()

print(name)
print(height)
print(age)
print(gender)

"""
Writing CSV
"""
file = open('output_data.csv','w')

for x in range(len(name)):
    file.write(f'"{name[x]}",{height[x]},{age[x]},"{gender[x]}"\n')

file.close()

