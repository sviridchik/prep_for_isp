intervals = [[6,9], [1,3]]
newInterval = [2, 5]
# intervals = [[3,5],[8,10],[1,2],[6,7],[12,16]]
# newInterval = [4,8]
# 1)a в один b в другой
# 2)a and b в один
# 3)ни в один

def f7(intervals,newInterval):
    a = newInterval[0]
    b = newInterval[-1]
    flag_a,flag_b = False,False
    new_res_Interval = []
    inter_a,inter_b = [],[]
    for inter in intervals:
        # 1)a в один b в другой
        if inter[0]<=a<=inter[-1]:
            new_res_Interval.append(inter[0])
            flag_a = True


        if inter[0] <= a <= inter[-1]:
            new_res_Interval.append(inter[-1])
            flag_b = True

    if not flag_a:
        new_res_Interval.append(a)
    if not flag_b:
        new_res_Interval.append(b)
    if len(new_res_Interval)==2 and new_res_Interval[-1]<b:
        new_res_Interval[-1]  = b
    intervals.append(new_res_Interval)

    # print(intervals)
    intervals.sort()
    # print(intervals)
    # cleaning
    # for inter in intervals:
    #     for int2 in intervals[::-1]:
    #         if inter[0]>=int2
    rm = []
    add = []
    for i in range(len(intervals)-1):
        for j in range(len(intervals)-1):
            el1 = intervals[i]
            if j == i:
                continue
            el2 = intervals[j]
            # first match
            # tmp = []
            if el1[0] == el2[0]:
                tmp = []
                tmp.append(el2[0])
                tmp.append(max(el1[-1],el2[-1]))
                rm.append(el1)
                rm.append(el2)
                add.append(tmp)
            # second match
            if el1[-1] == el2[-1]:
                tmp = []
                tmp.append(min(el1[0], el2[0]))
                tmp.append(el2[-1])
                rm.append(el1)
                rm.append(el2)
                add.append(tmp)
            if el1[-1] == el2[0]:
                tmp = []
                tmp.append(el1[0])
                tmp.append(el2[-1])
                rm.append(el1)
                rm.append(el2)
                add.append(tmp)
            if el1[0]>=el2[0] and el1[-1]<= el2[-1] and el1 not in rm:
                # tmp = []
                # tmp.append(el2)
                rm.append(el1)
                # add.append(tmp)
            if el2[0] >= el1[0] and el2[-1] <= el1[-1]:
                # tmp = []
                # tmp.append(el1)
                rm.append(el2)
                # add.append(tmp)
    # print(intervals)
    for el in add:
        intervals.append(el)
    for el in rm:
        if el in intervals:
            intervals.remove(el)

    print(intervals)
    return intervals
f7(intervals,newInterval)
