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

(the first time you do this)
- get `maintainer` access to the `wayscript` project on pypi
- create an API key for the project (save for future use)
(all times)
- run `export TWINE_PASSWORD="<your api key>"` in terminal to set up environment variable
- tag final commit hash with `git tag <VERSION>`, e.g. `git tag 0.3.1`.
- in `publish.sh`, update `VERSION="<your version tag>"`
- publish to pypi with:
```
docker-compose run --rm app bash publish.sh
```
- push tag to github with `git push --tags`