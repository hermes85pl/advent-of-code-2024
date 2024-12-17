from common import execute, load

registries, program = load()

output_str = ",".join(str(x) for x in execute(program, registries))

assert output_str == "7,5,4,3,4,5,3,4,6"
