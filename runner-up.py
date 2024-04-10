if __name__ == '__main__':
    n = int(input())
    arr = sorted(list(map(int, input().split())))

    max_num = arr[0]
    runner_up = None

    for i in arr:
        if i > max_num:
            runner_up = max_num
            max_num = i

    print(runner_up)
