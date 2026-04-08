from kafka import KafkaConsumer
from kafka import KafkaProducer
import time
import sys
import importlib
importlib.reload(sys)

consumer = KafkaConsumer(bootstrap_servers='kafka1:9092')
producer = KafkaProducer(bootstrap_servers='kafka3:9094')
consumer.subscribe(['testkafka'])

action_click = 0
action_incart = 0
action_buy = 0
action_attention = 0

age0_18 = 0
age18_24 = 0
age25_29 = 0
age30_34 = 0
age35_39 = 0
age40_49 = 0
age50_80 = 0

gender_boy = 0
gender_girl = 0

province_Liaoning = 0
province_Fujian = 0
province_Sichuan = 0
province_Jiangsu = 0
province_Hainan = 0
province_Guizhou = 0
province_Shandong = 0
province_Shaanxi = 0
province_Hunan = 0
province_Macao = 0
province_Shanxi = 0
province_Jilin = 0
province_Gansu = 0
province_Hebei = 0
province_HongKong = 0
province_Guangxi = 0
province_Anhui = 0
province_Ningxia = 0
province_Jiangxi = 0
province_Shanghai = 0
province_Yunnan = 0
province_TianjinCity = 0
province_Beijing = 0
province_Hubei = 0
province_Chongqing = 0
province_Xinjiang = 0
province_Taiwan = 0
province_InnerMongolia = 0
province_Heilongjiang = 0
province_Zhejiang = 0
province_Qinghai = 0
province_Henan = 0
province_Tibet = 0
province_Guangdong = 0


