yearly_practice_price = int(input())
sneakers = yearly_practice_price - yearly_practice_price * 0.40
kit = sneakers - sneakers * 0.20
ball = kit * 0.25
minor_basketball_stuff = ball * 0.20

final_price = yearly_practice_price + sneakers + kit + ball + minor_basketball_stuff
print(final_price)