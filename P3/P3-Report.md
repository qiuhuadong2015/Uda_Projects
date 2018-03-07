## 可视化探索电影市场

#### 背景及问题

你是一名业务分析师顾问，你的客户是一个电影制作新公司，他们将制作一部新电影。客户想确保电影能成功，从而使新公司立足市场。他们希望你能帮助他们了解电影市场趋势，使他们能做出正确的决策。他们提供了指导，希望你能研究以下三大领域：

- **问题 1：**电影类型是如何随着时间的推移发生变化的？
- **问题 2：** Universal Pictures 和 Paramount Pictures 之间的对比情况如何？
- **问题 3：** 改编电影和原创电影的对比情况如何？(通过keywords变量中的based on novel字段来判断)

更重要的是，客户请你根据提供的数据，额外回答第四个问题。

#### 第四个问题

为了帮助了解电影趋势，这里从观众的角度考虑怎样的电影是受欢迎的，因此选择评分值和流行度（观看数）作为分析变量，提出第四个问题：

- **问题 4：**根据电影的评分和流行程度推荐一些值得参考学习的电影？

#### 研究变量

- release_year 发行年份
- vote_average 评分值
- popularity 流行度（观看数）
- budget_adj 成本
- revenue_adj 收入

#### 回答及链接

- **问题 1：**电影类型是如何随着时间的推移发生变化的？

  - 在线面板链接为 [Tableau Public Q1](https://public.tableau.com/profile/.10216883#!/vizhome/P3-Lab/Q1)

  ![屏幕快照 2018-03-07 下午10.48.23](/Users/qiuhuadong/Desktop/屏幕快照 2018-03-07 下午10.48.23.png)

  ![屏幕快照 2018-03-07 下午10.49.16](/Users/qiuhuadong/Desktop/屏幕快照 2018-03-07 下午10.49.16.png)

  - 如图《Q1-各风格利润随时间变化》，假设 2 亿为高利润的标准，筛选 2 亿利润以上的电影进行分析
  - 发现历史上平均利润最高的是 Animation 风格电影，该风格电影利润不断下降，自 1992 年后没有再超过 2 亿
  - Western 风格电影在 1974 - 1998 年利润稳定在 2亿多，但也逐渐下降，之后也没有再超过 2 亿
  - 该图体现早期利润较高的几个风格电影，利润都在不断减少，体现的趋势是电影市场的竞争越来越大

    ![屏幕快照 2018-03-07 下午11.43.56](/Users/qiuhuadong/Desktop/屏幕快照 2018-03-07 下午11.43.56.png)
  - 如图《Q1-个风格电影数》，可发现电影数增长最多的前三名分别是 Drama、Thriller 和 Comedy 风格


- **问题 2：** Universal Pictures 和 Paramount Pictures 之间的对比情况如何？

  - 在线面板链接为[Tableau Public Q2](https://public.tableau.com/profile/.10216883#!/vizhome/P3-Lab/Q2)

    ![屏幕快照 2018-03-07 下午11.54.46](/Users/qiuhuadong/Desktop/屏幕快照 2018-03-07 下午11.54.46.png)

  - 如上图《Q2-流行度》和《Q2-评分》，可发现两个公司的电影评价流行度、平均评分差不多，Paramount Pictures 的评价略高于 Universal Pictures 一点

  ![屏幕快照 2018-03-07 下午10.03.56](/Users/qiuhuadong/Desktop/屏幕快照 2018-03-07 下午10.03.56.png)

  ![屏幕快照 2018-03-07 下午10.33.30](/Users/qiuhuadong/Desktop/屏幕快照 2018-03-07 下午10.33.30.png)

  - 如图《Q2-两公司对比各年利润》，选择近三年来两公司的利润进行对比
  - 发现 Paramount Pictures 公司三年的每年利润和都不如 Universal Pictures 公司
  - 13 年、14 年 Paramount Pictures 公司的平均利润虽然高于 Universal Pictures 公司，但总利润不如 Universal Pictures 公司，可推断 Universal Pictures 公司实现总利润高的原因是发行电影数量更多
  - 该数据体现，公司想实现更高的总利润，不一定依靠每个电影有很高的利润，还可以通过发行更多电影的策略来实现目标



- **问题 3：** 改编电影和原创电影的对比情况如何？(通过keywords变量中的based on novel字段来判断)

  - 在线面板链接为[Tableau Public Q3](https://public.tableau.com/profile/.10216883#!/vizhome/P3-Lab/Q3)

  ![屏幕快照 2018-03-07 下午10.04.14](/Users/qiuhuadong/Desktop/屏幕快照 2018-03-07 下午10.04.14.png)

  - 如图《Q3-各风格改编原创对比评价所示》，可以发现大部分风格的电影都是改编电影评价（流行度、评分）均比原创电影高
  - 少数风格是原创电影的流行度高、改编电影评分高
  - 少数风格是改编电影流行度高、原创电影评分高
  - 只有 Forign 和 TV movie 两种风格的电影是改编电影的评价均比原创电影略低
  - 只有 Documentary 风格还没有发行过改编电影
  - 总体上看，改编电影的成本、收入、利润都要高于原创电影


- **问题 4：**根据电影的评分和流行程度推荐一些值得参考学习的电影？
  - 在线面板链接为[Tableau Public Q4](https://public.tableau.com/profile/.10216883#!/vizhome/P3-Lab/Q4) 和 [Tableau Public Q4 Story](https://public.tableau.com/views/P3-Lab/Q4Story?:embed=y&:display_count=yes&publish=yes)
  ![屏幕快照 2018-03-07 下午10.04.56](/Users/qiuhuadong/Desktop/屏幕快照 2018-03-07 下午10.04.56.png)
  - 如图《Q4-最高电影评价》所示，综合流行度和评分作为评价指标，发现《Jurassic World》、《Mad Max: Fury Road》和《Interstellar》是综合评价最高的三部电影
  ![屏幕快照 2018-03-07 下午10.35.55](/Users/qiuhuadong/Desktop/屏幕快照 2018-03-07 下午10.35.55.png)
  - 如上图所示，综合流行度和评分作为评价指标，发现 Animation、War、Crime 是综合评价最高的三种电影风格
  ![屏幕快照 2018-03-07 下午10.05.34](/Users/qiuhuadong/Desktop/屏幕快照 2018-03-07 下午10.05.34.png)
  - 如上图所示，在综合评价最高的三种电影风格中，进一步找出了综合评价最高的五部电影《Furious 7》、《Big Hero 6》、《The Dark Knight》、《The imitation Game》和《Pulp Fiction》
  ![屏幕快照 2018-03-07 下午10.05.46](/Users/qiuhuadong/Desktop/屏幕快照 2018-03-07 下午10.05.46.png)
  - 如上图所示，将找到的 8 部优秀电影进行利润分析，发现每一部电影利润都超过 2 亿，可认为都是高利润的电影
  - 不管是在所有风格中找到的前 3 名电影，还是在优秀风格中找到的前 5 名电影，在利润上都有相同数量级的电影
  - 该数据体现了即使不是评价最好的电影，在利润上也有机会达到评价最好的电影的水平，而以上电影则都值得学习参考



