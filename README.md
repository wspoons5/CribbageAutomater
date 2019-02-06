# Purpose
This repository contains code in Python 2 that takes a cribbage hand in a two player game of cribbage (i.e six card hands) and returns which four cards from the hand to keep in order to maximize the expected score of that hand. 

# Explanation
Given the six card input hand, there are fifteen possible four card hands that can be created by dropping two cards. For each of these hands, there are fourty possible flip cards remaining in the deck because both you and your opponent were dealt six cards. However, for the purpose of computing the expected score of each hand, we will ignore the six cards dealt to the opponent making fourty-six possible flip cards. Ignoring the opponent's six cards does not compromise our calculation of the expected hand value because we have no information about which cards the opponent was dealt. We could remove them, but it adds an unnecessary computational layer.

For each of the fifteen possible four card hands we iterate through all possible flip cards and calculate the score of the hand formed by the four cards plus the flip cards. The probability of obtaining this hand is the probability of obtaining that particular flip card. For this application, we ignore card suit. Therefore, the probability of a particular flip card being obtained is \frac{c}{46} where *c* is the number of that card type remaining in the deck. Formally, the expected score of a hand is:

![alt_text][summation]
[summation]: https://github.com/wspoons5/CribbageAutomater/blob/master/summation1.png

where *s(h)* is the score of the hand formed by the four cards kept and the one flip card, *E(s(h))*, is the expected value of *s(h)*, *k* is the set of possible flip cards, k_{i} is an element of *k*, and *p(k_{i})* is the probability of obtaining k_{i}. 

The program then returns the hand which maximize *E(s(h))*.

# Future Work
