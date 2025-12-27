import inspect


def one_level():
    print("one level")

    def second_level():
        print("second level")
    second_level()


string_representation = 'def one_level():\n\tprint("one level")\n\n\tdef second_level():\n\t\tprint("second level")\n\tsecond_level()'
raw = """
    def f():
        if True:
            x = 1
        y = 2
    z = 3
    """
braw = raw.replace("\n", '\\n')
braw = braw.replace(" ", '\\t')

print(braw)
print(string_representation)
print(repr(string_representation))

lines = string_representation.splitlines()


for line in lines:
    stripped = line.lstrip()

    print(stripped)
    print(len(line) - len(stripped))
