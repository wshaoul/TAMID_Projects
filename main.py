
def isPalindrome(word) -> bool:
    return word == ''.join(list(reversed(word)))


def sortArrays(arr1, arr2, k):
    arr1.extend(arr2)
    return sorted(arr1)[:k]


def main():
    print(isPalindrome("racecar"))
    print(isPalindrome("poop"))
    print(isPalindrome("hub"))
    print(sortArrays([1, 3, 5, 8], [4], 10))


if __name__ == '__main__':
    main()

