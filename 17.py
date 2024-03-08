d = {    0 : "", 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' , 100:"hundred" , 1000:"thousand"}


def to_word(n):
    s = str() 
    if n == 1000: return len(d[n]) + 3
    st=0
    if n >= 100:
        s += d[int(str(n)[0])] 
        s+=d[100]
        n = n %100
        st =1
    if st == 1 and n > 0: s +="and"
    if n <= 20: s += d[n]
    else:
        s += d[n - n%10]
        if n%10 != 0: s += d[n%10]    
    return len(s)

print(sum(to_word(i) for i in range(1,1001)))
