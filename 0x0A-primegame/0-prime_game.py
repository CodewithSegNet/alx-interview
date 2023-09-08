#!/usr/bin/python3

'''A function that chooses a prime num
from it sets and
removes that number and it multiples
'''


def isWinner(x, nums):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def play_round(n):
        primes = [i for i in range(2, n + 1) if is_prime(i)]
        '''0 for Maria, 1 for Ben
        '''
        turn = 0
        while n > 0:
            found = False
            for prime in primes:
                if n % prime == 0:
                    n -= prime
                    found = True
                    break
            if not found:
                break
            '''Switch turn
            '''
            turn = 1 - turn
            '''Return the winner of the round (0 for Maria, 1 for Ben)
            '''
            return turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_round(n)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
