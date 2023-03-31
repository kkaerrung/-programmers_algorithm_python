from collections import deque

def solution(begin, target, words): 
    q = deque()
    q.append([begin, 0])
    
    visit = [0]*len(words)

    if target not in words: 
        return 0 
    
    while q: 
        word, count = q.popleft()

        if target == word: 
            return count 
        
        for i in range(len(words)):
            different_count = 0 
            
            if not visit[i]: 

                for j in range(len(word)): 
                    if word[j] != words[i][j]: 
                        different_count += 1 

                if different_count == 1: 
                    visit[i] = 1 
                    q.append([words[i], count+1])
    return 0 