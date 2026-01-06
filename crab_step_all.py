import CRABClient
from CRABClient.UserUtilities import config 

config = config()

config.General.requestName = 'DQM_HLTTag_Step_all_ZMM2025_rseed_woduplicate_tnp_100'
config.General.workArea = 'Step_all'
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'pset_DQM_test_all.py'
config.JobType.scriptExe = 'step_all.sh'
config.JobType.maxMemoryMB = 7200
config.JobType.numCores = 4
config.JobType.inputFiles = ['step1_GEN_SIM.py', 'step2_DIGI_L1_DIGI2RAW_HLT.py', 'step3_RAW2DIGI_L1Reco_RECO_PAT_DQM.py', 'step4_HARVESTING.py']
config.JobType.outputFiles = ['DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root']

config.Data.inputDataset = '/Muon0/Run2024G-v1/RAW'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = 100
config.Data.inputBlocks = ['/Muon0/Run2024G-v1/RAW#136fa366-c612-4718-bfa5-aaf539efd48c']
config.Data.outLFNDirBase = '/store/user/sejang/DQM_test_ZMM'
config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3_DQM_Step_all_HLTTag_ZMM2025_rseed_woduplicate_tnp_100'

config.Site.storageSite = 'T3_KR_KNU'
