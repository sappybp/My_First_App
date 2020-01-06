# Thanks_for_Everyone

## アプリケーションの概要。
  - 感謝したくても出来ない人たちが気持ちを匿名で吐けるアプリケーション。
## デプロイ
  - https://thanksapp00001.herokuapp.com/
  - herokuでデプロイしました。（デプロイ時はDBをSQLite3からPostgresqlへ変更。）
  - こちらを参考にしました。: https://qiita.com/croquette0212/items/9b4dc5377e7d6f292671
## テストユーザー
  - メールアドレス: test@gmail.com
  - パスワード: Test0001
## アプリケーションで実装したこと。
  - 新規登録機能
  - ログイン、ログアウト機能(session)
  - アカウントを削除する機能。
  - ユーザー一覧ページの作成。
  - 簡単なマイページ（プロフィール）の作成。
  - プロフィールをアップデートする機能。
  - 感謝を投稿する機能。
  - 感謝一覧ページ作成。
  - 一覧ページのページネーション機能。
  - 管理者アカウントであれば、全ユーザーと、全投稿を削除できる機能。（コードでは、念のため"sample"にしています。）
## 開発環境
  - プログラミング言語はPythonです。
  - フレームワークはFlaskです。
  - データーベースには、SQLite3を使用しました。
  - フロントエンドフレームワークはBootstrap4を使用しています。
## スクリーンショット
  - topページ（背景などを追加しました。下のスクリーンショットも随時最新のものに変えていきます。）
  <img width="1680" alt="スクリーンショット 2019-12-11 9 32 56" src="https://user-images.githubusercontent.com/49954969/70581109-6b58a680-1bf9-11ea-83a7-402644dee9e0.png">

  - topページ（ログイン時）
  <img width="1680" alt="スクリーンショット 2019-12-16 15 47 14" src="https://user-images.githubusercontent.com/49954969/70885154-5c1f9180-201b-11ea-81fc-911960487335.png">

  - 新規登録ページ
  <img width="1221" alt="スクリーンショット 2019-11-15 9 34 54" src="https://user-images.githubusercontent.com/49954969/68908177-db584600-078d-11ea-88a2-0ac572859c3f.png">

  - ログインページ
  <img width="1221" alt="スクリーンショット 2019-11-15 9 34 57" src="https://user-images.githubusercontent.com/49954969/68908153-c5e31c00-078d-11ea-8978-d6436fea8f2e.png">

  - ユーザー一覧ページ
  <img width="1678" alt="スクリーンショット 2019-12-07 4 21 19" src="https://user-images.githubusercontent.com/49954969/70349945-17705980-18a9-11ea-93c7-1c19d26ab4d2.png">

  - 投稿一覧ページ
  <img width="1678" alt="スクリーンショット 2019-12-07 4 15 56" src="https://user-images.githubusercontent.com/49954969/70349620-68cc1900-18a8-11ea-9119-168eb6317cc8.png">

  - メニュー
  <img width="1221" alt="スクリーンショット 2019-11-15 9 36 30" src="https://user-images.githubusercontent.com/49954969/68908122-97fdd780-078d-11ea-851e-a09abe25ef72.png">

  - flashのポップ
  <img width="1109" alt="スクリーンショット 2019-11-15 9 36 09" src="https://user-images.githubusercontent.com/49954969/68908114-87e5f800-078d-11ea-8393-8f5a21f590ca.png">

  - プロフィールページ
  <img width="1221" alt="スクリーンショット 2019-11-15 9 35 50" src="https://user-images.githubusercontent.com/49954969/68908086-73096480-078d-11ea-9ce0-2b3eba04f289.png">

  - ページネーション
  <img width="762" alt="スクリーンショット 2019-12-08 9 54 59" src="https://user-images.githubusercontent.com/49954969/70382659-c5136380-19a2-11ea-9679-0ca12f57728a.png">

  - 管理者マーク
  <img width="1678" alt="スクリーンショット 2019-12-07 3 09 47" src="https://user-images.githubusercontent.com/49954969/70349126-7fbe3b80-18a7-11ea-9adc-a40876d9ef73.png">

  - 管理者のユーザー削除画面
  <img width="1678" alt="スクリーンショット 2019-12-07 3 10 03" src="https://user-images.githubusercontent.com/49954969/70349125-7f25a500-18a7-11ea-81b0-f3b0856ade83.png">

  - 管理者の投稿削除画面
  <img width="1678" alt="スクリーンショット 2019-12-07 3 10 10" src="https://user-images.githubusercontent.com/49954969/70349124-7f25a500-18a7-11ea-8c5d-c5ea622e3f96.png">
