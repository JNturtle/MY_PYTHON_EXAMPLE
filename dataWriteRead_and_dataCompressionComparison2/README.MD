
##Python 資料讀寫方法比較與資料壓縮比較 (二) 多進程

速度排行
「**mpzljzn** >= **mpbjjn** > **mpbjj** > **mpzljz** > **bstr json** > **json zlib**」

blog:https://jnturtle.blogspot.com/2020/03/python_16.html#more

""" 100萬筆資料寫讀</br>
data = [(i,"阿明", "身體狀況", {"體重":78.9, "肝功能": "正常"}, 90, 85, 97, 81,  85, True) for i in range(100000)]
[Statistics]</br>
Method: **bstr json**, Compress Ratio: 0.06：1</br>
Average Use Time: avgWtime:2.46935, avgRtime:3.14803, avgUtime:5.61739</br>
Data size: 8697464(8.49MB), Wspeed:3.43961 MB/s, Rspeed:2.69807 MB/s, Uspeed:1.51202 MB/s</br>
File size: 141888890(138.56MB), Wspeed:56.11319 MB/s, Rspeed:44.01585 MB/s, Uspeed:24.66687 MB/s</br>
Method: **json zlib**, Compress Ratio: 2.79：1</br>
Average Use Time: avgWtime:2.35145, avgRtime:3.29203, avgUtime:5.64348</br>
Data size: 8697464(8.49MB), Wspeed:3.61208 MB/s, Rspeed:2.58005 MB/s, Uspeed:1.50503 MB/s</br>
File size: 3117715(3.04MB), Wspeed:1.29480 MB/s, Rspeed:0.92485 MB/s, Uspeed:0.53950 MB/s</br>
Method: **json xz**, Compress Ratio: 71.11：1</br>
Average Use Time: avgWtime:14.73717, avgRtime:3.62832, avgUtime:18.36548</br>
Data size: 8697464(8.49MB), Wspeed:0.57634 MB/s, Rspeed:2.34093 MB/s, Uspeed:0.46248 MB/s</br>
File size: 122316(0.12MB), Wspeed:0.00811 MB/s, Rspeed:0.03292 MB/s, Uspeed:0.00650 MB/s</br>
Method: **mpbj**, Compress Ratio: 0.06：1</br>
Average Use Time: avgWtime:2.60734, avgRtime:3.34684, avgUtime:5.95418</br>
Data size: 8697464(8.49MB), Wspeed:3.25758 MB/s, Rspeed:2.53781 MB/s, Uspeed:1.42650 MB/s</br>
File size: 141888890(138.56MB), Wspeed:53.14356 MB/s, Rspeed:41.40131 MB/s, Uspeed:23.27163 MB/s</br>
Method: **mpbjn**, Compress Ratio: 0.06：1</br>
Average Use Time: avgWtime:2.19224, avgRtime:3.98733, avgUtime:6.17957</br>
Data size: 8697464(8.49MB), Wspeed:3.87440 MB/s, Rspeed:2.13015 MB/s, Uspeed:1.37447 MB/s</br>
File size: 141888890(138.56MB), Wspeed:63.20630 MB/s, Rspeed:34.75091 MB/s, Uspeed:22.42282 MB/s</br>
Method: **mpbjj**, Compress Ratio: 0.06：1</br>
Average Use Time: avgWtime:2.05410, avgRtime:3.13490, avgUtime:5.18900</br>
Data size: 8697464(8.49MB), Wspeed:4.13496 MB/s, Rspeed:2.70937 MB/s, Uspeed:1.63685 MB/s</br>
File size: 141888890(138.56MB), Wspeed:67.45707 MB/s, Rspeed:44.20021 MB/s, Uspeed:26.70329 MB/s</br>
Method: **mpbjjn**, Compress Ratio: 0.06：1</br>
Average Use Time: avgWtime:0.06299, avgRtime:4.78647, avgUtime:4.84947</br>
Data size: 8697464(8.49MB), Wspeed:134.83090 MB/s, Rspeed:1.77450 MB/s, Uspeed:1.75145 MB/s</br>
File size: 141888890(138.56MB), Wspeed:2199.60744 MB/s, Rspeed:28.94895 MB/s, Uspeed:28.57290 MB/s</br>
Method: **mpzl**, Compress Ratio: 2.95：1</br>
Average Use Time: avgWtime:2.93715, avgRtime:3.43182, avgUtime:6.36897</br>
Data size: 8697464(8.49MB), Wspeed:2.89179 MB/s, Rspeed:2.47496 MB/s, Uspeed:1.33359 MB/s</br>
File size: 2950294(2.88MB), Wspeed:0.98093 MB/s, Rspeed:0.83954 MB/s, Uspeed:0.45237 MB/s</br>
Method:**mpzlz**, Compress Ratio: 2.79：1</br>
Average Use Time: avgWtime:2.57715, avgRtime:3.46488, avgUtime:6.04203</br>
Data size: 8697464(8.49MB), Wspeed:3.29574 MB/s, Rspeed:2.45134 MB/s, Uspeed:1.40575 MB/s</br>
File size: 3118214(3.05MB), Wspeed:1.18159 MB/s, Rspeed:0.87886 MB/s, Uspeed:0.50399 MB/s</br>
Method: **mpzlzn**, Compress Ratio: 2.79：1</br>
Average Use Time: avgWtime:2.19316, avgRtime:3.75349, avgUtime:5.94665</br>
Data size: 8697464(8.49MB), Wspeed:3.87278 MB/s, Rspeed:2.26286 MB/s, Uspeed:1.42830 MB/s</br>
File size: 3118214(3.05MB), Wspeed:1.38847 MB/s, Rspeed:0.81128 MB/s, Uspeed:0.51207 MB/s</br>
Method: **mpzljz**, Compress Ratio: 2.79：1</br>
Average Use Time: avgWtime:2.07069, avgRtime:3.32371, avgUtime:5.39440</br>
Data size: 8697464(8.49MB), Wspeed:4.10182 MB/s, Rspeed:2.55547 MB/s, Uspeed:1.57452 MB/s</br>
File size: 3117371(3.04MB), Wspeed:1.47019 MB/s, Rspeed:0.91594 MB/s, Uspeed:0.56435 MB/s</br>
Method: **mpzljzn**, Compress Ratio: 2.79：1</br>
Average Use Time: avgWtime:0.04629, avgRtime:4.76512, avgUtime:4.81140</br>
Data size: 8697464(8.49MB), Wspeed:183.49081 MB/s, Rspeed:1.78246 MB/s, Uspeed:1.76531 MB/s</br>
File size: 3117371(3.04MB), Wspeed:65.76732 MB/s, Rspeed:0.63887 MB/s, Uspeed:0.63273 MB/s</br>
Method: **mpxz**, Compress Ratio: 71.11：1</br>
Average Use Time: avgWtime:14.85270, avgRtime:4.02111, avgUtime:18.87381</br>
Data size: 8697464(8.49MB), Wspeed:0.57186 MB/s, Rspeed:2.11226 MB/s, Uspeed:0.45002 MB/s</br>
File size: 122316(0.12MB), Wspeed:0.00804 MB/s, Rspeed:0.02971 MB/s, Uspeed:0.00633 MB/s</br>
Method: **mpxzz**, Compress Ratio: 69.15：1</br>
Average Use Time: avgWtime:7.99850, avgRtime:2.42350, avgUtime:10.42200</br>
Data size: 8697464(8.49MB), Wspeed:1.06190 MB/s, Rspeed:3.50469 MB/s, Uspeed:0.81497 MB/s</br>
File size: 125776(0.12MB), Wspeed:0.01536 MB/s, Rspeed:0.05068 MB/s, Uspeed:0.01179 MB/s</br>
Method: **mpxzzj**, Compress Ratio: 71.62：1</br>
Average Use Time: avgWtime:6.89620, avgRtime:3.59600, avgUtime:10.49220</br>
Data size: 8697464(8.49MB), Wspeed:1.23164 MB/s, Rspeed:2.36197 MB/s, Uspeed:0.80952 MB/s</br>
File size: 121444(0.12MB), Wspeed:0.01720 MB/s, Rspeed:0.03298 MB/s, Uspeed:0.01130 MB/s</br>
Method: **mpxzzjn**, Compress Ratio: 71.62：1</br>
Average Use Time: avgWtime:0.04867, avgRtime:8.94961, avgUtime:8.99828</br>
Data size: 8697464(8.49MB), Wspeed:174.53017 MB/s, Rspeed:0.94905 MB/s, Uspeed:0.94392 MB/s</br>
File size: 121444(0.12MB), Wspeed:2.43699 MB/s, Rspeed:0.01325 MB/s, Uspeed:0.01318 MB/s</br>
"""
