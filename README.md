

# brainf-ck
Brainf*ck interpreter with Python
----
Brainf*ckのインタプリタです。思いついて10分弱でコーディングしたので穴だらけだと思いますw<br>
Pythonを普段使っているのですが、Wikipadiaで難解言語のページを見ているときにPythonで作ったらどれくらいの大きさになるのか気になって作ってみました。<br>
コードにミス等見つけられた方はこっそり教えていただけると幸いです。<br>
注:オリジナルのものと違い、変数の配列長は3000しか用意していません。<br>
mail: sakaic2003@gmail.com

苦労した点
----
- スクエアブランケットのネスト数カウント　正直一番苦労したのはここ。<br>
- スクエアブランケットのジャンプ<br>
- スクエアブランケットのジャンプ後の動作(もう一度ループするか判定したうえでジャンプ先を選択する。)<br>
**結論、スクエアブランケットが大変だった**

将来的な改善点
----
- 対話的シェルの実装
- 小型化、可読性の向上
- デバッグモードの可視性の向上<br>など。
