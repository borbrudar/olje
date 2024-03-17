pairs = [(1,1),(7,5)] 
i=0
while 1:
    pairs.append((6*pairs[-1][0] - pairs[-2][0], 6*pairs[-1][1] - pairs[-2][1]))
    k = (pairs[-1][0]-1)//2
    if k > int(1e12):
        print((pairs[-1][1]-1)//2 + 1)
        exit()

# torej zmnozek dveh zaporednih stevil mora bit enak zmnoznku 
# dveh zaporednih stevil *2 ig
#14*15 *2 = 20*21
# ig lhk generiras use pa prevers ce obstajajo
# ouch actually ne 
# 5*3 * 2*7 * 2 = 2*2*5 *  3*7
# 5*17 * 2*2*3*7  * 2 = 2*2*2*3*5 * 7*17
# 5*17 + 6*14 * 2 = 8*15 + 7*17
# k(k+1)/2 = b*(b+1) ....
# mogoc generiras k(k+1)/2 in pol sqrt da dobis b-ish
# pa pol okul prevers sosednje integerje ce je ok?
# mmmmmmmmmm mathoverflow ftw
# B = 2b  +1, K = 2k+1
# 2B^2 = K^2 + 1
# K^2 - 2B^2 = -1
# b = 3 k = 4
# 3/4 * 2/3 = 6/12 = 1/2 less go
# resitve of pell equation??
# torej some angry googling later lhk mende generiras 
# resitve z (3x+4y,2x+3y) kjer je zaceten (1,1)
# oh nice se rekurzivna je 