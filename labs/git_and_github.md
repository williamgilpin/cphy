Lab 2: Git, GitHub, and GitHub pages
==============

## Setting up git and GitHub

1. Install git on your local computer by following the instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Git is a code project management tool that is used primarily for version control and collaboration. The [documentation](https://git-scm.com/doc) is excellent.

2. Make a GitHub account. You might consider applying to link your account to your school email via [GitHub for Education](https://education.github.com/). This comes with a lot of perks, like private repositories and free access to the [GitHub Copilot](https://github.com/features/copilot) plugin for VSCode and PyCharm.

3. Create a local project folder on your computer containing code that you want to track. For example, you might want to create a folder for your course homeworks, or for these labs, or for your final project when the time comes. For now, let’s just make a test repository, to make sure that everything is working.

```
$ mkdir test_repo
$ cd test_repo
```

4. You should now be inside your new repository. Add a README.md file to your local repository. You can use a text editor like VSCode, Jupyter Lab, or Sublime Text, or you can do this in the Terminal with your preferred editor (I use emacs):

```
$ emacs README.md
```

5. Connect your local project to a public GitHub repo by following the instructions here. Briefly, you will start by logging into your GitHub account, and then making a repository with the exact same name as your local project folder. When prompted, do *not* initialize your online remote repo with a README or license. When the empty repository has been created, it should be located online.

	https://github.com/yourusername/test_repo

6. On your empty repo's GitHub page, there will be instructions listing what to do in order to get everything working on your local repo. I've summarized them here. Briefly, in your local repo, you should initialize git, add/stage, commit them, switch branches, connect to the remote, and then push

```
$ git init
$ git add .
$ git commit -m "first commit"
$ git branch -M main
$ git remote add origin https://github.com/yourusername/test_repo.git
$ git push -u origin main
```

If this is your first time setting up GitHub and git, the commands will fail at some point and you will be asked to set up your git and GitHub credentials. You can follow the prompts in your Terminal, but if that fails then you need to create a settings file manually. Create a top-level file on your system called `.gitconfig`. Mine is located at the top level `~/.gitconfig` and contains the following lines

```
[user]
        name = williamgilpin
        email = williamgilpin@gmail.com
[core]
        editor = emacs
[credential]
        helper = store
```

7. Once you have your `.gitconfig` set up, attempt again to run the commands from step 6. You will probably be prompted for your password or access token. To set up your local Terminal to automatically remember your GitHub login info, you need to create a Personal Access Token (PAT) using the instructions [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token). I set mine up with maximal priveleges and no expiry. After obtaining the PAT, attempt yet again to run the commands from step 6, but this time enter your PAT instead of your password.

8. The basic solo git workflow is pretty straightforward; it's like a manual Dropbox folder you manage from the Terminal. Make some changes to your local repository; for example, by editing into your README.md file. Whenever you want to apply those changes to the remote (the GitHub version of your code), first add these files in the Terminal (make sure you are in your repository). Since we already made a README.md file, you will need to start by staging the changes in your local repository. 

```
$ git add .
```

9. Then commit the changes with a short but descriptive message

```
$ git commit -m "added example changes to the README file"
```

10. Then finally send the update to GitHub

```
$ git push
```

Both your local and the GitHub versions of your repo will keep track of the sequence of commits you've applied, making it easier to roll back your changes at any time. You'll notice that GitHub treats README.md as a special file---it renders it into a nice page, similar to a website's index page, that represents the first thing a user sees when they look at your repo. Usually we want to put a description of the repo, dependencies, and a minimal working example into the README.md---although sometimes the README contains full documentation, graphics, etc. The Google [Jax repository](https://github.com/google/jax) is a great example. Rather than HTML, the markup language used for README files is Markdown, which is like a blend of HTML and LaTeX with lighter syntax than either one. You can learn more from the [Markdown guide](https://www.markdownguide.org/basic-syntax/) or by looking at [the unrendered version](https://raw.githubusercontent.com/williamgilpin/cphy/main/README.md) of this course's own README file

You might have local files that you don't want to appear in your public repo. For example, in the course repository I have solution files, as well as personal files like cached data, that I don't want to appear on GitHub. For files of this nature, it's usually a good idea to create a file called `.gitignore` in the top-level repository of your local repo. This specifies files or patterns that should be ignored. See the [gitignore documentation](https://git-scm.com/docs/gitignore) as well as [the one I'm using for the course repo](https://github.com/williamgilpin/cphy/blob/main/.gitignore)

## GitHub pages

We are now going to a create a basic website to accompany our repository. This usually isn’t necessary, but I think this feature is worth knowing about for when you quickly need to create a website—--for example, for [this course’s webpage](https://www.wgilpin.com/cphy/) is written entirely in Markdown, and rendered into HTML internally via GitHub (which also provides free hosting for small websites)

1. We will follow the instructions [from GitHub](https://pages.github.com/) are pretty clear. The simplest thing you can do is go into your repository’s online settings through the GitHub GUI, and activate the option for GitHub pages. It should automatically convert your README.md file into an index.html file and then host it at:

	https://yoursusername.github.io/my_repository

GitHub pages are structured as “actions” that run every time you push from your local to the remote on GitHub. This is similar to automated testing, which we will explore in a future lab. As a result, your website won’t automatically update as quickly as the repo itself, due to an extra “build” step. If the “build” fails, then on your repository you will see a red “X” on the commit. An orange dot indicates that the build has not occurred yet. If your website has still not updated, go to the URL and refresh the page with a clear cache; [CMD] + [Shift] + R


## Collaboration

When used for single projects, GitHub acts sort of like a manual Dropbox folder, where you deliberately decide when to update the copy of your code that exists in the cloud. This might seem tedious, but as projects grow it becomes useful to keep track of versions, run automated tests before commits, check for conflicting commits, etc. One of the most important use cases is collaboration, where multiple people are working with the same remote repository.

It's a bit too much to try to attempt this during the class period, but to practice with this in the future, at some point during the term you might try submitting a pull request to the course repository on GitHub. 

+ Fork the repository on GitHub [via these instructions](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository)
+ Make any changes that you want. It's probably best to start with something small, like fixing small errors
+ Make sure that your local branch is up-to-date with the course using fetch (see instructions [here](https://stackoverflow.com/questions/7244321/how-do-i-update-or-sync-a-forked-repository-on-github)). This is to account for the case where I've made changes to the course repo while you've been making your changes.
+ When everything looks good, submit a pull request [using the instructions here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

For smaller projects (like the class projects), it isn't necessary to use pull requests---instead, you can [invite collaborators to a shared repository](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository), and everyone wil be able to make commits.

Important: if you have a fork of the class repository that you are using to complete the homeworks, please make sure that you don’t use your assignment fork to submit pull requests to my main repository. Since your versions of the assignments will override mine, it could lead to weird merge conflicts. If you fork a single version of the class repo in order to complete the assignments, please make sure you periodically [`git pull`](https://git-scm.com/docs/git-pull) to get any changes in the assignments. Just double check to make sure that your pull doesn't override your completed assignments with my incomplete assignments




## Other useful git and GitHub facts
Any questions or problems that arise, as well as their solutions, can go here

### Downloading a remote repository without forking it

Sometimes you just want to download a copy of someone's code without collaborating, forking, etc. For situations like these, you can use [git clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository). I recommend cloning from the HTTP address rather than the git// address of the repo

### Installing a Python Package from GitHub

If there's a setup.py file in the repo, you can install using pip

pip install git+git://github.com/someusername/somerepo


### Modifying commit history

To alter or combine the last four commits, run
```
$ git rebase -i HEAD~4
```
A text editor will pop up. Replace "pick" with "squash" for the commits that you want to merge together. It will then prompt you to come up with a new commit message for all of the commits that you just squashed.

If you've already commited, you have to force the update:
```
$ git push origin main --force
```
### Forking a repository summarized

clone forked repo locally
```
$ git clone "https://...MY_USERNAME...
```
add upstream branch
```
$ git remote add upstream "https://...THEIR_USERNAME...git
```
make a new branch
```
$ git add branch BRANCH_NAME
```
switch to new branch and make edits
```
$ git checkout BRANCH_NAME
```
push new commits
```
$ git add .
$ git commit -m "test commit plz ignore"
$ git push
```
go to github and make a pull request


### Cannot stage changes

Sometimes instead of `git add .` you need to use `git add --all`
This can be fixed by stashing and then immediately un-stashing:
```
$ git stash
$ git stash apply
```
### Permission issues

`error: insufficient permission for adding an object to repository database .git/objects`

Somehow the ownership got messed up for some files. From project base directory, try running
```
cd .git/objects
ls -al
sudo chown -R yourname:yourgroup *
```
yourname and yourgroup can be figured out by seeing what the majority of of the ls -al usernames and groups are. My "group" appeared to be staff for some reason. This answer is taken from [StackExchange](http://stackoverflow.com/questions/6448242/git-push-error-insufficient-permission-for-adding-an-object-to-repository-datab)


### Receive warnings about passwords being deprecated 

Depending on when you created your GitHub account, you may need to follow the instructions [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) to create a PAT. 

To store the PAT after creating it, I followed the instructions [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token), and then [here](https://docs.github.com/en/get-started/getting-started-with-git/updating-credentials-from-the-macos-keychain). I also removed the file `~/..git-credentials`

+ Other useful information about storing PAT [here](https://askubuntu.com/questions/773455/what-is-the-correct-way-to-use-git-with-gnome-keyring-and-https-repos/959662#959662) and [here](https://stackoverflow.com/questions/46645843/where-to-store-the-personal-access-token-from-github)

