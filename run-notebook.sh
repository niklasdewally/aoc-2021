bash install.sh
# https://github.com/conda/conda/issues/7980
source $CONDA_BASE/etc/profile.d/conda.sh
conda activate ./env
nohup jupyter notebook &
