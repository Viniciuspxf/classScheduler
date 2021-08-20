import os
from crontab import CronTab

def createCommand():
    browser = input("Digite o navegador: ")
    link = input("Digite o link: ")
    user = input("Digite o usuário (ou aperte enter para default): ")

    if user != '':
        user = "&authuser=" + user
    
    command = "DISPLAY=:0 " + browser + " "  + link + user

    return command

def createDate():
    hour = int(input("Digite o horário: "))
    minute = int(input("Digite o minuto: "))
    dayOfWeek = input("Digite o dia da semana em inglês (SUN, MON, TUE): ")

    return hour, minute, dayOfWeek

def main():
    cron = CronTab(user= os.environ["USER"])
    
    n = int(input("Digite o número de aulas a serem adicionadas: "))
    
    for i in range(n):

        job = cron.new(command = createCommand())
        hour, minute, dayOfWeek = createDate()

        job.minute.on(minute)
        job.hour.on(hour)
        job.dow.on(dayOfWeek)
    
    cron.write()

main()
