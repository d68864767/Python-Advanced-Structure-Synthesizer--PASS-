# Contributing to Python Advanced Structure Synthesizer (PASS)

First off, thank you for considering contributing to PASS. It's people like you that make PASS such a great tool.

## Where do I go from here?

If you've noticed a bug or have a feature request, make sure to check our [Issues](https://github.com/yourusername/pass/issues) page to see if someone else in the community has already created a ticket. If not, go ahead and make one!

## Fork & create a branch

If this is something you think you can fix, then fork PASS and create a branch with a descriptive name.

A good branch name would be (where issue #325 is the ticket you're working on):

```shell
git checkout -b 325-add-japanese-localisation
```

## Implement your fix or feature

At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first.

## Get the code

The first thing you'll need to do is get the code. Start by [forking](https://help.github.com/articles/fork-a-repo) the repository.

Then, clone your fork locally:

```shell
git clone [your-fork-url]
cd pass
```

## Make your changes

Make the changes to the code and the documentation. Try to make your changes fit in with the existing code - follow the style the best you can.

## Test your changes

It's important to ensure your changes don't break anything and that the code runs as expected. Run the existing tests and create new ones for your changes.

## Create a pull request

At this point, you should switch back to your master branch and make sure it's up to date with PASS's master branch:

```shell
git remote add upstream git@github.com:yourusername/pass.git
git checkout master
git pull upstream master
```

Then update your feature branch from your local copy of master, and push it!

```shell
git checkout 325-add-japanese-localisation
git rebase master
git push --set-upstream origin 325-add-japanese-localisation
```

Finally, go to GitHub and [make a Pull Request](https://help.github.com/articles/creating-a-pull-request) :D

## Keeping your Pull Request updated

If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.

To learn more about rebasing in Git, there are a lot of [good](https://git-scm.com/book/en/v2/Git-Branching-Rebasing) [resources](https://www.atlassian.com/git/tutorials/merging-vs-rebasing) but here's the suggested workflow:

```shell
git checkout 325-add-japanese-localisation
git pull --rebase upstream master
git push --force-with-lease origin 325-add-japanese-localisation
```

## Code review

A team member will review your pull request and provide feedback. Please be patient, as review times can vary. Once approved, your pull request will be merged into the master branch.

## That's it!

Congratulations! You have just contributed to the PASS project. You're a member of the team. Thank you for your hard work and dedication.
