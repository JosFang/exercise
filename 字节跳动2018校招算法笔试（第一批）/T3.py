# """
# 解题思路：
# time_ideas字典
# while Ture:
#     time += 1
#     更新执行队列任务剩余时间
#     删除执行完的idea，更新程序员数量，记录完成时间
#     if 执行队列为空 and p = 0:
#         break
#     更新每个pm现有的idea
#     pm_ideas字典
#     while 还有程序员 并且 任务数p > 0：
#         找出每个pm现有的最想实现的idea
#         判断实现哪个idea，并加入执行队列,并从待执行队列中删除
#         任务数p -= 1
#         程序员数m -= 1
#
# """
#
#
#
#
# def find_times(pm_ideas, n, m, p):
#     """
#
#     :param pm_ideas:
#     :param n: n个pm
#     :param m:m个程序员, p个idea
#     :return:
#     """
#     for pm in pm_ideas:
#         pm_ideas[pm] = sorted(pm_ideas[pm], key=lambda s: (-s[1], s[2], s[0]))
#
#     ideas = []  # 当前每个pm最想实现的idea
#     for pm in pm_ideas:
#         if pm_ideas[pm] != []:
#             pm_ideas[pm][0].append(pm)
#             ideas.append(pm_ideas[pm][0])    # 4:提出这个idea的pm的编号
#     # ideas = sorted(ideas, key=lambda s: (s[2], s[3]))
#     task_rest_time = []
#     cur_time = 0
#     finsh_tasks = []
#     while True:
#         while m > 0 and p > 0:  # 让所有程序员干活
#
#             cur_idea = find_most_idea(ideas)
#             pm_ideas[cur_idea[4]].pop(0)
#             ideas.remove(cur_idea)
#             if pm_ideas[cur_idea[4]] != []:
#                 pm_ideas[cur_idea[4]][0].append(cur_idea[4])
#                 ideas.append(pm_ideas[cur_idea[4]][0])
#                 # print('check')
#             p -= 1
#             m -= 1
#             task_rest_time.append(cur_idea)
#         if task_rest_time == []:
#             print(pm_ideas)
#             print(ideas)
#             print(p)
#             print(m)
#         time_min = min(task_rest_time, key=lambda s: s[2])[2]
#         cur_time += time_min
#         temp_i = []
#         for i in range(len(task_rest_time)):
#             task_rest_time[i][2] -= time_min
#             if task_rest_time[i][2] == 0:
#                 temp_i.append(i)
#         for i in temp_i:
#             finsh_tasks = task_rest_time.pop(i)
#             finsh_tasks.append(cur_time)  # 5:完成时间
#             m += 0
#
#         if p <= 0 and task_rest_time == []:
#             break
#     finsh_tasks = sorted(finsh_tasks, key=lambda s: s[3])
#     for t in finsh_tasks:
#         print(t[5])
#
#
#
# def find_most_idea(ideas):
#     temp_ideas = []
#     max_p = 0
#     for i in ideas:
#         if i[2] > max_p:
#             temp_ideas = []
#             temp_ideas.append(i)
#         if i[2] == max_p:
#             temp_ideas.append(i)
#
#     most_idea = temp_ideas[0]
#     for i in temp_ideas:
#         # print(i)
#         # print(most_idea)
#         if i[4] < most_idea[4]:
#             most_idea = i
#     return most_idea
#
#
# [n, m, p] = [int(i) for i in input().strip().split()]
#
# # 0：提出时间，1：优先等级，2：所需时间，3：任务序号
# pm_ideas = {}
# for i in range(p):
#     idea = [int(i) for i in input().strip().split()]
#     idea.append(i)
#     if idea[0] not in pm_ideas:
#         pm_ideas[idea[0]] = []
#     pm_ideas[idea[0]].append(idea[1:])
#
# find_times(pm_ideas, n, m, p)


def find_finsh_time(time_ideas, n_chengxuyuan, n_idea):
    time = 0
    zhixining_ideas = []
    finsh_ideas = []
    pm_ideas_dic = {}
    n_xinyou_ideas = 0
    while True:
        time += 1
        if zhixining_ideas != []:
            deleted_ideas = []
            for i in zhixining_ideas:
                i[3] -= 1
                if i[3] == 0:
                    deleted_ideas.append(i)
            for i in deleted_ideas:
                zhixining_ideas.remove(i)
                n_chengxuyuan += 1
                i.append(time)   # 5:执行完成时间
                finsh_ideas.append(i)
        if zhixining_ideas == [] and n_idea == 0:
            break

        for t in time_ideas:
            if t == time:
                for i in time_ideas[t]:
                    if i[0] not in pm_ideas_dic:
                        pm_ideas_dic[i[0]] = []
                    pm_ideas_dic[i[0]].append(i)
                    n_xinyou_ideas += 1
                break

        while n_chengxuyuan > 0 and n_xinyou_ideas > 0:
            pm_want_idea = []
            for i in pm_ideas_dic:
                if pm_ideas_dic[i] != []:
                    pm_want_idea.append(min(pm_ideas_dic[i], key=lambda s: (-s[2], s[3], s[1])))

            if pm_want_idea != []:
                want_idea = min(pm_want_idea, key=lambda s: (s[3], s[0]))
                zhixining_ideas.append(want_idea)
                pm_ideas_dic[want_idea[0]].remove(want_idea)
                n_idea -= 1
                n_xinyou_ideas -= 1
                n_chengxuyuan -= 1

    finsh_ideas = sorted(finsh_ideas, key=lambda s: s[4])
    for i in finsh_ideas:
        print(i[5])


# def find_want_idea(ideas, asix):
#     houxuan_ideas = []
#
#     for d in asix:
#         max_youxian = ideas[0]
#         houxuan_ideas.append(max_youxian)
#         for i in range(1, len(ideas)):
#             if ideas[i][d] == max_youxian[d]:
#                 houxuan_ideas.append(ideas[i])
#             if ideas[i][d] > max_youxian[d]:
#                 max_youxian = ideas[i]
#                 houxuan_ideas = []
#                 houxuan_ideas.append(max_youxian)
#
#         if len(houxuan_ideas) == 1:
#             return houxuan_ideas
#         ideas = houxuan_ideas
#         houxuan_ideas = []
#     return ideas

# [n_pm, n_chengxuyuan, n_idea] = [int(i) for i in input().strip().split()]
# time_ideas = {}
# for i in range(n_idea):
#     # 0:pm序号，1：提出时间，2：优先等级，3：所需时间,4：任务序号
#     idea = [int(i) for i in input().strip().split()]
#     idea.append(i)
#     if idea[1] not in time_ideas:
#         time_ideas[idea[1]] = []
#     time_ideas[idea[1]].append(idea)
# find_finsh_time(time_ideas, n_chengxuyuan, n_idea)

array = [[5,1,9], [1,8,6],[98,4,7], [9458,8,7]]
# print(find_want_idea(array, [1, 2]))
print(sorted(array, key=lambda x: x[0]))

# def func(x):
#     return x[1]**2-x[0]**3+456454
# print(max(array, key=func))
