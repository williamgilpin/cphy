Docstrings and formatting code
==============

Formatting: Formatting Python code involves making changes that improve readability to human users. These are changes that don't necessarily change the logic of the program itself, but which make the code easier to read and understand. One does not necessarily need to focus on refactoring code, in which we change the logic of the program itself in order to make the code easier to extend, troubleshoot, or modify, although refactoring can certainly help with human readability. Python has a strong set of conventions regarding formatting, [PEP-8](https://peps.python.org/pep-0008/), which can help guide formatting code.

We’ve seen that whitespace in Python has meaning: Code written without proper indentation within loops, for example, will fail to run. We've also seen that comments are useful for explaining the code to human readers.

## Docstrings

Docstrings describe the structure and attributes of Python functions and classes. These have special treatment in most Python environments. For example, docstrings are printed out whenever the command `help(name_of_object)` is run, and some IDE like VSCode render docstrings in a popup when your cursor hovers over a function.

There are lots of different conventions for formatting docstrings, depending on preferences. For generality, it is usually recommended to use one of the [Napolean supported docstring formats](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/). The Google docstring format uses less vertical space at the expense of longer horizontal descriptions, while the NumPy format uses more verticle space, but has shorter lines. We will use the Google format throughout this tutorial. If you generally write code in a Terminal or other settings where horizonal scanning is difficult, then the NumPy format may be preferred.


# Docstrings

Docstrings describe the structure and attributes of Python functions and classes. These have special treatment in most Python environments. They are printed out whenever the command `help(name_of_object)` is run, and some IDE like VSCode render docstrings in a popup when your cursor hovers over a function.

There are lots of different conventions for formatting docstrings, depending on preferences. For generality, I usually recommend using one of the [Napolean supported docstring formats](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/). The Google docstring format uses less vertical space at the expense of longer horizontal descriptions, while the Numpy format uses more verticle space, but has shorter lines. I generally prefer less scrolling, and so I'll use the Google format throughout this tutorial. If you generally write code in a Terminal or other settings where horizonal scanning is difficult, then the numpy format may be preferred.

Here's an example of a function that computes each step of the dynamics of a particle in a potential well. The docstring briefly describes the function, and then lists the arguments, their types, and meaning. The return value is also described.

```python
    def ornstein_uhlenbeck(n, ic=0.0, x0=0):
        """
        Simulate the motion of a particle in a one-dimensional harmonic potential well
        with Brownian forcing

        Args:
            n (int): The number of steps to simulate
            ic (float): The initial value of the process
            x0 (float): The location of the potential minimum

        Returns:
            traj (list): The n steps of the dynamical process

        """
        curr = ic
        traj = list()
        for _ in range(n):
            traj.append(curr)
            curr = (curr - x0) + 0.1 * random.random()
        return traj
```

The syntax of the docstring is usually rather strict. We declare the type of each argument, and the type of the return value. We also include a description of the function, and the meaning of each argument. This explicit, rigid structure is useful for other users of your code, and also for your future self. If you come back to a function you wrote a year ago, you'll have a description of what it does. The strict syntax also helps the computer format the docstring when the `help` command is invoked, and it will also make it possible to automatically generated online documentation for code using an [autodoc tool](http://www.wgilpin.com/howto/howto_sphinx.html).

## Docstring entries

The docstring for a function should always include the following entries: 
+ Args: A description of each argument, including the type of the argument
+ Returns: A description of the return value, including the type of the return value

Additionally, you might find it useful to include the following entries:

+ Raises: A description of any errors that may be raised by the function
+ Yields: A description of the values yielded by a generator function
+ Warnings: A description of any warnings that may be raised by the function
+ Notes: Any additional information that may be useful to the user
+ See Also: A list of related functions. For subclasses, this would include the parent class.
+ Examples: A list of examples of how to use the function


## Docstrings for classes

