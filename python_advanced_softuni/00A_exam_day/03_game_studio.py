def sort_games(*args, **kwargs):
    console_games = []
    pc_games = []

    release_dates = {game_title: release_id for release_id, game_title in kwargs.items()}

    for platform, game_title in args:
        release_id = release_dates[game_title]
        release_date = "_".join([part for part in release_id.split("_")[:-1]])

        if platform == "console":
            console_games.append([release_id, release_date, game_title])

        elif platform == "pc":
            pc_games.append([release_id, release_date, game_title])

    console_games = sorted(console_games, key=lambda game: game[0])
    pc_games = sorted(pc_games, key=lambda game: game[0], reverse=True)

    result = []

    if console_games:
        result.append("Console Games:")

        for release_id, release_date, game_title in console_games:
            result.append(f">>>{release_date}: {game_title}")

    if pc_games:
        result.append("PC Games:")

        for release_id, release_date, game_title in pc_games:
            result.append(f"<<<{release_date}: {game_title}")

    return "\n".join(result)

print(sort_games(
    ("console", "Echo Dive"),
    ("pc", "Quantum Drift"),
    June_22_2025_001="Quantum Drift",
    March_15_2025_002="Echo Dive",
))
