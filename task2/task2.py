def cicle_form(x, y, center_x, center_y, r) -> int:
    return((x - center_x)**2 + (y - center_y)**2 - r**2)

def main():
    cycle_file = input()
    points_file = input()
    result = ""
    try:
        with open(cycle_file) as cycle:
            center, r = cycle.read().split('\n')
            r = int(r)
            center_x, center_y = [int(x) for x in center.split(" ")]
    except IOError:
        print("No cycle file")

    try:
        with open(points_file) as points_test:
            points = [x for x in points_test.read().split('\n')]
    except IOError:
        print("No points file")

    for coord in points:
        x, y = [int(i) for i in coord.split(" ")]
        if cicle_form(x, y, center_x, center_y, r) < 0:
            result += "1\n"
        elif cicle_form(x, y, center_x, center_y, r) > 0:
            result += "2\n"
        else:
            result += "0\n"
    print(result)


if __name__ == "__main__":
    main()