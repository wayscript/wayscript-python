# Contribution Guide

## Running Locally

To speed up development cycles you can run tests and linting locally with:
```
export DOCKER_DEFAULT_PLATFORM=linux/amd64

docker-compose run --rm app lint
docker-compose run --rm app test
```
This will mount your local working directory into the container and set it as the working directory within the container.

To exactly replicate the CI steps, add the `-f docker-compose.ci.yml` arg to the above commands.

## Publishing A New Version

To cut a new version, follow these steps:

- create and merge final feature branch updating `CHANGELOG.md`
- tag final commit hash with `git tag <VERSION>`, e.g. `git tag 0.1.3`.
- declare the `VERSION` veriable in `usr/local/bin/publish.sh` to the same version, e.g. `VERSION=0.1.3`
- make sure your terminal ENV variables have `TWINE_PASSWORD` set to the proper PyPi password
- publish to pypi with:
```
docker-compose run --rm app bash publish.sh
```
- push tag to github with `git push --tags`
