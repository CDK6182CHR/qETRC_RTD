安装与构建
----------

使用发行版安装
~~~~~~~~~~~~~~

对于普通用户在64位Windows操作系统上使用本程序，推荐直接采用发行版安装程序。可在下列地址获得发行版程序包：

- Github: https://github.com/CDK6182CHR/qETRC/releases
- Gitee: https://gitee.com/xep0268/qETRC/releases

首次安装请下载完整版程序，通常命名为 ``qETRC-win64_Vx.x.x_Rxx_xxxxx.7z`` 。下载后直接解压，无需安装，运行 ``qETRC.exe`` 即可。亦可自行创建快捷方式放到方便的位置。

对于已安装旧版本的用户，可以下载补丁包，通常命名为 ``qETRC-win64-patch_Vx.x.x_Rxx_xxxxx.7z`` 。下载解压后将压缩包内文件复制到程序目录，覆盖原有文件即可。

.. important::
    自V1.4.0版本起，发行的win64版本不再支持Windows 7及以下操作系统。

.. note::
    如果提示缺少\ ``msvc*.dll``\ 文件，请安装MSVC运行时库，下载地址：https://aka.ms/vs/17/release/vc_redist.x64.exe 


.. note::
    请注意部分发行版可能会指定支持使用补丁包升级的最低版本，或者指明支持库版本更新。如果使用补丁包后无法正常运行程序，请改用最新完整版程序包。


.. attention::
    程序所在目录有一些文件可能包含用户数据，如果需要覆盖，请慎重考虑是否包含重要修改。

    - ``CRPassengerMileage.pyetlib`` 为内置默认线路数据库。如果修改过线路数据库，默认保存在此文件中。
    - ``config.json`` 为用户设置文件。如果产生了此文件，通常是因为用户更改了默认设置，例如默认情况下的运行图显示比例等。
    - ``system.json`` 为系统自动产生的文件，包含打开文件的历史记录等信息。


从源代码构建
~~~~~~~~~~~~

桌面版
^^^^^^

如果希望修改或自行构建本程序，这里给出简单的提示。如有第三方库依赖问题，请查看报错信息自行解决。
构建本程序至少需要 ``Qt5`` 和 ``C++20`` 。自V1.4.0版本起，发行的win64版本采用Qt6构建，并采用C++20标准。Win64发行版采用以下构建环境：

- ``Qt 6.5.1`` ``MSVC 2019`` 

在以下IDE中已经成功构建过本项目：

- ``Visual Studio 2019 Community``
- ``QtCreator 4.15.1``

本项目依赖于第三方库 `SARibbon <https://gitee.com/czyt1988/SARibbon/>`_ 和 `Qt-Advanced-Docking-System <https://github.com/githubuser0xFFFF/Qt-Advanced-Docking-System/>`_ 。

自V1.3.7版本的发行版开始，本项目改用 ``CMake`` 构建。原基于 ``qmake`` 的构建系统不再支持。

.. 下载好这两个支持库后，分别构建得到 ``*.lib`` 和 ``*.dll`` 库文件。请将项目目录 ``dependencies`` 下的对应 ``pri`` 文件中所示的库位置修改为实际所在位置，然后将构建所得的 ``*.lib`` 和 ``*.dll`` 文件复制到项目目录 ``lib`` 子目录下对应的位置，然后构建程序即可。

移动版
^^^^^^

移动版不需要以上支持库。只需要选择好构建套件，直接构建即可。

.. note::
    移动版构建环境必须定义 ``QETRC_MOBILE`` 和 ``QETRC_MOBILE_2`` 两个宏。目前的 ``qETRC.pro`` 中仅考虑了了Android的情况。
    如需构建移动版到其他平台，请自行修改 ``qETRC.pro`` 文件。


