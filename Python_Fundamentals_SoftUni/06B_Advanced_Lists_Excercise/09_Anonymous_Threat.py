text = input().split()

while True:
    command = input()

    if command == "3:1":
        break

    command_data = command.split()
    action = command_data[0]

    if action == "merge":
        start_index = int(command_data[1])
        end_index = int(command_data[2])

        if start_index < 0:
            start_index = 0

        if end_index > len(text) - 1:
            end_index = len(text) - 1

        if start_index < len(text) and end_index >= 0 and start_index <= end_index:
            merged_text = ""

            for index in range(start_index, end_index + 1):
                merged_text += text[index]

            for index in range(end_index, start_index - 1, -1):
                text.pop(index)

            text.insert(start_index, merged_text)

    elif action == "divide":
        index = int(command_data[1])
        partitions = int(command_data[2])

        current_string = text.pop(index)
        parts = []

        part_length = len(current_string) // partitions
        start = 0

        for part in range(partitions):
            if part == partitions - 1:
                parts.append(current_string[start:])
            else:
                parts.append(current_string[start:start + part_length])
                start += part_length

        for part_index in range(len(parts) - 1, -1, -1):
            text.insert(index, parts[part_index])

print(" ".join(text))