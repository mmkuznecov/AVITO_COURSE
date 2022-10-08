If you just want to run tests and see results, run:

```python3 -m unittest -v wiyn_tests.py```

If you want to log the results to file, run:

```python3 -m unittest -v wiyn_tests.py 2>&1 | tee result.txt```

To check the code coverage, run:

```coverage run -m unittest wiyn_tests.py```

To see the html report, run:

```coverage html```

Then open the file `htmlcov/index.html` in your browser.