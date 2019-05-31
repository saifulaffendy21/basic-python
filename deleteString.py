file=['deleting JIRA_support_2018-04-23-14-43-52.zip','deleting JIRA_support_2018-03-07-17-59-56.zip','deleting 2019-May-28--1245.zip']

for i in range(len(file)):
	file[i]=file[i].replace('deleting ','')

print(file)
