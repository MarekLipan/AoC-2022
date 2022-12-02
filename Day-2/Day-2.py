# read the input into a list
file = open('Day-2\day2_input1.txt', 'r')
L = file.read().splitlines()

def total_score(l: list) -> int:
    """
    Total score obtained for rock-paper-scissors game.
    """

    total_score = 0

    opponent_moves = ["A", "B", "C"]
    my_moves = ["X", "Y", "Z"]

    for i in l:
        opponent=opponent_moves.index(i[0]) + 1
        me=my_moves.index(i[2]) + 1

        diff = me - opponent

        if diff==0:
            # draw
            total_score += 3 + me
        elif diff==1 or diff==-2:
            # win
            total_score += 6 + me
        elif diff==-1 or diff==2:
            total_score += 0 + me

    return total_score


def total_score_2(l: list) -> int:
    """
    Total score obtained for rock-paper-scissors game.
    """

    total_score = 0

    opponent_moves = ["A", "B", "C"]
    results = ["X", "Y", "Z"]

    for i in l:
        opponent=opponent_moves.index(i[0])
        result=results.index(i[2]) * 3

        if result==3:
            # draw
            total_score += result + opponent_moves
        elif result==6:
            # win
            total_score += result + (opponent + 1) % 3 + 1
        elif result==0:
            total_score += result + (opponent - 1) % 3 + 1

    return total_score

print(total_score_2(L))





    
    

