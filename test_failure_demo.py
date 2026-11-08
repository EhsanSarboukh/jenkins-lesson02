def test_intentionally_broken():
    # Simulates a developer pushing a bug.
    assert 1 == 2, "This test is meant to fail — demonstrating pipeline behavior"
