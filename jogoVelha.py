
import random

'''
    A função aceita um parâmetro contendo o status atual da placa
    e imprime no console.
'''
def display_board(board):
    print("\n+-------------+-------------+-------------+")
    for i in range(3):
        for j in range(3):
            if j == 0:
                print("|", end=" ")
            print(f"     {board[i][j]}      |", end=" ")
        print("\n+-------------+-------------+-------------+")
    print()
  
'''
    A função aceita o status atual do tabuleiro, pergunta ao usuário sobre sua movimentação,
    verifica a entrada e atualiza o quadro de acordo com a decisão do usuário.
'''
def enter_move(board):
    
    while True:
        try:
            move = int(input("Qual movimento.[1-9]: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um número de 1 a 9.")
            continue
        if move < 1 or move > 9:
            print("Movimento incorreto")
            continue
        
        row, col = divmod(move-1, 3)
        if board[row][col] in ['X', 'O']:
            print("Movimento já ocupado")
        else:
            board[row][col] = 'O'
            break
    
'''
    A função navega no tabuleiro e constrói uma lista de todos os quadrados livres;
    a lista consiste em tuplas, enquanto cada tupla é um par de números de linha e coluna.
'''
def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free_fields.append((row, col))
    return free_fields

'''
    A função analisa o estado da placa para verificar se
    o jogador que usou 'O's ou 'X's ganhou o jogo
'''
def victory_for(board, sign):
    
    # verifica se toda uma linha possui o simbolo
    for row in board:
        if all(symbol == sign for symbol in row) :
            return True
    
    # verifica se toda uma coluna possui o simbolo
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)) :
            return True
    
    # verifica se toda a diagonal possui o simbolo
    if all(board[dig][dig] == sign for dig in range(3)) or all(board[dig][2-dig] == sign for dig in range(3)):
        return True
    
    return False

'''
    A função desenha o movimento do computador e atualiza o tabuleiro.
'''
def draw_move(board):  
    free_fields = make_list_of_free_fields(board)
    move = random.choice(free_fields)
    
    board[move[0]][move[1]] = 'X'

'''
    Função principal onde o jogo começa
'''
def main() :
    
    board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
    
    while len(make_list_of_free_fields(board)) != 0:
        display_board(board)
        
        enter_move(board)
        if victory_for(board, 'O'):
            display_board(board)
            print("Você ganhou!!!\n")
            return

        if len(make_list_of_free_fields(board)) == 0:
            break
        
        draw_move(board)
        if victory_for(board, 'X'):
            display_board(board)
            print("O computador ganhou!!!\n")
            return

    display_board(board)
    print("Empate!!!\n")

if __name__ == "__main__":
    main()