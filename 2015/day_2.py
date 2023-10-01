from functools import reduce


def calculate_surface_area(box):
    """
    Fortunately, every present is a box (a perfect right rectangular prism),
    which makes calculating the required wrapping paper for each gift a little easier:
    find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.
    The elves also need a little extra paper for each present: the area of the smallest side.
    """
    length, weight, height = box
    sides = [length * weight, weight * height, height * length]
    return min(sides) + sum(map(lambda x: x * 2, sides))


def read_data(data_txt_path) -> list[tuple[int, ...]]:
    with open(data_txt_path, "r") as f:
        return [tuple(map(int, line.replace("\n", "").split("x"))) for line in f.readlines()]


def day_2_task_1(data):
    return sum(map(calculate_surface_area, data))


def calculate_feet_of_ribbon(box):
    """
    The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any
    one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect
    bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.
    """
    dimensions = sorted(list(box))
    ribbon_warp = sum(map(lambda x: x * 2, dimensions[:2]))
    ribbon_bow = reduce(lambda x, y: x * y, dimensions)
    return ribbon_warp + ribbon_bow


def day_2_task_2(data):
    return sum(map(calculate_feet_of_ribbon, data))


if __name__ == '__main__':
    assert 58 == calculate_surface_area((2, 3, 4))
    assert 43 == calculate_surface_area((1, 1, 10))

    data_day_2 = read_data("data/day_2.txt")

    assert 1606483 == day_2_task_1(data_day_2)

    assert 34 == calculate_feet_of_ribbon((2, 3, 4))
    assert 14 == calculate_feet_of_ribbon((1, 1, 10))

    assert 3842356 == day_2_task_2(data_day_2)
