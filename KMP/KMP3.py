"""
KMP算法：字串搜尋
"""
# TEST 3 簡化

Target = "abaabcababcabacababc"
Pattern = "ababc"

"""
建立前綴表，用字串當作標籤
"""
prefixTable = dict()
for i in range(len(Pattern)):
    key = Pattern[:i+1]
    if i == 0: 
        prefixTable[key] = -1
    else:
        key2 = Pattern[:i]
        maxLen = 0
        for i in range(len(key2)//2-1,-1,-1):
            if key2[:i+1] == key2[-i-1:]:
                maxLen = i + 1
                break
        prefixTable[key] = maxLen
#
print(prefixTable)

# 實踐 KMP 搜尋
Target 
Pattern 
prefixTable 

result = []

TI = Target_index = 0
PI = prefixTable_index = 0
TL = len_Target = len(Target)
PL = len_Pattern = len(Pattern)

while TI < TL - PL + 1:
    # 開始匹配，直到 PI 來到 -1 或是 全匹配為止。
    while PI > -1 and PI < PL:
        if  Pattern[PI] == Target[TI]:
            TI += 1
            PI += 1            
        else:
            PI = prefixTable[Pattern[:PI+1]]            
    # 不是 PI == -1 就是 PI == len_Pattern(全匹配)
    if PI == -1:
        PI = 0 #從P[0]開始
    else:
        # 如果全匹配就繼續搜尋
        result.append(TI-PL)
        PI = prefixTable[Pattern]  
    TI += 1 #往下一位搜尋


"""
Target = "abcabc「a」babcabac「a」babc"
Pattern = "ababc"
"""

if result:
    print("搜尋結果：{:} ".format(result))
else:
    print("搜尋結果：{:} 無匹配位置".format(result))