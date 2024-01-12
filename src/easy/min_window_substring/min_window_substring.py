import hydra


def min_window_substring(s, t):
    if not s or not t or len(s) < len(t):
        return ""

    freqs = {}
    for tt in t:
        freqs[tt] = freqs.get(tt, 0) + 1

    start, end = 0, 0
    min_start, min_length = 0, float("inf")
    seen_chars, required_chars = 0, len(t)

    while end < len(s):
        end_char = s[end]
        if end_char in freqs:
            freqs[end_char] -= 1
            if freqs[end_char] >= 0:
                seen_chars += 1

        while start <= end and seen_chars == required_chars:
            start_char = s[start]
            if end - start + 1 < min_length:
                min_length = end - start + 1
                min_start = start

            if start_char in freqs:
                freqs[start_char] += 1
                if freqs[start_char] > 0:
                    seen_chars -= 1
            start += 1

        end += 1
    if min_length == float("inf"):
        return ""
    else:
        return s[min_start : (min_start + min_length)]


@hydra.main(config_path=".", config_name="config.yaml", version_base=None)
def main(cfg):
    failures = []
    for test in cfg.tests:
        res = min_window_substring(*test[0])
        if type(res) not in [list, set]:
            success = res == test[1]
        else:
            success = set(res) == set([tuple(e) for e in test[1]])
        if not success:
            failures.append([test[0], test[1], res])
    print(f'Passed {len(cfg.tests) - len(failures)} of {len(cfg.tests)}')
    for failure in failures:
        print(
            f'input: {failure[0]}\n   '
            f' expected_output={failure[1]}\n    actual_output={failure[2]}\n'
        )


if __name__ == "__main__":
    main()
