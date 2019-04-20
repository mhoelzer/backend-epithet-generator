# Epithet Generator

Create a Flask API to serve random epithets from the [Shakespeare Insult Kit](http://www.pangloss.com/seidel/shake_rule.html).
Each sprint is an assignment with its own deliverables. Please create a pull request to the appropriate branch to submit
assignments.

## Instructions

Sprint|Description
---|---
[a](https://github.com/KenzieAcademy/backend-epithet-generator/blob/master/instructions/sprint_a.md)| Minimal Flask Applications
[b](https://github.com/KenzieAcademy/backend-epithet-generator/blob/sprint-b/instructions/sprint_b.md) | Unit Testing
[c](https://github.com/KenzieAcademy/backend-epithet-generator/blob/sprint-c/instructions/sprint_c.md) | Integration Testing

---

## Sprint A

This is getting things set up; there won't be a whole lot to display.

### Rubric
1. Repository contains `.gitignore` file containing the requested sections of GitHub's default Python `.gitignore` file.
2. Repository does not contain virtualenv and other artifacts ignored in GitHub's default Python `.gitignore` file.
3. Commit messages contain sufficient information to understand why changes were made.
4. Both `Pipfile` and `Pipfile.lock` are committed.
5. `__init__.py` should be empty, `app.py` contains the app instance and routes for home and vocabulary, and and `helpers.py` and `test_helpers.py` are empty files.
6. Development server successfully starts and serves defined routes with stubbed payloads.

---

## Sprint B

This is going to be using unit tests to test stuff that need to be tested with testing.

### Rubric
1. Unit test coverage. At least one happy & sad path test exists for each method of helper classes.
2. Endpoints serve expected payloads.
    - "/" route serves single epithet.
    - "/vocabulary" route serves vocabulary dataset.
    - "/epithets/<quantity>" route serves number of epithets specified by quantity.
3. Application logic is decoupled from views. Views are limited to instantiating classes, initializing variables to be passed as parameters to helper classes, and returning JSON encoded payloads.
4. Version Control: Every commit contains sufficient detail to understand why changes were made. 
