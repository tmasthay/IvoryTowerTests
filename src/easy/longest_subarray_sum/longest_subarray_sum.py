import hydra


def longest_subarray_sum(v):
    prefix_sum = [0, v[0]]
    [prefix_sum.append(e + prefix_sum[-1]) for e in v[1:]]
    seen = {}
    for i, e in enumerate(prefix_sum):
        if e in seen.keys():
            seen[e][-1] = i
        else:
            seen[e] = [i, i]
    res = max([v[1] - v[0] for v in seen.values()])
    return res


@hydra.main(config_path=".", config_name="config.yaml", version_base=None)
def main(cfg):
    failures = []
    for test in cfg.tests:
        res = longest_subarray_sum(*test[0])
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
