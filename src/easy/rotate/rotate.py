import hydra


def rotate(v):
    def swap(i_lcl, j_lcl, k_lcl, l_lcl):
        tmp = v[i_lcl][j_lcl]
        v[i_lcl][j_lcl] = v[k_lcl][l_lcl]
        v[k_lcl][l_lcl] = tmp

    def rotate_boundary_box(start, end):
        for i in range(end - start):
            swap(start, start + i, end - i, start)
            swap(end - i, start, end, end - i)
            swap(end, end - i, start + i, end)

    start_lcl, end_lcl = 0, len(v) - 1
    while start_lcl < end_lcl:
        rotate_boundary_box(start_lcl, end_lcl)
        start_lcl += 1
        end_lcl -= 1

    return v


@hydra.main(config_path=".", config_name="config.yaml", version_base=None)
def main(cfg):
    failures = []
    for test in cfg.tests:
        res = rotate(*test[0])
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
