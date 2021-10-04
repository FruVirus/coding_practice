"""This module contains the global configurations for all tests."""

# Standard Library
import os

# Third Party Library
import pytest

# Assign the repository name.
REPO_NAME = "coding_practice"

# Assign default directories.
REPO_DIR = os.path.join(os.getcwd().split(REPO_NAME)[0], REPO_NAME)
CLRS_DIR = os.path.join(REPO_DIR, "src", "clrs")
G4G_DIR = os.path.join(REPO_DIR, "src", "g4g")
LEET_DIR = os.path.join(REPO_DIR, "src", "leet")
PYTHON_DIR = os.path.join(REPO_DIR, "src", "python")
TESTS_DIR = os.path.join(REPO_DIR, "tests")
FIXTURES_DIR = os.path.join(TESTS_DIR, "fixtures")

# Define pytest marks.
PARAM = pytest.mark.parametrize
SKIP = pytest.mark.skip
SKIPIF = pytest.mark.skipif
XFAIL = pytest.mark.xfail


# Define pytest-bdd hooks.
def pytest_bdd_step_error(
    request, feature, scenario, step, step_func, step_func_args, exception
):
    print(f"Step failed: {step}")


# Define pytest fixtures.
def pytest_addoption(parser):
    parser.addoption(
        "--clrs_only",
        action="store_true",
        default=False,
        help="Run CLRS tests only.",
    )
    parser.addoption(
        "--g4g_only",
        action="store_true",
        default=False,
        help="Run G4G tests only.",
    )
    parser.addoption(
        "--leet_only",
        action="store_true",
        default=False,
        help="Run Leet Code tests only.",
    )
    parser.addoption(
        "--python_only",
        action="store_true",
        default=False,
        help="Run Python tests only.",
    )


def pytest_collection_modifyitems(config, items):
    if config.getoption("--clrs_only"):
        skip_nonclrs = pytest.mark.skip(
            reason="Skipping when --clrs_only option given."
        )
        for item in items:
            if "clrs_only" not in item.keywords:
                item.add_marker(skip_nonclrs)
    else:
        skip_clrs = pytest.mark.skip(reason="Need --clrs_only option to run.")
        for item in items:
            if "clrs_only" in item.keywords:
                item.add_marker(skip_clrs)
    if config.getoption("--g4g_only"):
        skip_nong4g = pytest.mark.skip(reason="Skipping when --g4g_only option given.")
        for item in items:
            if "g4g_only" not in item.keywords:
                item.add_marker(skip_nong4g)
    else:
        skip_g4g = pytest.mark.skip(reason="Need --g4g_only option to run.")
        for item in items:
            if "g4g_only" in item.keywords:
                item.add_marker(skip_g4g)
    if config.getoption("--leet_only"):
        skip_nonleet = pytest.mark.skip(
            reason="Skipping when --leet_only option given."
        )
        for item in items:
            if "leet_only" not in item.keywords:
                item.add_marker(skip_nonleet)
    else:
        skip_leet = pytest.mark.skip(reason="Need --leet_only option to run.")
        for item in items:
            if "leet_only" in item.keywords:
                item.add_marker(skip_leet)
    if config.getoption("--python_only"):
        skip_nonpython = pytest.mark.skip(
            reason="Skipping when --python_only option given."
        )
        for item in items:
            if "python_only" not in item.keywords:
                item.add_marker(skip_nonpython)
    else:
        skip_python = pytest.mark.skip(reason="Need --python_only option to run.")
        for item in items:
            if "python_only" in item.keywords:
                item.add_marker(skip_python)
