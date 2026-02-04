# same as list but unordered and can not contain duplicate and used {} instead of list's []

nums={1,3,4,5,7,8,1,4,8}

print(nums)

# it is unordered in terms of memory

arr={12,2,4,5,6,7,2,4}
print(arr)

# remove the element 7 from the arr

arr.discard(7)
print(arr)

# remove all elements from the set
arr.clear()
print(arr)

# add 1 single element
arr.add(199)
print(arr)

# add more elements at once
arr.update([12,13])
print(arr)