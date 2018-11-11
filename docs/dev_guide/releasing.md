# 🚀 Releasing

To release a new version of Thea a couple of steps need to be taken here
we will walk you trough all of them. First ensure all the the
[planned features](https://mikevansighem.github.io/thea/PLANNED) for the next
release are committed to the master branch. If so everything is set to start 
the release process.

## Clone the repository

Clone the repository using `git` for local editing of files.

```bash
git clone git@github.com:mikevansighem/thea.git
cd thea
```

Change to the branch for release creation.

```bash
git checkout -b release_v1.0.8
# replace `1.0.8` with the new version number
```

## Bump the version

Within `pyproject.toml` the version number needs to be bumped up according
to [Semantic versioning](https://semver.org/spec/v2.0.0.html).

## Updating the changelog

Update the [changelog]() 
to include all notable changes. The format of our changelog is based on 
[Keep a changelog](https://keepachangelog.com/en/1.0.0/). 
Most importantly this means we sort the changes in categories:

-   Added: new features;

-   Changed: changes in existing functionality;

-   Deprecated: soon-to-be removed features;

-   Removed: now removed features;

-   Fixed: bug fixes 
    (if available include a link to the issue);

-   Security: fixing of vulnerabilities 
    (if available include a link to the issue).

Within categories we sort based on importance to an end users. For the rest 
Of the formatting just copy it from a previous release 😉.
When in doubt whether to include a change in the log just remember:
*"Changelogs are for humans, not machines."*

## Commit and pull-request

Commit the changes to the release branch and push to origin.

```bash
git commit -m ":rocket: Getting ready for release v1.2.8" 
# replace `1.0.8` with the new version number

git push
```

Head over to [Github](https://github.com/mikevansighem/thea/pulls) 
and create a pull request to merge the changes into the master branch.
Wait for the checks to pass and merge.

## Adding a tag

Go to the [releases page](https://github.com/mikevansighem/thea/releases)
on Github and draft a new release where:

-   The tag is set to the version preceded by a `v` for example `v1.2.8`;
-   The target branch is set to `master`;
-   The title is set to the version preceded by a `v` for example `v1.2.8`;
-   The description copied from the [changelog]() minus the top header.

Press "Publish Release" and our the CI should takes care of releasing 
the binaries on [PyPi]() 
and updating our [documentation](https://pypi.org/project/thea/).
