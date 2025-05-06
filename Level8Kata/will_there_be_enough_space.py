def enough(cap, on, wait):
    # Your code here
    spaceLeft = cap - on
    ans = wait - spaceLeft
    if (ans < 0):
        return 0
    return ans