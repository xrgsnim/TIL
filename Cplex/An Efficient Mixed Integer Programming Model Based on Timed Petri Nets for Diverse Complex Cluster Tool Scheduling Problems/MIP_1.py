import numpy as np
import docplex.cp.expression
import docplex.mp.model as cpx

# create model
m = cpx.Model(name="MIP")
inf = docplex.cp.expression.INFINITY


# set parameter
# 작성해줘야 할 것 : v, w, incidence_matrix, M[0], holdingtime, 이 5개만 정해주면 끝

v = int(1)
w = int(1)

incidence_matrix = np.array([[1, -1, 0, 0, 0, 0, 0, 0],
                            [0, 1, -1, 0, 0, 0, 0, 0],
                            [0, -1, 1, 0, 0, 0, 0, 0],
                            [0, 0, 1, -1, 0, 0, 0, 0],
                            [0, 0, 0, 1, -1, 0, 0, 0],
                            [0, 0, 0, -1, 1, 0, 0, 0],
                            [0, 0, 0, 0, 1, -1, 0, 0],
                            [0, 0, 0, 0, 0, 1, -1, 0],
                            [0, 0, 0, 0, 0, -1, 1, 0],
                            [0, 0, 0, 0, 0, 0, 1, -1],
                            [-1, 1, -1, 1, -1, 1, -1, 1]])

num_transition = len(incidence_matrix[0])
num_place = len(incidence_matrix)

M = np.empty((num_transition+1, num_place), dtype=object)
M[0] = np.array([0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 2])

bigM = int(10000)
prc_time_of_PMs = np.array([100, 200, 100])
holdingtime = np.array([w+v, w+prc_time_of_PMs[0], 0, w+v, w+prc_time_of_PMs[1], 0, w+v, w+prc_time_of_PMs[2], 0, w+v, 0])


# non_conflict_place
# incidence_matrix를 돌며 각 place가 non_conflict한지 판별
# [1 1 1 1 1 1 1 1 1 1 0] 이렇게 생김, 1이면 non_conflict
non_conflict_place = np.array([0]*num_place)
for i in range(num_place):
   if ((np.where(incidence_matrix==-1))[0] == i).sum() == 1:
       non_conflict_place[i] = 1





# create decision variables
# cycletime
cycletime = m.continuous_var(0, inf, 'cycletime')

# x
x = np.empty(num_transition, dtype=object)
for i in range(len(non_conflict_place)):
    if non_conflict_place[i] == 1:
        for j in range(num_transition):
            if incidence_matrix[i][j] != 0 and x[j] is None:
                x[j] = m.continuous_var(0, inf, 'x[' + str(j) + ']')


# S
S = np.empty(num_transition, dtype=object)
for i in range(len(non_conflict_place)):
    if non_conflict_place[i] == 1:
        for j in range(num_transition):
            if incidence_matrix[i][j] != 0 and S[j] is None:
                S[j] = m.continuous_var(0, inf, 'S[' + str(j) + ']')

# z
z = np.empty((num_transition, num_transition), dtype=object)
for i in range(num_transition):
    for j in range(num_transition):
        z[i][j] = m.binary_var('z['+str(i)+']['+str(j)+']')



# M, M0는 위에서 초기 parameter로 지정해줬고, M1부터 decision variable
for i in range(1, num_transition+1):
    for j in range(num_place):
        M[i][j] = m.integer_var(0,inf, 'M['+str(i)+']['+str(j)+']')





#constraints
# (16)
for i in range(len(non_conflict_place)):
    if non_conflict_place[i] == 1 :
        for j in range(num_transition):
            if incidence_matrix[i][j] == 1:
                back = x[j]
            elif incidence_matrix[i][j] == -1:
                front = x[j]

        m.add_constraint(front - back >= holdingtime[i] - M[0][i]*cycletime)



# (17)
incidence_matrix_by_z = np.empty((9,11), dtype=object)
for i in range(num_transition):
    incidence_matrix_by_z[i+1] = np.dot(incidence_matrix, z[i])


for i in range(1, num_transition+1):
    for j in range(num_place):
        m.add_constraint(M[i][j] == M[i-1][j] + incidence_matrix_by_z[i][j])



# (18) (19)
for i in range(num_transition):
    m.add_constraint((z.sum(axis=0))[i] == 1)
    m.add_constraint((z.sum(axis=1))[i] == 1)



# (20)
for i in range(num_transition-1):
    m.add_constraint(S[i] - S[i+1] <= -(v + w))


# (21)
m.add_constraint(S[num_transition-1] - (S[0] + cycletime) <= -(v + w))



# (22) (23)
for k in range(num_transition):
    for i in range(num_transition):
        m.add_constraint(S[k] - x[i] <= (1 - z[k][i])*bigM)
        m.add_constraint(S[k] - x[i] >= (z[k][i] - 1)*bigM)




# Solve
m.minimize(cycletime)
m.print_information()
solver = m.solve() #(log_output=True)
if solver is not None:
    m.print_solution()
else:
    print("Solver is error")