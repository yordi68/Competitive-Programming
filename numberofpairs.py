def main():
    num_boys = int(input())
    boys_skill = list(map(int, input().split()))
    
    num_girls = int(input())
    girls_skill = list(map(int, input().split()))
    
    boys_skill.sort()
    girls_skill.sort()
    
    boys_ptr = 0
    girls_ptr = 0
    num_pairs = 0
    
    while boys_ptr < num_boys and girls_ptr < num_girls:
        cur_boy_skill = boys_skill[boys_ptr]
        cur_girl_skill = girls_skill[girls_ptr]
        
        if abs(cur_boy_skill - cur_girl_skill) <= 1:
            num_pairs += 1
            boys_ptr += 1
            girls_ptr += 1
            
        elif cur_boy_skill < cur_girl_skill:
            boys_ptr += 1
        
        else:
            girls_ptr += 1
    
    print(num_pairs)

main()