for msg in consumer:
    action_in = msg.value[0:1].decode('utf8')
    age_in = msg.value[2:3].decode('utf8')
    gender_in = msg.value[4:5].decode('utf8')
    province_in = msg.value[6:]

    if action_in == '0':
    	action_click = action_click + 1
    	print('action_click')
    if action_in == '1':
    	action_inca = action_inca + 1
    	print('action_inca')
    if action_in == '2':
        action_buy = action_buy + 1
        print('action_buy')
    if action_in == '3':
        action_attention = action_attention + 1
        print('action_attention')

    if age_in == '0':
        age0_18 = age0_18 + 1
        print('age0_18')
    if age_in == '1':
        age18_24 = age18_24 + 1
        print('age18_24')
    if age_in == '2':
        age25_29 = age25_29 + 1
        print('age25_29')
    if age_in == '3':
        age30_34 = age30_34 + 1
        print('age30_34')
    if age_in == '4':
        age35_39 = age35_39 + 1
        print('age35_39')
    if age_in == '5':
        age40_49 = age40_49 + 1
        print('age40_49')
    if age_in == '6':
        age50_80 = age50_80 + 1
        print('age50_80')


    if gender_in == '0':
        gender_girl = gender_girl + 1
        print('gender_girl')
    if gender_in == '1':
        gender_boy = gender_boy + 1
        print('gender_boy')

    if province_in == '辽宁'.encode('utf8'):
        province_Liaoning = province_Liaoning + 1
        print('Liaoning')
    if province_in == '福建'.encode('utf8'):
        province_Fujian = province_Fujian + 1
        print('Fujian')
    if province_in == '四川'.encode('utf8'):
        province_Sichuan = province_Sichuan + 1
        print('Sichuan')
    if province_in == '江苏'.encode('utf8'):
        province_Jiangsu = province_Jiangsu + 1
        print('Jiangsu')
    if province_in == '海南'.encode('utf8'):
        province_Hainan = province_Hainan + 1
        print('Hainan')
    if province_in == '贵州'.encode('utf8'):
        province_Guizhou = province_Guizhou + 1
        print('Guizhou')
    if province_in == '山东'.encode('utf8'):
        province_Shandong = province_Shandong + 1
        print('Shandong')
    if province_in == '陕西'.encode('utf8'):
        province_Shaanxi = province_Shaanxi + 1
        print('Shaanxi')
    if province_in == '湖南'.encode('utf8'):
        province_Hunan = province_Hunan + 1
        print('Hunan')
    if province_in == '澳门'.encode('utf8'):
        province_Macao = province_Macao + 1
        print('Macao')
    if province_in == '山西'.encode('utf8'):
        province_Shanxi = province_Shanxi + 1
        print('Shanxi')
    if province_in == '吉林'.encode('utf8'):
        province_Jilin = province_Jilin + 1
        print('Jilin')
    if province_in == '甘肃'.encode('utf8'):
        province_Gansu = province_Gansu + 1
        print('Gansu')
    if province_in == '河北'.encode('utf8'):
        province_Hebei = province_Hebei + 1
        print('Hebei')
    if province_in == '香港'.encode('utf8'):
        province_HongKong = province_HongKong + 1
        print('HongKong')
    if province_in == '广西'.encode('utf8'):
        province_Guangxi = province_Guangxi + 1
        print('Guangxi')
    if province_in == '安徽'.encode('utf8'):
        province_Anhui = province_Anhui + 1
        print('Anhui')
    if province_in == '宁夏'.encode('utf8'):
        province_Ningxia = province_Ningxia + 1
        print('Ningxia')
    if province_in == '江西'.encode('utf8'):
        province_Jiangxi = province_Jiangxi + 1
        print('Jiangxi')
    if province_in == '上海市'.encode('utf8'):
        province_Shanghai = province_Shanghai + 1
        print('Shanghai')
    if province_in == '云南'.encode('utf8'):
        province_Yunnan = province_Yunnan + 1
        print('Yunnan')
    if province_in == '天津市'.encode('utf8'):
        province_TianjinCity = province_TianjinCity + 1
        print('TianjinCity')
    if province_in == '北京市'.encode('utf8'):
        province_Beijing = province_Beijing + 1
        print('Beijing')
    if province_in == '湖北'.encode('utf8'):
        province_Hubei = province_Hubei + 1
        print('Hubei')
    if province_in == '重庆市'.encode('utf8'):
        province_Chongqing = province_Chongqing + 1
        print('Chongqing')
    if province_in == '新疆'.encode('utf8'):
        province_Xinjiang = province_Xinjiang + 1
        print('Xinjiang')
    if province_in == '台湾'.encode('utf8'):
        province_Taiwan = province_Taiwan + 1
        print('Taiwan')
    if province_in == '内蒙古'.encode('utf8'):
        province_InnerMongolia = province_InnerMongolia + 1
        print('InnerMongolia')
    if province_in == '黑龙江'.encode('utf8'):
        province_Heilongjiang = province_Heilongjiang + 1
        print('Heilongjiang')
    if province_in == '浙江'.encode('utf8'):
        province_Zhejiang = province_Zhejiang + 1
        print('Zhejiang')
    if province_in == '青海'.encode('utf8'):
        province_Qinghai = province_Qinghai + 1
        print('Qinghai')
    if province_in == '河南'.encode('utf8'):
        province_Henan = province_Henan + 1
        print('Henan')
    if province_in == '西藏'.encode('utf8'):
        province_Tibet = province_Tibet + 1
        print('Tibet')
    if province_in == '广东'.encode('utf8'):
        province_Guangdong = province_Guangdong + 1
        print('Guangdong')
    print('-----------------------------')

    totalcontent =\
    str(action_click) + ',' + \
    str(action_incart) + ',' + \
    str(action_buy) + ',' + \
    str(action_attention) + ',' + \
    str(age0_18) + ',' + \
    str(age18_24) + ',' + \
    str(age25_29) + ',' + \
    str(age30_34) + ',' + \
    str(age35_39) + ',' + \
    str(age40_49) + ',' + \
    str(age50_80) + ',' + \
    str(gender_boy) + ',' + \
    str(gender_girl) + ',' + \
    str(province_Liaoning) + ',' + \
    str(province_Fujian) + ',' + \
    str(province_Sichuan) + ',' + \
    str(province_Jiangsu) + ',' + \
    str(province_Hainan) + ',' + \
    str(province_Guizhou) + ',' + \
    str(province_Shandong) + ',' + \
    str(province_Shaanxi) + ',' + \
    str(province_Hunan) + ',' + \
    str(province_Macao) + ',' + \
    str(province_Shanxi) + ',' + \
    str(province_Jilin) + ',' + \
    str(province_Gansu) + ',' + \
    str(province_Hebei) + ',' + \
    str(province_HongKong) + ',' + \
    str(province_Guangxi) + ',' + \
    str(province_Anhui) + ',' + \
    str(province_Ningxia) + ',' + \
    str(province_Jiangxi) + ',' + \
    str(province_Shanghai) + ',' + \
    str(province_Yunnan) + ',' + \
    str(province_TianjinCity) + ',' + \
    str(province_Beijing) + ',' + \
    str(province_Hubei) + ',' + \
    str(province_Chongqing) + ',' + \
    str(province_Xinjiang) + ',' + \
    str(province_Taiwan) + ',' + \
    str(province_InnerMongolia) + ',' + \
    str(province_Heilongjiang) + ',' + \
    str(province_Zhejiang) + ',' + \
    str(province_Qinghai) + ',' + \
    str(province_Henan) + ',' + \
    str(province_Tibet ) + ',' + \
    str(province_Guangdong)
    print(totalcontent.encode('utf8'))
    producer.send('result',totalcontent.encode('utf8'))

