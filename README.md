# Digital Tech IQ security practice lab

Proposed public training source for Lessons 35 and 36. This is deliberately
flawed practice code, not a service to deploy. All lesson rows are invented;
SQLite exists only in memory. Tests use Flask's in-process client, with no
server, cloud deployment, real database, or live credentials.

Lesson 35 will demonstrate an actual blocked commit using the inactive fixture
provided by GitHub Skills. The baseline retains its disabling marker. After
observing the block, discard the attempted token insertion and use an environment
variable reference; do not bypass protection. A blocked attempt and a historical
secret-scanning alert are different evidence, and we will label them accurately.

Lesson 36 will enable GitHub CodeQL, inspect an actual SQL-injection finding,
reproduce the flaw with the regression test, change interpolation to a bound
parameter, and verify passing tests and the hosted finding's resolved state.
The security regression intentionally fails on this baseline. Hosted findings
have not yet been generated or verified.

Run locally in a disposable virtual environment:

```text
python -m pip install -r requirements.txt
python -m unittest -v
```

The inactive fixture is reused under the bundled GitHub Skills MIT license.
See `PROVENANCE.json` for its exact source revision. Teaching prose, sample
application, and tests are original. No course videos or private course data
are included in this repository candidate.
