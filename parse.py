from config import load_config
from cronsql import CONFIG_FILE


def build_crontab():
    cron = load_config(CONFIG_FILE)["cron"]

    crontab = (
        cron +
        " /usr/local/bin/python /cronsql.py >> /proc/1/fd/1 2>/proc/1/fd/2" +
        "\n"
    )

    f = open("crontab", "w")
    f.write(crontab)
    f.close()


build_crontab()
