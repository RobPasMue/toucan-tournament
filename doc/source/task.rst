Task
####

The following statement was provided as a technical practical.

Context - Toucan Tournament MVP calculator
==========================================

Toucan Tournament is a tournament where several players compete in several sports.
Right now, the sports played are basketball and handball matches. They plan to add more sports in the future.

You have been contacted to create a program to calculate the Most Valuable Player
(MVP) of the tournament.

You will receive a set of files, each one containing the stats of one match.
Each file will start with a row indicating the sport it refers to.

Each player is assigned a unique nickname.

Each file represent a single match.

The MVP is the player with the most rating points, adding the rating points in all matches.

A player will receive 10 additional rating points if their team won the match. Every match must have
a winner team. One player may play in different teams and positions in different matches,
but not in the same match.

The program responsible of generating the files has a bug, that can be reflected in wrong files
format. If one file is wrong, the whole set of files is considered to be wrong and the
MVP won't be calculated.

Basketball
^^^^^^^^^^

Each row will represent one player stats, with the format::

   player name;nickname;number;team name;position;scored points;rebounds;assists

This table details the rating points each player in a basketball match receives
depending on his position:

+--------------+---------------+----------+--------+
|              | Scored point  | Rebound  | Assist |
+==============+===============+==========+========+
| Guard (G)    | 2             | 3        | 1      |
+--------------+---------------+----------+--------+
| Forward (F)  | 2             | 2        | 2      |
+--------------+---------------+----------+--------+
| Center (C)   | 2             | 1        | 3      |
+--------------+---------------+----------+--------+

E.g. a player playing as center with 10 scored points, 5 rebounds and no assists will be
granted 25 rating points (10*2 + 5*1 + 0*3 ).

The winner team is the one with more scored points.

An example is shown here::

   BASKETBALL
   player 1;nick1;4;Team A;G;10;2;7
   player 2;nick2;8;Team A;F;0;10;0
   player 3;nick3;15;Team A;C;15;10;4
   player 4;nick4;16;Team B;G;20;0;0
   player 5;nick5;23;Team B;F;4;7;7
   player 6;nick6;42;Team B;C;8;10;0

Handball
^^^^^^^^

Each row will represent one player stats, with the format::

   player name;nickname;number;team name;position;goals made;goals received

This table details the rating points each player in a handball match receives
depending on his position:

+-------------------+-----------------------+-----------+---------------+
|                   | Initial rating points | Goal made | Goal received |
+===================+=======================+===========+===============+
| Goalkeeper (G)    | 50                    | 5         | -2            |
+-------------------+-----------------------+-----------+---------------+
| Field player (F)  | 20                    | 1         | -1            |
+-------------------+-----------------------+-----------+---------------+

E.g. a player playing as goalkeeper with 1 goals made and 10 received will be
granted 35 rating points (50 + 1*5 - 10*2 = 35).

The winner team is the one with more goals made.

An example is shown here::

   HANDBALL
   player 1;nick1;4;Team A;G;0;20
   player 2;nick2;8;Team A;F;15;20
   player 3;nick3;15;Team A;F;10;20
   player 4;nick4;16;Team B;G;1;25
   player 5;nick5;23;Team B;F;12;25
   player 6;nick6;42;Team B;F;8;25


What we look at
===============

You have 4 hours to complete the test and you can use any programming language you want.

No UI or database access code is needed. It is not mandatory to read input
from file system. It is acceptable to read from stdin, forms or any other source.

This task is designed to give us an idea of how you think when faced with a very
limited amount of time to solve a task of significant complexity.

We are interested in how you structure your code so that it's easily extendable,
complies with best practices for the language used, and is easy to modify /understand by others.

We are also interested in seeing how efficient the algorithm you implement is.
