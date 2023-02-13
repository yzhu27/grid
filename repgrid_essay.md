# Essay


我们找到了三个对汽车行业有兴趣和一定知识了解的受访者,采访他们对于不同型号车辆的认知情况.
## Our scale
我们的grid选择了六个方面评估车辆型号:
- 使用体验方面:偏向家庭出行还是个人驾驶
- 驾乘舒适度方面:偏向乘坐舒适还是驾驶反馈
- 内饰方面:偏向传统机械内饰还是现代科技内饰
- 二手市场方面:偏向高保值率还是高周转率
- 消费群体方面:偏向年轻消费者还是年长消费者
- 油耗方面:偏向低油耗还是短百公里加速时间
## Our Car Makes
我们的grid选择了六种受访者感兴趣的车型:
- Audi A7
- Land Rover Range Rover
- Lexus IS350
- BMW M3
- Mazda MX-5 Miata
- Tesla Model Y
## Scores from interview

#### Interviewee 1
|          1 score | Model 1 |        Model 2         |   Model 3   | Model 4 |     Model 5      |    Model 6    | 5 score          |
| ---------------: | :-----: | :--------------------: | :---------: | :-----: | :--------------: | :-----------: | :--------------- |
| FamilyExperience |    4    |           2            |      1      |    3    |        5         |       2       | DriveExperience  |
|  RideComfortable |    4    |           5            |      1      |    4    |        5         |       3       | DriveComfortable |
|  ClassicInterior |    3    |           1            |      2      |    2    |        1         |       5       | TechInterior     |
| ValuePreservable |    2    |           4            |      1      |    4    |        5         |       2       | HighTurnover     |
|       YoungBuyer |    2    |           4            |      4      |    1    |        1         |       3       | ElderBuyer       |
|   HighGasMileage |    1    |           3            |      4      |    3    |        4         |       5       | Quick0-60Time    |
|                  | Audi A7 | Land Rover Range Rover | Lexus IS350 | BMW M3  | Mazda MX-5 Miata | Tesla Model Y |                  |

#### Interviewee 2
|          1 score | Model 1 |        Model 2         |   Model 3   | Model 4 |     Model 5      |    Model 6    | 5 score          |
| ---------------: | :-----: | :--------------------: | :---------: | :-----: | :--------------: | :-----------: | :--------------- |
| FamilyExperience |    5    |           1            |      3      |    5    |        5         |        4      | DriveExperience  |
|  RideComfortable |    4    |           1            |      3      |    4    |        4         |        5      | DriveComfortable |
|  ClassicInterior |    2    |           4            |      3      |    4    |        1         |        5      | TechInterior     |
| ValuePreservable |    4    |           4            |      1      |    2    |        2         |        3      | HighTurnover     |
|       YoungBuyer |    1    |           5            |      2      |    1    |        1         |        2      | ElderBuyer       |
|   HighGasMileage |    5    |           1            |      3      |    4    |        4         |        5      | Quick0-60Time    |
|                  | Audi A7 | Land Rover Range Rover | Lexus IS350 | BMW M3  | Mazda MX-5 Miata | Tesla Model Y |                  |


#### Interviewee 3

|          1 score | Model 1 |        Model 2         |   Model 3   | Model 4 |     Model 5      |    Model 6    | 5 score          |
| ---------------: | :-----: | :--------------------: | :---------: | :-----: | :--------------: | :-----------: | :--------------- |
| FamilyExperience |    4    |           2            |      3      |    5    |        4         |       3       | DriveExperience  |
|  RideComfortable |    4    |           3            |      3      |    5    |        4         |       4       | DriveComfortable |
|  ClassicInterior |    3    |           3            |      3      |    4    |        2         |       5       | TechInterior     |
| ValuePreservable |    3    |           3            |      2      |    4    |        4         |       3       | HighTurnover     |
|       YoungBuyer |    1    |           4            |      3      |    1    |        2         |       3       | ElderBuyer       |
|   HighGasMileage |    4    |           3            |      3      |    5    |        4         |       5       | Quick0-60Time    |
|                  | Audi A7 | Land Rover Range Rover | Lexus IS350 | BMW M3  | Mazda MX-5 Miata | Tesla Model Y |                  |

## Results

#### Attributes Clusters

##### Interviewee 1

