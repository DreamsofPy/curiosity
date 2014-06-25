8 Queens Puzzle
===============

A backtracking solution to the [8 queens puzzle](http://en.wikipedia.org/wiki/Eight_queens_puzzle). The goal is to place 8 queens on an 8x8 chess board so that no two queens are attacking each other.

Returns the first solution it finds showing each attempt at a solution along the way. This could easily be extended to find and return all solutions for a given board size.

Sample output for `n=4`,

    no conflict
    Q---
    ----
    ----
    ----

    |
    Q---
    Q---
    ----
    ----

    \
    Q---
    -Q--
    ----
    ----

    no conflict
    Q---
    --Q-
    ----
    ----

    |
    Q---
    --Q-
    Q---
    ----

    \
    Q---
    --Q-
    -Q--
    ----

    |
    Q---
    --Q-
    --Q-
    ----

    \
    Q---
    --Q-
    ---Q
    ----

    backtrack
    Q---
    --Q-
    ----
    ----

    no conflict
    Q---
    ---Q
    ----
    ----

    |
    Q---
    ---Q
    Q---
    ----

    no conflict
    Q---
    ---Q
    -Q--
    ----

    |
    Q---
    ---Q
    -Q--
    Q---

    |
    Q---
    ---Q
    -Q--
    -Q--

    \
    Q---
    ---Q
    -Q--
    --Q-

    |
    Q---
    ---Q
    -Q--
    ---Q

    backtrack
    Q---
    ---Q
    -Q--
    ----

    \
    Q---
    ---Q
    --Q-
    ----

    |
    Q---
    ---Q
    ---Q
    ----

    backtrack
    Q---
    ---Q
    ----
    ----

    backtrack
    Q---
    ----
    ----
    ----

    no conflict
    -Q--
    ----
    ----
    ----

    \
    -Q--
    Q---
    ----
    ----

    |
    -Q--
    -Q--
    ----
    ----

    \
    -Q--
    --Q-
    ----
    ----

    no conflict
    -Q--
    ---Q
    ----
    ----

    no conflict
    -Q--
    ---Q
    Q---
    ----

    |
    -Q--
    ---Q
    Q---
    Q---

    |
    -Q--
    ---Q
    Q---
    -Q--

    no conflict
    -Q--
    ---Q
    Q---
    --Q-