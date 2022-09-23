from config import Config


class ConfigProvider:
    def __init__(self,cfg_path="./app_config.cfg"):
        self.cfg = Config(str(cfg_path))

    def provide_elasticsearch(self):
        return self.cfg.get("elasticsearch", {})
