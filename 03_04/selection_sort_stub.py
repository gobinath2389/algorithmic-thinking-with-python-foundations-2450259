def selection_sort(xs):
    for i in range(len(xs)):
        small_idx = find_min(xs[i:])+i
        print(small_idx)
        xs[i],xs[small_idx] = xs[small_idx],xs[i]
    return xs

def find_min(arr):
    min_value = 0
    print(arr)
    for idx,value in enumerate(arr):
        if arr[min_value]> value:
            min_value = idx
    return min_value

xs = [3, 2, 1, 5, 4]
print(xs)
selection_sort(xs)
print(xs)

# A nice Pythonic way to check  a list is sorted
# without relying on using Python's own sorting methods to compare.
print(all(xs[i] <= xs[i + 1] for i in range(len(xs) - 1)))
