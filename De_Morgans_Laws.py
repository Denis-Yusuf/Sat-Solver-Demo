from z3 import *

# Create P and Q variables in z3
P = Bool('P')
Q = Bool('Q')

# Theorem 1
theorem_1 = Not(And(P, Q)) == Or(Not(P), Not(Q))

# Theorem 2
theorem_2 = Not(Or(P, Q)) == And(Not(P), Not(Q))

# Create Z3 solver
s = Solver()

# Add negation of theorems to solver
s.add(Not(theorem_1))
s.add(Not(theorem_2))

# Check if theorems hold or not
if __name__ == '__main__':
    if s.check() == sat:
        print("Theorems are not valid.")
    else:
        print("Theorems are valid.")
