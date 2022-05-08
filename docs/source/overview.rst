文档概述
--------

与pyETRC的关系
~~~~~~~~~~~~~~

一言以蔽之：pyETRC是本程序作者的前作；qETRC是pyETRC的重构版本。

渊源
^^^^
为了解决pyETRC早期框架设计的缺陷（此为主要）以及Python语言本身在较大项目中所面临的问题，作者于2021年6月开始以C++语言重构pyETRC项目，新项目暂定名为qETRC。自2021年9月底发布1.0.0版本以来，qETRC原则上已经能取代pyETRC，因此推荐pyETRC用户如无特殊需要可升级到qETRC；原pyETRC项目及其文档原则上不再维护。

qETRC在继承了pyETRC几乎全部功能的基础上，支持多线路和路网管理功能，能在路网层次（而不仅仅是单条线路层次）上管理运行图；且新增贪心推线等新功能。
技术上，qETRC重新设计了底层数据结构，重新实现运行图铺画等核心算法，以获得更强的可扩展性。

文件交互
^^^^^^^^
目前pyETRC与qETRC所用文件扩展名默认皆为\ ``*.pyetgr``\ （这实际上是一种具有我们规定结构的\ ``JSON``\ 格式）。\ **在两程序皆支持的范围内**\ ，运行图文件数据完全互联互通互认。

由于Python语言的易扩展性等优点，原pyETRC项目（特别是数据部分）可以用于外部编程，方便地生成本系统所能读取的运行图文件格式。具体请参见\ `pyETRC代码库 <https://github.com/CDK6182CHR/train_graph/>`_\ 。


.. _sec_more:

更多支持
~~~~~~~~

- 本项目发行版所附发行注记\ ``ReleaseNote.pdf``\ 
- 本项目开源库主页\ ``README.md``\ 
- 原pyETRC项目用户文档：https://pyetrc-rtd.readthedocs.io/
- 作者邮箱：mxy0268@qq.com
- 软件交流QQ群：865211882
- B站视频合集《qETRC列车运行图系统》，由软件作者制作，对一些功能或者逻辑的专题讲解为主：https://space.bilibili.com/179545382/channel/collectiondetail?sid=350082&ctype=0  
- 知乎专栏《qETRC开发小记》，软件作者在开发过程中的一些记录，偏向技术，以数据结构、算法说明为主：https://www.zhihu.com/column/c_1410676601487613952
