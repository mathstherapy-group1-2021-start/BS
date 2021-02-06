
nomber = int(input())
def test(number):
    if nomber % 5 == 0:
        if nomber % 7 == 0:
            print('FlipFlop')
        else:
            print('Flip')
    elif nomber % 7 == 0:
        print('Flop')
    elif nomber % 7 != 0:
        print(nomber)
a = test(nomber)
print(a)

