"""
Enumerate objects and create a list out of that in one expression.
"""

sample = {
    'items': [ 1, 2, 3, 4],
    'other': [ 8, 2, 3, 4]
}

items = [ item for item in sample['items'] ]
otha = [ item for item in sample['other'] ]
print items
print otha
