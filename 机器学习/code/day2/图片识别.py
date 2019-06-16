from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '15649251'
API_KEY = 'RPGGLWTWZWvHSoao70XO8RTr'
SECRET_KEY = 'rvxUlGeVv6aFz5XzsHy8nA7jBtfAk25C'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('2.jpg')

""" 调用通用文字识别, 图片参数为本地图片 """
result=client.basicGeneral(image)
print(result)