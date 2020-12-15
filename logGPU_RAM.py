

import tensorflow as tf

import numpy as np

import os

import time

import tf2lib as tl

import nvidia_smi

nvidia_smi.nvmlInit()
loggers = []
gpus = []

def init_gpu_writers(logdir):
    global gpus, loggers
    '''
    Set up tensorboard file writers.
    '''
    for i in range(nvidia_smi.nvmlDeviceGetCount()):
        handle = nvidia_smi.nvmlDeviceGetHandleByIndex(i)
        gpus.append(handle)
        name = nvidia_smi.nvmlDeviceGetName(handle).decode().replace(' ','-')+':'+str(int(i))
        loggers.append(tf.summary.create_file_writer(os.path.join(logdir, os.uname().nodename, name)))

def log_gpu_memory_to_tensorboard():
    '''
    Log every gpus current free memory level to tensorboard.
    '''
    for i in range(nvidia_smi.nvmlDeviceGetCount()):
        info = nvidia_smi.nvmlDeviceGetMemoryInfo(gpus[i])
        with loggers[i].as_default():
            tl.summary({'free':np.array(info.free)/(1024**3)}, step=int(time.time()), name='GPUs')
        

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='log gpu memory level to tensorboard')
    parser.add_argument('logdir', help='Directory or subdirectory where tensoboard should look for logs. Same as tensorboard --logdir.')
    parser.add_argument('--update-frequency', '-f', type=float, help='seconds to wait between logs')
    args = parser.parse_args()
    print(f'PID:{os.getpid()}:PID')
    init_gpu_writers(logdir=args.logdir)
    while True:
        time.sleep(args.update_frequency)
        log_gpu_memory()