Toucan tournament MVP calculator
================================

|made-with-python| |made-with-sphinx-doc| |black|

.. |made-with-python| image:: https://img.shields.io/badge/Source%20code%20with-Python-1f425f.svg
   :target: https://www.python.org/

.. |made-with-sphinx-doc| image:: https://img.shields.io/badge/Documentation%20with-Sphinx-1f425f.svg
   :target: https://www.sphinx-doc.org/

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat
   :target: https://github.com/psf/black

This is a coding test resolution provided by `Roberto Pastor Muela <https://www.linkedin.com/robertopastormuela>`_
for Telefónica. This technical practical has been approached by the creation of a Python library
named ``toucan-mvp-calculator``, which can easily be extended and reused for similar tournaments.

Simple example
--------------

The following example shows how to use the ``toucan-mvp-calculator`` to process
a directory in which the match files for the Toucan tournament have been stored:

.. code:: python

   import os

   from toucan.mvp.calculator import ToucanTournament

   # Provide the path to your files directory...
   # We will assume in this example that it is stored in an
   # environment variable called MY_TOUCAN_TOURNAMENT_FILES_DIRECTORY
   DATA_PATH = os.environ.get("MY_TOUCAN_TOURNAMENT_FILES_DIRECTORY")

   # Create the tournament
   tournament = ToucanTournament("ReferenceTournament")

   # Process the tournament files
   tournament.process_tournament(DATA_PATH)

   # Figure out who is the MVP!
   print("And the MVP is...\n")
   print(tournament.mvp)


How to install ``toucan-mvp-calculator``
----------------------------------------

1. Start by downloading the repository (in the following `ZIP link <>`_)
   and uncompress it at your desired location.

2. Create a fresh-clean Python environment and activate it:

    .. code:: bash

        # Create a virtual environment
        python -m venv .venv

        # Activate it in a POSIX system
        source .venv/bin/activate

        # Activate it in Windows CMD environment
        .venv\Scripts\activate.bat

        # Activate it in Windows Powershell
        .venv\Scripts\Activate.ps1

3. Make sure you have the latest required build system and tools:

    .. code:: bash

        python -m pip install -U pip flit tox

4. Install the project in editable mode from the root of the uncompressed directory:

    .. code:: bash
    
        python -m pip install --editable .

5. **EXTRA**: you can also install the test and documentation build
   requirements by running instead the following:

    .. code:: bash

        python -m pip install --editable .[tests,doc]

How to run the tests
--------------------

This project takes advantage of `pytest <https://docs.pytest.org/>`_. This tool allows to
automate the run of unit tests on Python. Also, other additional tools are used for ensuring
a proper code coverage (i.e. `pytest-cov <https://pytest-cov.readthedocs.io/en/latest/>`_).

If you want to run the tests, just do as follows:

.. code:: bash

    pip install -e .[tests]

    # Launch the test suite
    pytest


Currently, the status of the code coverage is as follows::

  ---------- coverage: platform win32, python 3.10.4-final-0 ------------
  Name                                      Stmts   Miss  Cover   Missing
  -----------------------------------------------------------------------
  src\toucan\mvp\calculator\__init__.py         5      0   100%
  src\toucan\mvp\calculator\discipline.py      19      0   100%
  src\toucan\mvp\calculator\errors.py           3      0   100%
  src\toucan\mvp\calculator\players.py         49      0   100%
  src\toucan\mvp\calculator\tournament.py      62      0   100%
  -----------------------------------------------------------------------
  TOTAL                                       138      0   100%


Building documentation
----------------------

To build the documentation locally you need to follow these steps at the root
directory of the repository:

.. code:: bash

    pip install -e .[doc]

    # Navigate to the documentation directory
    cd doc

    # On Linux, run
    make html

    # On Windows, run
    .\\make.bat html

After the build completes the HTML documentation locates itself in the
``_builds/html`` directory and you can load the ``index.html`` into a web
browser. To clean the documentation you can execute this command:

.. code:: bash

    # On Linux, run
    make clean

    # On Windows, run
    .\\make.bat clean


Code style
----------

Code style checks use `pre-commit <https://pre-commit.com/>`_. Install this tool and
activate it executing the following commands:

.. code::

   python -m pip install pre-commit
   pre-commit install

Then, you can make used of the available configuration file ``.pre-commit-config.yml``,
which will be automatically detected by pre-commit:

.. code::

   pre-commit run --all-files --show-diff-on-failure

Its current status is as follows::

  black....................................................................Passed
  isort....................................................................Passed
  flake8...................................................................Passed
  codespell................................................................Passed
  pydocstyle...............................................................Passed

.. ## Code Test - Toucan Tournament

.. ### **Task**

.. Toucan Tournament is a tournament where several players compete in
.. several sports.

.. **Facts**
.. - Right now, the sports played are basketball and handball matches.
..   They plan to add more sports in the future.
.. - You have been contacted to create a program to calculate the Most
..   Valuable Player (MVP) of the tournament.
.. - You will receive a set of files, each one containing the stats of one
..   match. Each file will start with a row indicating the sport it refers to.
.. - Each player is assigned a unique nickname.
.. - Each file represent a single match.
.. - The MVP is the player with the most rating points, adding the rating points in all matches.
.. - A player will receive 10 additional rating points if their team won the match.
.. - Every match must have a winner team. One player may play in different teams and
..   positions in different matches, but not in the same match.
.. - The program responsible of generating the files has a bug, that can
..   be reflected in wrong files format. If one file is wrong, the whole set of files
..   is considered to be wrong and the MVP won't be calculated.

.. ## Thoughts

.. From the previous condition, it is clear that the main target of the tournament is
.. selecting which is the MVP. Also, players are allowed to participate in different
.. teams and different matches in fact, meaning that teams and matches are not good
.. elections for unique identifiers. Players must be the unique identifiers of the
.. software code implemented.

.. Since the language of choice is Python, and there is no need to implement databases
.. (i.e. simple processing script) the most ideal solution might be the usage of a
.. dictionary in which the keys are the player's nicknames (i.e. unique identifiers).

.. ## Missing tasks

.. - [ ] Finish up main README
.. - [ ] More robust regex pattern
.. - [ ] Send over practical resolution
