# 飞机大战
# v1
- 主要作为技术验证
- 画出一个舞台,包括背景,包括一个小飞机

# v2
- 小蜜蜂会动,从上往下慢慢的飞
- 能控制小蜜蜂左右移动
- 入场算法
    - y轴要求是负数,这样会形成慢慢入场的效果, y = 0 - bee.height
    - x轴要求有一定富余,即要求蜜蜂等移动不能紧贴着边,比如富余是50
        基本上x轴的值应该是50起,最右边的计算方式应该 world.width - bee.width - 50
- 移动速度问题
   -包含x,y两个值
   - 对于绝大多数舞台,则只考虑y值
   - 但是,蜜蜂和英雄是特例
   - 蜜蜂是从上向下移动的同时具有横向运动
   - 英雄的移动有上下左右键盘控制
   - 速度应该是一个tuple=(x,y)
    
- 方向问题
   - 具体移动方向有x,y控制
   - 值只能是 -1, 0, 1三个就好
   - 应该是一个tuple
   - 例如 (-1, 0)表示水平向左移动
   - (0, 1)表明向下垂直运动

# v3
- 重构代码,使用oop方法
    - 世界的构成
        - 小飞机
        - 大飞机
        - 小蜜蜂
        - 子弹
        - 英雄机
        - 天空
    - 配置文件
        - 可以通过一次性配置来让程序正确运行
        - 降低了代码软件工程方面的成本
        - python的配置文件包: configparser
            - 以前叫ConfigParser
            - 配置文件一般以cfg或者ini结尾
            - 语法:
                - 中括号: 表示的是section
                - 每个section下是键值对
                - 键值对用等号或者冒号链接
            - get(section_name, key_name),返回相应的值
            - getint(section_name, key_name), 返回相应的整数值
            
                
        
- 在oop的基础上创建小飞机,蜜蜂等,相对简单很多
- 程序可以正常产生飞行物,包括英雄,子弹,云星等

# v03
- 1. Find some objects
    - SmallPlane
    - Bee
    - BigPlane
    - Bullet
    - Hero
    - Sky
    - PlanWar
    
- 2. BaseClass
      - Img, and some functions
      - Position,  fly into screen with position(x, 0-height)
      - move
     
- 3. SubClass
    - Bee
    - SmallPlane
    - BigPlane
    - Sky
    - Bullet
    - Hero
  
# v4 - 实现碰撞检测
- 碰撞检测算法是游戏通过算法,必须掌握
- 一旦判断发生碰撞
    - 生命值会发生改变
    - 生命状态发生改变
        - life_status_live
        - life_status_dead : 已经发生碰撞,播放死亡画面
        - life_status_removable : 可以移除
    - 如果生命状态为dead,则播放死亡动画

- 在处理小飞机的时候
    - 初始化的时候吧五张图片全部初始化完毕,放入list中
    - 考虑到资源的消耗,图片保存成类变量(所谓静态变量)
    - 正常播放的是第一张图片,一旦中单,则连续播放其余四张图片
    
- 游戏状态
    - READY : 游戏没有开始,显示一张准备图片
    - RUNNING : 正常游戏运行
    - DONE : gameover,显示结束图片,注意游戏停止循环运行
    
- 游戏分数:
    - 一个变量, 每次碰撞后检测对方身份,如果是子弹撞击对方,则直接根据敌人类型更改分数
    - 把分数提示显示在屏幕上
    
   

    
    