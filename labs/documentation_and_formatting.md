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

For classes, we usually place the appropriate docstring in the `__init__` method. This is because the `help` command will print out the docstring for the class when it is called on the class itself, and not on an instance of the class. 

```python
class OrnsteinUhlenbeck:
    """
    A class for simulating the motion of a particle in a one-dimensional harmonic potential well
    with Brownian forcing

    Args:
        x0 (float): The location of the potential minimum

    Attributes:
        x0 (float): The location of the potential minimum
        traj (list): The trajectory of the particle

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
```

The docstring for the class itself should include a description of the class, and a description of each attribute. The docstring for the `__init__` method should include a description of the class, and a description of each argument. The docstring for the `step` method should include a description of the method, and a description of the return value.

+ Attributes: A description of each attribute of the class
+ Methods: A description of each method of the class
+ Raises: A description of any errors that may be raised by the class
+ Warnings: A description of any warnings that may be raised by the class
+ Notes: Any additional information that may be useful to the user
+ See Also: A list of related classes
+ Examples: A list of examples of how to use the class
