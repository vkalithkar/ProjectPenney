from generate import create_game_combos, get_n_decks
from score import run_full_sim_and_score
from visualize import visualize_all_games_output
import pandas as pd
import datetime

seq_len = 3
deck_size = 52
num_decks = 10
scoring = "tricks"

all_combos = create_game_combos(seq_len = seq_len) 
master_seq_list, seeds = get_n_decks(n_decks = num_decks, half_num_cards = int(deck_size/2))

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

all_games_output = run_full_sim_and_score(master_seq_list = master_seq_list, 
                                          deck_size = deck_size, seq_len = seq_len,  
                                          num_decks=num_decks, all_combos=all_combos, 
                                          scoring=scoring)
                                
all_games_output_one = all_games_output.pivot(index = 'p1 combo', 
                                          columns = 'p2 combo', 
                                          values = "p1 winner freq")

all_games_output_two = all_games_output.pivot(index = 'p1 combo', 
                                          columns = 'p2 combo', 
                                          values = "p2 winner freq")
print("Visualizing...")
visualize_all_games_output(all_games_output = all_games_output_one, 
                           title = f"P1's Win Freq. Over {num_decks} Decks Scored by {scoring}")
visualize_all_games_output(all_games_output = all_games_output_two,
                           title = f"P2's Win Freq. Over {num_decks} Decks Scored by {scoring}")

# save logs to csv
#clean up function explanations
    # 4 in game (3/4) (recurse)
#clean up function args
    # 4 in game (3/4) (recurse)
