# 武侠RPG游戏demo-缅怀武侠泰斗金庸
## 游戏名字：还没想好
##  致武侠
### 赵客缦胡缨 吴钩霜雪明
### 银鞍照白马 飒踏如流星
### 十步杀一人 千里不留行
### 事了拂衣去 深藏功与名
### 闲过信陵饮 脱剑膝前横
### 将炙啖朱亥 持觞劝候嬴
### 三杯吐然诺 五岳倒为轻
### 眼花耳热后 意气素霓生
### 救赵挥金锤 邯郸先震惊
### 千秋二壮士 烜赫大梁城
### 纵死侠骨香 不惭世上英
### 谁能书阁下 白首太玄经
</br>

#机制详解
##1.人物属性篇
### 外功攻击
基础属性，外功攻击可以被格挡，如果被格挡了，则外功伤害降低为原来的10%。
如命中，则使对方减掉相同攻击数值的HP。
### 内功攻击
基础属性，内功攻击无法被格挡，命中率为100%。
可使对方减掉相同攻击数值的HP。
### 外功防御
基础属性，人物被对方外功攻击后，可以按百分比抵扣掉对方的攻击，百分比表示
### 内功防御
基础属性，人物被对方内功攻击后，可以按百分比抵扣掉对方的攻击，百分比表示
### 格挡
基础属性，人物被对方攻击后，可以有几率格挡掉对方的外功攻击（减去90%外功攻击伤害），百分比表示
### 命中
基础属性，人物攻击对方时，命中率=人物命中率-对方的格挡率，百分比表示
### 会心抗性
基础属性，可以降低被对方会心（暴击）的几率，百分比表示
### 会心
基础属性，可以对对方造成暴击伤害，暴击率=人物暴击率-对方的会心抗性，百分比表示
### 会心伤害
基础属性，暴击造成的伤害倍数，用百分比表示。
</br>
### 气海
五维属性之一，根据不同职业，主加成角色的内功攻击，内功防御
### 力道
五维属性之一，根据不同职业，主加成角色的外功攻击，外功防御
### 洞察
五维属性之一，根据不同职业，主加成角色的外功攻击，命中，会心率，会心伤害
### 根骨
五维属性之一，根据不同职业，主加成角色的HP
### 身法
五维属性之一，根据不同职业，主加成角色的会心率，会心抗性，会心伤害
### 人物属性篇总结
一次攻击发起后，需要计算如下内容：<br/>
真实命中率 = 自身命中率 - 对方格挡率<br/>
真实会心率 = 自身会心率 - 对方会心抗性<br/>
真实外功攻击 = 自身外功攻击 * 对方外功防御(0-1)<br/>
真实内功攻击 = 自身内功攻击 * 对方内功防御(0-1)<br/>
<br/>
## 人物装备篇
### 主武器
根据不同门派，有不同的主武器。主武器加成外功攻击，内功攻击，命中率，
会心率，格挡率，会心伤害，五维属性。内功门派主加成内功攻击，外功门派主加成
外功攻击。
### 副武器
同主武器，加成比主武器少20%
### 戒指
通用装备，加成内功攻击，内功防御和五维属性。
### 手镯
通用装备，加成外功攻击，外功防御和五维属性。
### 项链
通用装备，加成会心率，会心伤害，命中，外功攻击，内功攻击。
### 帽子
加成各种防御，加成系数60%（上衣为基准）
### 上衣
加成各种防御，加成系数100%
### 内裤
加成各种防御，加成系数40%
### 下衣
加成各种防御，加成系数70%
### 鞋子
加成各种防御，加成系数60%
### 心法
有N多种心法，每种心法主加成的东西不一样
### 修为
战斗力的综合评估
### 经脉
到达一定的修为后可以打通相应的经脉。
### 气息
修炼获得 可以用于打通经脉，用于研习，升级心法。

### 。。。编不下去了，东西太多，这里写了个大概。具体内容请参阅每个文件的注释


