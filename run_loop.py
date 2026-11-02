import subprocess
import time
import os
import json
from pathlib import Path

os.environ['UV_CACHE_DIR'] = 'E:\\uv-cache'
base = Path('E:\\techarena-career-sim')
outdir = base / '.career_sim_runner' / 'career_emu' / 'outputs' / "Hhhhhhhhhhhhh's team"
best = 0
best_dir = None

for i in range(15):
    print(f'=== RUN {i+1} ===')
    log_out = Path(f'E:\\loop_out_{i}.txt')
    log_err = Path(f'E:\\loop_err_{i}.txt')
    with open(log_out,'w') as fo, open(log_err,'w') as fe:
        p = subprocess.Popen(['uv','run','python','-m','career_sim_runner','play','--submission','solution'], 
                             cwd=str(base), stdout=fo, stderr=fe)
    for _ in range(400):
        if p.poll() is not None:
            break
        time.sleep(5)
    if p.poll() is None:
        p.kill()
        time.sleep(3)
    if outdir.exists():
        dirs = sorted([d for d in outdir.iterdir() if d.is_dir()], key=lambda x: x.name, reverse=True)
        for d in dirs[:2]:
            sr = d / 'score_report.json'
            if sr.exists():
                try:
                    with open(sr,'r',encoding='utf-8-sig') as f:
                        data = json.load(f)
                    sc = data.get('ending_score',{}).get('quantitative_score') or data.get('quantitative_score')
                    print(f'RUN{i+1} score: {sc}')
                    if sc and sc > best:
                        best = sc
                        best_dir = str(d)
                    break
                except Exception as e:
                    print(e)
    print(f'BEST: {best}')
    if best >= 90:
        break
    time.sleep(5)
