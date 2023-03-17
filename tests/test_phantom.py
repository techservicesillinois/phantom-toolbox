import pytest

import phtoolbox


def test_phantom():
    """Regression test for issue #4."""
    with pytest.raises(NotImplementedError):
        phtoolbox._main()
