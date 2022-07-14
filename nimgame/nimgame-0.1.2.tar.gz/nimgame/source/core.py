"""The Nim Game core

This main class implements the init and maintenance of heaps, movements of
coins, records the statuses and calculates decisions.
"""


from dataclasses import dataclass
import itertools
import random; random.seed()
import valid8 as v8
from source.typedefs import Move, ErrorRate, ErrorRate_T, ErrorRateTypes, \
    MyTurn_T, HeapCoinRange, HeapCoinRange_T, HeapCoinRangeTypes
from source import calculations


@dataclass
class Nim(calculations.Mixin):
    """Class to implement the Nim game

    Methods:
    - setup_heaps(): initiate the heaps. Note that this creates the heaps
        instance attribute, i.e. there is no need for __init__()
    - set_start(): set which party is to start the game
    - do_move(): do a move, either the Computer's or the Player's turn
    - get_heapstatus(): get the heap status (coins in heaps)
    - game_end(): figure out whether the game ended
    - calculation methods from the mixin

    Attributes:
        heaps (list): it contans the number of coins in each heap. This is
            initiated in setup_heaps().
        activeplayer (str): either the "Computer" or "Player"; or "start" in the
            beginning
        nextturn (iterator.__next__): calling it infinitely yields the swapped
            player names

    Args:
        error_rate: The rate percentage of mistakes the Computer is to make. By
            deafult it is 0%, i.e. the computer never makes mistakes, and the
            Player has no chance to win (unless the Player decides who to start
            and never makes mistakes). If it was set to the extreme 100%, the
            Computer would always intentionally make wrong moves, practically
            making all attempts to lose. NB, if the Player does the same, the
            Computer may still win.
            For testing, when moves of both parties are made by the program,
            the error rate of both parties can be set with the "ErrorRate"
            namedtuple. This can be used to create staistics of games played by
            different skilled players. NB, still, the 1st party will be reported
            in the results as Computer, and the 2nd as Player, just to name
            them.
        heapcount_range: The min and max number of heaps to be set up. Less than
            3 heaps makes little sense, more than 15 is a bit of an overkill.
            So, the default is (3-15), but it can be set otherwise. NB, since
            the heaps are displayed with letters (A-Z), the heap number is
            limited to 26.
        coincount_range: The min and max number of strwas to be set up in a
            heap. Less than 1 coin makes no sense, more than 20 is a bit of an
            overkill. So, the default is (1-20). NB, since the heap contents are
            displayed in max 2 digits, the coin number is limited to 99.
        misere: Whether it is the "misère" version of the game.
    """
    error_rate: ErrorRate_T=0
    heapcount_range: HeapCoinRange_T=(3, 15)
    coincount_range: HeapCoinRange_T=(1, 20)
    misere: bool=True
    
    
    def __post_init__(self):
        """Validate all input parameters for the instantiation, being paranoid
        
        This is rather an excercise for playing with a validator package.
        
        If any validation fails, exception is raised with detailed messages.
        """
        #validate the error rate
        self.set_error_rate(self.error_rate)
        
        #validate the heapcount_range type
        v8.validate(
            name='heapcount_range', 
            value=self.heapcount_range, 
            instance_of=HeapCoinRangeTypes, 
            custom=v8.validation_lib.collections.has_length(2)
        )
        #make sure the heap range is a namedtuple from here on
        self.heapcount_range = HeapCoinRange(*self.heapcount_range)
        #validate the heap range ends; less than 1 heap makes no any sense; 26 heaps are from A to Z, no more to allow
        v8.validate(
            name='heapcount_range.min', 
            value=self.heapcount_range.min, 
            instance_of=int, 
            min_value=1
        )
        v8.validate(
            name='heapcount_range.max', 
            value=self.heapcount_range.max, 
            instance_of=int, 
            max_value=26
        )
        #validate the heap range ends, i.e. min <= max
        v8.validate(
            name='heapcount_range min<max', 
            value=self.heapcount_range.max-self.heapcount_range.min, 
            min_value=0, 
            help_msg='Range max bigger than min'
        )
        
        #validate the coincount_range type
        v8.validate(
            name='coincount_range', 
            value=self.coincount_range, 
            instance_of=HeapCoinRangeTypes
        )
        #validate the coincount_range size
        v8.validate(
            name='coincount_range', 
            value=self.coincount_range, 
            custom=v8.validation_lib.collections.has_length(2)
        )
        #make sure the coin range is a namedtuple from here on
        self.coincount_range = HeapCoinRange(*self.coincount_range)
        #validate the coin range ends
        v8.validate(
            name='coincount_range.min', 
            value=self.coincount_range.min, 
            instance_of=int
        )
        v8.validate(
            name='coincount_range.max', 
            value=self.coincount_range.max, 
            instance_of=int
        )
        #validate the coin range min; must be a natural number, including zero
        v8.validate(
            name='"coincount_range" min', 
            value=self.coincount_range.min, 
            min_value=0
        )
        #validate the coin range max; being displayed as 2 digit, its max is 99
        v8.validate(
            name='"coincount_range" max', 
            value=self.coincount_range.max, 
            max_value=99
        )
        #validate the coin range ends, i.e. min <= max
        v8.validate(
            name='coincount_range min<max', 
            value=self.coincount_range.max-self.coincount_range.min, 
            min_value=0, 
            help_msg='Range max bigger than min'
        )
        
        #validate the misere flag
        v8.validate(
            name='misere', 
            value=self.misere, 
            instance_of=bool
        )
        
        #reset active player
        self.activeplayer='start'
    
    
    def setup_heaps(self, 
        heapcounts: list=None
    ) -> None:
        """Initial setup of heaps of coins
        
        If "heapcounts" is provided the number of heaps and the number of coins
        in each heap is checked whether they fall into the set valid range.
        Exception is raised if not.
        
        Args:
            heapcounts: list elements state the number of coins in each heap.
                If no list is provided, a random number of heaps are created
                with random number of coins.
        """
        #random heaps to be created?
        if not heapcounts:
            heapcounts = []
            #create a random int for the number of heaps
            heapnumber = random.randint(*self.heapcount_range)
            for _ in range(heapnumber):
                #create a random int for the number of coins in the heap
                coincount = random.randint(*self.coincount_range)
                #create the heap with the number of coins
                heapcounts.append(coincount)
        else:
            #validate the number of heaps
            v8.validate(
                name='Heaps in "heapcounts"', 
                value=len(heapcounts), 
                custom=v8.validation_lib.comparables.between(
                    *self.heapcount_range
                )
            )
            #loop on all heaps
            for idx, heap in enumerate(heapcounts):
                #validate the number of coins in the given heap
                v8.validate(
                    name=f'Coins of heap#{idx} in "heapcounts"', 
                    value=heap, 
                    custom=v8.validation_lib.comparables.between(
                        *self.coincount_range
                    )
                )

        #create the heaps list
        self.heaps = heapcounts


    def set_start(self, 
            myturn: MyTurn_T='a'
    ) -> None:
        """Set the starting party
        
        User can explicitly set which party is to start. This makes sense if
        this decision is made based on the starting heap status.
        
        The user can also ask for random selection.
        
        By default the computer makes the decision using 2 factors. First it
        figures out whether the heap status is beneficial for starting. i.e. it
        is a winning status. Then it checks the required error rate and it
        intentionally makes a wrong decision with higher likelihood if the
        error_rate is higher.
        
        Note:
            The myturn argument is internally converted to a boolean if it
            arrives as a str. The myturn value is used in a bool context, i.e.
            it can be any type (e.g. empty list will act like a False, i.e.
            Computer is to start). No issues with "overwriting" it as the
            default remains the 'a' for subsequent calls and also the outer
            variable, where the argument comes from, remains unaffected.
        
        Args:
            myturn: the logical value from the Player's point of view.
                - 'a' (by default): the Computer figures out which party is to start
                    the game, based on the heap counts and the required error_rate
                - truthy or 'p': Player
                - falsy or 'c': Computer
                - 'r': random
        """
        #auto?
        if myturn=='a':
            #figure out whether the initial heap status is good for the Computer
            winning = self.is_winning_for_next()
            #whether to make a good decision
            smart = self.make_good_choice()
            
            #winning&smart or !winning&!smart makes the Computer start
            myturn = winning ^ smart
        
        #random?
        elif myturn=='r':
            myturn = random.choice([True, False])
        
        #map c to False, p to True
        elif isinstance(myturn, str):
            myturn = myturn.lower()
            if myturn=='c':
                myturn = False
            elif myturn=='p':
                myturn = True
            else:
                raise ValueError(f'"myturn" has an unknown value: "{myturn}"')
        
        #reset the "nextturn" cyclic iterator
        self.nextturn=itertools.cycle(('Computer', 'Player')).__next__
        
        #Player's turn needed?
        if myturn:
            #the cycle starts by the Computer, so get rid of it
            self.nextturn()
        #get the next player
        self.activeplayer = self.nextturn()


    def set_error_rate(self,
        error_rate: ErrorRate_T
    ) -> None:
        """Set the required error rate, even during a game
        
        For the definition of "error_rate", see the class argument. 
        """
        #validate the error rate
        v8.validate(
            name='error_rate', 
            value=error_rate, 
            instance_of=ErrorRateTypes
        )
        if isinstance(error_rate, ErrorRate):
            for player in ErrorRate._fields:
                v8.validate(
                    name=f'error_rate.{player}', 
                    value=getattr(error_rate, player), 
                    instance_of=int, 
                    custom=v8.validation_lib.comparables.between(0, 100)
                )
        else:
            v8.validate(
                name='error_rate', 
                value=error_rate, 
                instance_of=int, 
                custom=v8.validation_lib.comparables.between(0, 100)
            )
        
        self.error_rate = error_rate
    
    
    def do_move(self, 
        move: Move
    ) -> None:
        """Remove given number of coins from a given heap
        
        Before doing the coin removal, check for illegal moves and report
        issues.
        
        After the given number of coins have been removed from a given heap,
        swap the active player.

        Args:
            move: The designation of the heap and the number of coins to be
                removed from that heap. Heap designation can be a letter or a
                number (starting from 0).
        """
        #heap designation letter?
        if isinstance(move.heapdesig, str):
            if len(move.heapdesig) != 1:
                raise ValueError(
                    f'Wrong heap designation ({move.heapdesig})'
                )
            heapnumber = ord(move.heapdesig.upper()) - 65
            if heapnumber < 0:
                raise ValueError(
                    f'Wrong heap designation ({move.heapdesig})'
                )
        
        #heap designation number?
        elif isinstance(move.heapdesig, int):
            heapnumber = move.heapdesig
        
        else:
            raise ValueError(
                f'Wrong heap designation type ({type(move.heapdesig)})'
            )
            
        if len(self.heaps)-1 < heapnumber:
            raise ValueError(
                f'Wrong heap letter ({chr(heapnumber+65)}), there are '
                f'A-{chr(len(self.heaps)-1+65)} heaps only'
            )

        if self.heaps[heapnumber] < move.removecount:
            raise ValueError(
                f'Heap({chr(heapnumber+65)}) only has '
                f'{self.heaps[heapnumber]} coin(s), '
                f'cannot remove {move.removecount}'
            )

        #reduce the required heap
        self.heaps[heapnumber] -= move.removecount

        #get the next player
        self.activeplayer = self.nextturn()


    def get_heapstatus(self) -> str:
        """Get the heap status in a formatted string
        
        Returns:
            The number of coins per heap. Also header at the start.
        """
        status = ''
        #at the start?
        if self.activeplayer == 'start':
            #start with the heading line
            status = ' '.join([f' {chr(65+h)}' for h in range(len(self.heaps))]) + '\n'
        #list the coins in the heaps, single-digit numbers padded with space
        status += ' '.join([f'{str(h):>2}' for h in self.heaps])
        
        return status
    

    def game_end(self) -> bool:
        """Identify whether the game ended, i.e. all heaps are empty

        Simply add up all the coins and return the boolean negate of the sum.
        
        Returns:
            The flag to indicate game end.
        """
        return not sum(self.heaps)
