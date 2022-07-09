import pytest
from stlbs.exceptions import SubtractionBelowZeroError

# Object instantiation tests


def test_stlb_class_is_importable():
    """
    Given that the StLbs package is installed
    as a user of the package
    I want to be able to import it.
    """


def test_input_weight_correctly_assigned():
    """
    Given that I have created an instance of StLb and passed it the correct parameters for stones and lbs
    as a user of the package
    I want the values of instance.whole_stones and instance.remainder_lbs to be correct
    """
    from stlbs import StLb

    x = StLb([10, 1])
    assert x.whole_stones == 10
    assert x.remainder_lbs == 1


def test_in_lbs():
    """
    Given that I have created an instance of StLb and passed it the correct parameters for stones and lbs
    as a user of the package
    I want the value of instance.in_lbs to be (stones * 14) + remainder lbs
    """
    from stlbs import StLb

    test1 = StLb([10, 1])
    assert test1.in_lbs == 141

    test2 = StLb([0, 4])
    assert test2.in_lbs == 4

    test3 = StLb([1, 0])
    assert test3.in_lbs == 14

    test4 = StLb([0, 281])
    assert test4.in_lbs == 281


def test_weight_in_lbs_only():
    """
    Given that an instance of StLb is instantiated with a "lbs only" value >= 14 (i.e [0, 280])
    as a user of the package
    I want the "lbs only" value to be correctly converted into stones and lbs and whole_stones and remainder_lbs to be set
    """
    from stlbs import StLb

    test1 = StLb([0, 281])  # 20 stones and 1 lb
    assert test1.whole_stones == 20
    assert test1.remainder_lbs == 1
    assert test1.in_lbs == 281

    test2 = StLb([0, 15])
    assert test2.whole_stones == 1
    assert test2.remainder_lbs == 1
    assert test2.in_lbs == 15

    test3 = StLb([0, 14])
    assert test3.whole_stones == 1
    assert test3.remainder_lbs == 0
    assert test3.in_lbs == 14


def test_text():
    """
    Given that I have an instance of StLb
    As the maintainer of the package
    I want the instance._text to accurately reflect the instance so that it can be used in str and repr methods
    Format: f"StLb object: {self.whole_stones}st and {self.remainder_lbs} lb [{self.in_lbs}]"
    """
    from stlbs import StLb

    spam = StLb((1, 7))
    assert spam.text == "1st and 7 lb [21 lb]"


def test_str():
    """
    Given that I have a StLb object
    As a user of the package
    I want its __str__() method to return a meaningful message
    """
    from stlbs import StLb

    foo = StLb([1, 7])
    correct = "StLb object: 1st and 7 lb [21 lb]"
    assert foo.__str__() == correct


def test_repr():
    """
    Given that I have a StLb object
    As a user of the package
    I want its __repr__() method to return a meaningful message
    """
    from stlbs import StLb

    foo = StLb([1, 7])
    correct = "StLb object: 1st and 7 lb [21 lb]"
    assert foo.__repr__() == correct


# Tests for arithmetic operator overloads


def test_add():
    """
    Given that I have StLb objects called spam and eggs, and the expression (foo = spam + eggs)
    as a user of the package
    I want foo to be an instance of StLb with its whole_stones, remainder_lbs and in_lbs values equal to the total of
    the corresponding values in spam and eggs
    """
    from stlbs import StLb

    test1_spam = StLb([1, 0])
    test1_eggs = StLb([0, 7])
    test1_foo = test1_spam + test1_eggs
    assert test1_foo.whole_stones == 1
    assert test1_foo.remainder_lbs == 7
    assert test1_foo.in_lbs == 21

    test2_spam = StLb([10, 7])
    test2_eggs = StLb([1, 8])
    test2_foo = test2_spam + test2_eggs
    assert test2_foo.whole_stones == 12
    assert test2_foo.remainder_lbs == 1
    assert test2_foo.in_lbs == 169
    assert test2_foo.__str__() == "StLb object: 12st and 1 lb [169 lb]"


