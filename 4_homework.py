
def MadMax(N, Tele):    
    Tele.sort()
    max_num = max(Tele)
    max_index = Tele.index(max_num)
    median_index = (len(Tele)//2)
    Tele.pop(max_index)
    Tele.insert(median_index, max_num)
    Tele[median_index+1:len(Tele)].sort()
    Tele[median_index+1:len(Tele)] = sorted(Tele[median_index+1:len(Tele)], reverse=True)

    return Tele
