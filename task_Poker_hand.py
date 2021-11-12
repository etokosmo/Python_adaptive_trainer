'''
A poker deck contains 52 cards. Each card has a suit of either clubs, diamonds, hearts, or spades (denoted C, D, H, S).
Each card also has a value of either 2 through 10, jack, queen, king, or ace (denoted 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A).
For scoring purposes card values are ordered as above, with 2 having the lowest and ace the highest value.
The suit has no impact on value.

A poker hand consists of five cards. Poker hands are ranked by the following partial order from lowest to highest.

High Card
Hands which do not fit any higher category are ranked by the value of their highest card.

Pair
Two of the five cards in the hand have the same value.

Two Pairs
The hand contains two different pairs.

Three of a Kind
Three of the cards in the hand have the same value.

Straight
Hand contains five cards with consecutive values.

Flush
Hand contains five cards of the same suit.


Full House
Three cards of the same value, with the remaining two cards forming a pair.

Four of a Kind
Four cards with the same value.

Straight Flush
Five cards of the same suit in numerical order.


Royal Flush
Consists of the ace, king, queen, jack and ten of a suit.

Напишите программу, которая получает на вход пять карт и выводит старшую покерную комбинацию, которая образуется этими картами.

Формат ввода:
Одна строка, на которой указаны пять карт в формате <value><suit>, записанные через пробел.

Формат вывода:
Название старшей комбинации, сформировавшейся на пришедшем наборе.

Sample Input:

10C JC QC KC AC
Sample Output:

Royal Flush
'''


# def -> five cards with consecutive values
def straight(card_value_lst):
    for i in range(len(card_value_lst) - 1):
        if card_value_lst[i] + 1 != card_value_lst[i + 1]:
            return False
    return True


# def -> max count same cards
def max_counter(some_list):
    my_list_counter = list()
    for i in set(some_list):
        my_list_counter.append(some_list.count(i))
    return max(my_list_counter)


my_list = input()
my_list = [i.replace('10', 'T') for i in my_list.split()]

# from list of card - > list values + list suits
card_value = [i[0] for i in my_list]
card_suit = [i[1] for i in my_list]

# rename card value to numbers
value_dict = {'T': '10', 'J': '11', 'Q': '12', 'K': '13', 'A': '14'}

for i, key in enumerate(card_value):
    if card_value[i] in value_dict:
        card_value[i] = key.replace(key, value_dict[key])

# everyone values in card_value -> int
card_value = sorted([int(i) for i in card_value])

if straight(card_value):
    if len(set(card_suit)) == 1:
        if card_value[0] == 10:
            print('Royal Flush')
        else:
            print('Straight Flush')
    else:
        print('Straight')

elif len(set(card_value)) == 2:
    if max_counter(card_value) == 4:
        print('Four of a Kind')
    else:
        print('Full House')

elif len(set(card_suit)) == 1:
    print('Flush')

elif len(set(card_value)) == 3:
    if max_counter(card_value) == 3:
        print('Three of a Kind')
    else:
        print('Two Pairs')

elif len(set(card_value)) == 4:
    print('Pair')

else:
    print('High Card')
