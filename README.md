# VRChat 心率显示

这是一个结合了 **Bluetooth Low Energy (BLE)** 扫描和 **OSC** 消息发送的 Python 项目。它可以扫描附近的 BLE 设备，提取心率数据，并通过 **Open Sound Control (OSC)** 协议将心率数据发送到 **VRChat** 客户端，实现实时显示和控制。

## 功能

- 扫描并连接到符合特定 **公司 ID** 的 BLE 设备。
- 提取 BLE 广告数据中的心率值。
- 将心率数据通过 **OSC** 协议发送到 VRChat。
- 支持实时心率更新。

## 环境要求

- Python 3.x
- 以下 Python 库：
  - **`bleak`**: 用于 BLE 设备扫描
  - **`python-osc`**: 用于 OSC 消息发送

## 安装依赖

你可以通过以下命令安装项目的所有依赖：

~~~bash
pip install -r requirements.txt
~~~

或者直接安装依赖：

~~~bash
pip install bleak python-osc
~~~

## 使用方法
1. **在类似**`zepp lite`软件中打开心率广播和蓝牙广播，然后在手环上启动一个运动，手环设备就会主动广播数据
   

3. **连接到 BLE 设备**  
   启动程序后，它会自动扫描附近的 BLE 设备，并提取符合条件的设备数据（例如带有特定公司 ID 的设备）。程序会检查心率数据，并将其发送到 VRChat 客户端。

4. **启动程序**  
   使用以下命令启动程序：
   
   ~~~bash
   python main.py
   ~~~
   
   程序会持续扫描 BLE 设备并将心率数据发送到 VRChat。

3. **停止扫描**  
   在命令行按 `Ctrl+C` 停止程序。

## 配置

* **VRChat 客户端的 IP 地址和端口** ：  
  默认情况下，程序将数据发送到本地的 VRChat 客户端。你可以修改 `VRCHAT_IP` 和 `VRCHAT_PORT` 变量来适配你的环境。
  
  ~~~python
  VRCHAT_IP = "127.0.0.1"  # VRChat 客户端的 IP 地址
  VRCHAT_PORT = 9000       # VRChat 默认的 OSC 端口
  ~~~
  
* **BLE 设备过滤条件** ：  
  `TARGET_COMPANY_ID` 用于过滤蓝牙设备，仅当设备的公司 ID 与此值匹配时，程序才会提取其数据。

  ~~~python
  TARGET_COMPANY_ID = 0x0157  # 设置要扫描的公司 ID
  ~~~

## 代码结构

* `main.py`：主程序文件，包含 BLE 扫描和 OSC 消息发送逻辑。
* `requirements.txt`：包含所有依赖库的文件。

## 注意事项

* 在使用该程序之前，确保你已在 VRChat 中启用了接收 OSC 消息的功能，并正确配置了 VRChat 客户端的 OSC 服务器地址和端口。
* 该程序通过蓝牙扫描心率数据，需要你确保扫描到符合条件的设备（如带有心率传感器的设备）。

## 常见问题

1. **程序无法识别设备**  
   请确保 BLE 设备在扫描范围内，并且设备的公司 ID 与 `TARGET_COMPANY_ID` 设置一致。

2. **无法连接到 VRChat**  
   请确认 VRChat 客户端正在运行，并且已经配置了正确的 OSC 接收设置。

3. **心率值显示异常**  
   检查蓝牙设备发送的广告数据，确保正确提取了心率信息。可以通过打印日志来调试。

## 许可证

本项目使用 **MIT** 许可证，详情请参见 [LICENSE](LICENSE) 文件。
