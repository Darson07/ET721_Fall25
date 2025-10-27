'''
Darson Hak
Project 11 - Connect 4 Unittest
'''

import unittest 
from main import Connect4
import io
import sys

class TestConnect4(unittest.TestCase):

    # TEST WIN CONDITIONS
    def test_horizontal_win(self):
        game = Connect4()
        for c in range(4):
            game.board[5][c] = 'X'
        self.assertTrue(game.check_win('X'))

    def test_vertical_win(self):
        game = Connect4()
        for r in range(4):
            game.board[5 - r][0] = 'O'
        self.assertTrue(game.check_win('O'))

    def test_diagonal_down_right_win(self):
        game = Connect4()
        coords = [(2,0), (3,1), (4,2), (5,3)]
        for r, c in coords:
            game.board[r][c] = 'X'
        self.assertTrue(game.check_win('X'))

    def test_diagonal_up_right_win(self):
        game = Connect4()
        coords = [(5,0), (4,1), (3,2), (2,3)]
        for r, c in coords:
            game.board[r][c] = 'O'
        self.assertTrue(game.check_win('O'))

    def test_no_win(self):
        game = Connect4()
        game.board[5][0] = 'X'
        game.board[5][1] = 'O'
        game.board[5][2] = 'X'
        game.board[5][3] = 'O'
        self.assertFalse(game.check_win('X'))
        self.assertFalse(game.check_win('O'))
    # END 

    # TEST CHIP DROPPING LOGIC
    def test_successful_drop(self):
        game = Connect4()
        result = game.drop_chip(1)
        self.assertTrue(result)
        self.assertEqual(game.board[5][0], 'X')

    def test_full_column(self):
        game = Connect4()
        for _ in range(game.ROWS):
            game.drop_chip(1)
        self.assertFalse(game.drop_chip(1))

    def test_invalid_column(self):
        game = Connect4()
        self.assertFalse(game.drop_chip(0))
        self.assertFalse(game.drop_chip(8))

    def test_full_board(self):
        game = Connect4()
        for col in range(1, game.COLS + 1):
            for _ in range(game.ROWS):
                game.drop_chip(col)
        self.assertTrue(game.is_full())
        self.assertFalse(any(game.drop_chip(c + 1) for c in range(game.COLS)))
    #END

    # TEST print_board METHOD
    def test_print_board_output(self):
            game = Connect4()
            captured_output = io.StringIO()
            sys.stdout = captured_output
            game.print_board()
            sys.stdout = sys.__stdout__
            output = captured_output.getvalue()
            self.assertIn('Current Board', output)
            self.assertIn('1 2 3 4 5 6 7', output)
    # END

if __name__ == '__main__':
    unittest.main()

# DOCUMENTATIONS
'''
- Took a while for me to understand that "io" and "sys" were needed to check that the right kind of board is created
- For "test_vertical_win", I needed to write "5 - r". For the longest time I just put a plain 5
- 
'''