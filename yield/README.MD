python 初學者速理解 yield與generator
這我很久以前碰過，但是也不清不楚，return 與 yield 都能回傳值，那為什麼有甚麼區分？

yeild用於function中回傳值，回傳的類型是產生器generator，這個產生器會產生回傳值，但本身並不是想要的回傳值。

所以很直覺地使用len()或是[:]切片在產生器上，會回報錯誤。

yeild產生器像是在函式中的斷點，可以得到當下變數的數值。意味著你可以在函式外影響函式內的值，也會直接牽連到yield。

要從產生器內取出回傳值，用 next() 或用 for迴圈 都可以，for迴圈會跑到產生器停止，無法再用next()取得值就跳出。

而generator進度是會保存下來的，因此一旦全部跑完一次，想要重頭，那就得重新產生generator一次。

yield能用在哪？從generator取值感覺並不直覺好用。

blog: https://jnturtle.blogspot.com/2020/03/python-yieldgenerator.html#more
