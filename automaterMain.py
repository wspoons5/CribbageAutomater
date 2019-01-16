from __future__ import division
from collections import Counter

def main():
	hand = SixCardHand(["A", "6", "7", "J", "2", "7"])
	hand.displayMoves()

'''
This class represents a hand of cards from a standard deck of 52 with user specified size and cards
Args:
	cardSize: Is an int that represents the number of cards in the hand
	cards: Is a list of strings representing the cards to be put into the hand
	Note: The class could have initialized cardSize as the length of the list, cards. However, cardSize was
	      deliberately included as an argument as an additional safeguard against the user including an 
	      unintended number of cards
Fields:
	cardSize: Is an int that represents the number of cards in the hand
	cards: Is a list of strings representing the cards in the hand
	cardOrderMap: Is a dictionary that maps a string representation of a card to its numerical order
	cardValueMap: Is a dictionary that maps a string representation of a card to its numerical value
'''
class Hand:
	def __init__(self, cardSize, cards):
		self.cardSize = cardSize
		self.cards = cards[:]
		
		self.cardOrderMap = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
		                     "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}
		self.cardValueMap = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
		                     "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
		self.raiseErrors()
		self.makeUpper() ## Makes user input uppercase to make compatible with cardOrderMap and cardValueMap
		self.cards = sorted(self.cards, key=lambda card: self.cardOrderMap[card]) ## Sorts cards by numerical order

	'''
	This method changes all of the strings in the class field "cards" to uppercase
	'''
	def makeUpper(self):
		for i in range(self.cardSize):
			self.cards[i] = self.cards[i].upper()

	'''
	This method checks user input to the constructor and raises ValueErrors for common input mistakes
	'''	
	def raiseErrors(self):
		if self.cardSize != len(self.cards):
			raise ValueError("ERROR: The card size does not equal the number of cards.")

		validCards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

		for card in self.cards:
			if isinstance(card, str):
				if card.upper() not in validCards:
					raise ValueError("ERROR: One or more of the passed cards is not a valid card type.")
			else:
				raise ValueError("ERROR: One or more of the passed cards is not a string.")
'''
This class inherits the parent "Hand" class and represents cribbage hand of six cards. It's function is to
list all possible moves from a six card hand and to rank each move by its expected score.
Args:
	cards: A list of strings representing the cards in the hand.
Fields:
	moveList: A list of FourCardHands where each represents a possible move from this six card hand.  
'''
class SixCardHand(Hand):
	def __init__(self, cards):
		Hand.__init__(self, 6, cards)
		self.moveList = self.makeMoveList()

	'''
	This method takes all possible combinations of four cards from the six total cards in this hand and
	returns a list of instances of the class FourCardHand constructed with each combination of four cards
	'''
	def makeMoveList(self):
		indexList = [[0,1,2,3], [0,1,2,4], [0,1,2,5], [0,1,3,4], [0,1,3,5],
		             [0,1,4,5], [0,2,3,4], [0,2,3,5], [0,2,4,5], [0,3,4,5],
		             [1,2,3,4], [1,2,3,5], [1,2,4,5], [1,3,4,5], [2,3,4,5]]
		moveList = []
		for item in indexList:
			keptCards = []
			droppedCards = []
			for i in range(self.cardSize):
				if i in item:
					keptCards.append(self.cards[i])
				else:
					droppedCards.append(self.cards[i])
			moveList.append(FourCardHand(keptCards, droppedCards))
		
		moveList = sorted(moveList, key=lambda move: move.expectedValue, reverse=True)

		return moveList
	'''
	This method prints each move and its expected value to the console
	'''
	def displayMoves(self):
		for move in self.moveList:
			print("Drop {} and keep {} to score {} on average.".format(move.droppedCards, 
				                                                       move.cards, move.expectedValue))

