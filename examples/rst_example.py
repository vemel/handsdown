class RSTExample:
    @staticmethod
    def reference():
        """
        This is a reference for ``RST-style`` docstrings. Check :data:`source` code
        to see how it works.

        :param my_param: Parameter example
        :param int typed_param: Typed parameter example
        :returns str: Return statement
        :raises ValueError: Raises example

        Code example::

            data = {
                'key': 'value',
            }

            print(data)
        """

    @staticmethod
    def rtype_test():
        """
        `:rtype:` test.

        :returns: Return statement
        :rtype: bool
        """

    @staticmethod
    def replace_test():
        """
        Check if all :attr:`attributes`, :data:``data`` and :exc:`Exception` in
        :class:``RSTExample`` and :class:`RSTExample` look good.
        """
