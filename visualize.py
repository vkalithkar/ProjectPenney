import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import os

def visualize_all_games_output(all_games_output: pd.DataFrame, title: str = None) -> None:
    '''
    Visualize and directly show both plots for percentage of player 1 wins and player 2 wins

    Arguments:
        all_games_output:
    
    Output: 
        None 
    '''

    # Define the directory where you want to save the heatmap
    save_dir = "heatmaps"  

    # Create the directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)

    # Generate and save the heatmap
    ax = sns.heatmap(all_games_output, linewidth=0.5, cmap='viridis', annot=True)
    ax.set_title(title)

    # Get figure and save it
    fig = ax.get_figure()
    file_path = os.path.join(save_dir, f"{title}.png")
    fig.savefig(file_path, dpi=300, bbox_inches="tight")  

    plt.close(fig)

    # put in the sequences too on the plot, grey out overlaps, 
    # generate 2 one for each player, and maybe do half?

    return


