import random

def main():
    print('现在开始投骰子！')

    game_continue = True

    first_rolled_point = random.randint(1, 6) + random.randint(1, 6)
    print(f'玩家投出的点数是 {first_rolled_point}。')
    if first_rolled_point == 7 or first_rolled_point == 11:
        print('玩家胜！')
        game_continue = False
    elif first_rolled_point == 2 or first_rolled_point == 3 or first_rolled_point == 12:
        print('庄家胜！')
        game_continue = False
    else:
        print('第一次未决出胜负，继续投骰子。')
        print('------------------------------')

    while game_continue:
        rolled_point = random.randint(1, 6) + random.randint(1, 6)
        print(f'玩家投出的点数是 {rolled_point}。')
        print(f'玩家第一次投出的点数是 {first_rolled_point}。')
        if rolled_point == 7:
            print('庄家胜！')
            break
        elif rolled_point == first_rolled_point:
            print('玩家胜！')
            break
        else:
            print('本次投骰子未决出胜负，继续投骰子。')
            print('----------------------------------')

if __name__ == '__main__':
    main()