yearly_bill_for_basketball = int(input())

basket_shoes = yearly_bill_for_basketball * 0.60
basket_kit = basket_shoes * 0.80
basket_ball = basket_kit * 0.25
basket_accessories = basket_ball * 0.20

total_basket_bill = yearly_bill_for_basketball + basket_shoes + basket_kit + basket_ball + basket_accessories

print(f"{total_basket_bill:.2f}")
