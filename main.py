from generate import create_game_combos, get_n_decks
from score import run_full_sim_and_score
from visualize import visualize_all_games_output

seq_len = 3
deck_size = 52
num_decks = 100
scoring = "tricks"

all_combos = create_game_combos(seq_len = seq_len) 
master_seq_list = get_n_decks(n_decks = num_decks, half_num_cards = deck_size/2)


all_games_output = run_full_sim_and_score(master_seq_list = master_seq_list, 
                                          deck_size = deck_size, seq_len = seq_len,  
                                          num_decks=num_decks, all_combos=all_combos, 
                                          scoring=scoring)
                                
# all_games_output = all_games_output.pivot(index = 'p1 combo', 
#                                           columns = 'p2 combo', 
#                                           values = "p1 winner freq")

# visualize_all_games_output(all_games_output = all_games_output)
