from game import Game
import random
import pandas as pd

def _score_sim_by_tricks(win_stats: dict):
    '''
    Return the player number that won more tricks (number of sequences) in this game
    
    Arguments:
        win_stats: the list of 5 elements from a previously-ran simulation containing 
        each player's number of tricks and number of sequences that game
    '''
    if(win_stats["tricks"][0]>win_stats["tricks"][1]):
        return(1)
    elif(win_stats["tricks"][0]<win_stats["tricks"][1]):
        return(2)
    else:
        return 0

def _score_sim_by_cards(win_stats: dict):
    '''
    Return the player number that won more cards (total number of deck cards) in this game

    Arguments:
        win_stats: the list of 5 elements from a previously-ran simulation containing 
        each player's number of tricks and number of sequences that game
    '''
    if(win_stats['p1_cards'][0]>win_stats["p2_cards"][0]):
        return(1)
    elif(win_stats['p1_cards'][0]<win_stats["p2_cards"][0]):
        return(2)
    else:
        return 0
    
def run_full_sim_and_score(master_seq_list: list, deck_size: int, seq_len: int, 
                           num_decks: int, all_combos: list, scoring: str = "tricks"):
    '''
    Runs the entire simulation with the desired number of executions to cumulatively calculate
    the frequency of player 1 winning

    Arguments:
        all_combos: the list of all possible ways for players to match sequences 
                    while playing the game (pregenerated)
        scoring: string representing the desired method to score the players (see scoring methods)
        runs: the desired number of Monte Carlo simulations to execute this simulation
    '''

    all_games_output = pd.DataFrame(columns = ["p1 combo", "p2 combo", "p1 winner freq"])
    p1 = []
    p2 = []
    freq_wins = [0] * len(all_combos)
    winner_ones = [0] * len(all_combos)

    if(scoring == "tricks"):
        for current_deck in range(num_decks):
            master_seq = master_seq_list[current_deck]
            winner = []
            count = 0

            for this_combo in all_combos:
                count+=1
                print("\nshuffle", current_deck+1)
                print('combo', count)
                if(current_deck == 0):
                    p1.append(''.join(str(e) for e in this_combo[0]))
                    p2.append(''.join(str(e) for e in this_combo[1]))
                g = Game(this_combo, master_seq=master_seq, deck_size = deck_size, seq_len = seq_len)
                win_stats = g.run_sim()
                winner.append(g._score_sim_by_tricks(win_stats))
            print("winners for this shuffle:", winner)

            for index, item in enumerate(winner):
                winner_ones[index] += 1 if (item==1) else 0

            freq_wins=[current_deck/num_decks for current_deck in winner_ones]
        print("freq wins: ", freq_wins)
        all_games_output["p1 combo"]=p1
        all_games_output["p2 combo"]=p2
        all_games_output["p1 winner freq"]=freq_wins
        
        return all_games_output

    elif(scoring == "cards"):
        for current_deck in range(num_decks):
            master_seq = master_seq_list[current_deck]
            winner = []
            count = 0

            for this_combo in all_combos:
                count+=1
                print("\nshuffle", current_deck+1)
                print('combo', count)
                if(current_deck == 0):
                    p1.append(''.join(str(e) for e in this_combo[0]))
                    p2.append(''.join(str(e) for e in this_combo[1]))
                g = Game(this_combo, master_seq=master_seq, deck_size = deck_size, seq_len = seq_len)
                win_stats = g.run_sim()
                winner.append(g._score_sim_by_cards(win_stats))
            print("winners for this shuffle:", winner)

            for index, item in enumerate(winner):
                winner_ones[index] += 1 if (item==1) else 0

            freq_wins=[current_deck/num_decks for current_deck in winner_ones]
        print("freq wins: ", freq_wins)
        all_games_output["p1 combo"]=p1
        all_games_output["p2 combo"]=p2
        all_games_output["p1 winner freq"]=freq_wins
        
        return all_games_output
    else: 
        '''
        throw error
        '''
        return