import sys
def solve_case(candidates, m):
    n = len(candidates)
    max_diff = 20 * m
    offset = max_diff
    width = max_diff * 2 + 1
    neg_inf = -10**9
    dp = [[neg_inf] * width for _ in range(m + 1)]
    dp[0][offset] = 0
    # take[i][j][d] == 1 means candidate i is used when reaching state (j, d)
    # after considering candidates 1..i.  bytearray keeps this compact enough.
    take = [[bytearray(width) for _ in range(m + 1)] for _ in range(n + 1)]
    for i, (prosecution, defence) in enumerate(candidates, start=1):
        diff = prosecution - defence
        total = prosecution + defence
        next_dp = [row[:] for row in dp]
        upper = min(i, m)
        for chosen in range(1, upper + 1):
            prev_row = dp[chosen - 1]
            curr_row = next_dp[chosen]
            for old_idx, old_total in enumerate(prev_row):
                if old_total == neg_inf:
                    continue
                new_idx = old_idx + diff
                if 0 <= new_idx < width and old_total + total > curr_row[new_idx]:
                    curr_row[new_idx] = old_total + total
                    take[i][chosen][new_idx] = 1
        dp = next_dp
    best_idx = -1
    for delta in range(max_diff + 1):
        left = offset - delta
        right = offset + delta
        left_total = dp[m][left] if 0 <= left < width else neg_inf
        right_total = dp[m][right] if 0 <= right < width else neg_inf
        if left_total == neg_inf and right_total == neg_inf:
            continue
        if right_total > left_total:
            best_idx = right
        else:
            best_idx = left
        break
    selected = []
    chosen = m
    idx = best_idx
    for i in range(n, 0, -1):
        if chosen > 0 and take[i][chosen][idx]:
            selected.append(i)
            prosecution, defence = candidates[i - 1]
            idx -= prosecution - defence
            chosen -= 1
    selected.reverse()
    prosecution_sum = sum(candidates[i - 1][0] for i in selected)
    defence_sum = sum(candidates[i - 1][1] for i in selected)
    return prosecution_sum, defence_sum, selected
def main():
    data = sys.stdin.read().split()
    pos = 0
    case_no = 1
    output = []
    while pos < len(data):
        n = int(data[pos])
        m = int(data[pos + 1])
        pos += 2
        if n == 0 and m == 0:
            break
        candidates = []
        for _ in range(n):
            prosecution = int(data[pos])
            defence = int(data[pos + 1])
            pos += 2
            candidates.append((prosecution, defence))
        prosecution_sum, defence_sum, selected = solve_case(candidates, m)
        output.append(f"Jury #{case_no}")
        output.append(
            f"Best jury has value {prosecution_sum} for prosecution "
            f"and value {defence_sum} for defence:"
        )
        output.append(" " + " ".join(map(str, selected)))
        output.append("")
        case_no += 1
    sys.stdout.write("\n".join(output))
if __name__ == "__main__":
    main()
