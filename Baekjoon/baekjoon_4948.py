#3. 백준 - 베르트랑 공준 / 문제번호 : 4948 / 문제 유형 : 수학 (에라스토테네스의 체) / 실버3
# [4948번: 베르트랑 공준](https://www.acmicpc.net/problem/4948)
    
import sys
while True:
    n = int(sys.stdin.readline())
    
    if n == 0 : 
        break
    def checkPrime(num):
        cnt = 0
        isprime = [True]*(num+1)
        isprime[0] = False
        isprime[1] = False
        
        for i in range(2, num+1):
            if isprime[i]:
                cnt += 1
                for j in range(2*i, num+1, i):
                    isprime[j] = False
        return cnt
               
    print(checkPrime(2*n)-checkPrime(n))
    
        