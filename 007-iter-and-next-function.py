# Declaring iterable (list)
items = [1, 2, 3, 4, 5]

# Creating iterator using the iter() method on the list created
iterator = iter(items)

# Creating while loop until we hit the dead-end of the iterator
while True:

    # Enclosed next() of iterator inside try & except to raise exception when we get to the end of iterator
    try:

        # Getting the next available item
        item = next(iterator)

        # Printing item
        print(item)
    except StopIteration:
        break

