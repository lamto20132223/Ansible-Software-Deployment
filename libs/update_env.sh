conda deactivate
conda remove --name viettel --all
cd /home/vttek/anaconda2/envs/
scp -r root@172.16.29.193:/root/anaconda2/envs/viettel ./
conda info --envs
conda acitvate viettel