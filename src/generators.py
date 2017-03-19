
"""
list, dict and set are iterables
files are also iterables


## this returns an iterators
iterator = iter(range(1,10))

## do iterator.next() ten times to read the items

## you can read the items in iterators lazily
## once the items are read they are not available
for x in iterator:
    print(iterator)
"""


"""
generator is a special kind of iterator
There are two types of generators in Python: generator functions and generator expressions.
A generator function is any function in which the keyword yield appears in its body.
"""
def generateIntegers():
    i = 0
    while i < 10:
        yield i
        i = i + 1

## generateIntegers is a function
## gen is generator. The function returns a generator using the yield keyword
## next(gen) returns the next value from the generator
gen = generateIntegers()
for i in range(1,3):
    print(next(gen))

print(list(generateIntegers()))

## this expression also returns a generator. The same result as above
aGenerator = ( i for i in range(0,10))
print(list(aGenerator))

## itertools package contains useful iterators

