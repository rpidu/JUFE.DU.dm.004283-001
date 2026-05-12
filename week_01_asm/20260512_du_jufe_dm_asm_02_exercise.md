# Day 2 Exercise – CLI & Git

## Objective

Create a repository and track changes.

## Example

Following example is in BASH, but works precisely the same in powershell;

```bash
mkdir project
cd project
git init
echo "# Project" > README.md
git add README.md
git commit -m "Initial commit"
```

## Tasks

- Modify README.md
- Create a second commit

## Challenges

Student work;

- Create a branch
- Do some edits to the README.md; ex. put in the name of the course in the headline
- Merge changes
- Upload as a private repository to an online hosting service, [gitee](https://gitee.com/) used in course, where alternatives are ex.
  - [gitcode](https://gitcode.com/)
- Share private repositories with all peers in class, **read only**
- Clone another students work
- Submit your `research stories`, from the day 1 exercise, into your private student repository.

Group work;

- Group up and create private repository for group memebers, with **write permissions** within the group
  - Ca. four students in each group
- Share group repositories with student peers, **read only**
- Each student within the group clones the group repository
- Each student create their own branch, and within their private branch
  - update `README.md` with a 3 sentence long **summary** of your course _intentions_ in a separate _paragraph_.
  - upload the student branch to the online hosted repository (origin)
- Merge all student branches into the default or `master` branch, in the group repo
- Push the default or `master` branch, with the merge, to origin (the online hosted repository)

## References

- https://en.wikipedia.org/wiki/Git
  - https://git-scm.com/
- https://en.wikipedia.org/wiki/Bash_(Unix_shell)
