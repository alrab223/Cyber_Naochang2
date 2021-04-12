<h1><span style="color: red; ">現在Webhookを利用した機能が使用できません</span></h1>
  
![ロゴ](https://github.com/allbear/Cyber_Naochang2/blob/read_images/images/nao22.gif)

神谷奈緒Discordサーバー【Frontier of the MAYUGE】で稼働しているBot「電脳ナオちゃん」です。


# About
<img src="https://github.com/allbear/Cyber_Naochang2/blob/read_images/images/rumor.png" width="500px">

基本的な機能から、画像、音声など闇鍋botです

## 目次
### コマンド一覧
* [ユーティリティ](#ユーティリティ)

* [ゲームコマンド](#ゲームコマンド)

* [絵文字系](#絵文字系)

* [デレマス](#デレマス)

* [その他](#その他)

* [画像系](#画像系)

* [音声系](#音声系)

### 補足
* [予約投稿について](#予約投稿について)

* [絵文字機能について](#絵文字機能について)

* [Webhookについて](#Webhookについて)

## 注意事項
* コマンドの先頭に`!`を付けてください

* コマンドの引数間は全て半角スペースです

* コマンドは予告無しに増えたり減ったりします

* 短時間でコマンド連打するのは

<img src="https://github.com/allbear/Cyber_Naochang2/blob/read_images/images/dame.png" width="300px" height="300px">

# コマンド一覧
## ユーティリティ
| コマンド | 説明 |
| ------------- | ------------- |
| `vc通知 [人数]` (DM Only) | ボイチャに指定した人数以上が参加した時に通知します |
| `予約投稿 [投稿時刻] [投稿チャンネルid]` (DM Only) | 指定時刻に自動投稿を行います。詳細は[こちら](#予約投稿について) |
| `予約投稿確認` | 予約投稿の一覧を表示します |
| `!del` | 予約投稿を取り消します |
| `status` | 様々なユーザーデータを表示します |
| `server_status` | サーバーの状態を確認します |


## ゲーム
| コマンド | 説明 |
| ------------- | ------------- |
| `なおすきスロット` | なおすきスロットを回します(1日一回) |
| `スーパーなおすきスロット` | スーパーなおすきスロットを回します(1日一回) |
| `レインボースロット` | レインボースロットを回します(3コイン消費) |
| `神谷奈緒チャレンジ` | チャレンジをします(1コイン消費) |
| `連続神谷奈緒チャレンジ` | 連続チャレンジをします(5コイン消費) |

## 絵文字系
| コマンド | 説明 |
| ------------- | ------------- |
| `rainbow` | 虹色橋 |
| `rainbow2` | 虹色橋2 |
| `rainbow3` | 虹色橋3 |
| `b [絵文字名]` | カスタム絵文字をデカ絵文字にします。[複数渡せば連結できます](#絵文字機能について)|
| `u [絵文字名]` | 絵文字をデカ絵文字にします |

## アイドル関連
| コマンド | 説明 |
| ------------- | ------------- |
| `ガシャ` | モバマスのカードがランダムで一枚出力されます |
| `納税` | デレステ版 |
| `奈緒ルーレット` | 奈緒ルーレットを回します |
| `カード検索 [カード名(部分一致可)]` | モバマスのカードを検索します。複数あった場合は、一覧が表示されます |
| `ユニット検索 [アイドル1] [アイドル2]...` | 指定したアイドルが所属しているユニットをAND検索します。指定人数は1人からです |

## その他
| コマンド | 説明 |
| ------------- | ------------- |
| `ping` | 応答時間を確認します |
| `goodbye` | bot停止コマンドです(通常時使用不可) |

## 画像系
* 画像処理のコマンドは以下の例のようにして入力してください

* !は必要ありません

![コマンド例](https://github.com/allbear/Cyber_Naochang2/blob/read_images/images/screen_shot1.gif)


| コマンド | 説明 | 
| ------------- | ------------- |
| `デレステコラ` | デレステのタイトルロゴをかぶせます |
| `nhk` | nhkのアレをかぶせます |
| `gaming` | 画像をゲーミングにします |
| `elon` | イーロンマスクのアレ |
| `onesin` | おねシンのタイトル |
| `切り抜き` | 画像の透過処理を行います。remove.bgのAPIを使用(1ヶ月に50回まで) |

## 音声系

* 工事中

# 補足
## 予約投稿について
予約投稿はbotのDMを介して行います。

```!予約投稿 y/m/d-H:M チャンネルID```  
というようにコマンドを送信します。
コマンド送信後は、投稿したいメッセージを書き込んでください。

![コマンド例](https://github.com/allbear/Cyber_Naochang2/blob/read_images/images/naosuki.gif)

例えば2021年6月15日 0時0分に投稿したい場合は、以下のように入力して下さい

```!予約投稿 2021/6/15-0:00 チャンネルid```

分の指定の際に、一桁の場合0を付けてください  
逆に日付の指定の際は一桁でも0は必要ありません

また、取り消しの際はdelコマンドを使用します。

![コマンド例](https://github.com/allbear/Cyber_Naochang2/blob/read_images/images/delete.png)

## 絵文字機能について

絵文字の連結は以下スクリーンショットを参考にしてください

![コマンド例](https://github.com/allbear/Cyber_Naochang2/blob/read_images/images/emoji.gif)

b(big)コマンドは、カスタム絵文字  
u(unicode)コマンドは通常絵文字をデカくします

## Webhookについて

Discordは画像をまとめて表示させることはできませんが、例外としてTwitterのリンクを張った時のみ添付画像を４枚までまとめて表示することができます。

botではこの仕様をもとに、Webhookを利用してTwitterのURLに見せかけて、画像をまとめて表示しているものがありますが、スマートフォンからの表示では１枚しか表示されないようになっています。ご了承くださいませ

|PC|スマホ|
|---|---|
|![](https://github.com/allbear/Cyber_Naochang2/blob/read_images/images/webhook-pc.png)|![](https://github.com/allbear/Cyber_Naochang2/blob/read_images/images/webhook-smart.jpg)|

## その他

ここには載せていませんが、リアルタイムツイート垂れ流し、読み上げ機能などを実装しています