```
75
|.. 48
|.. |.. ValuePreservable:HighTurnover
|.. |.. 36
|.. |.. |.. FamilyExperience:DriveExperience
|.. |.. |.. RideComfortable:DriveComfortable
|.. 55
|.. |.. ClassicInterior:TechInterior
|.. |.. 64
|.. |.. |.. YoungBuyer:ElderBuyer
|.. |.. |.. HighGasMileage:Quick0-60Time
```

##### Interviewee 2

```
69
|.. 58
|.. |.. ValuePreservable:HighTurnover
|.. |.. 57
|.. |.. |.. ClassicInterior:TechInterior
|.. |.. |.. YoungBuyer:ElderBuyer
|.. 22
|.. |.. FamilyExperience:DriveExperience
|.. |.. 10
|.. |.. |.. RideComfortable:DriveComfortable
|.. |.. |.. HighGasMileage:Quick0-60Time
```
##### Interviewee 3

```
74
|.. 60
|.. |.. ValuePreservable:HighTurnover
|.. |.. 46
|.. |.. |.. HighGasMileage:Quick0-60Time
|.. |.. |.. FamilyExperience:DriveExperience
|.. 76
|.. |.. YoungBuyer:ElderBuyer
|.. |.. 49
|.. |.. |.. RideComfortable:DriveComfortable
|.. |.. |.. ClassicInterior:TechInterior
```



#### Model Clusters

##### Interviewee 1

```
85
|.. 54
|.. |.. Lexus_IS350
|.. |.. 66
|.. |.. |.. Land_Rover_Range_Rover
|.. |.. |.. Tesla_Model_Y
|.. 47
|.. |.. Mazda_MX-5_Miata
|.. |.. 30
|.. |.. |.. Audi_A7
|.. |.. |.. BMW_M3
```

##### Interviewee 2

```
63
|.. 36
|.. |.. Lexus_IS350
|.. |.. 31
|.. |.. |.. Mazda_MX-5_Miata
|.. |.. |.. BMW_M3
|.. 80
|.. |.. Land_Rover_Range_Rover
|.. |.. 38
|.. |.. |.. Audi_A7
|.. |.. |.. Tesla_Model_Y
```

##### Interviewee 3

```
82
|.. 47
|.. |.. Lexus_IS350
|.. |.. 57
|.. |.. |.. Audi_A7
|.. |.. |.. Land_Rover_Range_Rover
|.. 50
|.. |.. BMW_M3
|.. |.. 54
|.. |.. |.. Tesla_Model_Y
|.. |.. |.. Mazda_MX-5_Miata
```


#### Matrix

```
A	Audi_A7
B	Land_Rover_Range_Rover
C	Lexus_IS350
D	BMW_M3
E	Mazda_MX-5_Miata
F	Tesla_Model_Y
```
##### Interviewee 1

```
{C                               E        }
{                                         }
{                                         }
{                        D                }
{                                         }
{                  A                      }
{                                         }
{              B                          }
{          F                              }
```

##### Interviewee 2

```
{C                       B                }
{                                         }
{                                         }
{                                         }
{                                         }
{                                         }
{D                                        }
{E                                        }
{                                         }
{F                                        }
{A                                        }
```

##### Interviewee 3

```
{C                               D        }
{                                         }
{                A                        }
{                                         }
{                                         }
{B                 E                      }
{                  F                      }
```

## Analysis

#### Attributes Clusters
从聚类结果可以看出, 三位受访者都将保值率作为一个与其他attributes有明显差异的attribute. 其他attributes很难看出在所有数据中都具有相似性,因此我们可以认为我们的attributes设置较好,保证各attribute之间的相似性不大.

#### Model Clusters
从聚类结果可以看出, Lexus IS350是最有特点的一款车,所有受访者都使它在聚类中体现了明显划分. 此外受访者2相较于其他两个受访者在评分上没有很强的区分度. Audi A7, BMW M3与Mazda MX-5 Miata在三个受访者的认知中都比较相似,这可能是它们在市场上的定位都是运动型轿跑/跑车的原因.

#### Matrix

从矩阵结果可以看出, 车辆C在所有受访者的评分中都在类似的位置,体现了明显的独特性. 受访者2的矩阵相较于其他两个受试者缺乏一定的区分性. 此外例如车辆E和F在受访者2和3的认知中差异较小, 车辆D和E在受访者1和2的认知中差异较小. 这体现了在不同车辆款式之间不同的受访者都有不同的认知, 但他们对车辆C都有一致的意见.