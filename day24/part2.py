from common import load

gates, _ = load()

swapped_gate_names: set[str] = set()


def swap_gates(a, b):
    gates[a], gates[b] = gates[b], gates[a]
    swapped_gate_names.update((a, b))


def find_gate_name(operator: str, inputs: tuple[str, str]):
    try:
        return next(
            name
            for name, (op, (a, b)) in gates.items()
            if op == operator and (inputs == (a, b) or inputs == (b, a))
        )
    except StopIteration:
        raise ValueError


z_gate_count = sum(1 for x in gates.keys() if x.startswith("z"))
c_gate_name = find_gate_name("AND", ("x00", "y00"))

for i in range(1, z_gate_count - 1):
    x_wire_name = f"x{i:02d}"
    y_wire_name = f"y{i:02d}"
    z_gate_name = f"z{i:02d}"

    t_gate_name = find_gate_name("XOR", (x_wire_name, y_wire_name))
    assert not t_gate_name.startswith("z")

    try:
        actual_z_gate_name = find_gate_name("XOR", (t_gate_name, c_gate_name))
        if actual_z_gate_name != z_gate_name:
            swap_gates(z_gate_name, actual_z_gate_name)
    except ValueError:
        for op, (a, b) in gates.values():
            if op == "XOR" and c_gate_name in (a, b):
                actual_t_gate_name = b if a == c_gate_name else a
                swap_gates(t_gate_name, actual_t_gate_name)
                t_gate_name = actual_t_gate_name
                break

    a_gate_name = find_gate_name("AND", (x_wire_name, y_wire_name))
    b_gate_name = find_gate_name("AND", (t_gate_name, c_gate_name))
    c_gate_name = find_gate_name("OR", (a_gate_name, b_gate_name))

answer = ",".join(sorted(swapped_gate_names))

assert answer == "kcd,pfn,shj,tpk,wkb,z07,z23,z27"
