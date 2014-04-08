#!/usr/bin/python
#
# A magic square is a an n x n array of numbers consist of the
# integers 1, 2, ..., n^2 arranged so that the sum of the numbers in
# every row, column and main diagonals is the same. For example, in a
# 4 x 4 square the numbers are 1, 2, ..., 16 and could be arranged
# thusly to create the sum 34:
#
# 16  3  2 13
#  5 10 11  8
#  9  6  7 12
#  4 15 14  1
#
# For the first part, write a program that can produce magic squares
# with values of n from 4 to, say, 28 (inclusively).
#

import genetic, math, random, sys

class MagicSquare(genetic.Individual):
    order = None
    genetic.Individual.seperator = ','

    def __init__(self, chromosome=None):
        genetic.Individual.__init__(self, chromosome)
        self.magicSum = self.order * (self.order * self.order + 1) / 2
        self.valueWidth = int(math.ceil(math.log10(self.magicSum)))
        self.valueFormat = "%" + str(self.valueWidth) + "i"

    def _makechromosome(self):
        chromosome = list(self.alleles)
        random.shuffle(chromosome)
        return chromosome

    def evaluate1(self, optimum = None):
        self.score = 0
        for rowNum in range(self.order):
            self.score += abs(self.rowSum(rowNum) - self.magicSum)
        for colNum in range(self.order):
            self.score += abs(self.colSum(colNum) - self.magicSum)
        self.score += abs(self.foreDiagSum() - self.magicSum)
        self.score += abs(self.backDiagSum() - self.magicSum)

    def evaluate(self, optimum = None):
        self.score = 0
        for rowNum in range(self.order):
            delta = self.rowSum(rowNum) - self.magicSum
            self.score += delta * delta
        for colNum in range(self.order):
            delta = self.colSum(colNum) - self.magicSum
            self.score += delta * delta
        delta = self.foreDiagSum() - self.magicSum
        self.score += delta * delta
        delta = self.backDiagSum() - self.magicSum
        self.score += delta * delta

    def mutate(self, gene):
        self.chromosome[gene] = random.choice(self.alleles)
        #print "mutate[", gene, "] =", self.chromosome[gene]

    def _repair(self, parent1, parent2):
        missing = list(self.alleles)
        dupIndices = []
        for index, gene in enumerate(self.chromosome):
            if gene in missing:
                missing.remove(gene)
            else:
                dupIndices.append(index)
        for index in dupIndices:
            gene = random.choice(missing)
            missing.remove(gene)
            self.chromosome[index] = gene
        self.checkIsValid()

    def checkIsValid(self):
        missing = list(self.alleles)
        for index, gene in enumerate(self.chromosome):
            if gene in missing:
                missing.remove(gene)
        if len(missing) != 0 or len(self.chromosome) != self.length:
            raise ValueError("invalid individual: " + repr(self))

    def rowSlice(self, row):
        return self.chromosome[row * self.order : (row + 1) * self.order]

    def colSlice(self, col):
        return self.chromosome[col : : self.order]

    def foreDiagSlice(self):
        return self.chromosome[self.order - 1 : self.length - 1 : self.order - 1]

    def backDiagSlice(self):
        return self.chromosome[ : : self.order + 1]

    def rowSum(self, row):
        return sum(self.rowSlice(row))

    def colSum(self, col):
        return sum(self.colSlice(col))

    def foreDiagSum(self):
        return sum(self.foreDiagSlice())

    def backDiagSum(self):
        return sum(self.backDiagSlice())

    def getScore(self):
        return self.score

    def toStrWithSums(self):
        result = " " * (self.valueWidth * self.order + self.order) + "| " + str(self.foreDiagSum()) + "\n"
        result += "-" * ((self.valueWidth + 1) * (self.order + 1) + 1) + "\n"
        for row in range(self.order):
            result += " ".join(self.valueFormat % v for v in self.rowSlice(row)) + " | " + str(self.rowSum(row)) + "\n"
        result += "-" * ((self.valueWidth + 1) * (self.order + 1) + 1) + "\n"
        result += " ".join(self.valueFormat % self.colSum(col) for col in range(self.order)) + " | " + str(self.backDiagSum()) + "\n"
        return result

class MagicSquareEnvironment(genetic.Environment):
    def _select(self):
        i = int(random.triangular(mode = 0) * self.size)
        if i == self.size:
            i = self.size - 1
        return self.population[i]

    def crossover(self, other):
        "creates offspring"
        pivot = random.randrange(1, self.length - 1)
        def mate(p0, p1):
            chromosome = p0.chromosome[:]
            chromosome[pivot:] = p1.chromosome[pivot:]
            child = p0.__class__(chromosome)
            child._repair(p0, p1)
            return child
        return mate(self, other), mate(other, self)

#    def _select(self):
#        size = 8
#        choosebest = 0.90
#        competitors = [random.choice(self.population) for i in range(size)]
#        competitors.sort()
#        #print "_tournament competitors"
#        #print competitors
#        if random.random() < choosebest:
#            #print "_tournament choosing best"
#            return competitors[0]
#        else:
#            #print "_tournament choosing other"
#            return random.choice(competitors[1:])

    def report(self):
        scores = map(MagicSquare.getScore, self.population)
        print "=" * 80
        print "generation: ", self.generation
        print "scores:     ", min(scores), "to", max(scores)
        print "best:       ", self.best
        print self.best.toStrWithSums()
        if self.generation == self.maxgenerations:
            for id, individual in enumerate(self.population):
                print "%4i:       " % id, individual

def main():
    print "\n" * 10
    order = int(sys.argv[1])
    MagicSquare.order = order
    genetic.Individual.length = order * order
    genetic.Individual.alleles = range(1, order * order + 1)

    for attempt in range(10):
        # size should be >> _tournament size
        env = MagicSquareEnvironment(
            MagicSquare,
            size = order * order * 2,
            maxgenerations = 250,
            mutation_rate = 0.2,
            optimum = 0
        )
        env.run()
        if env.best.score == 0:
            break
    return 0

if __name__ == '__main__':
    sys.exit(main())

# try simulated annealing?
