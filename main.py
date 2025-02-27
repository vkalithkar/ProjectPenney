from generate import create_game_combos, get_n_decks
from score import run_full_sim_and_score
from visualize import visualize_all_games_output
import pandas as pd
import datetime

# update these parameters for variations on the simulation
seq_len = 3
deck_size = 52
num_decks = 10
scoring = "tricks" #alternatively, scoring = "cards"

# create all of the possible sequence combinations match-ups of length seq_len between the two players
# store in a list of tuples
all_combos = create_game_combos(seq_len = seq_len) 

# create a num_decks amount of randomly generated deck shuffles of deck_size number of cards
# store in a list of lists
master_seq_list, seeds = get_n_decks(n_decks = num_decks, half_num_cards = int(deck_size/2))

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# run the simulation with all decks and all possible shuffles and score it 
all_games_output = run_full_sim_and_score(master_seq_list = master_seq_list, 
                                          deck_size = deck_size, 
                                          seq_len = seq_len,  
                                          num_decks=num_decks, 
                                          all_combos=all_combos, 
                                          scoring=scoring)

# pivot the all_games_output into the shape of heatmaps, displaying 
# the sequence combinations along with Player 1's win frequency as the main data                              
all_games_output_one = all_games_output.pivot(index = 'p1 combo', 
                                              columns = 'p2 combo', 
                                              values = "p1 winner freq")

# pivot the all_games_output into the shape of heatmaps, displaying 
# the sequence combinations along with Player 2's win frequency as the main data                              
all_games_output_two = all_games_output.pivot(index = 'p1 combo', 
                                              columns = 'p2 combo', 
                                              values = "p2 winner freq")

print("Visualizing...")

# visualize the two heatmaps, once from Player 1's perspective and again from Player 2's perspective
visualize_all_games_output(all_games_output = all_games_output_one, 
                           title = f"P1's Win Freq. Over {num_decks} Decks Scored by {scoring}")
visualize_all_games_output(all_games_output = all_games_output_two,
                           title = f"P2's Win Freq. Over {num_decks} Decks Scored by {scoring}")

# save logs to csv
# try catch errors
