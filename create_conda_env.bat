conda create -n aind2-rnn python=3.5
activate aind2-rnn
pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/windows/gpu/tensorflow_gpu-1.2.1-cp35-cp35m-win_amd64.whl
conda install --file requirements-conda.txt
