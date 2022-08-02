import cplex
import docplex.mp
import sys
import json
from docplex.util.environment import get_environment
from docplex.mp.model import Model


model = Model(name='LP_example', log_output=True)

x1 = model.continuous_var(name='x1')
x2 = model.continuous_var(name='x2')

model.maximize(5*x1 + 4*x2)

model.add_constraint(6*x1 + 4*x2 <= 24)
model.add_constraint(x1 + 2*x2 <= 6)
model.add_constraint(-1*x1 + x2 <= 1)
model.add_constraint(x2 <= 2)
model.add_constraint(x1 >= 0)
model.add_constraint(x2 >= 0)



model.print_information()
sol_model = model.solve()
model.print_solution()

# how are you?