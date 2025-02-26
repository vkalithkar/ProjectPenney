import queue

class Game:
    '''
    Each individual instance of a game, meaning the chosen sequences of the two players
    and other general information like the size of deck and length of sequences

    '''
    def __init__(self,
                 two_player_seqs: list,
                 master_seq: list,
                 deck_size: int = 52,
                 seq_len: int = 3) -> None:
        self.two_player_seqs = two_player_seqs
        self.deck_size = deck_size
        self.master_seq = master_seq
        self.seq_len = seq_len
        return
    
    def __repr__(self) -> str:
        return f"Player's Sequences: {self.two_player_seqs} for a {self.seq_len} card-length sequence with a {self.deck_size}-card deck"
    
    def play_this_game_deck(self) -> dict:
        '''
        Assess the winner of this game given the players' chosen sequences and 
        the current shuffle, by breaking down the deck sequence

        Output:
            win_stats (dict):
        '''
        print(f'Deck shuffle sequence: {self.master_seq}')
        print(f"Two players' sequences: {self.two_player_seqs}")

        win_stats = self._recurse()
        print(f"Win stats this round:{win_stats} \n")

        return win_stats
    
    def _recurse(self, memory: queue.Queue=None, 
                 tricks:list = None, p1_cards=None, 
                 p2_cards=None, extra=None, 
                 num_cards=0, elem=0) -> dict:
        '''
        Arguments:
            memory (queue.Queue):
            tricks (list):
            p1_cards ():
            p2_cards ():
            extra ():
            num_cards ():
            elem ():

        Output:
            win_stats (dict):
        '''
        if memory is None:
            memory = queue.Queue()
        if tricks is None:
            tricks = [0, 0]
        if p1_cards is None:
            p1_cards = [0]
        if p2_cards is None:
            p2_cards = [0]  
        if extra is None:
            extra = [0]

        if(elem < len(self.master_seq)):
            # while we're still iterating through this deck

            memory.put(self.master_seq[elem])
            num_cards+=1
            print(f'Current {self.seq_len}-card sequence on the table: {tuple(memory.queue)}')
            
            if(tuple(memory.queue) == self.two_player_seqs[0]):
                #point for player 1            
                tricks[0]+=1
                p1_cards[0]+=num_cards
                num_cards = 0
                print("P1 trick")
                while not memory.empty():
                    memory.get()
                
                return self._recurse(memory, tricks, p1_cards, 
                                    p2_cards, extra, num_cards, elem+1)
            
            elif (tuple(memory.queue) == self.two_player_seqs[1]):
                #point for player two 
                tricks[1]+=1
                p2_cards[0]+=num_cards
                num_cards = 0
                print("P2 trick")
                while not memory.empty():
                    memory.get()
                return self._recurse(memory, tricks, p1_cards, 
                                    p2_cards, extra, num_cards, elem+1)            
            else:
                # tie point
                if(memory.qsize()>=self.seq_len):
                    memory.get()       
                return self._recurse(memory, tricks, p1_cards, 
                                    p2_cards, extra, num_cards, elem+1)        
        else: 
            # done iterating through deck, break and return the statistics here
            extra[0]+=num_cards
            print("Round Over")
            win_stats = {"tricks": tricks, "p1_cards": p1_cards, 
                         "p2_cards": p2_cards, "extra cards": extra}
            return(win_stats)