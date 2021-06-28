# opentypespec


[![PyPi Status]][PyPi]

[PyPi Status]: https://img.shields.io/pypi/v/opentypespec.svg
[PyPi]: https://pypi.python.org/pypi/opentypespec

This package currently provides the ``opentypespec.tags`` module, which
exports ``FEATURE_TAGS``, ``SCRIPT_TAGS``, ``LANGUAGE_TAGS`` and
``BASELINE_TAGS`` dictionaries, representing data from the
Layout Tag Registry (section 6.4 of the Open Font Format specification):

```python
        >>> from opentypespec.tags import SCRIPT_TAGS, LANGUAGE_TAGS
        >>> SCRIPT_TAGS["adlm"]
        {'name': 'Adlam'}
        >>> LANGUAGE_TAGS["ECR "]
        {'name': 'Eastern Cree', 'iso639': ['crj', 'crl']}
```

* Data derived from the ISO/IEC 14496-22 “Open Font Format” specification.
* The Python code in this module is licensed under the Apache Software License 2.0

## History

### 1.8.4 (2021-06-28)

* First release on PyPI.
