from search.local_search import HillClimbing, SimulatedAnnealing, Genetic
from exercises.cross_word.local_search.problem import CrossWord
from exercises.cross_word.input.words import words

# vocabolario
vocabulary = words
# lunghezza delle parole nel puzzle
word_lengths = [6, 7, 9]

# word1 si incrocia con word2 nelle rispettive posizioni 4, 1
word1 = 0
pos1 = 4
word2 = 1
pos2 = 1

same_letter1 = (word1, word2, pos1, pos2)

# word2 si incrocia con word3 nelle rispettive posizioni 5, 1
pos2 = 5
word3 = 2
pos3 = 1

same_letter2 = (word2, word3, pos2, pos3)

same_letters = (same_letter1, same_letter2)

problem = CrossWord(word_lengths=word_lengths, same_letters=same_letters, vocabulary=vocabulary)

print()
# search algorithm
# search = HillClimbing(problem=problem)
#search = SimulatedAnnealing(problem=problem, max_time=1000, lam=0.01)
search = Genetic(problem=problem, population=25, generations=50, p_mutation=0.1, gene_pool=list(range(8)))

# run algorithm
result, state = search.run()

# display the exercises
print(result)
print(problem.value(state))
print(state)
