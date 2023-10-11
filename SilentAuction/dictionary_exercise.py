#Dictionary
dictionary = {"Key":"Value"}
#Example
example = {"Bug":"An error in a program that prevents the program from running as expected."}
print(example["Bug"])

#Adding new items to dictionary
example["Loop"] = "The action of doing something over and over again"
print(example)

#Loop through a dictionary
for thing in example:
    print(thing)
    print(example[thing])

