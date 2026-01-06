import FWCore.ParameterSet.Config as cms

process = cms.Process('NoSplit')

process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring())
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(20))
process.options.numberOfThreads = cms.untracked.uint32(4)
process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root')
)
process.out = cms.EndPath(process.output)