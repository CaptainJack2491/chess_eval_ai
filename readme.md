# Goal
The main goal of this project is to create a model which can, within reasonable accuracy (85%+ accuracy), predict the evaluation of a chess board in the FEN notation.

## Data
The data will be sourced from [kaggle](https://www.kaggle.com/datasets/ronakbadhe/chess-evaluations).

## Steps
- [x] Get data
- [ ] Convert it into data which can be fed into a model
    - [ ] The data for the model will be a matrix containing:
        - [x] a [2x64] matrix of the the position of the black and white pieces
        ### The following information will be included in the future versions
        - [ ] whose turn it is
        - [ ] Castetling rights
        - [ ] En passant
        - [ ] halfmove clock
        - [ ] fullmove number
    - [ ] evaluation of the board normalized between 0 and 1
- [ ] Split the data into test and training
- [ ] Create the model
- [ ] Train the model
- [ ] Test the model

