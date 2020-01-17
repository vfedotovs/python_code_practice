# summ_with_recursion.py

### Spurce Mark lutz Learning python 5th edition


alist = [1, 2, 3, 4, 5, 7, 8, 9, 10]

def mysum(L):
	if not L:
		return 0
	else:
		return L[0] + mysum(L[1:]) # Call myself recursively


print(mysum(alist))



alist = [1, 2, 3, 4, 5, 7, 8, 9, 10]

def mysum2(L):
	print(L)  # Alows to see recursiveness
	if not L:
		return 0
	else:
		return L[0] + mysum2(L[1:]) # Call myself recursively


def mysum_tern(L):
	return 0 if not L else L[0] + mysum_tern(L[1:]) # Use ternary expression


def mysum3(L):
	return L[0] if len(L) == 1 else L[0] + mysum3(L[1:]) # Any type, assume one


print(mysum(alist))
print(mysum2(alist))
print(mysum_tern(alist))
print(mysum3(alist))


### llop vs recursion 

sum = 0
while alist:
	sum += alist[0]
	alist = alist[1:]

print("Iterative way sum list elements:", sum)


#end_sum = 0
#for x in alist: end_sum += x
#print("Iterative comprehension way:", end_sum)

"""
Handling Arbitrary Structures

On the other hand, recursion—or equivalent explicit stack-based algorithms we’ll
meet shortly—can be required to traverse arbitrarily shaped structures. As a simple
example of recursion’s role in this context, consider the task of computing the sum of
all the numbers in a nested sublists structure like this:
[1, [2, [3, 4], 5], 6, [7, 8]] # Arbitrarily nested sublists
Simple looping statements won’t work here because this is not a linear iteration. Nested
looping statements do not suffice either, because the sublists may be nested to
arbitrary depth and in an arbitrary shape—there’s no way to know how many nested
loops to code to handle all cases. Instead, the following code accommodates such general
nesting by using recursion to visit sublists along the way:
"""

def sumtree(L):
	tot = 0
	for x in L: # For each item at this level
		if not isinstance(x, list):
			tot += x # Add numbers directly
		else:
			tot += sumtree(x) # Recur for sublists
	return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]] # Arbitrary nesting

print(sumtree(L)) # Prints 36
# Pathological cases
print("(right-heavy)", sumtree([1, [2, [3, [4, [5]]]]])) # Prints 15 (right-heavy)
print("(left-heavy)", sumtree([[[[[1], 2], 3], 4], 5])) # Prints 15 (left-heavy)


"""
Recursion versus queues and stacks
It sometimes helps to understand that internally, Python implements recursion by
pushing information on a call stack at each recursive call, so it remembers where it
must return and continue later. In fact, it’s generally possible to implement recursivestyle
procedures without recursive calls, by using an explicit stack or queue of your
own to keep track of remaining steps.
For instance, the following computes the same sums as the prior example, but uses an
explicit list to schedule when it will visit items in the subject, instead of issuing recursive
calls; the item at the front of the list is always the next to be processed and summed:

"""


def sumtree_one(L):            # Breadth-first, explicit queue
	tot = 0
	items = list(L)        # Start with copy of top level
	while items:
		front = items.pop(0) # Fetch/delete front item
		if not isinstance(front, list):
			tot += front     # Add numbers directly
		else:
			items.extend(front) # <== Append all in nested list
	return tot


print("Summtree 1:", sumtree(alist))

def sumtree_two(L): # Depth-first, explicit stack
	tot = 0
	items = list(L) # Start with copy of top level
	while items:
		front = items.pop(0) # Fetch/delete front item
		if not isinstance(front, list):
			tot += front # Add numbers directly
		else:
			items[:0] = front # <== Prepend all in nested list
	return tot

print("Summtree_one:", sumtree_one(alist))
print("Summtree_two:", sumtree_two(alist))

