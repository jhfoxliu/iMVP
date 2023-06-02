from sjm_tools import job,check_env

imvp = check_env('/share/public1/data/yaoj/projects/1-active/iMVP_revision_202304/optimize/imvp/iMVP.fuction.py')
workpath = './'
sjm="imvp" 
JOB = job(SJM = sjm, workpath = workpath)
JOB.step_start(step_name='imvp',memory = '100G', hostName = "node2")
JOB.add_process('/share/public1/data/yaoj/biosotf/miniconda3/bin/python3.9 {imvp} /share/public1/data/yaoj/projects/1-active/iMVP_revision_202304/optimize/sim_out.100k.final.fa /share/public1/data/yaoj/projects/1-active/iMVP_revision_202304/optimize/imvp/simulate_F10.tsv'.format(imvp = imvp))
JOB.step_end()
JOB.job_finish()
JOB.submit(sjm='sjm+')