# Assignment - Roberto Pastor Muela

This is a coding test resolution provided by
[Roberto Pastor Muela](https://www.linkedin.com/robertopastormuela)
for Telefónica.

## Code Test - Toucan Tournament

### **Task**

Toucan Tournament is a tournament where several players compete in
several sports.

**Facts**
- Right now, the sports played are basketball and handball matches.
  They plan to add more sports in the future.
- You have been contacted to create a program to calculate the Most
  Valuable Player (MVP) of the tournament.
- You will receive a set of files, each one containing the stats of one
  match. Each file will start with a row indicating the sport it refers to.
- Each player is assigned a unique nickname.
- Each file represent a single match.
- The MVP is the player with the most rating points, adding the rating points in all matches.
- A player will receive 10 additional rating points if their team won the match.
- Every match must have a winner team. One player may play in different teams and
  positions in different matches, but not in the same match.
- The program responsible of generating the files has a bug, that can
  be reflected in wrong files format. If one file is wrong, the whole set of files
  is considered to be wrong and the MVP won't be calculated.

## Thoughts

From the previous condition, it is clear that the main target of the tournament is
selecting which is the MVP. Also, players are allowed to participate in different
teams and different matches in fact, meaning that teams and matches are not good
elections for unique identifiers. Players must be the unique identifiers of the
software code implemented.

Since the language of choice is Python, and there is no need to implement databases
(i.e. simple processing script) the most ideal solution might be the usage of a
dictionary in which the keys are the player's nicknames (i.e. unique identifiers).

## Missing tasks

- [ ] Finish up main README
- [ ] More robust regex pattern
- [ ] Send over practical resolution
