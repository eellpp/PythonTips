## itertools contains number of useful tools for functional operation

from itertools import *

list(islice(count(10,1),10))
## Out[7]: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

list(repeat(10,2))
#Out[9]: [10, 10]

list(repeat(range(2),2))
#Out[10]: [[0, 1], [0, 1]]

## Joining multiple lists with chain
list(chain(range(1,10,3), range(50,100,15)))
#Out[13]: [1, 4, 7, 50, 65, 80, 95]

## In python string is a list of chars
"".join(chain("this is a word 1","this is word 2"))
#Out[19]: 'this is a word 1this is word 2'


list(takewhile(lambda x: x > 2, [6,7,8,2,6,7,3]))
#Out[25]: [6, 7, 8]

list(dropwhile(lambda x : x > 2, [6,7,8,2,6,7,3]))
#Out[27]: [2, 6, 7, 3]

## using groupby
## this work like uniq in shell. But sort the list first and then run command
names = [("john","doe"),("tom","simpson"),("john","davis"),("kurt","simpson")]
names.sort()
## [('john', 'davis'), ('john', 'doe'), ('kurt', 'simpson'), ('tom', 'simpson')]
[ k for k,g in groupby(names, lambda x: x[0])]
#Out[54]: ['john', 'kurt', 'tom']

[ list(g) for k,g in groupby(names, lambda x: x[1])]
"""
Out[55]:
[[('john', 'davis')],
 [('john', 'doe')],
 [('kurt', 'simpson'), ('tom', 'simpson')]]
"""
### Filter
list(ifilter((lambda x: x > 5),[1,9,4,7]))
#Out[57]: [9, 7]

## imap
## itertools.imap(function, *iterables)
## Make an iterator that computes the function using arguments from each of the iterables.
list(imap(pow,(2,3,4),(1,2,3)))
##Out[64]: [2, 9, 64]

## zip
list(izip((2,3,4),(1,2,3)))
##Out[65]: [(2, 1), (3, 2), (4, 3)]

permutations('ABCD', 2)
combinations('ABCD', 2)
combinations_with_replacement('ABCD', 2)