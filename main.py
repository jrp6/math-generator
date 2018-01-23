#!/usr/bin/env python3
from random import randint
from sys import argv

# Prints the excercise c * (a + b) in LaTeX form
def printExercise(a, b, c):
    return """
    \\begin{equation}
    %d \\cdot (%d %+d) =
    \\end{equation}""" % (c, a, b)

def printExerciseAndSol(a, b, c):
    return """
    \\begin{equation}
    %d \\cdot (%d %+d) = %d
    \\end{equation}""" % (c, a, b, c * (a + b))

def randNonZeroOrOne(minimum, maximum):
    x = randint(minimum, maximum)
    return 2 if x == 0 else 2*x if abs(x) == 1 else x

def printRandomExercises(amount, start, end):
    minimum = -20
    maximum = 20
    minimumC = -10
    maximumC = 10

    params = []
    for _ in range(amount):
        thisParams = [randNonZeroOrOne(minimum, maximum) for _ in range(2)] + [randNonZeroOrOne(minimumC, maximumC)]
        params.append(thisParams)

    with open(argv[1], 'w') as f:
        f.write(start)
        for thisParams in params:
            f.write(printExercise(*thisParams))
        f.write(end)

    with open(argv[2], 'w') as f:
        f.write(start)
        for thisParams in params:
            f.write(printExerciseAndSol(*thisParams))
        f.write(end)

docStart = """
\\documentclass[12pt,a4paper,finnish,oneside,fleqn,leqno]{article}
\\usepackage[utf8]{inputenc}
\\usepackage{ae,aecompl}
\\usepackage{amsmath}
\\usepackage[finnish]{babel}
\\pagestyle{plain}

\\begin{document}

\\title{Musiikin vaikutus kognitiiviseen suorituskykyyn:\\\\
  Matemaattinen osio}
\\maketitle
"""
docEnd = "\\end{document}"
printRandomExercises(47, docStart, docEnd)
