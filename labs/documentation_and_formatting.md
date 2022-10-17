Lab 3: Docstrings, formatting, and autodoc
==============

Formatting: Formatting Python code involves making changes that improve readability to human users. Here we aren’t focusing on refactoring code, in which we change the logic of the program itself in order to make the code easier to extend, troubleshoot, or modify, although refactoring can certainly help with human readability. Python has a strong set of conventions regarding formatting, PEP-8, which can help guide formatting code.

We’ve seen that whitespace in Python has meaning: Code written without proper indentation within loops, for example, will fail to run. 



# Docstrings

Docstrings describe the structure and attributes of Python functions and classes. These have special treatment in most Python environments. They are printed out whenever the command `help(name_of_object)` is run, and some IDE like VSCode render docstrings in a popup when your cursor hovers over a function.

There are lots of different conventions for formatting docstrings, depending on preferences. For generality, I usually recommend using one of the [Napolean supported docstring formats](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/). The Google docstring format uses less vertical space at the expense of longer horizontal descriptions, while the Numpy format uses more verticle space, but has shorter lines. I generally prefer less scrolling, and so I'll use the Google format throughout this tutorial. If you generally write code in a Terminal or other settings where horizonal scanning is difficult, then the numpy format may be preferred.

Here's an example of a function that computes each step of the dynamics of a particle in a potential well.

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

There are a few things to note: the syntax of the docstring is rather strict. We declare the type of each argument, and the type of the return value. We also include a description of the function, and the meaning of each argument. This explicit, rigid structure is useful for other users of your code, and also for your future self. If you come back to a function you wrote a year ago, you'll have a description of what it does. The strict syntax helps the computer format the docstring when the `help` command is invoked, and it will also make it possible to automatically generated online documentation for code using an [autodoc tool](http://www.wgilpin.com/howto/howto_sphinx.html).

## Docstring entries

The docstring for a function should always include the following entries: 
+ Args: A description of each argument, including the type of the argument
+ Returns: A description of the return value, including the type of the return value

Additionally, you might find it useful to include the following entries:

+ Raises: A description of any errors that may be raised by the function
+ Yields: A description of the values yielded by a generator function
+ Warnings: A description of any warnings that may be raised by the function
+ Notes: Any additional information that may be useful to the user
+ See Also: A list of related functions
+ Examples: A list of examples of how to use the function


## Docstrings for classes

For classes, we usually place the appropriate docstring at the top level, rather than within the `__init__` method. However, placing documentation in the top-level class versus the `__init__` method is a [matter of convention,](https://peps.python.org/pep-0257/) and both are valid. However, in most environments, the `help` command will print out the docstring for both the class and the `__init__` method when it is called on the class itself, and not just on an instance of the class. 

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
