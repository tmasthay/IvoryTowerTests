import hydra


def max_sum_options(vals, k):
    vals.sort()
    vals = [-e if i < k else e for i, e in enumerate(vals)]
    return sum(vals)


@hydra.main(config_path=".", config_name="config.yaml", version_base=None)
def main(cfg):
    failures = []
    for test in cfg.tests:
        res = max_sum_options(*test[0])
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
