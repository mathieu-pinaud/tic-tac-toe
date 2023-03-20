#Lire doc tkinter
#se renseigner sur comment jouer en ligne
#squelette du jeu
# Ouvrir une wdwetre ?
# demander au joueur si il veut jouer en ligne
# si oui connecter (2 versions a faire)  ???
# si non demander si jeu en local J1/J2 (((ou J1/IA ?)))
# (((((faire IA)))))
#lancer jeu avec une boucle sur les conditions de victoire 
#faires alterner les programes/joueurs
#(((((faire des stats et les stocker dans du json)))))

from tkinter import *

board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn_bool = True
tp = 0

def my_refactor(board):
    r = []
    for i in board:
        if i == 2:
            r.append(-1)
        else:
            r.append(i)
    return(r)

def wining_condition(board, tp):
    l = [0, 0, 0, 0, 0, 0, 0, 0]
    r_board = my_refactor(board)
    l[0] = r_board[0] + r_board[1] + r_board[2]
    l[1] = r_board[3] + r_board[4] + r_board[5]
    l[2] = r_board[6] + r_board[7] + r_board[8]
    l[3] = r_board[0] + r_board[3] + r_board[6]
    l[4] = r_board[1] + r_board[4] + r_board[7]
    l[5] = r_board[2] + r_board[5] + r_board[8]
    l[6] = r_board[0] + r_board[4] + r_board[8]
    l[7] = r_board[2] + r_board[4] + r_board[6]

    for i in l:
        if i == 3:
            game_info.configure(text='Le joueur 1 a gagné')
            return(0)
        elif i == -3:
            game_info.configure(text='Le joueur 2 a gagné')
            return(1)
    if tp >= 9:
        game_info.configure(text='Egalitée')
        return(2)
    return(-1)

w = wining_condition(board, tp)        

def check_clic(pos_tuple):
    pos_index = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
    global board
    for i in range(len(pos_index)):
        if pos_index[i] == pos_tuple:
            if board[i] == 0:
                if turn_bool == True:
                    board[i] = 1
                    return(True)
                else:
                    board[i] = 2
                    return(True)
            else:
                return(False)

def mouse_clic(event):
        x = event.x // 100
        y = event.y //100
        global turn_bool
        global tp
        global w
        if (w == -1):
            if (turn_bool == True):
                if(check_clic((x,y))):
                    game_info.configure(text='Tour du joueur 2')
                    ma_grille.create_line(100*x+5, 100*y+5, 100*x+95, 100*y+95, width=3)
                    ma_grille.create_line(100*x+5, 100*y+95, 100*x+95, 100*y+5, width=3)
                    turn_bool = False
                    tp += 1
            elif (turn_bool == False):
                if(check_clic((x, y))):
                    game_info.configure(text='Tour du joueur 1')
                    ma_grille.create_oval(100*x+5, 100*y+5, 100*x+95, 100*y+95, width= 3)
                    turn_bool = True
                    tp += 1
            w = wining_condition(board, tp)

def my_restart():
    global board, turn_bool, tp, w
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn_bool = True
    tp = 0
    w = -1
    ma_grille.delete(ALL)

    for i in range(3):
        ma_grille.create_line(100 * i, 0, 100 * i, 300)
        ma_grille.create_line(0, 100 * i, 300, 100 * i)    
    game_info = Label(wdw, text='Tour du joueur 1')

wdw = Tk()
wdw.title('Tic-tac-toe')

ma_grille = Canvas(wdw, bg="white", width=301, height=301)
ma_grille.grid(row = 0, column = 0, columnspan = 2, padx=5, pady=5)
for i in range(3):
    ma_grille.create_line(100 * i, 0, 100 * i, 300)
    ma_grille.create_line(0, 100 * i, 300, 100 * i)


ma_grille.bind('<Button-1>', mouse_clic)
game_info = Label(wdw, text='Tour du joueur 1')
game_info.grid(row= 1, column = 0, )
    
bouton_quitter = Button(wdw, text='Quitter', command=wdw.destroy)
bouton_quitter.grid(row = 2, column = 1, padx=3, pady=3, sticky = S+W+E)

bouton_reload = Button(wdw, text='Recommencer', command=my_restart)
bouton_reload.grid(row = 2, column = 0, padx=3, pady=3, sticky = S+W+E)

wdw.mainloop()
