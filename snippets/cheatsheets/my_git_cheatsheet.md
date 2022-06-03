Ref: https://about.gitlab.com/images/press/git-cheat-sheet.pdf

# Branches
### Local
git branch
### Remote
git branch -a


### remote
git push origin --delete rkisnah/alarmfixes

#### local
git branch -d feature/login

## Create a branch
git checkout -b rkisnah/alarmfixes

### delete branches
// remote
// List branches
git branch -a

// Delete
git push origin --delete rkisnah/test
  
#### local
git branch -d rkisnah/test123

# git log 
git log --pretty=oneline

# BB and git

Create branch in BB  <br>
```
git fetch origin
git branch -v -a
git checkout -b rkisnah/onboardcentos origin/rkisnah/onboardcentos
```

## Tags
```
https://devconnected.com/how-to-checkout-git-tags/
https://git-scm.com/book/en/v2/Git-Basics-Tagging

# Fetch all tags 
git fetch --all --tags
# list all tags
git tag -l 
# checkout tag on a branch
git checkout tags/v2.12.0 -b test1

```
