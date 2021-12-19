# Repository Library
from clrs.advanced_design_and_analysis_techniques.greedy_algorithms.job_scheduling import (  # noqa: E501
    js_bu,
)


def test_job_scheduling_bu():
    d = [4, 2, 4, 3, 1, 4, 6]
    w = [70, 60, 50, 40, 30, 20, 10]
    assert js_bu(d, w, 3) == ["2", "1", "0"]
    assert js_bu(d, w) == ["3", "1", "2", "0", "-1", "6", "-1"]
