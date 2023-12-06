def get_data(path) -> dict[list[dict[str, int]]]:
    """
    -> {1: [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}], ...
    """
    result = {}
    for line in open(path):
        line = line.replace("\n", "")
        game_sets = line.split(":")[1].split(";")
        game_id = int(line.split(":")[0].split(" ")[-1])

        games = []
        for game_set in game_sets:
            game = {}
            for draw_str in game_set.split(","):
                number, color = draw_str.strip().split()
                game[color] = int(number)
            games.append(game)
        result[game_id] = games
    return result


def is_possible(draws: list, limits: dict) -> bool:
    for game_round in draws:
        for color, limit in limits.items():
            if game_round.get(color) is not None and game_round.get(color) > limit:
                return False
    return True


def day2_task_1(data, limits):
    result = 0
    for game_id, draws in data.items():
        if is_possible(draws, limits):
            result += game_id
    return result


if __name__ == '__main__':
    """
    The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 
    13 green cubes, and 14 blue cubes?
    """
    result_day_2_example = day2_task_1(data=get_data(path="data/day_2_demo.txt"),
                                       limits={"red": 12, "green": 13, "blue": 14})

    result_day_2_task_1 = day2_task_1(data=get_data(path="data/day_2.txt"),
                                       limits={"red": 12, "green": 13, "blue": 14})

    assert result_day_2_example == 8
    assert result_day_2_task_1 == 2810


