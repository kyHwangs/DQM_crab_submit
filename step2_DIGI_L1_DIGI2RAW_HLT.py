# Auto generated configuration file
# ZMM (Z->mu mu) simulation with 2024/2025 setup
# Step 2: DIGI, L1, DIGI2RAW, HLT
# Command: cmsDriver.py step2 -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2024 --conditions auto:phase1_2024_realistic --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --eventcontent FEVTDEBUGHLT --era Run3_2024 -n 100 --filein file:step1.root --fileout file:step2.root

import FWCore.ParameterSet.Config as cms
import os

from Configuration.Eras.Era_Run3_2025_cff import Run3_2025

process = cms.Process('HLT',Run3_2025)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
#process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('SimGeneral.MixingModule.mix_Run3_Flat55To75_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_2025v13_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

# Random Number Generator Service for parallel jobs
# Get job number from CRAB environment variable
jobNumber = int(os.getenv('CRAB_Id', '0'))
baseSeed = 234567  # Different base seed from step1

process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    # Mixing module
    mix = cms.PSet(
        initialSeed = cms.untracked.uint32(baseSeed + jobNumber),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    # Muon system digitizers
    simMuonCSCDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(baseSeed + jobNumber + 10000),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    simMuonDTDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(baseSeed + jobNumber + 20000),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    simMuonRPCDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(baseSeed + jobNumber + 30000),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    simMuonGEMDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(baseSeed + jobNumber + 40000),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    # Tracker digitizers
    simSiPixelDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(baseSeed + jobNumber + 50000),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    simSiStripDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(baseSeed + jobNumber + 60000),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    # Forward detectors
    RPixDetDigitizer = cms.PSet(
        initialSeed = cms.untracked.uint32(baseSeed + jobNumber + 70000),
        engineName = cms.untracked.string('TRandom3')
    ),
    # Calorimeter digitizers
    simEcalUnsuppressedDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(baseSeed + jobNumber + 80000),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    simHcalUnsuppressedDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(baseSeed + jobNumber + 90000),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    # Additional detectors
    simCastorDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(baseSeed + jobNumber + 100000),
        engineName = cms.untracked.string('HepJamesRandom')
    ),
    simHGCalUnsuppressedDigis = cms.PSet(
        initialSeed = cms.untracked.uint32(baseSeed + jobNumber + 110000),
        engineName = cms.untracked.string('HepJamesRandom')
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(800),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:step1.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:800'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition
process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW-HLTDEBUG'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step2.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/relval/CMSSW_15_1_0_pre5/RelValMinBias_14TeV/GEN-SIM/151X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_noPU-v1/2580000/0a5011e3-6e0f-407c-918d-745895827755.root', '/store/relval/CMSSW_15_1_0_pre5/RelValMinBias_14TeV/GEN-SIM/151X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_noPU-v1/2580000/5e64b3cf-4596-4cf4-8336-c1b39d4ac38d.root', '/store/relval/CMSSW_15_1_0_pre5/RelValMinBias_14TeV/GEN-SIM/151X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_noPU-v1/2580000/6fa83838-9a61-4354-b3b1-d5597b092d98.root', '/store/relval/CMSSW_15_1_0_pre5/RelValMinBias_14TeV/GEN-SIM/151X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_noPU-v1/2580000/9483a3c2-5738-4153-a028-2e849a4f8322.root', '/store/relval/CMSSW_15_1_0_pre5/RelValMinBias_14TeV/GEN-SIM/151X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_noPU-v1/2580000/c0da1169-51b1-4021-833b-513cddc93eeb.root', '/store/relval/CMSSW_15_1_0_pre5/RelValMinBias_14TeV/GEN-SIM/151X_mcRun3_2025_realistic_v4_STD_RegeneratedGS_2025_noPU-v1/2580000/c990cfc5-1dd8-4b6d-871c-620da78f1e19.root'])
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2025_realistic', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
# process.schedule imported from cff in HLTrigger.Configuration
process.schedule.insert(0, process.digitisation_step)
process.schedule.insert(1, process.L1simulation_step)
process.schedule.insert(2, process.digi2raw_step)
process.schedule.extend([process.endjob_step,process.FEVTDEBUGHLToutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# Customisation from command line

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

