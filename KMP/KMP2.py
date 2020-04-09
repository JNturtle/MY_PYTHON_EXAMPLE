"""
KMP算法：字串搜尋
"""
# TEST 2 (Target尾部加長，有兩個符合條件的位置)
"""
Target = abaabcababcabacababc
Pattern = ababc
"""
Target = "abaabcababcabacababc"
Pattern = "ababc"

"""
自動建立前綴表
"""
prefixTable = dict()
for i in range(len(Pattern)):
    prefixTable[Pattern[:i+1]] = None

"""
自動填寫前綴表數值，數值為該鍵最大前後綴相等長度
"""
for key in prefixTable:
    maxLen = 0
    for i in range(len(key)//2):
        if key[:i+1] == key[-i-1:]:
            maxLen = max(maxLen, i+1)
    prefixTable[key] = maxLen

"""
移動前綴表數值
"""
prev = -1
for key in prefixTable:    
    prefixTable[key], prev = prev, prefixTable[key]

#
print(prefixTable)

# 實踐 KMP 搜尋
Target 
Pattern 
prefixTable 

result = []

prefixTable_index = 0
Target_index = 0
len_Target = len(Target)
len_Pattern = len(Pattern)

while Target_index < len_Target - len_Pattern + 1:
    # 開始匹配，直到 prefixTable_index 來到 -1 或是 全匹配為止。
    while prefixTable_index > -1 and prefixTable_index < len_Pattern:
        if  Pattern[prefixTable_index] == Target[Target_index]:
            Target_index += 1
            prefixTable_index += 1            
        else:
            prefixTableKey = Pattern[:prefixTable_index+1]
            prefixTable_index = prefixTable[prefixTableKey]            
    # 不是 prefixTable_index == -1 就是 prefixTable_index == len_Pattern(全匹配)
    if prefixTable_index == -1:
        prefixTable_index = 0 #從P[0]開始
    else:
        # 如果全匹配就繼續搜尋
        result.append(Target_index-len_Pattern)
        prefixTable_index = prefixTable[Pattern]  
    Target_index += 1 #往下一位搜尋


"""
Target = "abcabc「a」babcabac「a」babc"
Pattern = "ababc"
"""

if result:
    print("搜尋結果：{:} ".format(result))
else:
    print("搜尋結果：{:} 無匹配位置".format(result))