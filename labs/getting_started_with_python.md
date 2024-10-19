## Lab 1: Getting Started with Python
*William Gilpin*

Additional information about Python and conda environments can be found in [William’s detailed notes](http://www.wgilpin.com/howto/howto_conda.html)

1. Before following the instructions below, go ahead and set up a Google Colaboratory account. You should be able to do by clicking one of the "Live Notebook" links on [the course webpage](https://github.com/williamgilpin/cphy). [Here is a link to the first lecture.](https://colab.research.google.com/github/williamgilpin/cphy/blob/main/talks/python_intro.ipynb) Google Colab is a purely cloud-based development environment. If you ever run into issues with Python on your own computer, feel free to use Google Colab as a backup. However, I would recommend setting up Python on your own computer for the course, since there many features that are not available in Google Colab.

2. If you are a Windows user, make sure that you have activated Windows Subsystem for Linux (WSL). Instructions for doing this can be found [here](https://www.wgilpin.com/howto/howto_pythononwindows.html). For all of the Terminal/bash commands that we will use in this tutorial, it is recommended that you use the WSL Terminal application, rather than the Anaconda Terminal, Powershell, or Command Prompt. If you are a macOS or Linux user, you can use the default Terminal application that comes with your computer.

3. Install Miniconda on your development environment. OS-specific instructions can be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). macOS users should install [Homebrew](https://brew.sh/) as well, while Linux or WSL users should have access to `apt-get` or `yum` package managers. The instructions on the conda webpage include a step where you download an installer shell script with a `.sh` extension. The script you download depends very specifically on your OS and hardware (Intel, Apple Silicon, etc), double check that you download the correct [installation script version](https://docs.conda.io/en/latest/miniconda.html).

    > Note: if you are already a Python user, you may already have a preferred package and environment manager. William, for example, uses [mamba](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html) instead of conda.
    
    Depending on your research needs, you may find the [full Anaconda distribution](https://www.anaconda.com/) preferable. Advanced users may also want to consider [Mamba](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html), which is a faster drop-in replacement for conda, but which has less existing support threads.

4. Open your computer’s terminal app. On Windows, Miniconda will install the Anaconda Terminal, which you can use as the default Terminal for this class. Otherwise, you may need to use [Windows Terminal](https://github.com/microsoft/terminal) or [gitbash](https://gitforwindows.org/) instead. If you plan to use Windows for the class, please post in the class forum about any bugs or compatibility issues you encounter, as well as their solutions---that will make it easier for us to make the materials more accessible in future iterations.

5. In your terminal app, create a new virtual environment using the base Python install. I named mine hwenv, but you can call it whatever you want.
  ```bash
    $ conda create -n hwenv python=3
  ```
  This virtual environment will be used to isolate your code and the packages on which it depends from your system’s own Python installation, as well as from other Python projects you might make in the future. For example, you will likely want to make a separate environment for your final project, and for separate personal projects. On my personal computer, I have about a half-dozen environments—one for each different project, including one for this class. If I make a mistake while working on this class and break my environment’s Python installation, it won’t affect my other projects.

6.  Before writing any code, always make sure that you have activated your environment.
  ```bash
    $ conda activate hwenv
  ```

7. We can now start Python and check that it is working
  ```bash
      (hwenv) $ python
  ```

8. Check that your Python version is greater than 3.0
  ```python
    >> import sys
    >> print("User Current Version:-", sys.version)
  ```

9. Terminate the Python process with Ctrl + D on \*nix, or  Ctrl + Z followed by Enter on Windows.

10. *(Optional).* If your Python version does not start with a 3, delete your environment and then make a new environment with a newer version
  ```bash
    $ (hwenv) $ conda deactivate
    $ conda remove -n hwenv --all
    $ conda create -n hwenv python=3
    $ conda activate hwenv
  ```
  If you need to exit the environment for any reason in order to get back to your base Python installation, you can do so by running
  ```bash
    $ conda deactivate
  ```

11. Back in the Terminal, install some other packages that we will end up using a lot 
  ```bash
    $ conda activate hwenv
    (hwenv) $ conda install numpy matplotlib ipykernel
    (hwenv) $ conda install -c conda-forge jupyterlab
  ```
  A list of other common packages you will need to install appears on [the course homepage.](https://www.wgilpin.com/cphy) Notice how your current environment appears to the left of the `$` symbol in the Terminal. If you close and re-open your Terminal, you'll need to re-activate your conda environment before installing new files.

12. There are two ways that I would recommend using Jupyter notebooks for the class. One option is to manually activate an environment and then launch the notebook server from the Terminal.
  ```bash
    (hwenv) $ jupyter lab
  ```
  This should forcefully open a browser window running the environment. You can run this step to make sure that everything is working.

13. To test that you have everything working, try downloading the [first lecture notebook](https://github.com/williamgilpin/cphy/blob/main/talks/python_intro.ipynb). Now would be a good time to make a dedicated folder on your local computer for this course. If you are a git user, you can clone the repository. Otherwise, you can download the notebook directly from the browser into the folder you've created. Run the cells in the notebook in order (top to bottom) by pressing Shift + Enter. If you get an error, make sure that you have activated the correct environment, and that you have installed the necessary packages.

14. **Setting up VSCode.** You can Jupyter Notebooks directly in Jupyter Lab, however I recommend using a full-featured integrated development environment (IDE). I really like Visual Studio Code. [Installation instructions](https://code.visualstudio.com/). PyCharm is another common IDE for Python, though I will not be using it in this class.
  If you successfully install VSCode, you can simply open the course notebooks by double-clicking them to open them in the VSCode GUI, as you would a document or slide deck.  However, if opening a `.ipynb` file, you should always check in the upper-right-hand corner of the notebook that you are using the correct conda environment (since we skipped using the Terminal, we never specified what environment to use). VSCode should automatically find and list the available environments in a drop-down menu, and it will remember your selection for each notebook. 
  The first time you open a notebook, VSCode will prompt you to install extensions for Jupyter, Python, and a few other utilities. Go ahead and accept the installation. 
  For VSCode, you will still need to use a Terminal session to create/edit your conda environments, as well as install and update packages into your environment. You will likely need to install `ipykernel` in your Python environment.

<!-- 12. Now that we know that everything is working, head over to the class repository on GitHub and start working on Lab 1, which uses some parts of the Python ecosystem in order to make really cool embeddings of high-dimensional datasets. -->


## FAQ:


*After installing Miniconda/Anaconda on Windows and accepting defaults, running `conda list` in the Anaconda Terminal doesn't work*



*Any questions or problems that arise, as well as their solutions, go here.*

On windows, `conda create` fails. Unset [SSL](https://stackoverflow.com/questions/50125472/issues-with-installing-python-libraries-on-windows-condahttperror-http-000-co) or use the Anaconda terminal

How do I downloading and access files on GitHub?
+ You can download an entire repository as a zip file through the GitHub GUI, or use `git clone` from the Terminal
+ When downloading `ipynb` files from the browser, watch out for conversion to `.txt`

My conda installation throws strange errors that refer to an executable file
+ Double check that you downloaded the correct [installation script version](https://docs.conda.io/en/latest/miniconda.html) for your particular OS and hardware (Intel, Apple Silicon, etc)

Anaconda Navigator

My VSCode fails to automatically detect the environment?
+ If VSCode failed to detect the environment automatically, you can point it toward the virtualenv like this:
bring up the VSCode command palette by pressing `Ctrl/Command + Shift + p` Then type in the search bar  `Open Workspace Settings (JSON)` This creates a `settings.json` file in a `.vscode` directory where you have opened the VSCode. Then add these lines to it:
```json
{
"python.defaultInterpreterPath": "PATH_TO_ENV/hwenv/bin/python"
}
```
After that head to the command palette again and search for `Python: Select Interpreter` then from the list that shows up you can select your environment. If you create a new Terminal you can find that all your changes have been applied.