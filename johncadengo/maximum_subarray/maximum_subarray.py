"""Maximum Subarray Problem"""


def find_max_subarray(arr):
    total_max = 0
    current_max = 0

    for i in arr:
        current_max = max(0, current_max + i)
        total_max = max(current_max, total_max)

    return total_max


def main():
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected = sum([4, -1, 2, 1])
    max_subarray = find_max_subarray(arr)

    print 'Array: {}'.format(arr)
    print 'Expected max subarray: {}'.format(expected)
    print 'Actual max subarray: {}'.format(max_subarray)

    assert max_subarray == expected
    print 'Success!'

if __name__ == '__main__':
    main()
