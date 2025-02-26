from matplotlib import pyplot as plt
import seaborn as sns

def visualize_all_games_output(all_games_output) -> None:
    '''
    Visualize and directly show both plots for percentage of player 1 wins and player 2 wins

    Arguments:
        all_games_output: 
    '''
    # generic visualizer, seaborn heatmap
    ax = sns.heatmap(all_games_output, linewidth=0.5, cmap='viridis', annot = True)
    plt.show()  


