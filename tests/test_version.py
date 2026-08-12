# Copyright Contributors to the BaySIL project.
# SPDX-License-Identifier: Apache-2.0

"""Smoke tests for BaySIL."""

import baysil


def test_version_is_set():
    """The package exposes a version string."""
    assert isinstance(baysil.__version__, str)
    assert len(baysil.__version__) > 0
