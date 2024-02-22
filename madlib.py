# Collect data using the input function
large_object = input("Enter any large object: ")
plural_object = input("Enter large objects (plural): ")
adj = input("Enter an adjective: ")
body_part = input("Enter any body part: ")
restaurant = input("Enter a restaurant: ")
food1 = input("Enter any food: ")
food2 = input("Enter another food: ")


# Construct the story using f-string for better readability and conciseness
story = f"I had a very {adj} day. This morning, I dropped a box of {plural_object} on my {body_part}. " \
       f"At lunch, I went to {restaurant} for their delicious {food1}, but the waiter brought me {food2}, " \
       f"which I wasn't hungry for. Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof."


# Print the story
print(story)