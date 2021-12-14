alist = ("a", "c", "d", "f", "f", "h", "t")


def find(alist, value, left, right):
    while(left <= right):
        mid = (right//2)
        if alist[mid] == value:
            return True
        elif value < alist[mid]:
            right = mid - 1
        else:
            left = alist[mid] + 1
        return False

a = find(alist, 'h', 0, len(alist))
print(a)