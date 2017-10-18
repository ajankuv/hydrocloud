from crontab import CronTab


#grab crons for outlets 0-3
listcron0 = CronTab(user='pi')
for job in listcron0:
    if job.comment == 'outlet0':
        print job

listcron1 = CronTab(user='pi')
for job in listcron1:
    if job.comment == 'outlet1':
        print job

listcron2 = CronTab(user='pi')
for job in listcron2:
    if job.comment == 'outlet2':
        print job

listcron3 = CronTab(user='pi')
for job in listcron3:
    if job.comment == 'outlet3':
        print job
