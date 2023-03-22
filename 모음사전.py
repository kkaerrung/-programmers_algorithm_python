words = ['A','E','I','O','U']
flag = False
num = 0 
cnt = 0 

def solution(word): 
    AlphaDic('', word)
    return num

def AlphaDic(now, word):
    global num, cnt 
    
    # 현재 단어와 주어진 단어가 일치하는 경우
    if now == word:
        global flag
        flaf = True 
        num = cnt 
        return 
    
    if flag or num != 0 or len(now) == 5: 
        return 
    
    # 현재 단어 뒤에 순서대로 words의 배열 요소를 붙여서 탐색한다.
    for k in range(5): 
        cnt += 1
        AlphaDic(now + words[k], word)