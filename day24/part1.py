from common import GateConf, load

OPS = {
    "AND": lambda a, b: a & b,
    "OR": lambda a, b: a | b,
    "XOR": lambda a, b: a ^ b,
}

gates, wires = load()


def eval_gate(
    name: str,
) -> int:
    op, (a, b) = gates[name]
    return OPS[op](
        eval_gate(a) if a in gates else wires[a],
        eval_gate(b) if b in gates else wires[b],
    )


z_gate_names = sorted(x for x in gates.keys() if x.startswith("z"))

z_gate_values = [eval_gate(x) for x in z_gate_names]

number = sum(x << i for i, x in enumerate(z_gate_values))

assert number == 57588078076750
