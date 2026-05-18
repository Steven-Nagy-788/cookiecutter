import json
import shlex
from pathlib import Path
from unittest import mock
from cookiecutter.prompt import prompt_for_config
from click.testing import CliRunner
from cookiecutter.cli import main as cli_main

def test_use_already_generated_samples():
    """
    Reads all existing samples from the `samples/` directory and executes them
    against cookiecutter to collect coverage.
    """
    root = Path(__file__).parent
    samples_dir = root / "samples"
    
    if not samples_dir.exists():
        print("No samples directory found. Please run `./generate all -n <amount>` first.")
        return

    # 1. Process JSON samples
    json_samples = list(samples_dir.glob("json/*.json"))
    print(f"Found {len(json_samples)} JSON samples.")
    for json_sample in json_samples:
        content = json_sample.read_text(encoding="utf-8")
        try:
            data = json.loads(content)
            context = {"cookiecutter": data}
            try:
                prompt_for_config(context, no_input=True)
            except Exception as e:
                pass # expected during fuzzing
        except json.JSONDecodeError:
            pass

    # 2. Process SSTI samples
    ssti_samples = list(samples_dir.glob("ssti/*.json"))
    print(f"Found {len(ssti_samples)} SSTI samples.")
    for ssti_sample in ssti_samples:
        content = ssti_sample.read_text(encoding="utf-8")
        try:
            data = json.loads(content)
            context = {"cookiecutter": data}
            try:
                # Mock os.abort so it doesn't kill the pytest run
                with mock.patch("os.abort", lambda: None):
                    prompt_for_config(context, no_input=True)
            except Exception as e:
                pass # expected during fuzzing
        except json.JSONDecodeError:
            pass

    # 3. Process CLI samples
    cli_samples = list(samples_dir.glob("cli/*.txt"))
    print(f"Found {len(cli_samples)} CLI samples.")
    runner = CliRunner()
    
    cli_out = root / "cli_output"
    cli_out.mkdir(exist_ok=True)
    
    for cli_sample in cli_samples:
        content = cli_sample.read_text(encoding="utf-8").strip()
        if not content:
            continue
            
        args = shlex.split(content)
        if '-o' not in args and '--output-dir' not in args:
            args.extend(['-o', str(cli_out)])
            
        runner.invoke(cli_main, args)

if __name__ == "__main__":
    test_use_already_generated_samples()
