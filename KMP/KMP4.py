"""
KMP算法：字串搜尋
"""
# TEST 4 函式化

Target = "abaabcababcabacababc"
Pattern = "ababc"


def KMP(target, pattern):    
    result = []
    prefixTable = dict()
    TI = 0
    PI = 0    
    TL = len(target)
    PL = len(pattern)

    """
    prefixTable 解說
    [0] a = 0 # 預設
    [1] 如果長度要加1，後面的字符要跟 [1-1] => [0] 一樣，也就是與 pattern[prefixTable[1-1]] a 一樣。 => b != a, prefixTable[1] = 0
    [2] pattern[2] == pattern[prefixTable[2-1]] => 最後加入的字符 跟 pattern[prefixTable[2-1]] 一樣 => 長度+1
    [3] 2
    [4] pattern[4] != pattern[prefixTable[4-1]] => pattern[4] != pattern[prefixTable[2-1]] => prefixTable[4] = 0
             c     !=           a(※[2])        =>    c       !=         a(※[0])        => 
    如果沒有搜尋到，就到跳最後通過該跳的位置 prefixTable[4-1-1]-1 => [0]
    ab「abc」， 若最後一個位置是 a，長度就變成 2+1，但是沒有通過。拿來比較的是 「ab」abc 這位置上的ab ，因此你要跳到 a「b」abc 該回去的索引，也就是 0，到了這個位置「a」babc，再去比較。
    """      

    # 更換標籤，換成 index,，往後挪移(條件的pattern[i-1])
    for i in range(len(pattern)):
        if i == 0: 
            prefixTable[i] = -1
        else:
            pi = prefixTable[i-1]
            while pi >= -1:
                if pattern[i-1] == pattern[pi]:
                    prefixTable[i] = pi + 1
                    break
                else:
                    # 跳到最後通過的索引位置
                    if  pi == -1:
                        prefixTable[i] = 0
                        break
                    pi = prefixTable[pi] # 退到 prefixTable[pi-1] 
    #

    while  TI < TL - PL + 1:
        # 開始匹配，直到 PI 來到 -1 或是 全匹配為止。
        while PI > -1 and PI < PL:
            if  pattern[PI] == Target[TI]:
                TI += 1
                PI += 1            
            else:
                PI = prefixTable[PI]            
        # 不是 PI == -1 就是 PI == len_Pattern(全匹配)
        if PI == -1:
            PI = 0 #從P[0]開始
        else:
            # 如果全匹配就繼續搜尋
            result.append(TI-PL)
            PI = prefixTable[PI-1]  
        TI += 1 #往下一位搜尋

    return result


"""
Target = "abcabc「a」babcabac「a」babc"
Pattern = "ababc"
"""
Target = "abaabcababcabacababc"
Pattern = "ababc"

result = KMP(Target, Pattern)

if result:
    print("搜尋結果：{:} ".format(result))
else:
    print("搜尋結果：{:} 無匹配位置".format(result))