import math , time 
def  invoke_square_root_function(num , mili):
    time.sleep(mili / 1000)
    return math.sqrt(num)

print("Sample Input:")
num = int(input())
mili = int(input())
reslt = invoke_square_root_function(num , mili)
print(f"Square root of {num} after {mili} miliseconds is {reslt}")
