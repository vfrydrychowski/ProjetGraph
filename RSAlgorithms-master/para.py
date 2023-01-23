from mpi4py import MPI
from configx.configx_base import ConfigX as Ep80
from model.social_reg import goSocialReg
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

start = time.time()
print("thread %s started at %s" % (rank, time.strftime("%d %b %Y %H:%M:%S", time.gmtime(start))))
ep80 = Ep80()
rmses, maes = goSocialReg(ep80, rank, verbose = False)
rmse_avg = comm.allreduce(rmses[0], op=MPI.SUM)/size
mae_avg = comm.allreduce(maes[0], op=MPI.SUM)/size

end = time.time()
print("thread %s stoped at %s" % (rank, time.strftime("%d %b %Y %H:%M:%S", time.gmtime(end))))
print("exec time thread %s : %s secondes" % (rank, end-start))

comm.barrier()
end = time.time()
if rank==0:
    print("the average of rmses is %s " % rmse_avg)
    print("the average of maes is %s " % mae_avg)
    print("total exec time : %s secondes" % (end-start))

