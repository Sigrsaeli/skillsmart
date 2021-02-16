
def ConquestCampaign (N, M, L, battalion):
    days = 0
    areas = [[0 for j in range(M)] for i in range(N)]
    for i in range(len(battalion)):
        if i % 2 == 0:
            areas[battalion[i]-1][battalion[i+1]-1] = 1
    while any(0 in row for row in areas):
        for i in range(N):
            for j in range(M):
                if areas[i][j] >= 1:
                    areas[i][j] += 1
                    if (i == 0) and (j != 0) and (j != M-1):
                        areas[i][j+1] += 1
                        areas[i][j-1] += 1
                        areas[i+1][j] += 1
                    elif (i != 0) and (i != N-1) and (j == 0):
                        areas[i-1][j] += 1
                        areas[i+1][j] += 1
                        areas[i][j+1] += 1
                    elif (i != 0) and (i != N - 1) and (j == M-1):
                        areas[i-1][j] += 1
                        areas[i+1][j] += 1
                        areas[i][j-1] += 1
                    elif (i == 0) and (j == 0):
                        areas[i+1][j] += 1
                        areas[i][j+1] += 1
                    elif (i == N-1) and (j == M-1):
                        areas[i-1][j] += 1
                        areas[i][j-1] += 1
                    elif (i == N-1) and (j != 0) and (j != M-1):
                        areas[i][j+1] += 1
                        areas[i][j-1] += 1
                        areas[i-1][j] += 1
                    elif (i == N-1) and (j == 0):
                        areas[i-1][j] += 1
                        areas[i][j+1] += 1
                    elif (i == 0) and (j == M-1):
                        areas[i+1][j] += 1
                        areas[i][j-1] += 1
                    else:
                        areas[i+1][j] += 1
                        areas[i-1][j] += 1
                        areas[i][j+1] += 1
                        areas[i][j-1] += 1
        print(areas)
        days += 1
    return days

