
def PatternUnlock(N, hits):
    dist_len = 0
    if (set([1,5]).issubset(hits)) or (set([5,1]).issubset(hits)):
        dist_len += 1.4142135
    elif (set([9,2]).issubset(hits)) or (set([2,9]).issubset(hits)):
        dist_len += 1.4142135
    elif (set([4,2]).issubset(hits)) or (set([2,4]).issubset(hits)):
        dist_len += 1.4142135
    elif (set([8,3]).issubset(hits)) or (set([3,8]).issubset(hits)):
        dist_len += 1.4142135
    elif (set([3,5]).issubset(hits)) or (set([5,3]).issubset(hits)):
        dist_len += 1.4142135
    elif (set([6,2]).issubset(hits)) or (set([2,6]).issubset(hits)):
        dist_len += 1.4142135
    elif (set([7,2]).issubset(hits)) or (set([2,7]).issubset(hits)):
        dist_len += 1.4142135
    elif (set([8,1]).issubset(hits)) or (set([1,8]).issubset(hits)):
        dist_len += 1.4142135
    elif (set([9,1]).issubset(hits)) or (set([1,9]).issubset(hits)):
        dist_len += 1
    elif (set([6,1]).issubset(hits)) or (set([1,6]).issubset(hits)):
        dist_len += 1
    elif (set([2,5]).issubset(hits)) or (set([5,2]).issubset(hits)):
        dist_len += 1
    elif (set([2,8]).issubset(hits)) or (set([8,2]).issubset(hits)):
        dist_len += 1
    elif (set([4,3]).issubset(hits)) or (set([3,4]).issubset(hits)):
        dist_len += 1
    elif (set([3,7]).issubset(hits)) or (set([7,3]).issubset(hits)):
        dist_len += 1
    elif (set([6,5]).issubset(hits)) or (set([5,6]).issubset(hits)):
        dist_len += 1
    elif (set([5,4]).issubset(hits)) or (set([4,5]).issubset(hits)):
        dist_len += 1
    elif (set([2,1]).issubset(hits)) or (set([1,2]).issubset(hits)):
        dist_len += 1
    elif (set([2,3]).issubset(hits)) or (set([3,2]).issubset(hits)):
        dist_len += 1
    elif (set([9,8]).issubset(hits)) or (set([8,9]).issubset(hits)):
        dist_len += 1
    elif (set([8,7]).issubset(hits)) or (set([7,8]).issubset(hits)):
        dist_len += 1
    dist_len = str(dist_len)
    if '.' in dist_len:
        dist_len = dist_len.replace('.','')
    elif '0' in dist_len:
        dist_len = dist_len.replace('0','')
    return dist_len
