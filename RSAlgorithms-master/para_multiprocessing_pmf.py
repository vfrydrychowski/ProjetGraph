import multiprocessing as mp
import time
from multiprocessing import Manager, Process

from configx.configx_Epinions_80_early import ConfigX as Ep80
from model.pmf import goPMF


def worker(rank, return_dict):
    start = time.time()
    print(f"Process {rank} started at {time.strftime('%d %b %Y %H:%M:%S', time.gmtime(start))}")
    ep80 = Ep80()
    rmses, maes = goPMF(ep80, rank, verbose = False)
    return_dict[rank] = (rmses[0], maes[0])
    print(return_dict)
    end = time.time()
    print(f"Process {rank} stopped at {time.strftime('%d %b %Y %H:%M:%S', time.gmtime(end))}")
    print(f"Execution time for process {rank} : {end-start} seconds")

if __name__ == '__main__':
    import os

    current_file_path = os.path.abspath(__file__)
    current_file_directory = os.path.dirname(current_file_path)

    # change cwd to the current file directory
    os.chdir(current_file_directory)

    manager = Manager()
    return_dict = manager.dict()
    processes = []

    available_cpu = mp.cpu_count()
    nb_folds = 5
    num_processes = nb_folds

    start = time.time()

    for rank in range(num_processes):
        p = Process(target=worker, args=(rank, return_dict))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    rmse_sum = 0
    mae_sum = 0
    for i in range(num_processes):
        rmse_sum += return_dict[i][0]
        mae_sum += return_dict[i][1]

    rmse_avg = rmse_sum / num_processes
    mae_avg = mae_sum / num_processes

    end = time.time()
    print(f"The average of RMSES is {rmse_avg}")
    print(f"The average of MAES is {mae_avg}")
    print(f"Total execution time : {end-start} seconds")
