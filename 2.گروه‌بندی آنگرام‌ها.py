

def check(words: list) -> list:
    result = {}

    for word in words:
        tmp = "".join(sorted(word))

        if tmp not in result:
            result[tmp] = []

        result[tmp].append(word)

    return [result.values()]


print(check(words=["eat", "tea", "tan", "ate", "nat", "bat"]))
