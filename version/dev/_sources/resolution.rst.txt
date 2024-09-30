Resolution
##########

Initial thoughts
================

From the previous task, it is clear that the main target of the tournament is
selecting which is the MVP. Also, players are allowed to participate in different
teams and different matches in fact, meaning that teams and matches are not good
elections for unique identifiers. Players must be the unique identifiers of the
software code implemented.

Since the language of choice is Python, and there is no need to implement databases
(i.e. simple processing script) the most ideal solution might be the usage of a
dictionary in which the keys are the player's nicknames (i.e. unique identifiers).

However, another important aspect to was its extensibility and reusability. The
easy integration of new disciplines is an important design point in the library's
architecture.

Also, since we are developing a library, one of the most important points are
a proper error handling, test suite and API documentation, in order to facilitate
the job to new developers that may come in and improve or extend the source code.

Architecture
============

The Python package is structured as shown in the :ref:`API reference <ref_api_reference>`
section. The package is structured following the rule of "separation of concerns",
such that each module is in charge of dealing with their related contributions.

For example, all player related computations are performed in the
``toucan.mvp.calculator.player`` module, were as the details for each discipline
and the retrieval of data from them is located at ``toucan.mvp.calculator.discipline``.
An additional ``toucan.mvp.calculator.errors`` module was created to provide an
ad-hoc error handling, and thus creating our own ``Exception`` type.

Finally, the main module in terms of end-user purpose is the
``toucan.mvp.calculator.tournament`` module, which provides an easy interface for
tournament organizers to provide the path to their data and extract the
MVP without having to do many efforts.

Testing
=======

Following best practices, software libraries should be tested as much as possible to
ensure their robustness. Though, at the moment, this library has a ``~100%`` line coverage,
it is true that the branch coverage can always be improved. However, due to the limited
amount of time available for this task, this is good enough. An explanation on how
to run the test suite can be found in the landing page of this documentation.

Documentation
=============

As important as it is to deliver software, it is equally important to deliver its documentation.
An advanced developer would look first for library documentation before even
trying to debug on its own why a weird error has just occurred. Documentation also
is critical in terms of usability, since if the code is not documented, it will be difficult
for external contributors to actually provide some value to your library.

For this reason, I decided to use standard Python tools for generating documentation,
such as Sphinx. Together with the PyData Sphinx Theme and Sphinx's autoapi plugin,
generating documentation from properly documented code (with docstrings) becomes an easy task.
