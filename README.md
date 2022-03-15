# SudokuSolver
This is an app to solve a sudoku using backtracking. 

# Table of Contents
- [General Info](#general-info)
- [Technology](#technology)
- [Improvements](#Improvements)

# General Info
The input will be a `9 x 9` board. The empty spaces will be marked with `0` and it will return a valid completed board. The idea is to find an empty square and try all possible valid options. After each valid option, it will move on to a new square and try all posisble valid options and each time a new square cannot put any number or all possible values make the board invalid, we would backtrack one interation and try another combination. 
There will a few functions:
* `isValid()`
* `findSquare()`
* `solveBoard()`

## `isValid()`
| This method will check if the attempted number is a valid answer. It will check horizontally, vertically, and in the `3x3` box of the coordinate.  
## `findSquare()`
| This method will find a square that is not filled in so we do not overwrite a preexisting/filled square.   
## `solveBoard()`
| This method is where the backtracking happens. It will interate through the board and find an empty square. With it, it will try every possible number while checking it is valid. If it works, it will move on to a different square and do the same thing. If it encounters an invalid number and there are no other options, it will then backtrack one square (the previous square) and try the next possible number and continue.   

# Technology 
This project is created with: 
* Python 
* VS Code


# Improvements
* I plan on using my code to make an interactive web page. The user is able to solve sudoku puzzles and will also indicate when a certain move is invalid. 
I will need to make a visualization on how the program works. 
