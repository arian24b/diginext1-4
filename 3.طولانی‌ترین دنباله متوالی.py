

def longest_consecutive_sequence(numbers: list) -> int:
    number_set = set(numbers)
    longest_streak = 0

    for number in number_set:
        if number - 1 not in number_set:
            current_num = number
            current_streak = 1

            while current_num + 1 in number_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


print(longest_consecutive_sequence(numbers=[100, 4, 200, 1, 3, 2]))
