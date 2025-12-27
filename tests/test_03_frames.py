import pytest
from pal import project_03_frames


def setup_function():
    project_03_frames.snapshots.clear()


def test_factorial_math():
    assert project_03_frames.factorial(5) == 120


def test_stack_depth_tracking():

    project_03_frames.factorial(5)

    assert len(project_03_frames.snapshots) == 6

    depths = [s['depth'] for s in project_03_frames.snapshots]
    assert len(set(depths)) == 6


def test_frame_isolation():
    project_03_frames.factorial(5)

    n_values = []
    for snap in project_03_frames.snapshots:
        n_values.append(snap['locals']['n'])

    expected = {0, 1, 2, 3, 4, 5}
    assert set(n_values) == expected
