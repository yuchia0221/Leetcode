from typing import List

class Solution:
    def summaryRanges(self, numbers: List[int]) -> List[str]:
        start_index = 0
        output_list = []
        numbers.append(float("inf"))
        for current_index in range(len(numbers)-1):
            if numbers[current_index] + 1 == numbers[current_index+1]:
                continue
            
            if current_index - start_index > 0:
                output_list.append(f"{numbers[start_index]}->{numbers[current_index]}")
            else:
                output_list.append(str(numbers[current_index]))
            
            start_index = current_index + 1
                
        
        return output_list