# Belief Revision Simulation
# Topic: Non-Monotonic Reasoning

# Rule: If an animal is a bird, assume it can fly.
# Exceptions: penguin, ostrich

def reasoning_process(animal):
    print("Reasoning Process:")
    print(f"1. You entered: {animal}")
    print("2. Rule: If an animal is a bird, assume it can fly.")

    birds = ["sparrow", "eagle", "parrot", "penguin", "ostrich"]
    exceptions = ["penguin", "ostrich"]

    if animal.lower() not in birds:
        print(f"3. {animal} is not a bird, so the rule doesn’t apply.")
        print(f"Conclusion: I don’t know if {animal} can fly.")
    elif animal.lower() in exceptions:
        print(f"3. However, {animal} is an exception.")
        print(f"Conclusion: {animal} cannot fly.")
    else:
        print(f"3. {animal} follows the default rule.")
        print(f"Conclusion: {animal} can fly.")

animal_input = input("Enter an animal: ")
reasoning_process(animal_input)
