# Python script that randomly shuffles the group order with the condition that "Gr 6" appears among the first three groups:
import random

groups = ["Gr 1", "Gr 2", "Gr 3", "Gr 4", "Gr 5", "Gr 6", "Gr 7", "Gr 10", "Gr 11", "Gr 12", "Gr 13"]

# Ensure "Gr 6" is among the first 3 groups
def generate_order_with_constraint(groups, target="Gr 6", constraint_index=3):
    others = [g for g in groups if g != target]
    random.shuffle(others)

    # Pick a random position among the first 3 to insert Gr 6
    insert_index = random.randint(0, constraint_index - 1)
    presentation_order = others[:insert_index] + [target] + others[insert_index:]
    return presentation_order

# Generate and print
order = generate_order_with_constraint(groups)
print("Presentation Order:")
for i, group in enumerate(order, 1):
    print(f"{i}. {group}")