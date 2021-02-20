
def SynchronizingTables(N, ids, salary):
    new_ids=sorted(ids)
    new_salary=sorted (salary)
    connect_dict=dict(zip(new_ids,new_salary))
    return_salary=[]
    return_salary.append(connect_dict[item] for item in ids)
    for i in return_salary:
        return list(i)
