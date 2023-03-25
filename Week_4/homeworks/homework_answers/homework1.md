# PhytonSeleniumCamp
Share the notes you created by researching the decorators in PyTest on github as a "ReadMe" file.


@pytest.fixture
A test function can use a fixture by mentioning the fixture name as an input parameter.
A fixture function is created that provides input to the tests. To access the fixture function, the tests must specify the fixture name as an input parameter.

@pytest.mark.skipif() Used to conditionally skip tests

Skipping tests using @pytest.mark.skip

We can parameterize the tests using @pytest.mark.parametrize

@pytest.mark.xfail is used when we expect the test to fail

@pytest.mark.timeout() Used for test timeout management