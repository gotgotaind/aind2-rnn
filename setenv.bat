set PATH=%PATH%;C:\down\progs\cudnn-8.0-windows10-x64-v5.1\cuda\bin;C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v8.0\bin
activate aind2-rnn
set KERAS_BACKEND=tensorflow
python -c "from keras import backend"