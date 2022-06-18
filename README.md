# MathAnimation

## Installation
<details><summary>For Mac OS: (https://docs.manim.community/en/stable/installation/macos.html)</summary>

1. Youtubeを参考にインストール-->[Youtube解説](https://youtu.be/EEBCcySkuxA)
3. Pycharmでインタプリタを選択（/opt/homebrew/bin/python3）
4. 必要ならパッケージをインストール
5. Terminal(Pycharmから)上で、manim -pql main.py CreateCircle を実行すると映像が出力される
</details>

<details><summary>For Windows OS: (https://docs.manim.community/en/stable/installation/windows.html)</summary>
  
1. Scoopをインストールするために、PowerShell(管理者権限なしで)を開く
2. Set-ExecutionPolicy RemoteSigned -Scope CurrentUser # Optional: Needed to run a remote script the first time(入力が求められるのでAを入力しエンターを押す)
4. irm get.scoop.sh | iex
5. PowerShellを閉じる
6. コマンドプロンプトを開く
7. scoop install python ffmpeg
8. python -m pip install manim
9. scoop install latex
10. コマンドプロンプトを閉じる
11. Pycharmでプロジェクトの新規作成(既存のインタープリタを選択)
12. C:\\Users\\user\\scoop\\apps\\python\\3.10.5\\python.exeを選択
13. 必要なパッケージをインストール(manim, latex)
14. Terminal(Pycharmから)上で、manim -pql main.py CreateCircle を実行すると映像が出力される
</details>

## Useful Links
[Mobject](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.arrange)  
[Demo1](https://docs.manim.community/en/stable/examples.html)  
[Demo2](https://3b1b.github.io/manim/getting_started/example_scenes.html)  
[Text, Tex, MathTex](https://docs.manim.community/en/stable/tutorials/using_text.html)  

## 色の割り当て(Set Color to Mobject/VGroup)

```py
# 座標軸はVectrolized Mobjectsのグループなので直接的にAxes(color=BLACK)とはできない
ax = Axes(x_range=[-1, 10], y_range=[-1, 10])  
ax.color=BLACK
```

```py
# Mobjectは生成時にcolorを指定することができる
dot = Dot(ax.i2gp(graph.t_min, graph), color=BLUE)
```

```py
# 背景色の変更
class SetBackGroundColor(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
```


## Object Appering
|                                                       |                                      |                                                  |
| :---------------------------------------------------: | :----------------------------------: | :----------------------------------------------: |
|<img width="300" src="https://user-images.githubusercontent.com/95124230/174217020-8a271bbd-6283-478a-8101-a7bbe0001ba5.gif"></br>[Fade In / Out](https://azarzadavila-manim.readthedocs.io/en/latest/animation.html#fade)|<img width="300" src="https://user-images.githubusercontent.com/95124230/174215393-e942fad6-c12f-4d85-bb9c-cabe781a8207.gif"></br>[Fade In / Out and Shift]()|<img width="300" src="https://user-images.githubusercontent.com/95124230/174218309-fd9804de-8529-430d-9e8a-27d3e3407e8e.gif"></br>[Grow from Edge](https://azarzadavila-manim.readthedocs.io/en/latest/animation.html#grow)|
|<img width="300" src="https://user-images.githubusercontent.com/95124230/174218544-ee74746c-6b48-4afb-96d5-bc9cf69a18c0.gif"></br>[Grow from Center](https://azarzadavila-manim.readthedocs.io/en/latest/animation.html#grow)|<img width="300" src="https://user-images.githubusercontent.com/95124230/174218733-39ee3e9d-9638-4b3b-a8f0-fda556f367c4.gif"></br>[Diagonal Directions](https://azarzadavila-manim.readthedocs.io/en/latest/animation.html#diagonal-directions)|<img width="300" src="https://user-images.githubusercontent.com/95124230/174222626-5a04a2f7-298d-45e9-adf0-80c636ce193a.gif"></br>[Create / Unreate](https://azarzadavila-manim.readthedocs.io/en/latest/animation.html#showcreation)|
|<img width="300" src="https://user-images.githubusercontent.com/95124230/174222859-5a95f14a-70d2-4629-bea0-42fc847812ba.gif"></br>[Draw Border Then Fill](https://azarzadavila-manim.readthedocs.io/en/latest/animation.html#drawborderthenfill)|<img width="300" src="https://user-images.githubusercontent.com/95124230/174223074-23fc860f-7c55-4903-bb39-bc12b02fee00.gif"></br>[Increasing Subsets](https://azarzadavila-manim.readthedocs.io/en/latest/animation.html#showincreasingsubsets)|<img width="300" src="https://user-images.githubusercontent.com/95124230/174223274-41d6ffe5-961f-4d86-8357-e04ac2107d58.gif"></br>[Submobjects One by One](https://azarzadavila-manim.readthedocs.io/en/latest/animation.html#showsubmojectsonebyone)|
|<img width="300" src="https://user-images.githubusercontent.com/95124230/174224958-5597af91-fdef-4a4c-99e2-b5d2d48521b3.png"></br>[Add](https://azarzadavila-manim.readthedocs.io/en/latest/animation.html#)| | |

<br>

## Text Appering
|                                                       |                                      |                                                  |
| :---------------------------------------------------: | :----------------------------------: | :----------------------------------------------: |
|<img width="300" src="https://user-images.githubusercontent.com/95124230/174223512-b03b9ff9-dd4b-4016-9e8a-691744c83b96.gif"></br>[Write](https://azarzadavila-manim.readthedocs.io/en/latest/animation.html#write)|<img width="300" src="https://user-images.githubusercontent.com/95124230/174223787-b9cdeb6b-f90e-45b1-81fc-7baf910e638f.gif"></br>[Add Text Word by Word](https://azarzadavila-manim.readthedocs.io/en/latest/animation.html#addtextwordbyword)| |

<br>

## Movement
|                                                       |                                      |                                                  |
| :---------------------------------------------------: | :----------------------------------: | :----------------------------------------------: |
|<img width="300" src="https://user-images.githubusercontent.com/95124230/174224486-37bfd010-f0c5-453e-a665-76bb216e01c6.gif"></br>[Move to Target](https://azarzadavila-manim.readthedocs.io/en/latest/animation.html#movetotarget)|<img width="300" src="https://user-images.githubusercontent.com/95124230/174225185-fd978ff2-9e38-4511-a1ee-07e2e0071c62.gif"></br>[Scale in Place](https://azarzadavila-manim.readthedocs.io/en/latest/animation.html#scaleinplace)|<img width="300" src="https://user-images.githubusercontent.com/95124230/174225341-22d593e8-7919-4d1e-8ac6-76da81f8abb9.gif"></br>[Shrink to Center](https://azarzadavila-manim.readthedocs.io/en/latest/animation.html#shrinktocenter)|
|<img width="300" src="https://user-images.githubusercontent.com/95124230/174225513-6a2fb5e5-b0f9-4070-82b0-83632928b852.gif"></br>[Apply Matrix](https://azarzadavila-manim.readthedocs.io/en/latest/animation.html#applymatrix)|<img width="300" src="https://user-images.githubusercontent.com/95124230/174225845-ec3cab88-091f-44d9-b81f-8478f4f64e24.gif"></br>[Complex Function](https://azarzadavila-manim.readthedocs.io/en/latest/animation.html#applycomplexfunction)|<img width="300" src="https://user-images.githubusercontent.com/95124230/174225978-559688c4-9eee-461c-8fa3-913f6f49e516.gif"></br>[Cyclic Replace](https://azarzadavila-manim.readthedocs.io/en/latest/animation.html#cyclicreplace)|
|<img width="300" alt="Swap"></br>[Swap](https://azarzadavila-manim.readthedocs.io/en/latest/animation.html#swap)| | |




