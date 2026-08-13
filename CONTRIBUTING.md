# Contributing to BaySIL

Thanks for your interest in contributing.

## Getting set up

BaySIL uses [uv](https://docs.astral.sh/uv/) for dependency management and
Python 3.12 or later.

```bash
git clone https://github.com/michaelellis003/BaySIL.git
cd BaySIL
uv sync
```

Install the pre-commit hooks. All three stages are used, so all three
need installing:

```bash
uv run pre-commit install
uv run pre-commit install --hook-type commit-msg
uv run pre-commit install --hook-type pre-push
```

| Stage | What runs |
|---|---|
| `pre-commit` | whitespace and EOF fixes, YAML/TOML checks, private-key detection, `uv.lock` sync, license headers, `ruff check --fix`, `ruff format` |
| `commit-msg` | conventional commit message validation |
| `pre-push` | `ty` type check |

## Making changes

A `Makefile` collects the common commands:

```bash
make test        # lint, then pytest
make lint        # ruff check, format check, license headers, ty
make format      # add license headers, ruff format, ruff fix
make docs        # build documentation
make serve-docs  # serve documentation locally
```

`make test` runs `make lint` first, so it is the single command to run
before pushing.

Every Python file needs an SPDX license header. `make license` adds any
that are missing.

## Commit messages

Commit messages must follow
[Conventional Commits](https://www.conventionalcommits.org/) — this is
enforced by a `commit-msg` hook, so a non-conforming message is rejected
locally before it reaches CI.

The prefix determines the next version when a release is cut:

| Prefix | Effect |
|---|---|
| `fix:` | patch release |
| `feat:` | minor release |
| `BREAKING CHANGE:` footer, or `!` after the type | major release |
| `docs:`, `ci:`, `chore:`, `test:`, `refactor:` | no version change |

Pick the prefix that describes the change honestly. A `fix:` on something
that fixes nothing puts a misleading line in a published changelog.

## Opening a pull request

1. Fork the repository and branch from `main`.
2. Make your change, with tests where it makes sense.
3. Run `make test`.
4. Open a pull request against `main`.

**If you are an outside contributor, CI will not start automatically.**
Workflows on pull requests from forks require a maintainer to approve the
run first, so your PR may show no checks for a while. This is expected —
it is not a sign that anything is wrong.

Once CI runs, the `ci-pass` check must be green before the PR can merge.
It aggregates linting, type checking, and the test matrix across Python
3.12–3.14 on Linux, macOS, and Windows.

A maintainer merges the PR once it is approved and green.

## Releases

Contributors do not need to do anything for a release. Releases are cut
deliberately by a maintainer running the Release workflow, which requires
approval before it publishes anything. Your merged commits determine the
version number automatically via their conventional commit prefixes.

## License

By contributing, you agree that your contributions will be licensed under
the Apache 2.0 License, the same license that covers this project.
