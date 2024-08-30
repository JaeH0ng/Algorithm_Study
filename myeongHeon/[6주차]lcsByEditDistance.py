
#! 젤 중요한게, 이거 틀렸음. 논리 틀린거임. 
#s1길이 m, s2길이 n, edit값을 e, lcs의 값을 l라 하자
#이때, m,n,e를 안다고 가정(edit알고리즘 활용 위해. 그 결과 활용.
#이때, 최소 편집 과정은, lcs에 속한 문자를 기준으로 편집되는 것으로 보기 가능
#s1에서 l개의 문자에 속하지 않으면 삭제 대상. s2에 존재하는 문자 중 l에 속하지 않으면 s1에 삽입 대상.
#그러므로, s1은 m-l의 삭제와 n-l의 삽입이 일어남.
#단, 이 경우 대체연산을 따로 카운트해서 중복 제거 필요. 그걸 트레이싱 해야 함.
#대체 연산 일어나면 삽입-삭제 하나를 퉁 치는거라서 e=m+n-2l에서, 좌변에 추가로 -대체 수 필요 필요.
#그러려면 트레이스 함수를 만들어서 트레이드 횟수 세야 하고, 식은 e=m+n-2l-r임
# 정확히는 e=(m-l-r)+(n-l-r)+r인 것
#아니, 수기로 한건 다 맞고, 논리적으로도 맞는데 왜지.
#=> e는 같은데, 내부 조합이 다른 케이스 발생했던 것임. (3,1,1)(5,0,0)등
#규칙 추가 필요했던 것. "대체"연산은 최소화 해야 함. 그래야 공통 부분 존중이 됨.
# 근데 이거로도 안됨, 생각해보니 예외가 너무 많음. lcs의 수와 문자열 길이간의 상대적 크기따라 갈리는것도 있고.
#! 굳이 이용하자면 대체 연산을 다른걸로 우회해야 하는데, 그걸 우회시키다 보면 그냥 다른 알고리즘이 됨. 그럴바엔 걍 푸는게 낫지.
#! 즉, 순수한 edit_distance로는 lcs값 계산안됨.

def edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)

    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j  
            elif j == 0: 
                dp[i][j] = i  
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]  
            else:
                dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    return (dp,dp[m][n])

def countReplace(dp,s1,s2):
    replaceCount=0
    y=len(s1)
    x=len(s2)
    while(True):
        if(x==0 or y==0):
            break
        if(s1[y-1]==s2[x-1]):
            y-=1
            x-=1
        else:
            delete=[dp[y-1][x],1,y-1,x,"d"]
            insert=[dp[y][x-1],2,y,x-1,"i"]
            replace=[dp[y-1][x-1],3,y-1,x-1,"r"]
            # 1,2,3을 통해 우선순위를 추가로 더 부여했음. 공통순열 존중.
            minimum=min(delete,insert,replace)
            if(minimum[4]=="r"):
                replaceCount+=1
            y=minimum[2]
            x=minimum[3]
    return replaceCount

def test_lcs():
    test_cases = [
     
        ("ACAYKP", "APCAKC", 4),
        ("ABC", "ABC", 3),
        ("AGGTAB", "GXTXAYB", 4),
        ("ABCDEF", "FBDAMN", 2),
        ("", "", 0),  
        ("ABC", "", 0),  
        ("", "ABC", 0),  
        ("XMJYAUZ", "MZJAWXU", 4),  
    ]
    all_passed = True
    for s1, s2, expected in test_cases:
        dp, editDistance = edit_distance(s1, s2)
        replaceCount=countReplace(dp,s1,s2)
        calculated_lcs=int((len(s1)+len(s2)-editDistance-replaceCount)/2)
        if calculated_lcs == expected:
            print(f"PASSED: LCS({s1}, {s2}) = {calculated_lcs}")
        else:
            print(f"FAILED: LCS({s1}, {s2}) = {calculated_lcs}, expected = {expected},replace={replaceCount},edit={editDistance}")
            all_passed = False

    if all_passed:
        print("All test cases passed!")
    else:
        print("Some test cases failed.")

test_lcs()



