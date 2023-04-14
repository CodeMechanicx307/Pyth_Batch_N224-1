lst = ( 10 , 20 , 20 , 30 , 40 , 50 , 50, 60)
def r_dpl (duplist):
    real_list=[]

    for value in duplist:
        if value not in real_list:
            real_list.append(value)
    return real_list
print(r_dpl(lst))




