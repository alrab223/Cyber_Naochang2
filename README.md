![ロゴ](https://github.com/allbear/Cyber_Naochang2/blob/read_images/images/nao22.gif)

神谷奈緒Discordサーバー【Frontier of the MAYUGE】で稼働しているBot「電脳ナオちゃん」です。


# About
<img src="https://github.com/allbear/Cyber_Naochang2/blob/read_images/images/rumor.png" width="500px">

基本的な機能から、画像、音声など思いついた機能をどんどん放り込んだ闇鍋botです
# コマンド一覧
## 目次
* [ユーティリティ](#ユーティリティ)

* [ゲームコマンド](#ゲームコマンド)

* [絵文字系](#絵文字系)

* [デレマス](#デレマス)

* [その他](#その他)

* [画像系](#画像系)

* [音声系](#音声系)

## 注意事項
* コマンドの先頭に`!`を付けてください

* コマンドの引数間は全て半角スペースです

* 短時間でコマンド連打するのはいかんぜよ

***
### ユーティリティ
| コマンド | 説明 |
| ------------- | ------------- |
| `vc通知 [人数]` (DM Only) | ボイチャに指定した人数以上が参加した時に通知します |
| `予約投稿 [投稿時刻] [投稿チャンネルid]` (DM Only) | 指定時刻に自動投稿を行います。詳細は[こちら](#予約投稿について) |
| `status` | 様々なユーザーデータを表示します |
| `server_status` | サーバーの状態を確認します |


### ゲーム
| コマンド | 説明 |
| ------------- | ------------- |
| `なおすきスロット` | なおすきスロットを回します(1日一回) |
| `スーパーなおすきスロット` | スーパーなおすきスロットを回します(1日一回) |
| `レインボースロット` | レインボースロットを回します(3コイン消費) |
| `神谷奈緒チャレンジ` | チャレンジをします(1コイン消費) |
| `連続神谷奈緒チャレンジ` | 連続チャレンジをします(5コイン消費) |

### 絵文字系
| コマンド | 説明 |
| ------------- | ------------- |
| `rainbow` | 虹色橋 |
| `rainbow2` | 虹色橋2 |
| `rainbow3` | 虹色橋3 |
| `b [絵文字名]` | カスタム絵文字をデカ絵文字にします。複数渡せば連結できます|
| `u [絵文字名]` | 絵文字をデカ絵文字にします |

### デレマス
| コマンド | 説明 |
| ------------- | ------------- |
| `ガシャ` | カードがランダムで一枚出力されます（1日一回） |
| `納税` | デレステ版 |
| `奈緒ルーレット` | 奈緒ルーレットを回します |
| `肇ルーレット` | 肇ルーレットを回します |
| `なおはじルーレット` | なおはじルーレットを回します |
| `カード検索 [カード名(部分一致可)]` | モバマスのカードを検索します。複数あった場合は、一覧が表示されます |
| `ユニット検索 [アイドル1] [アイドル2]...` | 指定したアイドルが所属しているユニットをAND検索します。指定人数は1人からです |

### その他
| コマンド | 説明 |
| ------------- | ------------- |
| `ping` | 応答時間を確認します |
| `goodbye` | bot停止コマンドです |

### 画像系
* 画像処理のコマンドは以下の例のようにして入力してください

* !は必要ありません

![コマンド例](https://github.com/allbear/Cyber_Naochang2/blob/read_images/images/screen_shot1.gif)


| コマンド | 説明 | 
| ------------- | ------------- |
| `デレステコラ` | デレステのタイトルロゴをかぶせます |
| `ミリシタコラ` | ミリシタのタイトルロゴをかぶせます |
| `nhk` | nhkのアレをかぶせます |
| `gaming` | 画像をゲーミングにします |
| `elon` | イーロンマスクのアレ |
| `onesin` | おねシンのタイトル |
| `切り抜き` | 画像の透過処理を行います。remove.bgのAPIを使用 |

### 音声系

* 工事中

## 補足
### 予約投稿について
予約投稿はbotのDMを介して行います。

```!予約投稿 y/m/d-H:M チャンネルID```  
というようにコマンドを送信します。
コマンド送信後は、投稿したいメッセージを書き込んでください。

![コマンド例](https://github.com/allbear/Cyber_Naochang2/blob/read_images/images/naosuki.gif)