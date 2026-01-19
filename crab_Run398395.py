import CRABClient
from CRABClient.UserUtilities import config 

config = config()

config.General.requestName = 'HLTOfflineDQM_2025G_TnP_Run398395'
config.General.workArea = 'Step_all'
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'pset_DQM_test_all.py'
config.JobType.scriptExe = 'step_all.sh'
config.JobType.maxMemoryMB = 7500
config.JobType.numCores = 4
config.JobType.inputFiles = ['step3_RAW2DIGI_L1Reco_RECO_PAT_DQM.py', 'step4_HARVESTING.py']
config.JobType.outputFiles = ['DQM_V0001_R000398395__Global__CMSSW_X_Y_Z__RECO.root']

config.Data.inputDataset = '/Muon0/Run2025G-ZMu-PromptReco-v1/RAW-RECO'
config.Data.userInputFiles = open('Run398391_ZMu.txt').readlines()
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/group/phys_muon/ec/HLT/MuonHLTRun3_PixelDegradation_From2024B/DQMTest/Run398395/'
config.Data.publication = False
config.Data.outputDatasetTag = 'HLTOfflineDQM_2025G_TnP_Run398395'

config.Site.storageSite = 'T2_CH_CERN'
