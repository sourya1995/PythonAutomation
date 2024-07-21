from pathlib import Path
import os


def find_rc(rc_name=".examplerc"):
    var_name = "EXAMPLERC_DIR"
    if var_name in os.environ:
        var_path = Path(os.environ[var_name]) / rc_name
        print(f"Checking {var_path}")
        if var_path.exists():
            return str(var_path)
    
    config_path = Path.cwd() / rc_name
    print(f"Checking {config_path}")
    if config_path.exists():
        return str(config_path)
    
    home_dir = Path.home()
    config_path = home_dir / rc_name
    print(f"Checking {config_path}")
    if config_path.exists():
        return str(config_path)
    
    file_path = Path(__file__).resolve()
    parent_path = file_path.parent
    config_path = parent_path / rc_name
    print(f"Checking {config_path}")
    if config_path.exists():
        return str(config_path)
    
    print(f"File {rc_name} not found in any of the following locations:")
    print(f"1. Environment variable {var_name}")
    print(f"2. Current working directory")
    print(f"3. Home directory")
    print(f"4. Parent directory of the current file")
    raise FileNotFoundError(f"File {rc_name} not found in any of the above locations.")