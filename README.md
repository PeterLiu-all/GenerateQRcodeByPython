# GenerateQRcodeByPython

用 python 生成二维码，使用 json 文件配置

## 使用方法

```bash
git clone https://github.com/PeterLiu-all/GenerateQRcodeByPython.git
cd GenerateQRcodeByPython
pip install -r requirements.txt
```

```python
import qr
qr_obj = qr.QRgenerater()
qr_obj.ActTransform()
```

或者直接使用 test.py 进行测试

## json 配置文件

该工具使用 json 文件进行配置

- origin:需要解析的二维码文件路径
- words:内置变量，对最终二维码的内容无影响
- picture:使用的二维码背景图片的路径（不含后缀名）
- save_dir:最终生成二维码图片保存路径
- save_name:最终生成二维码图片的名字（不含后缀名）
- ext:背景图片和最终图片的后缀名
- colorized:是否生成彩色图片
- level:精确度('L','M','Q','H')
- version:密集度(<=41)
- contrast:对比度
- brightness:亮度
- if_covered:最终生成图片如果和现有图片重名是否覆盖
- if_pay:是否是微信支付码
- if_parse:是否提供原始二维码进行解析|是否手动输入二维码内容

## 其他说明

由于微信支付码有自己的 api，因此 opencv 需要更新到较高版本才能使用

项目文件夹中亦包含了微信提供的几个识别模型
