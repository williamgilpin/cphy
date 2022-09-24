Lab 3: Docstrings, formatting, and autodoc
==============

Formatting: Formatting Python code involves making changes that improve readability to human users. Here we aren’t focusing on refactoring code, in which we change the logic of the program itself in order to make the code easier to extend, troubleshoot, or modify, although refactoring can certainly help with human readability. Python has a strong set of conventions regarding formatting, PEP-8, which can help guide formatting code.

We’ve seen that whitespace in Python has meaning: Code written without proper indentation within loops, for example, will fail to run. 



# Docstrings

Docstrings describe the structure and attributes of Python functions and classes. These have special treatment in most Python environments. They are printed out whenever the command `help(name_of_object)` is run, and some IDE like VSCode render docstrings in a popup when your cursor hovers over a function.

Here are some example docstrings:

    def add(num1, num2):
        """
        Add up two integer numbers.

        This function simply wraps the ``+`` operator, and does not
        do anything interesting, except for illustrating what
        the docstring of a very simple function looks like.

        Parameters
        ----------
        num1 : int
            First number to add.
        num2 : int
            Second number to add.

        Returns
        -------
        int
            The sum of ``num1`` and ``num2``.

        See Also
        --------
        subtract : Subtract one integer from another.

        Examples
        --------
        >>> add(2, 2)
        4
        >>> add(25, 0)
        25
        >>> add(10, -10)
        0
        """
        return num1 + num2


