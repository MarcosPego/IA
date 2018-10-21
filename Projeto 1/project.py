import search
from search import *
import copy

# ---- First functions -------------------------------------------------
#TAI content

def c_peg ():
    return "O";

def c_empty():
    return "_";

def c_blocked():
    return "X";

def is_empty(e):
    return e == c_empty()

def is_blecked(e):
    return e == c_blocked()

def is_peg(e):
    return e == c_peg()


#TAI pos
#Tuplo (l, c)

def make_pos(l, c):
    return (l,c)

def pos_l (pos):
    return pos[0]

def pos_c (pos):
    return pos[1]

#TAI move
#Lista [p_initial, p_final]

def make_move (i,f):
    return[i,f]

def move_initial (move):
    return move[0]

def move_final(move):
    return move[1]


#--------------------------------------------------------------------

# Project

# Board_moves function
def board_moves(board):
    moves=[]
    for list in range(0,len(board)):
        for column in range(0, len(board[list])):
            pos = make_pos(list, column)
            moves.extend(check_adjacent_moves(board, pos, len(board), len(board[0])))


    filtered_move = [x for x in moves if x != []]
    return filtered_move




def check_adjacent_moves(board, pos, line_size, column_size):
    move=[]
    move.append(left_move(board, pos, line_size, column_size))
    move.append(right_move(board, pos, line_size, column_size))
    move.append(upper_move(board, pos, line_size, column_size))
    move.append(lower_move(board, pos, line_size, column_size))
    filtered_move = [x for x in move if x != []]
    return filtered_move


def left_move(board, pos, line_size, column_size):
    if pos_c(pos) -2 >= 0:
        possible_pos = make_pos(pos_l(pos) , pos_c(pos)-2)
        adjacent_pos = make_pos(pos_l(pos) , pos_c(pos)-1)
        if is_possible_move(board, pos, possible_pos) and is_adjacent_marble(board, pos, adjacent_pos):
            move = make_move(pos, possible_pos)
            return move
    return []

def right_move(board, pos, line_size, column_size):
    if pos_c(pos) +2 < column_size:
        possible_pos = make_pos(pos_l(pos) , pos_c(pos)+2)
        adjacent_pos = make_pos(pos_l(pos) , pos_c(pos)+1)
        if is_possible_move(board, pos, possible_pos) and is_adjacent_marble(board, pos, adjacent_pos):
            move = make_move(pos, possible_pos)
            return move
    return []

def upper_move(board, pos, line_size, column_size):
    if pos_l(pos) -2 >= 0:
        possible_pos = make_pos(pos_l(pos)-2, pos_c(pos))
        adjacent_pos = make_pos(pos_l(pos)-1, pos_c(pos))
        if is_possible_move(board, pos, possible_pos) and is_adjacent_marble(board, pos, adjacent_pos):
            move = make_move(pos, possible_pos)
            return move
    return []

def lower_move(board, pos, line_size, column_size):
    if pos_l(pos) +2 < line_size:
        possible_pos = make_pos(pos_l(pos)+2 , pos_c(pos))
        adjacent_pos = make_pos(pos_l(pos)+1 , pos_c(pos))
        if is_possible_move(board, pos, possible_pos) and is_adjacent_marble(board, pos, adjacent_pos):
            move = make_move(pos, possible_pos)
            return move
    return []


def is_adjacent_marble(board, pos, adjacent_pos):
    if is_peg(board[pos_l(pos)][pos_c(pos)]):
        if is_peg(board[pos_l(adjacent_pos)][pos_c(adjacent_pos)]):
            return True
        else:
            return False
    else:
        return False


def is_possible_move(board, pos, possible_pos):
    if is_peg(board[pos_l(pos)][pos_c(pos)]):
        if is_empty(board[pos_l(possible_pos)][pos_c(possible_pos)]):
            return True
        else:
            return False
    else:
        return False

# board_perform_move

def board_perform_move(board, move):
    new_board = board.copy()
    new_board = remove_marble(new_board, move[0])


    middle_position = check_middle_move_position(move)
    new_board = remove_marble(new_board, middle_position)

    new_board = add_marble(new_board, move[1])

    return new_board


def check_middle_move_position(move):
    inicial_position = move[0]
    final_position = move[1]
    if(pos_l(inicial_position) != pos_l(final_position)):
        if(pos_l(inicial_position) > pos_l(final_position)):
            middle_position = make_pos(pos_l(inicial_position)-1, pos_c(inicial_position))
        else:
            middle_position = make_pos(pos_l(inicial_position)+1, pos_c(inicial_position))

    if(pos_c(inicial_position) != pos_c(final_position)):
        if(pos_c(inicial_position) > pos_c(final_position)):
            middle_position = make_pos(pos_l(inicial_position), pos_c(inicial_position)-1)
        else:
            middle_position = make_pos(pos_l(inicial_position), pos_c(inicial_position)+1)

    return middle_position


def remove_marble(board, pos):
    new_board = board.copy()
    new_board[pos_l(pos)][pos_c(pos)] = c_empty()
    return new_board

def add_marble(board, pos):
    new_board = board.copy()
    new_board[pos_l(pos)][pos_c(pos)] = c_peg()
    return new_board

#sol_state

class sol_state:
    def __init__(self, board):
        self.board = board

    #def __lt (self, other):
    #    var = 'filler'

class solitare(Problem):
    def __init__(self, board):
        self.p_initial = sol_state(board)



#b1 = [['O','_','_','O','_'], ['O','_','O','_','O'], ['_','O','_','O','_'],['O','_','O','_','_'], ['_','O','_','_','_']]
#print(board_perform_move(b1, [(0, 2), (0, 0)]))

#print(b1)
#    [["_","O","O","O","_"], ["O","_","O","_","O"], ["_","O","_","O","_"],["O","_","O","_","_"], ["_","O","_","_","_"]]
#    /mnt/c/Users/Utilizador/Documents/GitHub/IA
