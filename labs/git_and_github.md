# Lab 2: Git, GitHub, and GitHub pages

## Setting up git and GitHub

1. Install git on your local computer by following the instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Git is a code project management tool that is used primarily for version control and collaboration. The [documentation](https://git-scm.com/doc) is excellent.

2. Make a GitHub account. You might consider applying to link your account to your school email via [GitHub for Education](https://education.github.com/). This comes with a lot of perks, like private repositories and free access to the GitHub Copilot plugin for VSCode and PyCharm.

3. Create a local project folder on your computer containing code that you want to track. For example, you might want to create a folder for your course homeworks, or for these labs, or for your final project when the time comes. For now, let’s just make a test repository, to make sure that everything is working.


	$ mkdir my_repository
	$ cd my_repository


4. You should now be inside your new repository. Add a README.md file to your local repository. You can use a text editor like VSCode, Jupyter, or Sublime text, or, if you are familiar with emacs, you can do this in the terminal

	$ emacs README.md

5. Connect your local project to a public GitHub repo by following the instructions here. Briefly, you will start by logging into your GitHub account, and then making a repository with the exact same name as your local project folder. When prompted, do *not* initialize your remote repo with a README or license. When the empty repository has been created, it should be located online.

	https://github.com/yourusername/my_repository


6. On that webpage, GitHub should show you the exact steps you need to perform locally to connect. Since we already made a README, you will need to start by staging the changes in your local repository. 

	git add .

You can then follow the rest of GitHub’s instructions to push your local repository onto your remote repository. When you navigate to your project directory online, you should see your README file

	https://github.com/yourusername/my_repository



Once everything is working 

## Collaboration

When used for single projects, GitHub acts sort of like a manual Dropbox folder, where you deliberately decide when to update the copy of your code that exists in the cloud. This might seem tedious, but as projects grow it becomes useful to keep track of versions, run automated tests before commits, etc. One of the most important use cases is collaboration, where multiple people are working with the same remote repository.

If, during the course, you notice a typo or error in the class repository, please fork the repository, correct the change, and submit a pull request [using the instructions here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request). Make sure that your PR has been synchronized with the latest version of the class repository (git pull first), in order to avoid merge conflicts. If you have time in class today, feel free to try doing this—even to correct a minor typo, or improve some formatting. 

Important: if you have a fork of the class repository that you are using to complete the homeworks, please make sure that you don’t use your assignment fork to submit pull requests to my main repository. Since your versions of the assignments will override mine, it could lead to weird merge conflicts. If you fork a single version of the class repo in order to complete the assignments, please make sure you periodically [`git pull`](https://git-scm.com/docs/git-pull) to get any changes in the assignments. Double check to make sure that your pull doesn't override your completed assignments with my incomplete assignments

For the Jupyter Notebooks and for README.md, we will be using a typesetting language called Markdown. This is like a blend of LaTeX and HTML, and it is a very common tool nowadays for code documentation


## GitHub pages

We are now going to a create a basic website to accompany our repository. This usually isn’t necessary, but I think this feature is worth knowing about for when you quickly need to create a website—for example, for [this course’s webpage](https://www.wgilpin.com/cphy/)

1. We will follow the instructions [from GitHub](https://pages.github.com/) are pretty clear. The simplest thing you can do is go into your repository’s online settings through the GitHub GUI, and activate the option for GitHub pages. It should automatically convert your README.md file into an index.html file and then host it at:

	https://yoursusername.github.io/my_repository


GitHub pages are structured as “actions” that run every time you push from your local to the remote on GitHub. This is similar to automated testing, which we will explore in a future lab. As a result, your website won’t automatically update as quickly as the repo itself, due to an extra “build” step. If the “build” fails, then on your repository you will see a red “X” on the commit. An orange dot indicates that the build has not occurred yet. If your website has still not updated, go to the URL and refresh the page with a clear cache; [CMD] + [Shift] + R


## FAQ:
Any questions or problems that arise, as well as their solutions, can go here

