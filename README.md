# ロボットシステム学　ROS
--------

## 概要
ROSの理解を深めるために、1から1000までを繰り返しカウントし続けるプログラムと、カウントした数値を受け取り、その数値の偶数を全て0に変換するプログラムを作成した。

--------

## 使用機器
・Raspberry Pi4

--------

## 環境
・Ubuntu 20.04 server
・ROS noetic

--------

## ROS 環境構築
以下のリンクのリポジトリの指示に従い、ROSの環境を構築する。
https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_server.git

--------

## プログラムの実行方法
        
        $ cd scripts                  //scriptsに移動する
        
        $chmod +x count.py            //count.pyに実行権限を与える
        
        $chmod +x gusu0.py            //gusu0.pyに実行権限を与える
        
        //ここで新しく端末を3つ開く
        
        $roscore                      //ROSを立ち上げる（1つ目の端末で行う）
        
        $rosrun mypkg count.py        //count.pyのプログラムを実行する（2つ目の端末で行う）
        
        $rosrun mypkg gusu0.py        //gusu0.pyのプログラムを実行する（3つ目の端末で行う）
        
        $rostopic echo /gusu0         //gusu0のプログラムの実行状況を表示する（最初に使っていた端末で行う）
        
--------

## 実行動画
https://youtu.be/uW_VJhfp46Q

--------

## ライセンス
