
from sec_api import ExtractorApi; import sys, json, pathlib
ex = ExtractorApi("YOUR_KEY")
cik, out = sys.argv[1], pathlib.Path("data/raw")/f"{cik}.json"
txt = ex.get_section(cik, "10-K", "riskfactors", "text")
out.write_text(json.dumps({"cik": cik, "text": txt}))

