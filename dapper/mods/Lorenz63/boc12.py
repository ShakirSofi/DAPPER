# Reproduce results from Fig 11 of 
# M. Bocquet and P. Sakov (2012): "Combining inflation-free and
# iterative ensemble Kalman filters for strongly nonlinear systems"
from dapper.mods.Lorenz63.sak12 import HMM
# The only diff to sak12 is R: boc12 uses 1 and 8, sak12 uses 2 (and 8)

from dapper import *

HMM.Obs.noise.C = CovMat(eye(3))

HMM.name = os.path.relpath(__file__,'mods/')

####################
# Suggested tuning
####################
# from dapper.mods.Lorenz63.boc12 import HMM                # Expected RMSE_a:
# HMM.t.dkObs = 25
# cfgs += iEnKS('Sqrt', N=10,infl=1.02,rot=True)            # 0.22
# cfgs += iEnKS('Sqrt', N=3, infl=1.04)                     # 0.23
# cfgs += iEnKS('Sqrt', N=3, xN=1.0)                        # 0.22
# 
# HMM.t.dkObs = 5
# cfgs += iEnKS('Sqrt', N=10,infl=1.02,rot=True)            # 0.13
# cfgs += iEnKS('Sqrt', N=3, infl=1.02)                     # 0.13
# cfgs += iEnKS('Sqrt', N=3, xN=1.0)                        # 0.15
# cfgs += iEnKS('Sqrt', N=3, xN=2.0)                        # 0.14
# 
# HMM.t.dkObs = 25 and R=8*eye(3):
# cfgs += iEnKS('Sqrt', N=3, xN=1.0)                        # 0.70
