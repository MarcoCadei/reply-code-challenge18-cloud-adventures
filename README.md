# Reply code challenge18 - Cloud adventures
My solution to the reply coding challenge of 2018 - [Cloud adventures](https://challenges.reply.com/tamtamy/challenge/5/detail)  
I used Python 3 to solve the problem and numpy to help me with some vector calculus.

## My scores
* **7619**
* **1047367308**
* **252065419**
* **28624268**

![Scores](/score.png)

### 8th place! (out of 1207 teams)
I tried to simulate the challenge, so i gave myself just 4 hours of time: if i had partecipated i would have arrived 8th.  
I'm quite happy of this result, but as a side effect the code is ugly. It should be refactored in order to be more comprehensible.
In particular the choice of using tuples makes the code hard to read.  
A more elegant solution would be to use [named lists](https://pypi.org/project/namedlist/).

## The idea
The idea i used is pretty basic: from the example in the description of the problem i noticed that the score of the considered project dropped when considering the SLA Penalty.  
Therefore i ordered the projects in descending order of base penalty and bought the packages for each project in this order. In order to avoid to allocate too much packages to a single project i set a limit based on the total quantity of resources at disposal.  
The idea is super easy and in fact  the solution is just 106 lines long, where most of them are for the ```read``` and ```write``` functions.
