
## Testing out some different things in Python for the Machine Learning Anthropology/Archaeology Project

starting_value = input("Please enter your starting value: ")

decay_rate = input("Please enter your decay rate as a percentage (i.e; .50): ")

decaying_value = starting_value

print decaying_value

while decaying_value > .000001:
    decaying_value = decaying_value * decay_rate
    print decaying_value
