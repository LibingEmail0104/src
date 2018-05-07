from PIL import Image,ImageFont,ImageDraw
import time
# img=Image.open("")
# jpg=Image.open("")
# img.paste(jpg,(23,23))
# img.show()
# print(img.show())
#
# print()
# 时间戳转换时间
timestamp = 1462451334
# 转换成localtime

time_local = time.localtime(timestamp)
time_local = time.localtime(timestamp)
time_local = time.localtime(timestamp)
# 转换成新的时间格式(2016-05-05 20:28:54)
dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)

print(dt)

# 时间转换时间戳
dte = "2018/4/19 14:43:55"

# 转换成时间数组
timeArray = time.strptime(dte, "%Y/%m/%d %H:%M:%S")
# 转换成新的时间格式(20160505-20:28:54)
dt_new = time.mktime(timeArray)

print(int(dt_new))


def printme(str):

    """打印字符串"""

    print(str)
    return


printme("asdiasjd")






