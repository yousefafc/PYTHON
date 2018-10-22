#!/usr/bin/python
first_names = ['Steve', 'Jane', 'Sara', 'Mary','Jack','Bob', 'Bily', 'Boni', 'Chris','Sori', 'Will', 'Won','Li']
def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]\
            (list(chunks(first_names, 5)))