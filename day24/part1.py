from common import load


def eval_gate(
    name: str, gates: dict[str, tuple[str, tuple]], wires: dict[str, int]
) -> int:
    op, (in0, in1) = gates[name]
    val0 = eval_gate(in0, gates, wires) if in0 in gates else wires[in0]
    val1 = eval_gate(in1, gates, wires) if in1 in gates else wires[in1]
    if op == "AND":
        return val0 & val1
    if op == "OR":
        return val0 | val1
    if op == "XOR":
        return val0 ^ val1
    raise ValueError(f"operator {op!r} not supported")


gates, wires = load()

z_gate_names = sorted(x for x in gates.keys() if x.startswith("z"))

z_gate_values = [eval_gate(x, gates, wires) for x in z_gate_names]

number = sum(x << i for i, x in enumerate(z_gate_values))

assert number == 57588078076750
