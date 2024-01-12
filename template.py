import hydra


def your_function_name(*args):
    return 0


@hydra.main(config_path=".", config_name="config.yaml", version_base=None)
def main(cfg):
    failures = []
    for test in cfg.tests:
        res = your_function_name(*test[0])
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
