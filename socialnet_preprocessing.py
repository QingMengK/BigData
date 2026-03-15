# coding: utf-8

import random

classmate = "袁欣,王俪,元明亮,周宇飞,丁淑霞,于凤敏,于金艳,马海军,王俊栋,王洪洋,\
王梓新,冉波太,宁雅文,刘天刚,孙传迅,孙继来,朱妍,吴双列,张天申,张程程,李东霖,李孟新,\
杨欢,杨俊贤,杨海军,杨璐,沈名杰,邵京京,陆骁,范振江,赵宏天,郭李萍,矫明津,郝弘毅,徐溶,\
王嘉浚,于楠,韦松,王永悦,王俊婷,王祺中,王蓝袖,孙泽洋,朱美同,何雨,吴仁博,张千祥,杨汶翰,\
杨淋钧,杨维玉,陈婷,罗子昂,姜淼,赵可欣,赵凌波,栾司琪,郭家铭,寇悦,梁哲,储潇玥,彭奥龙,焦美晴,\
董宇,韩赢震,王纯,王佳,王高峰,白少东,孙钰博,曲贺,朱宁,邢振国,闫津龙,严聪聪,吴琪蒙,张云洁,\
张丽萍,李本龙,李航,李智海,辛佳明,明佳音,范思会,胡建珍,郝鑫,唐鹏,郭昊,高偲淼,曹丽颖,符式江,蒋宇晖"

# 切分成列表，91个人对应91个元素
social_pool = classmate.split(',')

# 把姓名中有两个汉字的名字中间加上2个空格，这样对其好看
social_pool_format = []
for people in social_pool:
	if len(people) == 2:
		people_format = people[0]+'  '+people[1]
		social_pool_format.append(people_format)
	else:
		social_pool_format.append(people)

# 存放生成的人际关系contacts_content
# 列表是二维的，一个人对应一行
# 每一行有多个列，一个列上表示这个行的人的一个朋友或者一个联系人
contacts_content = []

# 计算器
count = 0

# 人际关系contacts_content第一次建设，开设91行
# 每一行对应social_pool_format中的一个人
# 91人对应91行
# 每行随机从social_pool_format选取除了本人以外的10个人
# 这10个人存在人际关系contacts_content对应的一行中
# 这一行有来自于social_pool_format的people决定
for people in social_pool_format:
	# 直接=赋值会导致social_pool_sel的变化作用在social_pool_format上
	# 使用list使得产生一个新列表，social_pool_sel与social_pool_format无关
	social_pool_sel = list(social_pool_format)
	# 删除掉所有者自己
	social_pool_sel.pop(count)
	# 在剩下的人中随机选择10个人
	contacts_people = random.sample(social_pool_sel, 10)
	contacts_content.append(contacts_people)	
	count = count + 1
# 人际关系contacts_content第二次建设
# 遍历91行，某一行内容为 A: B C D E时
# 在contacts_content对应的行B 行C 行D 行E上都要添加A
# 这样保证了如果A是B的朋友，那么在B对应的contacts_content行中也会出现A
# 这使得人际关系是双向的网络，A是B的朋友的同时B也是A的朋友
# 如果缺少这一轮建设，那么无法保证B出现在A的朋友列表时，A也一定在B的朋友列表
# contacts_content的行的序号与social_pool_format的行序号完全一致
# contacts_content的行的每一列就是对应social_pool_format行的每一位朋友
for count in range(len(social_pool_format)):
	for people in contacts_content[count]:
		contacts_content[social_pool_format.index(people)].append(social_pool_format[count])

# 生成的人际关系列表保存在一个文本文件中
file_dst = "/home/ldzh/data_set/BigDataApplicationPractice/exp3/socialnet.txt"
with open(file_dst, "w", encoding="utf-8") as writer:
	for count in range(len(social_pool_format)):
		# 防止人际关系contacts_content的每一行中出现重复的人名，用set的元素唯一性实现去重复元素
		contacts_content[count] = list(set(contacts_content[count]))
		# contacts_content的行的序号与social_pool_format的行序号完全一致
		# 因此social_pool_format[count]和contacts_content[count]都指向同一个人
		# 这个人就是contacts_owner
		# 这个人的通讯录或者朋友列表就是contacts_list
		contacts_owner = social_pool_format[count]
		# 全部朋友列表时list，用join把list中全部元素合并为一个大字符串，逗号分隔每个元素内容
		contacts_list = ','.join(contacts_content[count])
		print(contacts_owner+':'+contacts_list)
		writer.write(contacts_owner+':'+contacts_list+'\n')






    
