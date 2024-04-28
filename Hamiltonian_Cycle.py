from z3 import *

# Create Z3 variables for the edges
def create_boolean_variables(graph_length : int) -> list[list[BoolRef]]:
    return [[Bool(f"edge_{i}_{j}") for j in range(graph_length)] for i in range(graph_length)]

# The vertex visitation constraint
def add_vertex_visitation_constraints(solver : Solver, edges : list[list[BoolRef]], graph : list[tuple[int, int]]) -> None:
    graph_length = len(graph)
    for i in range(graph_length):
        solver.add(Or([edges[i][j] for j in range(graph_length) if (i, j) in graph or (j, i) in graph]))

# The cycle constraint (note vertex visitation constraint and cycle constraint could be under the same loop, but for readability reasons I am avoiding this)
def add_cycle_constraint(solver : Solver, edges : list[list[BoolRef]], graph : list[tuple[int, int]]) -> None:
    graph_length = len(graph)
    for i in range(graph_length):
        for j in range(graph_length):
            for k in range(graph_length):
                for l in range(graph_length):
                    if (i, j) in graph and (j, k) in graph and (k, l) in graph and (l, i) in graph:
                        solver.add(Or([edges[i][j], edges[j][k], edges[k][l], edges[l][i]]))


def find_hamiltonian_cycle(graph : list[tuple[int, int]]):
    solver = Solver()
    edges = create_boolean_variables(len(graph))
    add_vertex_visitation_constraints(solver, edges, graph)
    add_cycle_constraint(solver, edges, graph)

    if solver.check() == sat:
        model = solver.model()
        cycle = [(i, j) for i in range(len(graph)) for j in range(len(graph)) if model[edges[i][j]] == True]
        return cycle
    return None

# Check if there is a ham cycle or not and print it
def check_cycle(graph : list[tuple[int, int]]) -> None:
    cycle = find_hamiltonian_cycle(graph)
    if cycle:
        print("Hamiltonian cycle exists:", cycle)
    else:
        print("No Hamiltonian cycle exists.")

if __name__ == "__main__":
    # Example graph represented as an adjacency list with Hamiltonian cycle
    graph_sat = [(0, 1), (1, 2), (2, 3), (3, 0)]
    # Example graph represented as an adjacency list without Hamiltonian cycle
    graph_unsat = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 2)]
    check_cycle(graph_sat)
    check_cycle(graph_unsat)


