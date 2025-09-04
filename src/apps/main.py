import importlib, json, time, yaml, pathlib
def load_config():
    cfg_path = pathlib.Path(__file__).resolve().parents[1] / "config.yaml"
    with open(cfg_path,"r",encoding="utf-8") as f:
        return yaml.safe_load(f)
def run_pipeline(seed):
    cfg = load_config()
    ctx = dict(seed)
    for mod_path in cfg["pipeline"]:
        ctx = importlib.import_module(mod_path).run(ctx)
    return ctx
if __name__ == "__main__":
    print(json.dumps(run_pipeline({"seed":"ok","started_at": time.time()}), indent=2))
