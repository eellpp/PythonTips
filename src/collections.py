

## Different ways of comprehension
aList = [i for i in range(1,10)]
## Out[71]: [1, 2, 3, 4, 5, 6, 7, 8, 9]

aSet = {i for i in range(1,10)}
### Out[72]: set([1, 2, 3, 4, 5, 6, 7, 8, 9])

aDict = {i:i for i in range(1,10)}
##Out[73]: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

## but this returns a generator
aGenerator = (i for i in range(1,10))
list(aGenerator)
#Out[84]: [1, 2, 3, 4, 5, 6, 7, 8, 9]
