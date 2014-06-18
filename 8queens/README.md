A backtracking solution to the (8 queens puzzle)[http://en.wikipedia.org/wiki/Eight_queens_puzzle].

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