For classes, we usually place the appropriate docstring at the top level, rather than within the `__init__` method. However, placing documentation in the top-level class versus the `__init__` method is a [matter of convention,](https://peps.python.org/pep-0257/) and both are valid. However, in most environments, the `help` command will print out the docstring for both the class and the `__init__` method when it is called on the class itself, and not just when it is called on an instance of the class. Here is an example of a docstring for a class that simulates the dynamics of a particle in a potential well:

```python
class OrnsteinUhlenbeck:
    """
    A class for simulating the motion of a particle in a one-dimensional harmonic potential well
    with Brownian forcing

    Args:
        x0 (float): The location of the potential minimum. Defaults to 0.

    Attributes:
        x0 (float): The location of the potential minimum
        traj (list): The trajectory of the particle

    Methods:
        step: Simulate a single step of the process
        run: Simulate the process for a given number of steps

    Examples:
        >>> ou = OrnsteinUhlenbeck()
        >>> ou.run(10)
        >>> ou.traj
        [0.0, 0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

    Notes:
        This implementation uses a Gaussian random number generator to simulate the
        discrete-time effects of Brownian forcing.
        
    """
    def __init__(self, x0=0):
        self.x0 = x0
        self.traj = list()

    def step(self):
        """
        Take a single step of the dynamical process

        Returns:
            float: The new value of the process

        """
        if len(self.traj) == 0:
            curr = 0.0
        else:
            curr = self.traj[-1]
        self.traj.append((curr - self.x0) + 0.1 * random.random())
        return self.traj[-1]

    def run(self, n):
        """
        Simulate the process for a given number of steps

        Args:
            n (int): The number of steps to simulate

        Returns:
            list: The n steps of the dynamical process

        """
        for _ in range(n):
            self.step()
        return self.traj
```

The docstring for the class itself should include a description of the class, and a description of each attribute. The docstring for the `__init__` method should include a description of the class, and a description of each argument. The docstring for class-specific methods like the `step` method should include a description of the method, and a description of the return value, just as for functions.

Some common fields in a class-level docstring are:

+ Attributes: A description of each attribute of the class. This would include instance variables that are bound to the class, such as `self.x0` in the example above.
+ Methods: A description of each method of the class. This would include custom instance methods, such as `step` in the example above. This usually would not include any methods inherited from a parent class.
+ Raises: A description of any errors that may be raised by the class, especially if the class is a subclass of a built-in class.
+ Warnings: A description of any warnings that may be raised by the class.
+ Notes: Any additional information that may be useful to the user, such as citations or a description of the algorithm used to implement the class.
+ See Also: A list of related classes or functions.
+ Examples: A list of examples of how to use the class.


## Formatting code

In Python, the formatting of the code can convey literal meaning to the interpreter. For example, the following code will not run:

```python
    def f(x):
    return x + 1

    f(1)
```

The reason is that the second line is not indented, and so the interpreter interprets it as a continuation of the first line. The spaces that shoudl indent the second line thus have direct meaning in Python, in contrast to other languages like R, C, or Java.

Beyond the literal meaning of the code, there are also conventions for formatting code that make it easier to read and understand. These sets of conventions are called [PEP-8](https://peps.python.org/pep-0008/). Among the most important are:

- **Indentation**: Always use 4 spaces per indentation level. Tabs should be avoided. In many modern IDEs like VSCode, you can set the tab size to 4 spaces, and the IDE will automatically convert tabs to 4 spaces when you save the file.
- **Line length**: Limit all lines to a maximum of 79 characters (72 for docstrings). In some newer environments like Google Colab, the line length is set to 80 characters, while in others like Jupyter, the line length is set to 100 characters.
- **Blank lines**: Use blank lines to separate functions, classes, and logical sections of code.
- **Imports**: Keep imports at the top of the file, grouped as standard library, third-party, and local modules. Avoid putting imports at the top of functions or classes deep within a `.py` file.
- **Whitespace**: Use spaces around operators and after commas, but not directly inside parentheses or brackets. For example, `x = 1` is preferred over `x=1`.

For example, the following code follows PEP 8 conventions:

```python
def f(x: int) -> int:
    """Return x + 1."""
    return x + 1


if __name__ == "__main__":
    print(f(1))

```

Here, the function is indented consistently, type annotations and a docstring are provided for clarity, and the if __name__ == "__main__": guard is used to make the file runnable as a script while still allowing imports. Tools like black, isort, and flake8 can automatically format code to conform to PEP 8 conventions. Black is a particularly popular tool for formatting code that invokes several additional formatting conventions, and many IDEs like VSCode and Jupyter have built-in plugins that can automatically format code with black.
