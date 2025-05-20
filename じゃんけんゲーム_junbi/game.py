from com import comHand, userHand, judge

userHand = int(input('0:グー 1:チョキ 2:パー'))
msg = judge(userHand, comHand)
print(msg)
