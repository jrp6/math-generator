#!/bin/bash

for i in 1 2 3 4; do
    ./main.py math$i.tex math$i-solutions.tex
    pdflatex math$i.tex
    pdflatex math$i-solutions.tex
done
