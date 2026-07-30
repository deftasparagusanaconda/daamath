# voting

i created this elaborate system for fun but i wont use it. if we need a new leader for daamath, the dictator should just appoint who she/he wants. that saves time and effort and is most credible and accepted. but if you want to read anyway, read away!

# introduction

if this project ever needs to transfer dictatorship to another, the following voting system should be used:

a voter is someone who casts a vote. they are identified based on their github account's numeric ID. if the github account was created after the voting period was opened, it may not vote. this is to prevent gaming.

a candidate is someone who runs for leadership. only people who have contributed to daamath may become candidates, but this does not guarantee that the dictator has allowed them on the roster. the system shows all candidates that applied though, showing clearly who the dictator has blacklisted. candidates are identified based on their github account's numeric ID.

a vote is a tuple of (familiarity, endorsement). a voter can submit or retract a vote for each candidate.

# the process

the dictator opens a voting period, during which anyone can visit the [voting] page (hosted on the documentation website). here, they prove their identity on github. if they are a valid voter, the page then presents them with the roster. then they score each candidate on how well they know them and how strongly they like/dislike them.

familiarity is measured as an integer in \[0, 3\]:

| familiarity | meaning |
| - | - |
| 0 | never heard of them. i dont know what they do. |
| 1 | aware of them. ive seen their name float around. |
| 2 | familiar with them. i have seen their work. |
| 3 | well-acquainted with them. i have direct experience with their work. |

endorsement is measured as an integer in \[-3, 3\]:

| endorsement | meaning |
| - | - |
| -3 | i strongly oppose them. theyre the ideal anticandidate |
| -2 | i oppose them. they would make a bad leader |
| -1 | i mildly oppose them. theyre unacceptable |
|  0 | i have no opinion |
| +1 | i mildly endorse them. theyre acceptable |
| +2 | i endorse them. they would be a good leader |
| +3 | i strongly endorse them. theyre the ideal candidate |

during the voting period, voters can update or retract their votes freely, and candidates can request the dictator to change their appearance/disappearance on the roster. 

after the voting period, ballots are closed and the roster is frozen. the system takes a sum of weighted endorsements (calculated as familiarity * endorsement) for each candidate. results are verified by whoever the dictator wants. the candidate with the greatest total is nominated. finally, the dictator officially hands over ownership to the nominee.

# python program

as a python program, the process goes roughly as follows:

```python
from dataclasses import dataclass
from collections import defaultdict

@dataclass(frozen = True)
class Vote:
    voter_identity: int
    candidate_identity: int
    familiarity: int
    endorsement: int

votes: set[Vote] = set()

# candidates[candidate_identity] = weighted_endorsement
candidates: defaultdict[int, int] = defaultdict(int)

for vote in votes:
    candidates[vote.candidate_identity] += vote.familiarity * vote.endorsement

winner = max(candidates.keys(), key = lambda candidate: candidates[candidate])

print('winner is', winner)
```

# notes

- the dictator is recommended to participate too, in case a new roster is bad/stagnant, and the voters want the old dictator to continue their reign.
- candidates may cast their own vote too.
- individuals' votes shall not be publicized. 
- candidates' results shall be publicized as a table:

| candidate | ∑ familiarity | ∑ endorsement | ∑ weighted endorsement |
| - | - | - | - |
| bob | 2 | 4 | 5 |
| ann | 3 | 3 | 8 |
| … | … | … | … |

(the system can show additional statistics such as how good the roster was, if it wants to)

# rant

- this system is closer to a survey than an election
- since scores are not normalized, we can see how good/competitive or bad/stagnant the roster is. if a roster is particularly bad, we may want to extend the current dictator's reign. 

a dictator running a democracy... heh

[voting]: https://deftasparagusanaconda.github.io/daamath/vote
