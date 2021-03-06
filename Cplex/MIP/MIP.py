import docplex.mp.model as cpx
import random
import pandas as pd


M_0 = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1]


n = 10
m = 5
set_I = range(1, n+1)
set_J = range(1, m+1)
c = {(i,j): random.normalvariate(0,1) for i in set_I for j in set_J}
a = {(i,j): random.normalvariate(0,5) for i in set_I for j in set_J}
l = {(i,j): random.randint(0,10) for i in set_I for j in set_J}
u = {(i,j): random.randint(10,20) for i in set_I for j in set_J}
b = {j: random.randint(0,30) for j in set_J}




opt_model = cpx.Model(name="MIP Model")

# if x is Continuousd
x_vars = {(i,j): opt_model.continuous_var(lb=l[i,j], ub= u[i,j],
                                 name="x_{0}_{1}".format(i,j))
for i in set_I for j in set_J}

# if x is Binarys
#x_vars  = {(i,j): opt_model.binary_var(name="x_{0}_{1}".format(i,j))
#for i in set_I for j in set_J}
#
## if x is Integer
#x_vars  = {(i,j): opt_model.integer_var(lb=l[i,j], ub= u[i,j],
#                              name="x_{0}_{1}".format(i,j))
#for i in set_I for j in set_J}



# <= constraints
constraints = {j :
opt_model.add_constraint(
ct=opt_model.sum(a[i,j] * x_vars[i,j] for i in set_I) <= b[j],
ctname="constraint_{0}".format(j))
    for j in set_J}
# >= constraints
#constraints = {j :
#opt_model.add_constraint(
#ct=opt_model.sum(a[i,j] * x_vars[i,j] for i in set_I) >= b[j],
#ctname="constraint_{0}".format(j))
#    for j in set_J}
## == constraints
#constraints = {j :
#opt_model.add_constraint(
#ct=opt_model.sum(a[i,j] * x_vars[i,j] for i in set_I) == b[j],
#ctname="constraint_{0}".format(j))
#    for j in set_J}


objective = opt_model.sum(x_vars[i,j] * c[i,j]
                          for i in set_I
                          for j in set_J)


# for maximization
opt_model.maximize(objective)
## for minimization
#opt_model.minimize(objective)


# solving with local cplex
opt_model.solve()
## solving with cplex cloud
#opt_model.solve(url="your_cplex_cloud_url", key="your_api_key")



opt_df = pd.DataFrame.from_dict(x_vars, orient="index",
                                columns = ["variable_object"])
opt_df.index = pd.MultiIndex.from_tuples(opt_df.index,
                                         names=["column_i", "column_j"])

opt_df.reset_index(inplace=True)