'''
This class represents a four card hand in cribbage after two cards from the initial six card hand
have been dropped.
Args:
	privateCards: Is an array of strings representing the four cards kept from the initial hand
	droppedCards: Is an array of strings representing the two cards dropped from the initial hand
Fields:
	remainingCards: Is an array of strings representing the remaining cards in the deck
	possibleFlipCards: Is a set representing all unique cards left in the deck
	cardDist: Is a map with string int pairs where each key is a unique card left in the deck
	          and each value is the number of them left in the deck
	deckSize: Is an int representing the total number of remaining cards in the deck
	expectedValue: Is a float representing the expected score of this move given the cards
	               remaining in the deck 

'''
class FourCardHand(Hand):
	def __init__(self, privateCards, droppedCards):
		Hand.__init__(self, 4, privateCards)
		self.droppedCards = droppedCards[:]
		self.remainingCards = self.getRemainingCards()
		self.possibleFlipCards = set(self.remainingCards)
		self.cardDist = Counter(self.remainingCards)
		self.deckSize = len(self.remainingCards)
		self.expectedValue = self.getExpectedValue()

	'''
	This method calculates the expeced value of this four card hand given the remaining cards in the deck
	and returns it as a float
	'''
	def getExpectedValue(self):
		ev = 0
		for flipCard in self.possibleFlipCards:
			newHand = FiveCardHand(self.cards, flipCard)
			ev += newHand.score*self.cardDist[flipCard]/self.deckSize
		return ev

	'''
	This method makes and returns a list of strings representing a standard deck of 52 and then removes
	the cards in the four card hand from it and the cards that were dropped from it
	'''
	def getRemainingCards(self):
		deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4
		for card in self.cards:
			deck.remove(card)
		for card in self.droppedCards:
			deck.remove(card)
		return deck
'''
This method represents a five card hand formed by the four cards the player kept and the common flip card.
Its function is the calculate the score of this hand.
Args:
	privateCards: Is a list of strings representing the four cards kept from the initial six
	flipCard: Is a string representing the card flipped from the cards remaining in the deck
Fields:
	score: Is an int representing the total score of this hand
'''
class FiveCardHand(Hand):
	def __init__(self, privateCards, flipCard):
		Hand.__init__(self, 4, privateCards) 
		self.cards = self.cards + [flipCard]
		self.cardSize = 5
		self.score = self.scoreDoubles() + self.scoreFifteens() + self.scoreRuns()

	'''
	This method caluculates the total number of points scored from doubles, triples, and quadruples
	and returns it as an int
	'''
	def scoreDoubles(self):
		score = 0
		cardCountMap = Counter(self.cards)
		for card in cardCountMap.keys():
			if cardCountMap[card] == 2:
				score += 2
			elif cardCountMap[card] == 3:
				score += 6
			elif cardCountMap[card] == 4:
				score += 12
		return score

	'''
	This method calculates the total number of points scored from combinations of cards that sum to 
	fifteen and returns it as an int
	'''
	def scoreFifteens(self):
		score = 0
		idxMap = [[0,1], [0,2], [0,3], [0,4], [1,2], [1,3], [1,4], [2,3], [2,4], [3,4],
		          [0,1,2], [0,1,3], [0,1,4], [0,2,3], [0,2,4], [0,3,4], [1,2,3], [1,2,4], [1,3,4], [2,3,4],
		          [0,1,2,3], [0,1,2,4], [0,1,3,4], [0,2,3,4], [1,2,3,4],
		          [0,1,2,3,4]]

		for idxSet in idxMap:
			sum = 0
			for idx in idxSet:
				sum += self.cardValueMap[self.cards[idx]]
			if sum == 15:
				score += 2
		return score

	'''
	This method calculates the total number of points scored from runs and returns it as an int
	'''
	def scoreRuns(self):
		cardsInRun = set()
		curRunSize = 1
		for i in range(self.cardSize - 1):
			if self.cardValueMap[self.cards[i + 1]] - self.cardValueMap[self.cards[i]] == 1:
				curRunSize += 1
				cardsInRun.add(self.cards[i])
				cardsInRun.add(self.cards[i + 1])
			else:
				if curRunSize < 3:
					curRunSize = 0
					cardsInRun.clear()
				else:
					break

		maxRunLength = len(cardsInRun)
		cardCountMap = Counter(self.cards)
		if maxRunLength >= 3:
			duplicates = 0
			for card in cardsInRun:
				count = cardCountMap[card]
				if count > 1:
					duplicates += count

			if duplicates != 0:
				return maxRunLength*duplicates
			else:
				return maxRunLength
		else:
			return 0

main()