"""
# PEP 257 - reStructuredText docstrings examples

## Links

[PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0287/)
"""
from typing import Text


class ClassExample:
    """
    PEP257-style class example

    Attributes:
        attr1 -- Description of `attr1`.
        attr2 -- Description of `attr2`.
    """

    def method_example(self, text: Text = "hello") -> int:
        """Summary line.

        Extended description of method.

        Examples:
            Examples should be written in doctest format, and should illustrate how
            to use the function.

            >>> print([i for i in
            ... example_generator(2)])
            [
                'one',
                'two',
            ]

            >>> setup_env()
            >>> func_call(
            ...     first_name='test',
            ...     last_name='test',
            ... )

        Args:
            text -- Description of arg1
            *args -- Description of args
            **kwargs -- Description of kwargs

        Returns:
            Description of return value
        """
        return len(text)


def function_example(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    return real == imag
