import sys
input = sys.stdin.readline

def a_test_case():
    n, m = map(int, input().split())
    total = 0

    num_avai = list(map(int, input().split()))
    num_avai.sort()

    houzhuihe = [0] * (m + 1)

    for j in range(m - 1, -1, -1):
        houzhuihe[j] = houzhuihe[j + 1] + num_avai[j]

    # 计算 m1
    if num_avai[m - 1] < n:
        m1 = m
    else:
        for j in range(m - 1, -1, -1):
            if num_avai[j] >= n:
                m1 = j
            else:
                break

    total += (n-1) * (m - m1) * (m - m1 - 1)
    total += ((houzhuihe[0] - houzhuihe[m1]) * 2) * (m - m1)

    if m1 == 0:
        return total

    zhizhen = m1
    b = num_avai[zhizhen - 1]

    for i in range(m1):

        a = num_avai[i]

        if 2 * a >= n:
            total += 2 * (houzhuihe[i + 1] - houzhuihe[m1])
            total += 2 * (a - n + 1) * (m1 - i - 1)
            continue

        if b + a >= n:
            while b + a >= n:
                zhizhen -= 1
                b = num_avai[zhizhen]
            zhizhen += 1

        total += 2 * (houzhuihe[zhizhen] - houzhuihe[m1])
        total += 2 * (a - n + 1) * (m1 - zhizhen)

    return total


def main():
    t = int(input())
    for _ in range(t):
        print(a_test_case())


if __name__ == "__main__":
    main()