"""
KMP算法：字串搜尋
"""
# TEST 1 
"""
Target = abaabcababcabac
Pattern = ababc
"""
Target = "abcabcababcabac"
Pattern = "ababc"
"""
手動建立前綴表
ababc 拆成五種前綴
"""
prefixTable = dict()
prefixTable["a"] = None
prefixTable["ab"] = None
prefixTable["aba"] = None
prefixTable["abab"] = None
prefixTable["ababc"] = None #已匹配
"""
手動填寫前綴表數值，數值為該鍵最大前後綴相等長度
a => 無法拆前後綴 => 0
ab => 無法 => 0
aba => ab != ba => a = a => 1
abab => ab == ab => 2
"""
prefixTable["a"] = 0
prefixTable["ab"] = 0
prefixTable["aba"] = 1
prefixTable["abab"] = 2
#已匹配 prefixTable["ababc"] = None 
"""
abaabcababcabac
|||x
ababc

到 aba「b」c，匹配失敗。前面的aba已經通過，對照prefixTable => prefixTable["aba"]:1 => 回到P位置1的地方繼續匹配 
=> 用 a「b」abc 匹配 aba「a」bcababcabac  => 匹配失敗，回到 prefixTable["a"] 的該值對應的位置 0。
=> 用「a」babc 匹配 aba「a」bcababcabac => 匹配成功，往下一位匹配。

當前狀況是看前一個鍵的值決定回到哪裡，為了使搜尋過程更順暢，讓 prefixTable[key] 為匹配失敗該回到的位置，所以每個鍵將對應位置往後移。
#尚未提及 prefixTable["a"] = -1
prefixTable["ab"] = 0
prefixTable["aba"] = 0
prefixTable["abab"] = 1
prefixTable["ababc"] = 1

移動前綴表數值
"""
prefixTable["ababc"] = prefixTable["abab"]
prefixTable["abab"] = prefixTable["aba"]
prefixTable["aba"] = prefixTable["ab"]
prefixTable["ab"] = 0
"""
abaa「b」cababcabac & 「a」babc 匹配 => 匹配失敗，但返回值尚未設定。
如果為 0，代表要回到 「a」babc 匹配，會造成無限循環。
設定為 -1，表示往下搜尋。
"""
prefixTable["a"] = -1

# 實踐 KMP 搜尋
Target 
Pattern 
prefixTable 

result = False 

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
        Target_index += 1 #往下一位搜尋
        prefixTable_index = 0 #從P[0]開始匹配
    else:
        # 如果全匹配就跳出，暫無設定處理
        result = True
        break

"""
Target = "abcabc「a」babcabac"
Pattern = "ababc"
"""

if result:
    print("搜尋結果：{:} 匹配位置：{:}".format(result, Target_index-len_Pattern) )
else:
    print("搜尋結果：{:} 無匹配位置".format(result) )