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
- Upload as a public repository to an online hosting service, [gitee](https://gitee.com/) used in course, where alternatives are ex.
  - [gitcode](https://gitcode.com/)
- Share repository URL with all peers in class, **read only** (default)
- Clone another students work
- Submit your `research stories`, from the day 1 exercise, into your public student repository.

Group work;

- Group up and create public repository for group memebers, with **write permissions** (optional, see below) within the group
  - Ca. four students in each group
  - There can be one **central repository**, and several subsidiary repositories; **requirement** is, share the central repository with teacher and peer students.
    - this substitute collaboration over the same repository, with write permissions.
- Share central group repository URL with student peers
- Each student within the group accesses the group repository, according to agreed way of work
- Each student create their own branch, and within their private branch
  - update `README.md` with a 3 sentence long **summary** of your course _intentions_ in a separate _paragraph_.
  - upload the student branch to the central repository
    - might inglude requests etc., depending on your setup on group work
- Merge all student branches in the group, into the default or `master` branch, in the central group repository
- Make sure that the merged default branch is updated to the groups central repository.

## References

- https://en.wikipedia.org/wiki/Git
  - https://git-scm.com/
- https://en.wikipedia.org/wiki/Bash_(Unix_shell)