def test_add_iteratble():
    """
    Given that I have an StLb object
    As a user of the package
    I want to add the value of an iterable, (1, 7) for example, to whole_stones and remainder_lbs
    in_lbs should be updated accordingly
    """
    from stlbs import StLb

    spam = StLb([1, 0])
    spam += (1, 0)
    assert spam.whole_stones == 2 and spam.remainder_lbs == 0 and spam.in_lbs == 28

    spam = StLb([1, 0])
    spam += (0, 15)
    assert spam.whole_stones == 2 and spam.remainder_lbs == 1 and spam.in_lbs == 29
    assert spam.__str__() == "StLb object: 2st and 1 lb [29 lb]"


def test_subtract():
    """
    Given that I have StLb objects called spam and eggs, and the expression (foo = spam - eggs)
    as a user of the package
    I want foo to be an instance of StLb with its whole_stones, remainder_lbs and in_lbs values equal to the value of
    the corresponding values in spam minus the corresponding value in eggs
    """
    from stlbs import StLb

    test1_spam = StLb([1, 0])
    test1_eggs = StLb([0, 7])
    test1_foo = test1_spam - test1_eggs
    assert test1_foo.whole_stones == 0
    assert test1_foo.remainder_lbs == 7
    assert test1_foo.in_lbs == 7

    test2_spam = StLb([10, 7])
    test2_eggs = StLb([1, 8])
    test2_foo = test2_spam - test2_eggs
    assert test2_foo.whole_stones == 8
    assert test2_foo.remainder_lbs == 13
    assert test2_foo.in_lbs == 125
    assert test2_foo.__str__() == "StLb object: 8st and 13 lb [125 lb]"


def test_subtract_iterable():
    """
    Given that I have an StLb object
    As a user of the package
    I want to subtract the value of an iterable, (1, 7) for example, from whole_stones and remainder_lbs
    in_lbs should be updated accordingly
    If the final value is negative, raise a SubtractionBelowZeroError (but not if the value is zero)
    """
    from stlbs import StLb

    spam = StLb([3, 7])
    spam -= (1, 1)
    assert spam.whole_stones == 2 and spam.remainder_lbs == 6 and spam.in_lbs == 34

    spam = StLb([2, 0])
    spam -= (0, 7)
    assert spam.whole_stones == 1 and spam.remainder_lbs == 7 and spam.in_lbs == 21

    # result is exactly zero: should not raise SubtractionBelowZeroError
    spam = StLb((2, 0))
    spam -= [2, 0]
    assert spam.in_lbs == 0


def test_subtraction_below_zero_raises_exception():
    """
    Given that the result of (StLb1 - StLb2) cannot be below zero
    as a user of the package
    I want a SubtractionBelowZeroError exception to be raised if (StLb1 - StLb2) < 0
    An error should not be raised if the total == 0
    """
    from stlbs import StLb

    spam = StLb([1, 0])
    eggs = StLb([1, 1])

    with pytest.raises(SubtractionBelowZeroError):
        foo = spam - eggs

    with pytest.raises(SubtractionBelowZeroError):
        spam = StLb([1, 0])
        spam -= (1, 1)

    # Test that subtraction resulting in zero does not raise error
    spam = StLb([1, 0])
    eggs = StLb([1, 0])
    foo = spam - eggs
    assert foo.in_lbs == 0


def test_multiply_objects_together():
    """
    Given that I have a StLb object
    As a user of the package
    I want to be able to multiply it by another StLB instance or list / tuple representation
    E.g. StLb(2, 0) * StLB(2, 0) == StLb(56, 0)  [i.e. 28lbs * 28lbs]
    StLB(2, 0) * (2, 0) == StLb(56, 0)
    """
    from stlbs import StLb

    # Test that two objects multiplied together create a new object correctly
    spam = StLb([2, 0])
    eggs = StLb([2, 0])
    foo = spam * eggs
    assert foo.whole_stones == 56 and foo.remainder_lbs == 0

    # Test that multiplication assignment works
    spam = StLb([2, 0])
    spam *= StLb([2, 0])
    assert foo.whole_stones == 56 and foo.remainder_lbs == 0

    # Test that multiplication by a tuple / list works correctly
    spam = StLb([2, 0])
    foo = spam * (2, 0)
    assert foo.whole_stones == 56 and foo.remainder_lbs == 0


