#!
export TF_ENABLE_ONEDNN_OPTS=0
python -m unittest discover -s "tests/ml" -p "*_.py"
