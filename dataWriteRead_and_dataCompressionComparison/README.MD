##Python 資料讀寫方法比較與資料壓縮比較

**「bstr json > json zlib > json gz > str json」**

blog: https://jnturtle.blogspot.com/2020/03/python.html#more

**[Statistics]**</br>
Method: **bstr json**, Compress Ratio: 0.06：1
Average Use Time: avgWtime:0.09391, avgRtime:0.13125, avgUtime:0.22516 </br>
Data size: 400064(0.39MB), Wspeed:4.16025 MB/s, Rspeed:2.97668 MB/s, Uspeed:1.73516 MB/s </br>
File size: 6700000(6.54MB), Wspeed:69.67296 MB/s, Rspeed:49.85146 MB/s, Uspeed:29.05932 MB/s </br>
Method: **json zlib**, Compress Ratio: 15.32：1 </br>
Average Use Time: avgWtime:0.12470, avgRtime:0.13500, avgUtime:0.25969 </br>
Data size: 400064(0.39MB), Wspeed:3.13309 MB/s, Rspeed:2.89404 MB/s, Uspeed:1.50441 MB/s</br>
File size: 26112(0.03MB), Wspeed:0.20450 MB/s, Rspeed:0.18889 MB/s, Uspeed:0.09819 MB/s</br>
Method: **str json**, Compress Ratio: 0.06：1 </br>
Average Use Time: avgWtime:0.11081, avgRtime:0.15140, avgUtime:0.26222 </br>
Data size: 400064(0.39MB), Wspeed:3.52566 MB/s, Rspeed:2.58044 MB/s, Uspeed:1.48994 MB/s </br>
File size: 6700000(6.54MB), Wspeed:59.04533 MB/s, Rspeed:43.21538 MB/s, Uspeed:24.95256 MB/s </br>
Method: **json gz**, Compress Ratio: 15.31：1</br>
Average Use Time: avgWtime:0.12756, avgRtime:0.14514, avgUtime:0.27270</br>
Data size: 400064(0.39MB), Wspeed:3.06284 MB/s, Rspeed:2.69175 MB/s, Uspeed:1.43266 MB/s</br>
File size: 26124(0.03MB), Wspeed:0.20000 MB/s, Rspeed:0.17577 MB/s, Uspeed:0.09355 MB/s</br>
Method: **json xz**, Compress Ratio: 330.09：1</br>
Average Use Time: avgWtime:0.47223, avgRtime:0.17000, avgUtime:0.64223</br>
Data size: 400064(0.39MB), Wspeed:0.82732 MB/s, Rspeed:2.29813 MB/s, Uspeed:0.60833 MB/s</br>
File size: 1212(0.00MB), Wspeed:0.00251 MB/s, Rspeed:0.00696 MB/s, Uspeed:0.00184 MB/s</br>
Method: **json json**, Compress Ratio: 0.06：1</br>
Average Use Time: avgWtime:0.65894, avgRtime:0.15209, avgUtime:0.81103</br>
Data size: 400064(0.39MB), Wspeed:0.59291 MB/s, Rspeed:2.56879 MB/s, Uspeed:0.48172 MB/s</br>
File size: 6700000(6.54MB), Wspeed:9.92961 MB/s, Rspeed:43.02040 MB/s, Uspeed:8.06753 MB/s</br>
Method: **bstr list**, Compress Ratio: 0.08：1</br>
Average Use Time: avgWtime:0.10280, avgRtime:1.10890, avgUtime:1.21169</br>
Data size: 400064(0.39MB), Wspeed:3.80056 MB/s, Rspeed:0.35232 MB/s, Uspeed:0.32243 MB/s</br>
File size: 4750000(4.64MB), Wspeed:45.12448 MB/s, Rspeed:4.18314 MB/s, Uspeed:3.82826 MB/s</br>
Method: **str str (list)**, Compress Ratio: 0.10：1</br>
Average Use Time: avgWtime:0.10719, avgRtime:1.13352, avgUtime:1.24071</br>
Data size: 400064(0.39MB), Wspeed:3.64487 MB/s, Rspeed:0.34467 MB/s, Uspeed:0.31489 MB/s</br>
File size: 4100000(4.00MB), Wspeed:37.35399 MB/s, Rspeed:3.53229 MB/s, Uspeed:3.22712 MB/s</br>
Method: **str str (tuple)**, Compress Ratio: 0.10：1</br>
Average Use Time: avgWtime:0.10831, avgRtime:1.15125, avgUtime:1.25956</br>
Data size: 400064(0.39MB), Wspeed:3.60713 MB/s, Rspeed:0.33936 MB/s, Uspeed:0.31018 MB/s</br>
File size: 4100000(4.00MB), Wspeed:36.96712 MB/s, Rspeed:3.47788 MB/s, Uspeed:3.17881 MB/s</br>
Method: **json bz**, Compress Ratio: 137.76：1</br>
Average Use Time: avgWtime:1.72234, avgRtime:0.19822, avgUtime:1.92057</br>
Data size: 400064(0.39MB), Wspeed:0.22683 MB/s, Rspeed:1.97094 MB/s, Uspeed:0.20342 MB/s</br>
File size: 2904(0.00MB), Wspeed:0.00165 MB/s, Rspeed:0.01431 MB/s, Uspeed:0.00148 MB/s</br>

