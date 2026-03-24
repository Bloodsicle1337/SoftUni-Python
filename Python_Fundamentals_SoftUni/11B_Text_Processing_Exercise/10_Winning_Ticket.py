def check_ticket(some_ticket: str) -> str:
    if len(some_ticket) != 20:
        return "invalid ticket"

    winning_symbols = ('@', '#', '$', '^')
    left_part = some_ticket[:10]
    right_part = some_ticket[10:]

    for match_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            match_symbol_repetition = uninterrupted_match_length * match_symbol
            if (match_symbol_repetition in left_part) and (match_symbol_repetition in right_part):
                if uninterrupted_match_length == 10:
                    return f'ticket "{some_ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'

                return f'ticket "{some_ticket}" - {uninterrupted_match_length}{match_symbol}'

    return f'ticket "{some_ticket}" - no match'
tickets = [ticket.strip() for ticket in input().split(", ")]

for current_ticket in tickets:
    print(check_ticket(current_ticket))