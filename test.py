def main():
    # print("\t\t\t\t\t\t\t{}\n".format(15)) # 7 + 16
    # print("\t\t\t{}\t\t\t\t\t\t\t\t{}\n".format(13, 14)) # 3 + 8
    # print("\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\n".format(9, 10, 11, 12)) # 1 + 4
    # print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\n".format(1, 2, 3, 4, 5, 6, 7, 8)) # 0 + 2

    height = 3
    all_numbers = list(range(2 ** (height + 1) - 1))
    leftmost = 0

    for level in range(height + 1):
        counts_per_level = 2 ** level
        previous_leftmost = leftmost
        leftmost += counts_per_level

        entries_per_level = all_numbers[previous_leftmost : leftmost]
        format_string = "\t" * (2 ** (height - level) - 1)
        format_substring = "{}" + "\t" * (2 ** ((height - level) + 1))
        format_substring *= (counts_per_level - 1)
        format_string += (format_substring + "{}\n")

        # print(counts_per_level)
        # print(repr(format_string))

        print(format_string.format(*entries_per_level))
        

if (__name__ == "__main__"):
    main()