# TODO: Given a decimal integer convert it to binary string of 16 bits.


def integer_to_binary(value: int) -> str:
    binary = ""
    for i in range(16, 0, -1):
        binary += str(value % 2**i // 2 ** (i - 1))

    return binary


def test() -> None:
    # option 1
    assert integer_to_binary(0) == "0000000000000000"
    assert integer_to_binary(1) == "0000000000000001"
    assert integer_to_binary(2) == "0000000000000010"

    # option 2
    assert integer_to_binary(4) == "0" * 13 + "100"
    assert integer_to_binary(7) == "0" * 13 + "111"
    assert integer_to_binary(8) == "0" * 12 + "1000"

    # Note, it is more important to pick one option and
    # stick to it everywhere, than the option you choose itself.
    # Usually you discuss these kinds of things with teammates and
    # agree on the approach together.


def test_should_pad_to_16() -> None:
    assert len(integer_to_binary(15)) == 16


def test_should_convert_maximum_value() -> None:
    assert integer_to_binary(2**16 - 1) == "1" * 16
