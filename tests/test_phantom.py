import phtoolbox


def test_bad_command():
    '''Test that nonsense command returns -1'''
    args = phtoolbox.init_parser().parse_args(["nonsense"])
    result = phtoolbox._main(args)
    assert result == 1
