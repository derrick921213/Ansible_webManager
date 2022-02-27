def gen_code(gen):
    import random
    check_sum = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
    code = ''
    if gen:
        for i in range(0,len(check_sum)):
            if i==4:
                break
            num = (int)(random.random()*len(check_sum))
            code += check_sum[num]
        return code

def check_code(right,code):
    if len(code)>4:
        return False
    if right == code:
        return True
    

