import sys

arguments = sys.argv[1:]

if len(arguments) > 0:
    shortest = arguments[0]

    for arg in arguments:
        if len(arg) < len(shortest):
            shortest = arg

    print(f"The shortest argument is: {shortest}")
else:
    print("No arguments given")
