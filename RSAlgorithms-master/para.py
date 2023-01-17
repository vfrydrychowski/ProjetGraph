from mpi4py import MPI
from configx.configx_Epinions_80 import ConfigX as Ep80
from model.social_reg import goSocialReg

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

ep80 = Ep80()
rmses, maes = goSocialReg(ep80, rank)
rmse_avg = comm.reduce(rmses, op=MPI.SUM, root=0)/size
mae_avg = comm.reduce(maes, op=MPI.SUM, root=0)/size

if rank==0:
    print("the average of rmses is %s " % rmse_avg)
    print("the average of maes is %s " % mae_avg)

