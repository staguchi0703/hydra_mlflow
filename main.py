import hydra
from omegaconf import DictConfig

@hydra.main(config_path="./conf/config.yaml")
def my_ex(cfg: DictConfig) -> None:
    params = cfg.model
    print(params)

if __name__ == "__main__":
    my_ex()
