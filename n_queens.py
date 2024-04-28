from z3 import *

# Turn the queens into z3 variables
def create_queens(n : int) -> list[ArithRef]:
    return [Int('q_%i' % i) for i in range(n)]

# add row constraint
def add_row_constraints(solver : Solver, queens : list[ArithRef]) -> None:
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            solver.add(queens[i] != queens[j])

# add diagonal constraint
def add_diagonal_constraints(solver : Solver, queens : list[ArithRef]) -> None:
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            solver.add(queens[i] - queens[j] != i - j)
            solver.add(queens[i] - queens[j] != j - i)

# add the bounds
def add_bounds_constraints(solver : Solver, queens : list[ArithRef], n : int) -> None:
    for q in queens:
        solver.add(q >= 0, q < n)

# solve for n queens
def solve_n_queens(n):
    solver = Solver()
    queens = create_queens(n)
    add_row_constraints(solver, queens)
    add_diagonal_constraints(solver, queens)
    add_bounds_constraints(solver, queens, n)

    if solver.check() == sat:
        model = solver.model()
        for q in queens:
            print(model[q])
    else:
        print("No Solution!")


if __name__ == "__main__":
    print("-----Solving for 8 queens-----")
    solve_n_queens(8)
    print("-----Solving for 5 queens-----")
    solve_n_queens(8)
    print("-----Solving for 3 queens-----")
    solve_n_queens(3)
