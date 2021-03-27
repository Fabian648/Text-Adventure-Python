import configparser
import json, os
import configparser
name = "ben"
cfg = configparser.ConfigParser()
cfg.read(os.path.join("Saved_Games", name + "_data", "Config_TA_" + name + ".ini"))
a = json.loads(cfg.get("config_TA", "weapon"))

l = ["this", "is", "a", "test"]
l.remove("a")
l = " ".join(l)
print(l)

