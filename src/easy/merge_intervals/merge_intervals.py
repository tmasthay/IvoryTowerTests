import hydra
import numpy as np


def merge_intervals(intervals):
    idx = 0

    intervals = np.array(intervals)
    intervals = [tuple(e) for e in intervals[np.argsort(intervals[:, 0])]]

    while idx < len(intervals) - 1:
        a, b = intervals[idx]
        c, d = intervals[idx + 1]
        if (a <= c and c <= b) or (c <= a and a <= d):
            intervals[idx] = (min(a, c), max(b, d))
            intervals.pop(idx + 1)
        else:
            idx += 1
    return intervals


@hydra.main(config_path=".", config_name="config.yaml", version_base=None)
def main(cfg):
    failures = []
    for test in cfg.tests:
        res = merge_intervals(*test[0])
        if set(res) != set([tuple(e) for e in test[1]]):
            failures.append([test[0], test[1], res])
    print(f'Passed {len(cfg.tests) - len(failures)} of {len(cfg.tests)}')
    for failure in failures:
        print(
            f'input: {failure[0]}\n   '
            f' expected_output={failure[1]}\n    actual_output={failure[2]}\n'
        )


if __name__ == "__main__":
    main()
