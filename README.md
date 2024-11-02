# resilience-toolkit

[![PyPI - Version](https://img.shields.io/pypi/v/resilience-toolkit.svg)](https://pypi.org/project/resilience-toolkit)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/resilience-toolkit.svg)](https://pypi.org/project/resilience-toolkit)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install resilience-toolkit
```
## Examples

(Hypothetical) example of multiple resilience methods working together

```python

@timing(tmax=3)
@fallback()
@circuitbreaker()
@retry(tries=3, sleep=0.12, backoff=exponential)
@timing(tmax=0.3)
def foo(a,b):
    # do some networking stuff
    pass

@fallback.foo()
@timing(tmax=0.3)
def foo_alt():
    # some backup method
    pass

```

## License

`resilience-toolkit` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
