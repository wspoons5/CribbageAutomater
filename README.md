# Purpose
This repository contains code in Python 2 that takes a cribbage hand in a two player game of cribbage (i.e six card hands) and returns which four cards from the hand to keep in order to maximize the expected score of that hand. 

# Explanation
Given the six card input hand, there are fifteen possible four card hands that can be created by dropping two cards. For each of these hands, there are fourty possible flip cards remaining in the deck because both you and your opponent were dealt six cards. However, for the purpose of computing the expected score of each hand, we will ignore the six cards dealt to the opponent making fourty-six possible flip cards. Ignoring the opponent's six cards does not compromise our calculation of the expected hand value because we have no information about which cards the opponent was dealt. We could remove them, but it adds an unnecessary computational layer.

For each of the fifteen possible four card hands we iterate through all possible flip cards and calculate the score of the hand formed by the four cards plus the flip cards. The probability of obtaining this hand is the probability of obtaining that particular flip card. For this application, we ignore card suit. Therefore, the probability of a particular flip card being obtained is *c*/46 where *c* is the number of that card type remaining in the deck. Formally, the expected score of a hand is:

![alt text][summation]

[summation]: https://github.com/wspoons5/CribbageAutomater/blob/master/summation1.png

where ![alt text](https://github.com/wspoons5/CribbageAutomater/blob/master/sh.png) is the score of the hand formed by the four cards kept and the one flip card, ![alt text](https://github.com/wspoons5/CribbageAutomater/blob/master/esh.png), is the expected value of ![alt text](https://github.com/wspoons5/CribbageAutomater/blob/master/sh.png), ![alt text](https://github.com/wspoons5/CribbageAutomater/blob/master/k.png) is the set of possible flip cards, ![alt text](https://github.com/wspoons5/CribbageAutomater/blob/master/ki.png) is an element of ![alt text](https://github.com/wspoons5/CribbageAutomater/blob/master/k.png), and ![alt text](https://github.com/wspoons5/CribbageAutomater/blob/master/pki.png) is the probability of obtaining ![alt text](https://github.com/wspoons5/CribbageAutomater/blob/master/ki.png). 

The program then returns the hand which maximizes ![alt text](https://github.com/wspoons5/CribbageAutomater/blob/master/esh.png).

# Future Work
**Include crib score in optimization:** Currently, the opponent's hand is not factored into our determination of what the optimal hand is. We effectively treat the two dropped cards as simply being discarded. However, in reality these two cards would be put into the crib. If it is our crib, we not only want to maximize the score of our hand, but we also want to maximize the score of our crib *i.e*, we want to maximize the summed scores of our hand and our crib. If it is our opponent's crib, we want to minimize the score of their crib while maximizing the score of our hand *i.e*, we want to maximize the absolute difference of the score of our hand and the score of our opponent's crib.

**Support three player games:** The current version only supports hand optimization for a two player game. Adding support for a three player game would be useful.  

**Include decision structure for the play:** We currently only have support for determining what the optimal move for a hand is. However, scoring in cribbage goes beyond the hand score. Game changing points can be awarded during the play (the period before hand scores are determined). Including a decision structure to automatically play cards during the play would effectively create a complete cribbage AI.

**Include card suit to include nobs:** We currently do not take card suit into account when determining scoring and which cards to keep/drop. For the most part, this is a minor exclusion. The only effect card suit has on scoring is by adding one point through nobs (having a jack of the same suit as the flip card). However, this would be a nice addition for future versions.   
