import pathlib, os
from genvm_linter import GenVMLinter

# Force downloading stubs 
cache_dir = pathlib.Path.home() / '.cache' / 'genvm-linter'
cache_dir.mkdir(parents=True, exist_ok=True)

try:
    linter = GenVMLinter()
    print("Linter OK")
except Exception as e:
    print("Init error:", e)

# Check what version was resolved from the manifest in the tarball
from genvm_linter.validate.artifacts import get_latest_version, download_artifacts, get_stubs_path
ver = get_latest_version()
print("Latest version:", ver)

# Check which runners exist
stubs_path = get_stubs_path(ver)
print("Stubs path:", stubs_path)
if stubs_path.exists():
    for f in os.listdir(stubs_path):
        print("  stubs file:", f)
    # Check the runners dir if it exists
    runners_dir = stubs_path / "runners"
    if runners_dir.exists():
        for f in os.listdir(runners_dir):
            print("  runner:", f)
else:
    print("Stubs not yet downloaded")
    # Download them
    try:
        dl = download_artifacts(ver)
        print("Downloaded to:", dl)
    except Exception as e:
        print("Download error:", e)
