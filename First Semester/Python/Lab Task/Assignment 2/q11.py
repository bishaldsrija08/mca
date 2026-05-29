# Create a list with the ordered pair {(2,3),(1,4),(4,2),(5,6),(6,2)} and a function that returns the sum of two numbers. Use list comprehension to get the sum of each ordered pairs.
ordered_pairs = [(2,3), (1,4), (4,2), (5,6), (6,2)]

def sum_of_numbers(x, y):
    return x + y

sums = [sum_of_numbers(x, y) for x, y in ordered_pairs]
print("The sums of the ordered pairs are:", sums)