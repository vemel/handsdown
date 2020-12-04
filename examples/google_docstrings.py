# pylint: disable=missing-docstring,no-self-use
"""
# Google docstrings examples

## Links

[Google Python Style Guide](
    http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
)
"""


class ClassExample:
    """
    Google-style class example

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.
    """

    def method_example(self, text: str = "hello") -> int:
        """Summary line.

        Extended description of method.

        Examples:
            Examples should be written in doctest format, and should illustrate how
            to use the function::

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
            text (str, optional): Description of arg1
            *args (str): Description of args
            **kwargs (str): Description of kwargs

        Returns:
            int: Description of return value

        """
        return len(text)


def function_example(arg1, arg2, arg3=None):
    """Summary line.

    Extended description of function.
    You can use this function like::

      result = function_example(
          {
              'key': 'value',
          },
          None,
      )

      print result

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2
        arg3 (str, optional): Description of arg3

    Returns:
        bool: Description of return value

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.
    """
    return arg1 == arg2 or arg3


def function_with_pep484_type_annotations(param1: int, param2: str) -> bool:
    """Example function with PEP 484 type annotations.

    Args:
        param1: The first parameter.
        param2: The second parameter.

    Returns:
        The return value. True for success, False otherwise.

    """
    return param1 == param2
