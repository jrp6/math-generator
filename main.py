#!/usr/bin/env python3
from random import randint

# Prints the excercise c * (a + b) in LaTeX form
def printExercise(a, b, c):
    print("\\begin{equation}")
    print("%d \\cdot (%d %+d) =" % (c, a, b))
    print("\\end{equation}")

def randNonZeroOrOne(minimum, maximum):
    x = randint(minimum, maximum)
    return 2 if x == 0 else 2*x if abs(x) == 1 else x

def printRandomExercise():
    minimum = -20
    maximum = 20
    minimumC = -10
    maximumC = 10
    params = [randNonZeroOrOne(minimum, maximum) for _ in range(2)] + [randNonZeroOrOne(minimumC, maximumC)]

    printExercise(*params)

def printRandomExercises(amount):
    for _ in range(amount):
        printRandomExercise()

print("""
\\documentclass[12pt,a4paper,finnish,oneside,fleqn]{article}
\\usepackage[utf8]{inputenc}
\\usepackage{ae,aecompl}
\\usepackage{amsmath}
\\usepackage[finnish]{babel}
\\pagestyle{plain}

\\begin{document}

\\title{Musiikin vaikutus kognitiiviseen suorituskykyyn:\\\\
  Matemaattinen osio}
\\maketitle
""")
printRandomExercises(47)
print("\\end{document}")
