import hashlib


def get_hash(data_string) -> str:
    return hashlib.md5(data_string.encode()).hexdigest()


def day_4(key, n_leading_zeros=5):
    n = 0
    while True:
        if get_hash(key + str(n)).startswith("0" * n_leading_zeros):
            return n
        n += 1


if __name__ == '__main__':
    assert get_hash(data_string="abcdef609043").startswith("000001dbbfa")
    assert get_hash(data_string="pqrstuv1048970").startswith("000006136ef")
    assert 609043 == day_4(key="abcdef")
    assert 1048970 == day_4(key="pqrstuv")
    assert 254575 == day_4(key="bgvyzdsv")  # Task 1 solution
    assert 1038736 == day_4(key="bgvyzdsv", n_leading_zeros=6)  # Task 2 solution
