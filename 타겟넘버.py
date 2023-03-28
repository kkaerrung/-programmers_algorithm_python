def dfs(numbers, target, cur_sum, cur_idx): 
    if cur_idx == len(numbers): 
        if cur_sum == target:
            return 1 
        else: 
            return 0 
    else: 
        answer = 0 
        answer += dfs(numbers, target, cur_sum+numbers[cur_idx], cur_idx+1)
        answer += dfs(numbers, target, cur_sum-numbers[cur_idx], cur_idx+1) 
        return answer 
    
def solution(numbers, target): 
    answer = dfs(numbers,target,0,0)
    return answer