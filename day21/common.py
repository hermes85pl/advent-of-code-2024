from itertools import chain, pairwise


def key_coords(keys: tuple[str, ...]) -> dict[str, tuple[int, int]]:
    return {key: (x, y) for y, row in enumerate(keys) for x, key in enumerate(row)}


NUMPAD_KEY_COORDS = key_coords(
    (
        "789",
        "456",
        "123",
        " 0A",
    )
)

DIRPAD_KEY_COORDS = key_coords(
    (
        " ^A",
        "<v>",
    )
)


def setup(robot_count: int):
    layer_key_transition_costs = {
        (0, key0, key1): 1 for key0 in DIRPAD_KEY_COORDS for key1 in DIRPAD_KEY_COORDS
    }

    def min_cost(keys: str, layer: int) -> int:
        return sum(
            layer_key_transition_costs[(layer, key0, key1)]
            for key0, key1 in pairwise(chain("A", keys))
        )

    def fill_layer_key_transition_costs(layer: int, key_coords) -> None:
        for key0, (x0, y0) in key_coords.items():
            for key1, (x1, y1) in key_coords.items():
                hor_keys = (">" if x1 > x0 else "<") * abs(x1 - x0)
                ver_keys = ("^" if y1 < y0 else "v") * abs(y1 - y0)
                alt_keys: set[str] = set()
                if (x1, y0) != key_coords[" "]:
                    alt_keys.add(f"{hor_keys}{ver_keys}A")
                if (x0, y1) != key_coords[" "]:
                    alt_keys.add(f"{ver_keys}{hor_keys}A")
                if alt_keys:
                    cost = min(min_cost(keys, layer - 1) for keys in alt_keys)
                    layer_key_transition_costs[(layer, key0, key1)] = cost

    for layer in range(1, robot_count):
        fill_layer_key_transition_costs(layer, DIRPAD_KEY_COORDS)

    fill_layer_key_transition_costs(robot_count, NUMPAD_KEY_COORDS)

    def cost(code: str) -> int:
        return min_cost(code, robot_count)

    return cost
