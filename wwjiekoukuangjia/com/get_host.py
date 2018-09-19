from configparser import ConfigParser


def get_host():
    conf = ConfigParser()
    conf.read("../config/config.ini")
    host = conf.get("env", "env")
    if host == "pre":
        host = conf.get("pre", "host")
    if host == "test":
        host = conf.get("test", "host")
    return host

if __name__ == "__main__":
    print(get_host())