# coding: utf-8
import faker
import random

fake=faker.Faker(locale='zh-CN')  #选择地方为中国

cellphone_pool = []
address_pool = []
datetime_pool = []
talktime_pool = []

for i in range(100):
	cellphone_pool.append(fake.phone_number())
for i in range(10000):
	address_pool.append(fake.address())
	datetime_pool.append(fake.date_time_between(start_date="-10y", end_date="now"))
	talktime_pool.append(random.randint(30,300))

file_dst = "/home/ldzh/data_set/BigDataApplicationPractice/exp3/secondarysort_tel_log.txt"
with open(file_dst, "w", encoding="utf-8") as writer:
	for j in range(10000):
		cellphone = str(random.choice(cellphone_pool))		
		datetime = str(random.choice(datetime_pool))
		talktime = str(random.choice(talktime_pool))
		address = str(random.choice(address_pool))
		print('%s\t%s\t%s\t%s\t' %(cellphone,datetime,talktime,address))
		writer.write(cellphone+'\t'+datetime+'\t'+talktime+'\t'+address+'\n')

