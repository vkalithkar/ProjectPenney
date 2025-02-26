from game import Game
import random
import pandas as pd

def _score_sim_by_tricks(win_stats: dict) -> int:
    '''
    Compare the entry in the win_stats dict to see 
    which player won more tricks (number of sequences) in this game
    
    Arguments:
        win_stats (dict): the list of 5 elements from a previously-ran simulation containing 
                          each player's number of tricks and number of sequences that game

    Output: 

    '''
    if(win_stats["tricks"][0]>win_stats["tricks"][1]):
        return(1)
    elif(win_stats["tricks"][0]<win_stats["tricks"][1]):
        return(2)
    else:
        return 0

def _score_sim_by_cards(win_stats: dict) -> int:
    '''
    Compare the entry in the win_stats dict to see 
    which player won more cards (total number of deck cards) in this game

    Arguments:
        win_stats (dict): the list of 5 elements from a previously-ran simulation containing 
                          each player's number of tricks and number of sequences that game
        
    Output:

    '''
    if(win_stats['p1_cards'][0]>win_stats["p2_cards"][0]):
        return(1)
    elif(win_stats['p1_cards'][0]<win_stats["p2_cards"][0]):
        return(2)
    else:
        return 0
    
def run_full_sim_and_score(master_seq_list: list, deck_size: int, 
                           seq_len: int, num_decks: int, 
                           all_combos: list, scoring: str = "tricks"
                           ) -> pd.DataFrame:
    '''
    Runs the entire simulation with the desired number of executions to cumulatively calculate
    the frequency of player 1 winning

    Arguments:
        master_seq_list (list):
        deck_size (int):
        seq_len (int):
        num_decks (int): the desired number of Monte Carlo simulations to execute this simulation
        all_combos (list): all possible ways for players to match sequences 
                           while playing the game (pregenerated)
        scoring (str): the desired method to score the players (see scoring methods)
           
    Output:
        all_games_output (pd.DataFrame):

    '''

    all_games_output = pd.DataFrame(columns = ["p1 combo", "p2 combo", 
                                               "p1 winner freq", "p2 winner freq"])
    p1_seqs = []
    p2_seqs = []

    freq_wins_one = [0] * len(all_combos)
    winner_ones = [0] * len(all_combos)
    freq_wins_two = [0] * len(all_combos)
    winner_twos = [0] * len(all_combos)

    for current_deck_idx in range(num_decks):
        master_seq = master_seq_list[current_deck_idx].tolist()
        winners = []
        count = 0

        for this_combo in all_combos:
            count+=1

            print(f"\nshuffle {current_deck_idx + 1}")
            print(f'combo {count}')

            if(current_deck_idx == 0):
                p1_seqs.append(''.join(str(e) for e in this_combo[0]))
                p2_seqs.append(''.join(str(e) for e in this_combo[1]))

            g = Game(two_player_seqs = this_combo, 
                        master_seq = master_seq, 
                        deck_size = deck_size, 
                        seq_len = seq_len)
            
            win_stats = g.play_this_game_deck()

            if (scoring == "tricks"):
                winners.append(_score_sim_by_tricks(win_stats))
            elif (scoring == "cards"):
                winners.append(_score_sim_by_cards(win_stats))
            else:
                print("Invalid scoring method")

        print(f'Winners for this deck over all shuffles: {winners}')

        for index, item in enumerate(winners):
            winner_ones[index] += 1 if (item==1) else 0
        print(f"\nPlayer one's cumulative wins in this simulation so far: {winner_ones}")

        for index, item in enumerate(winners):
            winner_twos[index] += 1 if (item==2) else 0
        print(f"Player two's cumulative wins in this simulation so far: {winner_twos}")

        freq_wins_one=[current_deck_idx/num_decks for current_deck_idx in winner_ones]
        freq_wins_two=[current_deck_idx/num_decks for current_deck_idx in winner_twos]
    print('\n Simulation concluded, all card decks have been run with all shuffles')
    print(f"\nFreq wins player 1: {freq_wins_one}")
    print(f"Freq wins player 2: {freq_wins_two}")

    all_games_output["p1 combo"]=p1_seqs
    all_games_output["p2 combo"]=p2_seqs
    all_games_output["p1 winner freq"]=freq_wins_one
    all_games_output["p2 winner freq"]=freq_wins_two

    return all_games_output