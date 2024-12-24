import sys
from itertools import takewhile

GateConf = tuple[str, tuple[str, str]]


def wire_from_str(s: str) -> tuple[str, int]:
    name, value = s.partition(": ")[::2]
    return name, int(value)


def gate_from_str(s: str) -> tuple[str, GateConf]:
    name, conf = s.rpartition(" -> ")[::2][::-1]
    in0, op, in1 = conf.split(" ")
    return name, (op, (in0, in1))


def load():
    wires = dict(
        wire_from_str(line.rstrip())
        for line in takewhile(lambda l: l != "\n", sys.stdin)
    )
    gates = dict(gate_from_str(line.rstrip()) for line in sys.stdin)
    return gates, wires
