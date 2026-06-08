def math_operations(*args, **kwargs):
    operations = ["a", "s", "d", "m"]

    for index, number in enumerate(args):
        current_operation = operations[index % 4]

        if current_operation == "a":
            kwargs["a"] += number

        elif current_operation == "s":
            kwargs["s"] -= number

        elif current_operation == "d":
            if number != 0:
                kwargs["d"] /= number

        elif current_operation == "m":
            kwargs["m"] *= number

    sorted_items = sorted(
        kwargs.items(),
        key=lambda kvp: (-kvp[1], kvp[0])
    )

    result = []

    for key, value in sorted_items:
        result.append(f"{key}: {value:.1f}")

    return "\n".join(result)

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))