# Thanks_for_Everyone

## アプリケーションの概要。
  - 感謝したくても出来ない人たちが気持ちを匿名で吐けるアプリケーション。
## デプロイ
  - https://thanksapp00001.herokuapp.com/
  - herokuでデプロイしました。（デプロイ時はDBをSQLite3からPostgreSQLへ変更。）
  - こちらを参考にしました。: https://qiita.com/croquette0212/items/9b4dc5377e7d6f292671
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
  - 投稿、ユーザーを削除できる管理者を作りました。（管理者はマークがつきます。）
## 開発環境
  - プログラミング言語はPythonです。
  - フレームワークはFlaskです。
  - データーベースには、SQLite3を使用しました。(デプロイ時には、PostgreSQL)
  - Bootstrap
## スクリーンショット
  - topページ
  <img width="1256" alt="スクリーンショット 2019-11-15 9 39 36" src="https://user-images.githubusercontent.com/49954969/68908203-ee6b1600-078d-11ea-86a9-35cf71473f95.png">
  
  - topページ（ログイン時）
  <img width="1221" alt="スクリーンショット 2019-11-15 9 36 26" src="https://user-images.githubusercontent.com/49954969/68908225-ffb42280-078d-11ea-9cfc-7c3fb0b23dcc.png">
  
  - 新規登録ページ
  <img width="1221" alt="スクリーンショット 2019-11-15 9 34 54" src="https://user-images.githubusercontent.com/49954969/68908177-db584600-078d-11ea-88a2-0ac572859c3f.png">
  
  - ログインページ
  <img width="1221" alt="スクリーンショット 2019-11-15 9 34 57" src="https://user-images.githubusercontent.com/49954969/68908153-c5e31c00-078d-11ea-8978-d6436fea8f2e.png">
  
  - ユーザー一覧ページ
  <img width="1221" alt="スクリーンショット 2019-11-15 9 36 46" src="https://user-images.githubusercontent.com/49954969/68908133-ac41d480-078d-11ea-9a88-cc0d9e5d7c9e.png">
  
  - メニュー
  <img width="1221" alt="スクリーンショット 2019-11-15 9 36 30" src="https://user-images.githubusercontent.com/49954969/68908122-97fdd780-078d-11ea-851e-a09abe25ef72.png">

  - flashのポップ
  <img width="1109" alt="スクリーンショット 2019-11-15 9 36 09" src="https://user-images.githubusercontent.com/49954969/68908114-87e5f800-078d-11ea-8393-8f5a21f590ca.png">
  
  - プロフィールページ
  <img width="1221" alt="スクリーンショット 2019-11-15 9 35 50" src="https://user-images.githubusercontent.com/49954969/68908086-73096480-078d-11ea-9ce0-2b3eba04f289.png">

  - 管理者マーク
  <img width="1678" alt="スクリーンショット 2019-12-07 3 09 47" src="https://user-images.githubusercontent.com/49954969/70345556-af694580-189f-11ea-943e-fa5ef28129a2.png">
  
  - 投稿削除
  <img width="1678" alt="スクリーンショット 2019-12-07 3 10 10" src="https://user-images.githubusercontent.com/49954969/70345637-da539980-189f-11ea-91df-0854da0e2565.png">

  
  - ユーザー削除
  <img width="1678" alt="スクリーンショット 2019-12-07 3 10 03" src="https://user-images.githubusercontent.com/49954969/70345607-cad45080-189f-11ea-9280-dd92ee3a37d8.png">
  
