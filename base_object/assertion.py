from pytest_check import check

class Assertion:

    @staticmethod
    @check.check_func
    def assertion_equal(actual, expected):
        assert actual == expected, f'we expected {expected} but got {actual}'

    @staticmethod
    def assertion_not_equal(actual, expected):
        assert actual != expected