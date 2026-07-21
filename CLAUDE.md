# CLAUDE.md: python-sdk

The LiveStyled Python SDK (pip package `livestyled`): a shared REST client for apiv3's Hydra/JSON-LD
API, used by the platform's Python lambdas to read and write Spotlight resources (users, devices,
tickets, events, device realities, and so on) without each one re-implementing the HTTP + (de)serialization
layer. Historically named after LiveStyled (the company that became RealifeTech, then AudienceView).

## Role in the platform

This is a library, not a deployed service: it has no lambda handler, no `serverless.yml`, no runtime of
its own. It is published to public PyPI (`pypi.org`, project `livestyled`) and pulled in as a dependency by
the Python lambdas across the workspace, either directly (e.g. `connect.av.av_ticketing`,
`connect.realife.goodtill`, `connect.realife.axs`, `connect.realife.sso`, `platform.register_device_on_sns`,
`platform.cohort_actions`) or transitively via `reality-evaluator`
(`git@bitbucket.org:livestyled-dev/reality-evaluator.git`), which the Realities evaluators depend on.
It talks to apiv3, the platform's source of truth, over REST; it is not a GraphQL client (the Apollo
gateway is reached by other components). Every consumer pins an exact version, so a new SDK release never
reaches a consumer until that consumer explicitly bumps its own pin.

## Run it

- `pip install -r requirements_dev.txt` (all deps, runtime and dev, are on public PyPI; no private index
  needed here, unlike the consumer lambdas)
- `tox` runs flake8 + the pytest suite (`livestyled/tests/`, ~49 tests exercising the model schemas'
  serialization/deserialization). CI is GitHub Actions (`.github/workflows/unit_tests.yml`), matrixed
  across supported Python versions.

There is no application to start: you exercise it by instantiating `LiveStyledAPIClient`
(`livestyled/client.py`) against an apiv3 base URL + API key and calling its resource methods, or by running
the tests, which mock the HTTP layer with `requests-mock`.

## Deploy

Publishing is manual, to public PyPI, per the internal wiki:

1. Update `__version__` in `livestyled/__init__.py` (semver).
2. Commit the version bump.
3. From the repo root: `python setup.py sdist; python3 -m twine upload dist/* --verbose; rm dist/*`

You need a PyPI account token with publish rights on the `livestyled` project (this is separate from GitHub
access). There is no automated release pipeline in the repo (the only GitHub Actions workflow runs the
tests); the `.devN` versions on PyPI come from the same manual script run off non-release branches.

## How it works

`livestyled/client.py` (`LiveStyledAPIResourceClient`, ~26 resource methods) is a thin REST client over
`requests`: `_api_get` / `_api_get_paginated` / `_api_post` / `_api_patch` / `_api_put` / `_api_delete`
issue the HTTP calls with the configured API key headers, and `_api_get_paginated` follows apiv3's
Hydra/JSON-LD pagination (`hydra:member` for the page, `hydra:view` -> `hydra:next` for the next page).
Each resource has a model under `livestyled/models/` (~45) and a marshmallow schema under
`livestyled/schemas/` (~46) that maps between the API's camelCase JSON-LD payloads and the SDK's snake_case
model attributes; the resource methods return either model instances or raw dicts depending on the call.
The runtime deps (`marshmallow`, `requests`) require Python >= 3.9, so from 2.0.0 the SDK no longer runs on
Python 3.7/3.8 that earlier versions supported (which is why that jump was released as a major); the
marshmallow pin is kept on the 3.x line deliberately, since 4.x would break the schemas' `missing=` usage.
