def main():
    nums_input = input()
    result = 0
    with open(nums_input, "r") as nums_file:
        nums = [int(x) for x in nums_file.read().split("\n")]
    for num in nums:
        result += abs(num - round(sum(nums)/len(nums)))
    print(result)

if __name__ == "__main__":
    main()