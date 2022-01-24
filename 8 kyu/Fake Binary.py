def fake_bin(x):
    binlist = [0 if int(i) < 5 else 1 for i in x]
    return ''.join(str(item) for item in binlist)

    #reviewing other solutions a return statement like below is better, i should not have converted to int then back to string for this issue
    # return ''.join('0' if c < '5' else '1' for c in x)