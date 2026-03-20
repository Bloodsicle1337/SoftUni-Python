def data_type_result(data_type: str, value: str) -> str:
    if data_type == "int":
        return str(int(value) * 2)

    elif data_type == "real":
        return f"{float(value) * 1.5:.2f}"

    elif data_type == "string":
        return f"${value}$"


current_type = input()
current_value = input()

result = data_type_result(current_type, current_value)
print(result)