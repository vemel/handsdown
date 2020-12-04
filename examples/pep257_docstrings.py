# pylint: disable=missing-docstring,no-self-use
"""
# PEP 257 - PEP 257 and Google docstrings examples

## Links

[PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0287/)
"""


class ClassExample:
    """
    PEP257-style class example

    Attributes:
        attr1 -- Description of `attr1`.
        attr2 -- Description of `attr2`.

    ```python
    Example of a code block
    ```

    You can use `~~~` to start a block as well

    ~~~
    MD block example inside a tilde block

    ```python
    This is not a codeblock, test inside tildes rendered as it is
    ```
    ~~~
    """

    def method_example(self, text: str = "hello") -> int:
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
