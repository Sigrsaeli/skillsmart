

def ConquestCampaign (N, M, L, battalion):
    days = 0
    areas = [[0 for j in range(M)] for i in range(N)]
    for i in range(len(battalion)):
        if i % 2 == 0:
            areas[battalion[i]-1][battalion[i+1]-1] = 1
            days = 1
    while sum([sum(areas[i]) for i in range(N)]) != N*M:
        for i in range(N):
            for j in range(M):
                if (areas[i][j] == 0) and ((areas[i-1][j] == 1) or (areas[i+1][j] == 1) or (areas[i][j-1] == 1) or (areas[i][j+1] == 1)):
                    areas[i][j] = 1
                if (i == N-1) and (j == M-1):
                    days += 1

    return days
