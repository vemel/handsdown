# pylint: disable=missing-docstring
"""
# Sphinx docstrings examples

## Links

[reStructuredText Primer](http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
"""


class RSTExample:
    @staticmethod
    def reference():
        """
        This is a reference for ``Sphinx-style RST-style`` docstrings. Check :data:`source` code
        to see how it works.

        Code example::

            data = {
                'key': 'value',
            }

            print(data)


        :param my_param: Parameter example
        :param int typed_param: Typed parameter example
        :returns str: Return statement
        :raises ValueError: Raises example

        """

    @staticmethod
    def directives_test():
        """
        Test for some random Sphinx directives

        .. code-block:: ruby

            def sum_eq_n?(arr, n)
                return true if arr.empty? && n == 0
                arr.product(arr).reject { |a,b| a == b }.any? { |a,b| a + b == n }
            end

        .. note:: short note

        .. math::

            (a + b)^2 = a^2 + 2ab + b^2

            (a - b)^2 = a^2 - 2ab + b^2

        .. seealso::
            modules :py:mod:`zipfile`, :py:mod:`tarfile`
        """

    @staticmethod
    def version_directives_test():
        """
        Test for Version-related directives

        .. versionadded:: 2.5
            The *spam* parameter.

        .. versionchanged:: 2.7
            Mandatory *spam* parameter.

        .. deprecated:: 3.1
            Use :func:`spam` instead.
        """
