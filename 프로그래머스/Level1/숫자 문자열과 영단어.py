def solution(s):
    number = ["zero","one","two","three","four","five","six","seven","eight","nine"]

    for i in range(0,10):
        if s.find(number[i]) >= 0:
            s = s.replace(number[i], str(i))
    answer = int(s)
    return answer