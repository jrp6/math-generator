#!/usr/bin/env python3
from random import randint

# Prints the excercise c * (a + b) / d in LaTeX form
def printExercise(a, b, c, d):
    print("\\begin{equation}")
    print("\\frac{%d \\cdot (%d %+d)}{%d} =" % (a, b, c, d))
    print("\\end{equation}")

def printRandomExercise():
    minimum = -20
    maximum = 20
    array = []
    for _ in range(4):
        array.append(randint(minimum, maximum))

    printExercise(*array)

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
printRandomExercises(50)
print("\\end{document}")
