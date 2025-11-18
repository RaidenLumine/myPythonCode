def solve(sentence: str) -> str:
    table = tuple(chr(ord('Z') - i) for i in range(26))
    res = []
    for ch in sentence:
        if ch.isupper():
            res.append(table[ord(ch) - ord('A')])
        else:
            res.append(ch)
    return ''.join(res)

if __name__ == "__main__":
    sentence = input()
    print(solve(sentence))