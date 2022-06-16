import os
from typing import Dict
from MyQR import myqr
import cv2
import json


class QRgenerater:
    def __init__(self, cfg: str = "QRconfig.json") -> None:
        """初始化

        Args:
            cfg (str, optional): 配置文件名. Defaults to "QRconfig.json".
        """
        self.__cfgFile: str = cfg
        self.__config: Dict[(str, str)] = {}

    def _readConfig(self) -> None:
        """读取并解析json配置文件
        """
        try:
            with open(self.__cfgFile, "r") as js:
                self.__config = json.load(js)
        except FileNotFoundError as err:
            print("找不到json配置文件！"+str(err))

    def __parseQR2words(self) -> None:
        """将已有的QR码解析为字符串
        """
        if not os.path.exists(self.__config["origin"]):
            print("找不到原始二维码文件："+self.__config["origin"])
            return
        img: cv2.Mat = cv2.imread(self.__config["origin"])
        # 微信支付码有内置的cv模块
        if self.__config["if_pay"] == "true":
            qrCodeDetector = cv2.wechat_qrcode_WeChatQRCode(
                'detect.prototxt', 'detect.caffemodel', 'sr.prototxt', 'sr.caffemodel')
            self.__config["words"], points = qrCodeDetector.detectAndDecode(
                img)
            self.__config["words"] = str(self.__config["words"][0])
        else:
            qrCodeDetector = cv2.QRCodeDetector()
            self.__config["words"], points, _ = qrCodeDetector.detectAndDecode(
                img)

        if points is None:
            print("原始文件不是二维码文件！")
            return

    def __processData(self) -> None:
        """处理配置数据，使其对电脑更易读
        """
        cnt: int = 1
        while self.__config["if_covered"] != "true" and\
            os.path.exists(os.path.join(self.__config["save_dir"],
                                        self.__config["save_name"]+self.__config["ext"])):
            cnt += 1
        self.__config["save_name"] = self.__config["save_name"]+str(cnt)
        self.__config["picture"] += self.__config["ext"]
        self.__config["save_name"] += self.__config["ext"]

    def ActTransform(self) -> None:
        """执行转换操作
        """
        self._readConfig()
        # 如果配置里指明不需要解析，就读取输入为二维码内容
        if self.__config["if_parse"] == "true":
            self.__parseQR2words()
        else:
            self.__config["words"] = input("请输入需要转换成二维码的文字：")
        self.__processData()
        myqr.run(
            words=self.__config["words"] if self.__config["words"] != "" else "hello world!",
            version=int(self.__config["version"]),
            level=self.__config["level"],
            picture=self.__config["picture"] if self.__config["picture"] != "" and os.path.exists(
                self.__config["picture"]) else None,
            colorized=False if self.__config["colorized"] != "true" else True,
            contrast=float(self.__config["contrast"]),
            brightness=float(self.__config["brightness"]),
            save_name=self.__config["save_name"] if self.__config["save_name"] != "" else "hello.png",
            save_dir=os.getcwd(
            ) if self.__config["save_dir"] == "" else self.__config["save_dir"]
        )


