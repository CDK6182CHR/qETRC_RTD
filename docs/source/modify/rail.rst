线路数据调整
~~~~~~~~~~~~~

线路反排
^^^^^^^^^

:起始版本: V1.0.0
:最新修订: V1.2.4
:工具栏: :guilabel:`线路工具(8)` 上下文页面 | :guilabel:`线路反排`
:pyETRC对应功能: 线路反排

在说明反排运行图的功能前，有必要再强调一下本系统的上下行逻辑。在本系统中，总是以下行为主方向，即要求线路信息的车站排列顺序、里程递增方向、对里程递增方向（虽然对里程的意义是上行线里程，但仍然要求按下行方向递增）都是下行方向。参见 :ref:`线路基本概念<sec_rail_basic>` 。

在实际的操作中，有时候可能确实需要反排运行图，例如需要将当前线路以一段的身份加入到另一运行图中，或者确实排反了。此时可以使用本功能。

此功能完成的操作有：

* 将线路信息中的车站反序排列，并以终点里程为0点、反向地重新计算里程和对里程数据。
* 将对里程与里程数据交换。如果本来没有对里程数据，则新的里程数据就是原来的里程数据。
* 将所有车站的单向站性质取反。就是说，上行通过站变为下行通过站，反之亦然。

在V1.2.4版本中，修正了一些由本功能导致的错误。


.. note::
    与pyETRC不同，由于qETRC是多线路的，原则上和概念上列车并不与某一特定线路绑定，因此线路反排操作 **不会** 交换列车的上下行车次。

.. note::
    对于原来缺失对里程数据的站，反排后对里程和里程数据都是原来的里程数据。也就是说，连续两次反排得到的效果并不是原始运行图，而是可能多了一些对里程数据。

.. warning::
    再次提醒，系统上的行别和线路实际行别不同会导致一些反直觉的情况。因此，尽量让系统上的行别和实际线路行别保持一致。

线路拼接
^^^^^^^^^

:起始版本: V1.2.5
:工具栏: :guilabel:`线路工具(8)` 上下文页面 | :guilabel:`线路拼接`
:pyETRC对应功能: 线路拼接

此功能支持将两条线路首尾相接拼接成新的线路。

.. figure:: /_static/img/modify/rail-conj.png 
    :alt: 线路拼接-V1.3.2

具体操作层面，是以当前线路A为主（即当前所操作的线路，显示在工具栏\ :guilabel:`线路工具(8)`\ 上下文页面中的 ``当前线路`` 栏目），另外选择一条线路B（如上图所示），将新选择的线路B的车站信息添加到线路A中。线路B不会被修改。可以选择将线路B放置在线路A之前或者之后，也可以选择同时反排当前线路（线路A）。注意：

* 线路A与线路B合并方向应存在 **一个** 公共站点，否则里程无法正确计算。
* 仅能将线路B的车站数据引入线路A，暂不支持引入标尺、天窗数据。

.. note::
    与pyETRC不同（由于线路相关的底层逻辑和实现有较大变化），此功能需从当前运行图中存在的线路中拼接，而不是从外部文件中选择（自然，也不会导入外部文件中的车次）。如需引入外部文件的线路，请先将其中的线路导入当前运行图 （参见 :ref:`导入线路<sec_import_rail>` ）。

全局站名修改
^^^^^^^^^^^^^

:起始版本: V1.0.0
:pyETRC对应功能: 修改站名
:快捷键: :guilabel:`Ctrl` + :guilabel:`U`
:工具栏: :guilabel:`开始(1)` | :guilabel:`更改站名`

这是一个自pyETRC早期版本开始就存在的经典功能。严格来说，这并不只是线路调整的功能，而是同时作用于线路和列车的。

考虑以下场景。在已经铺画的运行图中，（因为某种原因）需要将一个车站站名修改为其他名称。此时如果直接在 :ref:`基线编辑<sec_rail_basic>` 中修改站名，则很可能导致已经与此站绑定的列车时刻表数据无法匹配，从而无法铺画该站的数据。如果要手工修改所有列车时刻表中的车站站名，则过于繁琐，因此提供本功能，自动修改线路站名、时刻表站名中的匹配者。

.. figure:: /_static/img/modify/change-station-name.png 
    :alt: 修改站名-V1.3.2

在上图所示的界面中，只要输入原站名和新站名，点击确定，即可执行。

 
.. note::
    由于线路数据结构的变化（技术细节参见 `知乎文章 <https://zhuanlan.zhihu.com/p/400406858>`_ ），qETRC中使用基线编辑功能单独修改车站站名（不同时进行增删车站、调序操作），标尺、天窗数据不会受到影响。在pyETRC中，若进行此操作，则相关区间的标尺、天窗数据将丢失。


合并标尺
^^^^^^^^^

:起始版本: V1.0.5
:最新更新: V1.1.7
:pyETRC对应功能: 合并标尺
:工具栏: :guilabel:`标尺管理(9)` 上下文页面 | :guilabel:`合并标尺`

此功能支持将 **同一线路** 下的两个不同标尺数据合并。具体操作是，以当前标尺（标尺A）为主，另外选择标尺（标尺B），将标尺B的所有数据合并到标尺A中。标尺B不会被修改，也不会被自动删除。对于重复数据，提供一个选项（如下图），如勾选则使用标尺B数据覆盖标尺A的同区间数据，否则保持标尺A的相应数据不变。

此处的“重复数据”是指，关于线路上的一个区间，标尺A、B同时提供了非空的数据。

.. note::
    标尺数据“非空”是指该区间的通通时分和起停附加时分三者有至少一个非零。反之，若三者皆为零，则认为该区间没有数据。此标准同样适用于按标尺铺画运行图。

.. figure:: /_static/img/modify/merge-ruler.png 
    :alt: 标尺合并-V1.3.2