def test_multiply_by_number():
    """
    Given that I have a StLb object
    As a user of the package
    I want to be able to multiply it by a number (float, integer, decimal)
    E.g StLb(2, 0) * 2 == StLb(4, 0)
    """
    from stlbs import StLb

    spam = StLb([2, 0])
    foo = spam * 2

    assert foo.whole_stones == 4 and foo.remainder_lbs == 0


def test_divide_by_object():
    """
    Given that I have a StLb object
    As a user of the package
    I want to be able to divide by another StLb instance or an equivalent iterable and return a numeric type
    E.g. StLb(4, 0) / StLb(2, 0) == 2
    StLb(4, 0) / (2, 0) == 2
    """
    from stlbs import StLb

    spam = StLb([4, 0])  # 56lb
    foo = StLb([2, 0])  # 28lb
    correct = 2  # 56 / 14
    assert spam / foo == correct

    spam = StLb([4, 0])  # 56lb
    correct = 2  # 56 / 14
    assert spam / (2, 0) == correct


def test_divide_by_number():
    """
    Given that I have a StLb object
    As a user of the package
    I want to be able to divide by a number (float, integer, decimal) and get the result StLb(0, answer)
    """
    from stlbs import StLb

    spam = StLb([4, 0])  # 56lb
    divided_spam = spam / 2
    assert divided_spam.in_lbs == 28


def test_divide_by_invalid_type_raises_valueerror():
    """
    Given that I have a StLb object
    As the maintainer of the package
    I want ValueError to be raised if the divisor is not in the following types:
        [int, float, list, tuple, StLb]
    """
    from stlbs import StLb

    spam = StLb([4, 0])  # 56lb

    with pytest.raises(ValueError):
        spam / "this is not a valid type for division"


# Test support methods


def test_convert_stones_and_lbs_to_lbs():
    """
    Given that have multiple places in the code where a (stones, lbs) format needs to be converted to (0, value_in_lbs)
    As the maintainer of the package
    I want a single function that does this calculation
    """
    from stlbs import StLb

    foo = StLb([1, 0])
    # Value of foo is irrelevant to this test - just need to instantiate an instance, so need to give required values
    correct = 15
    assert foo._convert_stones_and_lbs_to_lbs((1, 1)) == correct


def test_argument_validation_allows_perrmited_types_only():
    """
    Given that the StLb param should only accept a list or tuple
    As the maintainer of the package
    I want the validation code to raise a Type error if the argument is not a list or a tuple
    """
    from stlbs import StLb

    with pytest.raises(TypeError):
        foo = StLb("not a valid type")

    with pytest.raises(TypeError):
        spam = StLb(999)

    with pytest.raises(TypeError):
        eggs = StLb(StLb)


def test_argument_validation_allows_perrmited_length_sequences_only():
    """
    Given that the StLb param should only accept a list or tuple of two items
    As the maintainer of the package
    I want the validation code to raise a ValueError error if the argument does not have exactly two items
    """
    from stlbs import StLb

    with pytest.raises(ValueError):
        foo = StLb([2, 2, 2])

    with pytest.raises(ValueError):
        foo = StLb([2])


def test_argument_validation_does_not_allow_non_numeric_types():
    """
    Given that I am instantiating a StLb instance
    As the maintainer of the package
    I want the validation code to raise a Type error if either of the items in the argument contains any type other than int or float
    """
    from stlbs import StLb

    with pytest.raises(TypeError):
        foo = StLb(["one", 0])

    with pytest.raises(TypeError):
        bar = StLb([0, [1, 2]])


def test_argument_validation_does_not_allow_negative_numbers():
    """
    Given that I am instantiating a StLb instance
    As the maintainer of the package
    I want the validation code to raise a ValueError if either of the items in the argument are a negative number
    """
    ...
