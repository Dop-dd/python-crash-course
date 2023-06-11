# Start with some designs that need to be printed

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f" printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print(f"\nthe following models have been completed: ")
for completed_model in completed_models:
    print(completed_model)