"""
For more on the last two examples (and another variant), see file sumtree2.py in the
book’s examples. It adds items list tracing so you can watch it grow in both schemes,
and can show numbers as they are visited so you see the search order. For instance,
the breadth-first and depth-first variants visit items in the same three test lists used
for the recursive version in the following orders, respectively (sums are shown last):


In general, though, once you get the hang of recursive calls, they are more natural
than the explicit scheduling lists they automate, and are generally preferred unless
you need to traverse structure in specialized ways. Some programs, for example, perform
a best-first search that requires an explicit search queue ordered by relevance or
other criteria. If you think of a web crawler that scores pages visited by content, the
applications may start to become clearer.	
"""	


"""
Cycles, paths, and stack limits
As is, these programs suffice for our example, but larger recursive applications can
sometimes require a bit more infrastructure than shown here: they may need to avoid
cycles or repeats, record paths taken for later use, and expand stack space when using
recursive calls instead of explicit queues or stacks.
For instance, neither the recursive call nor the explicit queue/stack examples in this
section do anything about avoiding cycles—visiting a location already visited. That’s
not required here, because we’re traversing strictly hierarchical list object trees. If data
can be a cyclic graph, though, both these schemes will fail: the recursive call version
will fall into an infinite recursive loop (and may run out of call-stack space), and the
others will fall into simple infinite loops, re-adding the same items to their lists (and
may or may not run out of general memory). Some programs also need to avoid
repeated processing for a state reached more than once, even if that wouldn’t lead to a
loop

To do better, the recursive call version could simply keep and pass a set, dictionary, or
list of states visited so far and check for repeats as it goes. We will use this scheme in
later recursive examples in this book:
if state not in visited:
visited.add(state) # x.add(state), x[state]=True, or x.append(state)
...proceed...
The nonrecursive alternatives could similarly avoid adding states already visited with
code like the following. Note that checking for duplicates already on the items list
would avoid scheduling a state twice, but would not prevent revisiting a state traversed
earlier and hence removed from that list:
visited.add(front)
...proceed...
items.extend([x for x in front if x not in visited])
This model doesn’t quite apply to this section’s use case that simply adds numbers in
lists, but larger applications will be able to identify repeated states—a URL of a previously
visited web page, for instance. In fact, we’ll use such techniques to avoid cycles
and repeats in later examples listed in the next section.
Some programs may also need to record complete paths for each state followed so
they can report solutions when finished. In such cases, each item in the nonrecursive
scheme’s stack or queue may be a full path list that suffices for a record of states visited,
and contains the next item to explore at either end.
Also note that standard Python limits the depth of its runtime call stack—crucial to
recursive call programs—to trap infinite recursion errors. To expand it, use the sys
module:
>>> sys.getrecursionlimit() # 1000 calls deep default
1000
>>> sys.setrecursionlimit(10000) # Allow deeper nesting
>>> help(sys.setrecursionlimit) # Read more about it
The maximum allowed setting can vary per platform. This isn’t required for programs
that use stacks or queues to avoid recursive calls and gain more control over the traversal
process

"""

"""
More recursion examples
Although this section’s example is artificial, it is representative of a larger class of programs;
inheritance trees and module import chains, for example, can exhibit similarly
general structures, and computing structures such as permutations can require arbitrarily
many nested loops. In fact, we will use recursion again in such roles in more
realistic examples later in this book:
• In Chapter 20’s permute.py, to shuffle arbitrary sequences
• In Chapter 25’s reloadall.py, to traverse import chains
In Chapter 29’s classtree.py, to traverse class inheritance trees
• In Chapter 31’s lister.py, to traverse class inheritance trees again
• In Appendix D’s solutions to two exercises at the end of this part of the book:
countdowns and factorials
The second and third of these will also detect states already visited to avoid cycles and
repeats. Although simple loops should generally be preferred to recursion for linear
iterations on the grounds of simplicity and efficiency, we’ll find that recursion is
essential in scenarios like those in these later examples.


"""
