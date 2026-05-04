apples= int(input("whats the apples price?\n"))
oranges= int(input("whats the oranges price?\n"))
bananas= int(input("whats the bananas price?\n"))
budget= 100
total= apples + oranges +bananas
diff=budget-total
if diff > 0:
    print(f"cheap there is still  {diff}$ left")
elif diff <0:
    print(f"too expensive ,{abs(diff)}$ more is needed")
else:
    print("exact there is no money left")
