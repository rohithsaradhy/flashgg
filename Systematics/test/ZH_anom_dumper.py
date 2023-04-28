#!/usr/bin/env cmsRun

import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
import FWCore.ParameterSet.VarParsing as VarParsing
from flashgg.Systematics.SystematicDumperDefaultVariables import minimalVariables,minimalHistograms,minimalNonSignalVariables,systematicVariables
from flashgg.Systematics.SystematicDumperDefaultVariables import minimalVariablesHTXS,systematicVariablesHTXS
import os
import copy
from flashgg.MetaData.MetaConditionsReader import *

# SYSTEMATICS SECTION
dropVBFInNonGold = False  # for 2015 only!

process = cms.Process("FLASHggSyst")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 1000 )


systlabels = [""]
phosystlabels = []
metsystlabels = []
jetsystlabels = []
elesystlabels = []
musystlabels = []

from flashgg.MetaData.JobConfig import customize
import FWCore.ParameterSet.VarParsing as VarParsing
from flashgg.MetaData.JobConfig import customize

customize.options.register('tthTagsOnly',
                           False,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'tthTagsOnly'
                           )
customize.options.register('doubleHTagsOnly',
                           False,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'doubleHTagsOnly'
                           )
customize.options.register('addVBFDoubleHTag',
                           True,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'addVBFDoubleHTag'
                           )
customize.options.register('addVBFDoubleHVariables',
                           False,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'addVBFDoubleHVariables'
                           )
customize.options.register('doubleHTagsUseMjj',
                           False,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'doubleHTagsUseMjj'
                           )
customize.options.register('doubleHTagDumpMinVariables',
                           False,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'doubleHTagDumpMinVariables'
                           )
customize.options.register('ForceGenDiphotonProduction',
                           True,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'ForceGenDiphotonProduction'
                           )
customize.options.register('dumpGenWeight',
                           False,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'dumpGenWeight'
                           )
customize.options.register('doubleHReweight',
                           -1,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.int,
                           'doubleHReweight'
                           )
customize.options.register('doDoubleHTag',
                           False,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'doDoubleHTag'
                           )
customize.options.register('doDoubleHttHKiller',
                           False,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'doDoubleHttHKiller'
                           )
customize.options.register('ttHKillerSaveInputVariables',
                           False,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'ttHKillerSaveInputVariables'
                           )
customize.options.register('doDoubleHGenAnalysis',
                           False,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'doDoubleHGenAnalysis'
                           )
customize.options.register('doBJetRegression',
                           False,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'doBJetRegression'
                           )
customize.options.register('doHTXS',
                           False,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'doHTXS'
                           )
customize.options.register('doStageOne',
                           False,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'doStageOne'
                           )
customize.options.register('acceptance',
                           'NONE',
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.string,
                           'acceptance'
                           )
customize.options.register('doSystematics',
                           True,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'doSystematics'
                           )
customize.options.register('doGranularJEC',
                           False,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'doGranularJEC'
                           )
customize.options.register('doPdfWeights',
                           True,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'doPdfWeights'
                           )
customize.options.register('ignoreNegR9',
                           True,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'ignoreNegR9'
                           )
customize.options.register('dumpTrees',
                           False,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'dumpTrees'
                           )
customize.options.register('dumpWorkspace',
                           True,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'dumpWorkspace'
                           )
customize.options.register('verboseTagDump',
                           False,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'verboseTagDump'
                           )
customize.options.register('verboseSystDump',
                           False,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'verboseSystDump'
                           )
customize.options.register('analysisType',
                           'mainAnalysis',
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.string,
                           'analysisType'
                           )
customize.options.register('applyNNLOPSweight',
                           True,
                           VarParsing.VarParsing.multiplicity.singleton,
                           VarParsing.VarParsing.varType.bool,
                           'applyNNLOPSweight'
                           )



print "Printing defaults"
print 'acceptance '+str(customize.acceptance)
print 'tthTagsOnly '+str(customize.tthTagsOnly)
# import flashgg customization to check if we have signal or background
from flashgg.MetaData.JobConfig import customize
# set default options if needed
customize.setDefault("maxEvents",-1)
customize.setDefault("targetLumi",1.00e+3)
customize.parse()
customize.metaConditions = MetaConditionsReader(customize.metaConditions)

### Global Tag
from Configuration.AlCa.GlobalTag import GlobalTag
if customize.processId == "Data":
    process.GlobalTag.globaltag = str(customize.metaConditions['globalTags']['data'])
else:
    process.GlobalTag.globaltag = str(customize.metaConditions['globalTags']['MC'])

from flashgg.Systematics.SystematicsCustomize import *
jetSystematicsInputTags = createStandardSystematicsProducers(process , customize)
if dropVBFInNonGold:
    process.flashggVBFTag.SetArbitraryNonGoldMC = True
    process.flashggVBFTag.DropNonGoldData = True
modifyTagSequenceForSystematics(process,jetSystematicsInputTags)

print "Printing options"
print 'acceptance '+str(customize.acceptance)
print 'tthTagsOnly '+str(customize.tthTagsOnly)


# process.load("flashgg/Taggers/flashggTagSequence_cfi")
# process.flashggTagSequence = flashggPrepareTagSequence(customize.metaConditions)

# needed for 0th vertex from microAOD
if customize.tthTagsOnly:
    process.load("flashgg/MicroAOD/flashggDiPhotons_cfi")
    process.flashggDiPhotons.whichVertex = cms.uint32(0)
    process.flashggDiPhotons.useZerothVertexFromMicro = cms.bool(True)
    process.flashggDiPhotons.vertexIdMVAweightfile = customize.metaConditions['flashggDiPhotons']['vertexIdMVAweightfile'].encode("ascii")
    process.flashggDiPhotons.vertexProbMVAweightfile = customize.metaConditions['flashggDiPhotons']['vertexProbMVAweightfile'].encode("ascii")

print 'here we print the tag sequence before'
print process.flashggTagSequence

if customize.tthTagsOnly:
    process.flashggTagSequence.remove(process.flashggVBFTag)
    process.flashggTagSequence.remove(process.flashggVHMetTag)
    process.flashggTagSequence.remove(process.flashggWHLeptonicTag)
    process.flashggTagSequence.remove(process.flashggZHLeptonicTag)
    process.flashggTagSequence.remove(process.flashggVHHadronicTag)
    process.flashggTagSequence.remove(process.flashggUntagged)
    process.flashggTagSequence.remove(process.flashggVBFMVA)
    process.flashggTagSequence.remove(process.flashggVBFDiPhoDiJetMVA)
    process.flashggTagSequence.remove(process.flashggTTHHadronicTag) # Remove ttH tags as well, as we add these in later manually (with modified systematics worfklow)
    process.flashggTagSequence.remove(process.flashggTTHLeptonicTag)
    process.flashggTagSequence.remove(process.flashggTTHDiLeptonTag)
    process.flashggTagSequence.remove(process.flashggTHQLeptonicTag)

else:
    if not customize.doSystematics: # allow memory-intensive ttH MVAs if we are not running systematics
        allowLargettHMVAs(process)

if customize.doDoubleHTag:
    import flashgg.Systematics.doubleHCustomize 
    hhc = flashgg.Systematics.doubleHCustomize.DoubleHCustomize(process, customize, customize.metaConditions)
    minimalVariables += hhc.variablesToDump()
    systematicVariables = hhc.systematicVariables()

if customize.doStageOne:
    assert (not customize.doHTXS)
    from flashgg.Systematics.stageOneCustomize import StageOneCustomize
    soc = StageOneCustomize(process, customize, customize.metaConditions)
    minimalVariables = soc.variablesToDump()
    systematicVariables = soc.systematicVariables()

process.flashggTHQLeptonicTag.processId = cms.string(str(customize.processId))

print 'here we print the tag sequence after'
print process.flashggTagSequence

if customize.tthTagsOnly:
    process.flashggTagSorter.TagPriorityRanges = cms.VPSet(   
        cms.PSet(TagName = cms.InputTag('flashggTTHLeptonicTag')),
        cms.PSet(TagName = cms.InputTag('flashggTTHHadronicTag')) 
    )

    print "customize.processId:",customize.processId

    print "Removing FracRVNvtxWeight from syst and adding  PixelSeed"
    
    newvpset = cms.VPSet()
    for pset in process.flashggDiPhotonSystematics.SystMethods:
        if not pset.Label.value().count("FracRVNvtxWeight") :
            print  pset.Label.value()
            newvpset += [pset]
    #from flashgg.Systematics.flashggDiPhotonSystematics_cfi import PixelSeedWeight #FIXME: this does not currently work, so comment it out for now
    #newvpset += [ PixelSeedWeight ]
    
    process.flashggDiPhotonSystematics.SystMethods = newvpset
   

print "customize.processId:",customize.processId
# load appropriate scale and smearing bins here
# systematics customization scripts will take care of adjusting flashggDiPhotonSystematics
#process.load("flashgg.Systematics.escales.escale76X_16DecRereco_2015")

# Or use the official tool instead
useEGMTools(process)

# Only run systematics for signal events
# convention: ggh vbf wzh (wh zh) tth
signal_processes = ["ggh_","vbf_","wzh_","wh_","zh_","bbh_","thq_","thw_","tth_","ggzh_","HHTo2B2G","GluGluHToGG","VBFHToGG","VHToGG","ttHToGG","Acceptance","hh","vbfhh","qqh","ggh","tth","vh","WHiggs0MToGG","WHiggs0MToGG_","WHiggs0PMToGG","WHiggs0PMToGG_"]
is_signal = reduce(lambda y,z: y or z, map(lambda x: customize.processId.count(x), signal_processes))

applyL1Prefiring = customizeForL1Prefiring(process, customize.metaConditions, customize.processId)

#if customize.processId.count("h_") or customize.processId.count("vbf_") or customize.processId.count("Acceptance") or customize.processId.count("hh_"): 
if is_signal:
    print "Signal MC, so adding systematics and dZ"
    if customize.doHTXS:
        variablesToUse = minimalVariablesHTXS
    else:
        variablesToUse = minimalVariables

    if customize.doSystematics:
        for direction in ["Up","Down"]:
            phosystlabels.append("MvaShift%s01sigma" % direction)
            phosystlabels.append("SigmaEOverEShift%s01sigma" % direction)
            phosystlabels.append("MaterialCentralBarrel%s01sigma" % direction)
            phosystlabels.append("MaterialOuterBarrel%s01sigma" % direction)
            phosystlabels.append("MaterialForward%s01sigma" % direction)
            phosystlabels.append("FNUFEB%s01sigma" % direction)
            phosystlabels.append("FNUFEE%s01sigma" % direction)
            phosystlabels.append("MCScaleGain6EB%s01sigma" % direction)
            phosystlabels.append("MCScaleGain1EB%s01sigma" % direction)
            jetsystlabels.append("JEC%s01sigma" % direction)
            jetsystlabels.append("JER%s01sigma" % direction)
            jetsystlabels.append("PUJIDShift%s01sigma" % direction)
            if customize.doGranularJEC:
                for sourceName in customize.metaConditions['flashggJetSystematics']['listOfSources']:
                    jetsystlabels.append("JEC%s%s01sigma" % (str(sourceName),direction))
            if customize.metaConditions['flashggJetSystematics']['doHEMuncertainty']:
                jetsystlabels.append("JetHEM%s01sigma" % direction)
            metsystlabels.append("metJecUncertainty%s01sigma" % direction)
            metsystlabels.append("metJerUncertainty%s01sigma" % direction)
            metsystlabels.append("metPhoUncertainty%s01sigma" % direction)
            metsystlabels.append("metUncUncertainty%s01sigma" % direction)
            variablesToUse.append("LooseMvaSF%s01sigma[1,-999999.,999999.] := weight(\"LooseMvaSF%s01sigma\")" % (direction,direction))
            variablesToUse.append("PreselSF%s01sigma[1,-999999.,999999.] := weight(\"PreselSF%s01sigma\")" % (direction,direction))
            variablesToUse.append("electronVetoSF%s01sigma[1,-999999.,999999.] := weight(\"electronVetoSF%s01sigma\")" % (direction,direction))
            variablesToUse.append("TriggerWeight%s01sigma[1,-999999.,999999.] := weight(\"TriggerWeight%s01sigma\")" % (direction,direction))
            variablesToUse.append("FracRVWeight%s01sigma[1,-999999.,999999.] := weight(\"FracRVWeight%s01sigma\")" % (direction,direction))
            variablesToUse.append("MuonIDWeight%s01sigma[1,-999999.,999999.] := getObjectWeight(\"Muon%sIDWeight%s01sigma\")" % (direction,str(customize.metaConditions["MUON_ID"]),direction))
            variablesToUse.append("ElectronIDWeight%s01sigma[1,-999999.,999999.] := getObjectWeight(\"ElectronIDWeight%s01sigma\")" % (direction,direction))
            variablesToUse.append("ElectronRecoWeight%s01sigma[1,-999999.,999999.] := getObjectWeight(\"ElectronRecoWeight%s01sigma\")" % (direction,direction))
            variablesToUse.append("MuonIsoWeight%s01sigma[1,-999999.,999999.] := getObjectWeight(\"Muon%sISOWeight%s01sigma\")" % (direction,str(customize.metaConditions['MUON_ISO']),direction))
            variablesToUse.append("JetBTagCutWeight%s01sigma[1,-999999.,999999.] := getObjectWeight(\"JetBTagCutWeight%s01sigma\")" % (direction,direction))
            variablesToUse.append("JetBTagReshapeWeight%s01sigma[1,-999999.,999999.] := getObjectWeight(\"JetBTagReshapeWeight%s01sigma\")" % (direction,direction))
            if applyL1Prefiring:
                variablesToUse.append("prefireWeight%s01sigma[1,-999999.,999999.] := weight(\"prefireWeight%s01sigma\")" % (direction,direction))
            variablesToUse.append("THU_ggH_Mu%s01sigma[1,-999999.,999999.] := getTheoryWeight(\"THU_ggH_Mu%s01sigma\")" % (direction,direction))
            variablesToUse.append("THU_ggH_Res%s01sigma[1,-999999.,999999.] := getTheoryWeight(\"THU_ggH_Res%s01sigma\")" % (direction,direction))
            variablesToUse.append("THU_ggH_Mig01%s01sigma[1,-999999.,999999.] := getTheoryWeight(\"THU_ggH_Mig01%s01sigma\")" % (direction,direction))
            variablesToUse.append("THU_ggH_Mig12%s01sigma[1,-999999.,999999.] := getTheoryWeight(\"THU_ggH_Mig12%s01sigma\")" % (direction,direction))
            variablesToUse.append("THU_ggH_VBF2j%s01sigma[1,-999999.,999999.] := getTheoryWeight(\"THU_ggH_VBF2j%s01sigma\")" % (direction,direction))
            variablesToUse.append("THU_ggH_VBF3j%s01sigma[1,-999999.,999999.] := getTheoryWeight(\"THU_ggH_VBF3j%s01sigma\")" % (direction,direction))
            variablesToUse.append("THU_ggH_PT60%s01sigma[1,-999999.,999999.] := getTheoryWeight(\"THU_ggH_PT60%s01sigma\")" % (direction,direction))
            variablesToUse.append("THU_ggH_PT120%s01sigma[1,-999999.,999999.] := getTheoryWeight(\"THU_ggH_PT120%s01sigma\")" % (direction,direction))
            variablesToUse.append("THU_ggH_qmtop%s01sigma[1,-999999.,999999.] := getTheoryWeight(\"THU_ggH_qmtop%s01sigma\")" % (direction,direction))
            for r9 in ["HighR9","LowR9"]:
                for region in ["EB","EE"]:
                    phosystlabels.append("ShowerShape%s%s%s01sigma"%(r9,region,direction))
#                    phosystlabels.append("MCSmear%s%s%s01sigma" % (r9,region,direction))
                    phosystlabels.append("MCScale%s%s%s01sigma" % (r9,region,direction))
                    for var in ["Rho","Phi"]:
                        phosystlabels.append("MCSmear%s%s%s%s01sigma" % (r9,region,var,direction))
        systlabels += phosystlabels
        systlabels += jetsystlabels
        systlabels += metsystlabels
    customizeSystematicsForSignal(process)
elif customize.processId == "Data":
    print "Data, so turn off all shifts and systematics, with some exceptions"
    variablesToUse = minimalNonSignalVariables
    customizeSystematicsForData(process)
else:
    print "Background MC, so store mgg and central only"
    variablesToUse = minimalNonSignalVariables
    customizeSystematicsForBackground(process)

if customize.doubleHTagsOnly:
    variablesToUse = minimalVariables
   # if customize.processId == "Data":
   #     variablesToUse = minimalNonSignalVariables
  
if customize.doDoubleHTag:
   systlabels,jetsystlabels,metsystlabels = hhc.customizeSystematics(systlabels,jetsystlabels,metsystlabels)
           

print "--- Systematics  with independent collections ---"
print systlabels
print "-------------------------------------------------"
print "--- Variables to be dumped, including systematic weights ---"
print variablesToUse
print "------------------------------------------------------------"

#from flashgg.Taggers.globalVariables_cff import globalVariables
#globalVariables.extraFloats.rho = cms.InputTag("rhoFixedGridAll")

#cloneTagSequenceForEachSystematic(process,systlabels,phosystlabels,jetsystlabels,jetSystematicsInputTags)
cloneTagSequenceForEachSystematic(process,systlabels,phosystlabels,metsystlabels,jetsystlabels,jetSystematicsInputTags)

# Dump an object called NoTag for untagged events in order to track QCD weights
# Will be broken if it's done for non-central values, so turn this on only for the non-syst tag sorter
process.flashggTagSorter.CreateNoTag = True # MUST be after tag sequence cloning
process.flashggTagSorter.isGluonFusion = cms.bool(bool(customize.processId.count("ggh")))
process.flashggTagSorter.applyNNLOPSweight = cms.bool(customize.applyNNLOPSweight)

###### Dumper section

from FWCore.ParameterSet.VarParsing import VarParsing
from flashgg.MetaData.samples_utils import SamplesManager

process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring(
                                 #"/store/user/spigazzi/flashgg/Era2016_RR-17Jul2018_v2/legacyRun2FullV1/GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8/Era2016_RR-17Jul2018_v2-legacyRun2FullV1-v0-RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/190708_140500/0000/myMicroAODOutputFile_12.root"
                                 #"/store/user/spigazzi/flashgg/Era2017_RR-31Mar2018_v2/legacyRun2FullV1/GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8/Era2017_RR-31Mar2018_v2-legacyRun2FullV1-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/190703_101705/0000/myMicroAODOutputFile_45.root"
                                 #"/store/user/spigazzi/flashgg/Era2018_RR-17Sep2018_v2/legacyRun2FullV2/GluGluHToGG_M125_TuneCP5_13TeV-amcatnloFXFX-pythia8/Era2018_RR-17Sep2018_v2-legacyRun2FullV2-v0-RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/190710_093150/0000/myMicroAODOutputFile_41.root"
                                 "/store/user/spigazzi/flashgg/Era2018_RR-17Sep2018_v2/legacyRun2FullV2/EGamma/Era2018_RR-17Sep2018_v2-legacyRun2FullV2-v0-Run2018A-17Sep2018-v2/190610_103420/0001/myMicroAODOutputFile_1125.root"
                             ))

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("test.root"))

process.extraDumpers = cms.Sequence()

from flashgg.Taggers.TagsDumperCustomize import customizeTagsDumper
customizeTagsDumper(process, customize) ## move all the default tags dumper configuration to this function

if customize.processId == "tHq":
    import flashgg.Taggers.THQLeptonicTagVariables as var
    variablesToUse = minimalVariables + var.vtx_variables + var.dipho_variables

#tagList=[
#["UntaggedTag",4],
#["VBFTag",2],
#["VHTightTag",0],
#["VHLooseTag",0],
#["VHEtTag",0],
#["VHHadronicTag",0],
#["TTHHadronicTag",0],
##["TTHLeptonicTag",0]
#]

tag_only_variables = {}

if customize.tthTagsOnly:
    tagList=[
        ["TTHHadronicTag",4],
        ["TTHLeptonicTag",4]
        ]
elif customize.doubleHTagsOnly:
    tagList = hhc.tagList
    print "taglist is:"
    print tagList
    if customize.addVBFDoubleHTag and customize.addVBFDoubleHVariables:
        tag_only_variables["VBFDoubleHTag"] = hhc.vbfHHVariables()    
elif customize.doStageOne:
    tagList = soc.tagList
else:
    tagList=[
        ["NoTag",0],
        ["UntaggedTag",4],
        ["VBFTag",3],
        ["ZHLeptonicTag",2],
        ["WHLeptonicTag",6],
        ["VHMetTag",2],
        ["VHHadronicTag",0],
        ["TTHHadronicTag",4],
        ["TTHLeptonicTag",4],
        ["THQLeptonicTag",0],
        ["TTHDiLeptonTag",0]
        ]


tagList=[        
        ["NoTag",0],
        # ["UntaggedTag",4],
        ["ZHLeptonicTag",1],
        # ["WHLeptonicTag",4]
        ] #One Category ,["VHMetTag",2]


process.flashggWHLeptonicTag.Boundaries_GT75 = cms.vdouble(-1) #Loose cuts on WH_BDT mva... #Rohith
process.flashggZHLeptonicTag.Boundaries = cms.vdouble(-1) #Loose cuts on ZH_BDT mva... #Rohith



definedSysts=set()
process.tagsDumper.classifierCfg.remap=cms.untracked.VPSet()
import flashgg.Taggers.dumperConfigTools as cfgTools

# get the variable list
custom_vars = ['vh_mva :=  VHmva()'
                ]


WH_Anom_Vars = [
    'WHiggs0MToGG_MVA := WHiggs0MToGG_mva()',
    'WHiggs0Mf05ph0ToGG_MVA := WHiggs0Mf05ph0ToGG_mva()',
    'WHiggs0PHToGG_MVA := WHiggs0PHToGG_mva()',
    'WHiggs0PHf05ph0ToGG_MVA := WHiggs0PHf05ph0ToGG_mva()',
    'WHiggs0L1ToGG_MVA := WHiggs0L1ToGG_mva()',
    'WHiggs0L1f05ph0ToGG_MVA := WHiggs0L1f05ph0ToGG_mva()'
]
ZH_Anom_Vars = [
    'ZHiggs0MToGG_MVA := ZHiggs0MToGG_mva()',
    'ZHiggs0PHToGG_MVA := ZHiggs0PHToGG_mva()',
    'ZHiggs0PHf05ph0ToGG_MVA := ZHiggs0PHf05ph0ToGG_mva()',
    'ZHiggs0L1f05ph0ToGG_MVA := ZHiggs0L1f05ph0ToGG_mva()',
    'ZHiggs0L1ZgToGG_MVA := ZHiggs0L1ZgToGG_mva()',
    'ZHiggs0L1Zgf05ph0ToGG_MVA := ZHiggs0L1Zgf05ph0ToGG_mva()'
]

Anom_vars = [
'Anom_mva_pho1_eta := Anom_MVA_pho1_eta()',
'Anom_mva_pho1_phi := Anom_MVA_pho1_phi()',
'Anom_mva_pho1_idmva := Anom_MVA_pho1_idmva()',
'Anom_mva_pho1_full5x5_r9 := Anom_MVA_pho1_full5x5_r9()',
'Anom_mva_pho1_ptOverMgg := Anom_MVA_pho1_ptOverMgg()',
'Anom_mva_pho2_eta := Anom_MVA_pho2_eta()',
'Anom_mva_pho2_phi := Anom_MVA_pho2_phi()',
'Anom_mva_pho2_idmva := Anom_MVA_pho2_idmva()',
'Anom_mva_pho2_full5x5_r9 := Anom_MVA_pho2_full5x5_r9()',
'Anom_mva_pho2_ptOverMgg := Anom_MVA_pho2_ptOverMgg()',
'Anom_mva_mu1_pt := Anom_MVA_mu1_pt()',
'Anom_mva_mu1_eta := Anom_MVA_mu1_eta()',
'Anom_mva_mu1_phi := Anom_MVA_mu1_phi()',
'Anom_mva_mu1_energy := Anom_MVA_mu1_energy()',
'Anom_mva_mu2_pt := Anom_MVA_mu2_pt()',
'Anom_mva_mu2_eta := Anom_MVA_mu2_eta()',
'Anom_mva_mu2_phi := Anom_MVA_mu2_phi()',
'Anom_mva_mu2_energy := Anom_MVA_mu2_energy()',
'Anom_mva_ele1_pt := Anom_MVA_ele1_pt()',
'Anom_mva_ele1_eta := Anom_MVA_ele1_eta()',
'Anom_mva_ele1_phi := Anom_MVA_ele1_phi()',
'Anom_mva_ele1_energy := Anom_MVA_ele1_energy()',
'Anom_mva_ele2_pt := Anom_MVA_ele2_pt()',
'Anom_mva_ele2_eta := Anom_MVA_ele2_eta()',
'Anom_mva_ele2_phi := Anom_MVA_ele2_phi()',
'Anom_mva_ele2_energy := Anom_MVA_ele2_energy()',
'Anom_mva_jet1_pt := Anom_MVA_jet1_pt()',
'Anom_mva_jet1_phi := Anom_MVA_jet1_phi()',
'Anom_mva_jet1_eta := Anom_MVA_jet1_eta()',
'Anom_mva_jet1_energy := Anom_MVA_jet1_energy()',
'Anom_mva_jet2_pt := Anom_MVA_jet2_pt()',
'Anom_mva_jet2_phi := Anom_MVA_jet2_phi()',
'Anom_mva_jet2_eta := Anom_MVA_jet2_eta()',
'Anom_mva_jet2_energy := Anom_MVA_jet2_energy()',
'Anom_mva_cosPhiGG := Anom_MVA_cosPhiGG()',
'Anom_mva_cosPhiG1_Mu1 := Anom_MVA_cosPhiG1_Mu1()',
'Anom_mva_cosPhiG1_Ele1 := Anom_MVA_cosPhiG1_Ele1()',
'Anom_mva_cosPhiG2_Mu1 := Anom_MVA_cosPhiG2_Mu1()',
'Anom_mva_cosPhiG2_Ele1 := Anom_MVA_cosPhiG2_Ele1()',
'Anom_mva_dR_Pho1Ele1_wh := Anom_MVA_dR_Pho1Ele1_wh()',
'Anom_mva_dR_Pho2Ele1_wh := Anom_MVA_dR_Pho2Ele1_wh()',
'Anom_mva_dR_Pho1Mu1_wh := Anom_MVA_dR_Pho1Mu1_wh()',
'Anom_mva_dR_Pho2Mu1_wh := Anom_MVA_dR_Pho2Mu1_wh()',
'Anom_mva_dR_Pho1Jet1_wh := Anom_MVA_dR_Pho1Jet1_wh()',
'Anom_mva_dR_Pho1Jet2_wh := Anom_MVA_dR_Pho1Jet2_wh()',
'Anom_mva_dR_Pho2Jet1_wh := Anom_MVA_dR_Pho2Jet1_wh()',
'Anom_mva_dR_Pho2Jet2_wh := Anom_MVA_dR_Pho2Jet2_wh()',
'Anom_mva_dR_Mu1Jet1_wh := Anom_MVA_dR_Mu1Jet1_wh()',
'Anom_mva_dR_Mu1Jet2_wh := Anom_MVA_dR_Mu1Jet2_wh()',
'Anom_mva_dR_Ele1Jet1_wh := Anom_MVA_dR_Ele1Jet1_wh()',
'Anom_mva_dR_Ele1Jet2_wh := Anom_MVA_dR_Ele1Jet2_wh()',
]

diphoton_variables = ["mass            := diPhoton.mass",
                      "diphoton_pt     := diPhoton.pt",
                      "diphoton_mva    := diPhotonMVA.result",
                      "pho1_pt         := diPhoton.leadingPhoton.pt",
                      "pho1_eta        := diPhoton.leadingPhoton.eta",
                      "pho1_phi        := diPhoton.leadingPhoton.phi",
                      "pho1_energy     := diPhoton.leadingPhoton.energy",
                      "pho1_full5x5_r9 := diPhoton.leadingPhoton.full5x5_r9",
                      "pho1_idmva      := diPhoton.leadPhotonId",
                      "pho1_genMatchType:=diPhoton.leadingPhoton.genMatchType",
                      "pho2_pt         := diPhoton.subLeadingPhoton.pt",
                      "pho2_eta        := diPhoton.subLeadingPhoton.eta",
                      "pho2_phi        := diPhoton.subLeadingPhoton.phi",
                      "pho2_energy     := diPhoton.subLeadingPhoton.energy",
                      "pho2_full5x5_r9 := diPhoton.subLeadingPhoton.full5x5_r9",
                      "pho2_idmva      := diPhoton.subLeadPhotonId",
                      "pho2_genMatchType:=diPhoton.subLeadingPhoton.genMatchType",
                      "pho1_ptOverMgg  := diPhoton.leadingPhoton.pt/diPhoton.mass",
                      "pho2_ptOverMgg  := diPhoton.subLeadingPhoton.pt/diPhoton.mass",
                      ]


leptons_variables = [ "mu1_pt         :=  ? muons.size()>0 ? muons[0].pt() : -100 ",
                      "mu1_phi        :=  ? muons.size()>0 ? muons[0].phi() : -100 ",
                      "mu1_eta        :=  ? muons.size()>0 ? muons[0].eta() : -100 ",
                      "mu1_energy     :=  ? muons.size()>0 ? muons[0].energy() : -100 ",
                      "mu2_pt         :=  ? muons.size()>1 ? muons[1].pt() : -100 ",
                      "mu2_phi        :=  ? muons.size()>1 ? muons[1].phi() : -100 ",
                      "mu2_eta        :=  ? muons.size()>1 ? muons[1].eta() : -100 ",
                      "mu2_energy     :=  ? muons.size()>1 ? muons[1].energy() : -100 ",
                      "ele1_pt        :=  ? electrons.size()>0 ? electrons[0].pt() : -100 ",
                      "ele1_phi       :=  ? electrons.size()>0 ? electrons[0].phi() : -100 ",
                      "ele1_eta       :=  ? electrons.size()>0 ? electrons[0].eta() : -100 ",
                      "ele1_energy    :=  ? electrons.size()>0 ? electrons[0].energy() : -100 ",
                      "ele2_pt        :=  ? electrons.size()>1 ? electrons[1].pt() : -100 ",
                      "ele2_phi       :=  ? electrons.size()>1 ? electrons[1].phi() : -100 ",
                      "ele2_eta       :=  ? electrons.size()>1 ? electrons[1].eta() : -100 ",
                      "ele2_energy    :=  ? electrons.size()>1 ? electrons[1].energy() : -100 ",
                      "nMuons         :=  muons.size()",
                      "nEle           :=  electrons.size()"
                     ]

jets_variables = ["njets := jets.size()",
                  "jet1_pt     :=  ? jets.size()>0 ? jets[0].pt : -100 ",
                  "jet1_phi    :=  ? jets.size()>0 ? jets[0].phi : -100 ",
                  "jet1_eta    :=  ? jets.size()>0 ? jets[0].eta : -100 ",
                  "jet1_energy :=  ? jets.size()>0 ? jets[0].energy : -100 ",
                  "jet2_pt     :=  ? jets.size()>1 ? jets[1].pt : -100 ",
                  "jet2_phi    :=  ? jets.size()>1 ? jets[1].phi : -100 ",
                  "jet2_eta    :=  ? jets.size()>1 ? jets[1].eta : -100 ",
                  "jet2_energy :=  ? jets.size()>1 ? jets[1].energy : -100 ",
                  "jet3_pt     :=  ? jets.size()>2 ? jets[2].pt : -100 ",
                  "jet3_phi    :=  ? jets.size()>2 ? jets[2].phi : -100 ",
                  "jet3_eta    :=  ? jets.size()>2 ? jets[2].eta : -100 ",
                  "jet3_energy :=  ? jets.size()>2 ? jets[2].energy : -100 ",
                  "jet4_pt     :=  ? jets.size()>3 ? jets[3].pt : -100 ",
                  "jet4_phi    :=  ? jets.size()>3 ? jets[3].phi : -100 ",
                  "jet4_eta    :=  ? jets.size()>3 ? jets[3].eta : -100 ",
                  "jet4_energy :=  ? jets.size()>3 ? jets[3].energy : -100 ",
                  "jet5_pt     :=  ? jets.size()>4 ? jets[4].pt : -100 ",
                  "jet5_phi    :=  ? jets.size()>4 ? jets[4].phi : -100 ",
                  "jet5_eta    :=  ? jets.size()>4 ? jets[4].eta : -100 ",
                  "jet5_energy :=  ? jets.size()>4 ? jets[4].energy : -100 ",
                  "jet6_pt     :=  ? jets.size()>5 ? jets[5].pt : -100 ",
                  "jet6_phi    :=  ? jets.size()>5 ? jets[5].phi : -100 ",
                  "jet6_eta    :=  ? jets.size()>5 ? jets[5].eta : -100 ",
                  "jet6_energy :=  ? jets.size()>5 ? jets[5].energy : -100 ",
                  "jet7_pt     :=  ? jets.size()>6 ? jets[6].pt : -100 ",
                  "jet7_phi    :=  ? jets.size()>6 ? jets[6].phi : -100 ",
                  "jet7_eta    :=  ? jets.size()>6 ? jets[6].eta : -100 ",
                  "jet7_energy :=  ? jets.size()>6 ? jets[6].energy : -100 "
                  ]

met_variables = ["met_pt  := met.corPt()",
                 "met_phi := met.corPhi()"]


gen_variables = ["hasZ := tagTruth().associatedZ",
                 "hasW := tagTruth().associatedW",
                 "VhasL := tagTruth().VhasLeptons",
                 "VhasNu := tagTruth().VhasNeutrinos",
                 "VhasQ := tagTruth().VhasHadrons"
                 ]

#dR_variables_WHLeptonic = [ "dR_Pho1Jet1_wh :=  ? jets.size() > 0 ? whleptonictags_obj.deltaRPho1Jet1 : -100"
dR_variables_WHLeptonic = ["dR_Pho1Jet1_wh :=  ? jets.size() > 0 ? deltaR(jets[0].eta, jets[0].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                           "dR_Pho1Jet2_wh :=  ? jets.size() > 1 ? deltaR(jets[1].eta, jets[1].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",  
                           "dR_Pho2Jet1_wh :=  ? jets.size() > 0 ? deltaR(jets[0].eta, jets[0].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
                           "dR_Pho2Jet2_wh :=  ? jets.size() > 1 ? deltaR(jets[1].eta, jets[1].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
                           "dR_Pho1Ele1_wh :=  ? electrons.size() > 0 ? deltaR(electrons[0].eta, electrons[0].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                           "dR_Pho1Ele2_wh :=  ? electrons.size() > 1 ? deltaR(electrons[1].eta, electrons[1].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",                           
                           "dR_Pho2Ele1_wh :=  ? electrons.size() > 0 ? deltaR(electrons[0].eta, electrons[0].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",                          
                           "dR_Pho2Ele2_wh :=  ? electrons.size() > 1 ? deltaR(electrons[1].eta, electrons[1].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
                           "dR_Pho1Ele3_wh :=  ? electrons.size() > 2 ? deltaR(electrons[2].eta, electrons[2].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                           "dR_Pho2Ele3_wh :=  ? electrons.size() > 2 ? deltaR(electrons[2].eta, electrons[2].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",                          
                           "dR_Pho1Ele4_wh :=  ? electrons.size() > 3 ? deltaR(electrons[3].eta, electrons[3].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                           "dR_Pho2Ele4_wh :=  ? electrons.size() > 3 ? deltaR(electrons[3].eta, electrons[3].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",                          
                           "dR_Pho1Ele5_wh :=  ? electrons.size() > 4 ? deltaR(electrons[4].eta, electrons[4].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                           "dR_Pho2Ele5_wh :=  ? electrons.size() > 4 ? deltaR(electrons[4].eta, electrons[4].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",                          
                           "dR_Pho1Mu1_wh  :=  ? muons.size() > 0 ? deltaR(muons[0].eta, muons[0].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                           "dR_Pho1Mu2_wh  :=  ? muons.size() > 1 ? deltaR(muons[1].eta, muons[1].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                           "dR_Pho2Mu1_wh  :=  ? muons.size() > 0 ? deltaR(muons[0].eta, muons[0].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
                           "dR_Pho2Mu2_wh  :=  ? muons.size() > 1 ? deltaR(muons[1].eta, muons[1].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
                           "dR_Mu1Jet1_wh  :=  ? (muons.size() > 0 && jets.size() > 0) ? deltaR(muons[0].eta, muons[0].phi, jets[0].eta, jets[0].phi) : -100 ",
                           "dR_Mu1Jet2_wh  :=  ? (muons.size() > 0 && jets.size() > 1) ? deltaR(muons[0].eta, muons[0].phi, jets[1].eta, jets[1].phi) : -100 ",
                           "dR_Mu2Jet1_wh  :=  ? (muons.size() > 1 && jets.size() > 0) ? deltaR(muons[1].eta, muons[1].phi, jets[0].eta, jets[0].phi) : -100 ",
                           "dR_Mu2Jet2_wh  :=  ? (muons.size() > 1 && jets.size() > 1) ? deltaR(muons[1].eta, muons[1].phi, jets[1].eta, jets[1].phi) : -100 ",
                           "dR_Mu1Jet3_wh  :=  ? (muons.size() > 0 && jets.size() > 2) ? deltaR(muons[0].eta, muons[0].phi, jets[2].eta, jets[2].phi) : -100 ",
                           "dR_Mu2Jet3_wh  :=  ? (muons.size() > 1 && jets.size() > 2) ? deltaR(muons[1].eta, muons[1].phi, jets[2].eta, jets[2].phi) : -100 ",
                           "dR_Mu1Jet4_wh  :=  ? (muons.size() > 0 && jets.size() > 3) ? deltaR(muons[0].eta, muons[0].phi, jets[3].eta, jets[3].phi) : -100 ",
                           "dR_Mu2Jet4_wh  :=  ? (muons.size() > 1 && jets.size() > 3) ? deltaR(muons[1].eta, muons[1].phi, jets[3].eta, jets[3].phi) : -100 ",
                           "dR_Mu1Jet5_wh  :=  ? (muons.size() > 0 && jets.size() > 4) ? deltaR(muons[0].eta, muons[0].phi, jets[4].eta, jets[4].phi) : -100 ",
                           "dR_Mu2Jet5_wh  :=  ? (muons.size() > 1 && jets.size() > 4) ? deltaR(muons[1].eta, muons[1].phi, jets[4].eta, jets[4].phi) : -100 ",
                           "dR_Mu1Jet6_wh  :=  ? (muons.size() > 0 && jets.size() > 5) ? deltaR(muons[0].eta, muons[0].phi, jets[5].eta, jets[5].phi) : -100 ",
                           "dR_Mu2Jet6_wh  :=  ? (muons.size() > 1 && jets.size() > 5) ? deltaR(muons[1].eta, muons[1].phi, jets[5].eta, jets[5].phi) : -100 ",
                           "dR_Mu1Jet7_wh  :=  ? (muons.size() > 0 && jets.size() > 6) ? deltaR(muons[0].eta, muons[0].phi, jets[6].eta, jets[6].phi) : -100 ",
                           "dR_Mu2Jet7_wh  :=  ? (muons.size() > 1 && jets.size() > 6) ? deltaR(muons[1].eta, muons[1].phi, jets[6].eta, jets[6].phi) : -100 ",
                           "dR_Mu3Jet1_wh  :=  ? (muons.size() > 2 && jets.size() > 0) ? deltaR(muons[2].eta, muons[2].phi, jets[0].eta, jets[0].phi) : -100 ",
                           "dR_Mu3Jet2_wh  :=  ? (muons.size() > 2 && jets.size() > 1) ? deltaR(muons[2].eta, muons[2].phi, jets[1].eta, jets[1].phi) : -100 ",
                           "dR_Mu3Jet3_wh  :=  ? (muons.size() > 2 && jets.size() > 2) ? deltaR(muons[2].eta, muons[2].phi, jets[2].eta, jets[2].phi) : -100 ",
                           "dR_Mu3Jet4_wh  :=  ? (muons.size() > 2 && jets.size() > 3) ? deltaR(muons[2].eta, muons[2].phi, jets[3].eta, jets[3].phi) : -100 ",
                           "dR_Mu3Jet5_wh  :=  ? (muons.size() > 2 && jets.size() > 4) ? deltaR(muons[2].eta, muons[2].phi, jets[4].eta, jets[4].phi) : -100 ",
                           "dR_Mu3Jet6_wh  :=  ? (muons.size() > 2 && jets.size() > 5) ? deltaR(muons[2].eta, muons[2].phi, jets[5].eta, jets[5].phi) : -100 ",
                           "dR_Mu3Jet7_wh  :=  ? (muons.size() > 2 && jets.size() > 6) ? deltaR(muons[2].eta, muons[2].phi, jets[6].eta, jets[6].phi) : -100 ",  
                           "dR_Mu4Jet1_wh  :=  ? (muons.size() > 3 && jets.size() > 0) ? deltaR(muons[3].eta, muons[3].phi, jets[0].eta, jets[0].phi) : -100 ",
                           "dR_Mu4Jet2_wh  :=  ? (muons.size() > 3 && jets.size() > 1) ? deltaR(muons[3].eta, muons[3].phi, jets[1].eta, jets[1].phi) : -100 ",
                           "dR_Mu4Jet3_wh  :=  ? (muons.size() > 3 && jets.size() > 2) ? deltaR(muons[3].eta, muons[3].phi, jets[2].eta, jets[2].phi) : -100 ",
                           "dR_Mu4Jet4_wh  :=  ? (muons.size() > 3 && jets.size() > 3) ? deltaR(muons[3].eta, muons[3].phi, jets[3].eta, jets[3].phi) : -100 ",
                           "dR_Mu4Jet5_wh  :=  ? (muons.size() > 3 && jets.size() > 4) ? deltaR(muons[3].eta, muons[3].phi, jets[4].eta, jets[4].phi) : -100 ",
                           "dR_Mu4Jet6_wh  :=  ? (muons.size() > 3 && jets.size() > 5) ? deltaR(muons[3].eta, muons[3].phi, jets[5].eta, jets[5].phi) : -100 ",
                           "dR_Mu4Jet7_wh  :=  ? (muons.size() > 3 && jets.size() > 6) ? deltaR(muons[3].eta, muons[3].phi, jets[6].eta, jets[6].phi) : -100 ",  
                           "dR_Mu5Jet1_wh  :=  ? (muons.size() > 4 && jets.size() > 0) ? deltaR(muons[4].eta, muons[4].phi, jets[0].eta, jets[0].phi) : -100 ",
                           "dR_Mu5Jet2_wh  :=  ? (muons.size() > 4 && jets.size() > 1) ? deltaR(muons[4].eta, muons[4].phi, jets[1].eta, jets[1].phi) : -100 ",
                           "dR_Mu5Jet3_wh  :=  ? (muons.size() > 4 && jets.size() > 2) ? deltaR(muons[4].eta, muons[4].phi, jets[2].eta, jets[2].phi) : -100 ",
                           "dR_Mu5Jet4_wh  :=  ? (muons.size() > 4 && jets.size() > 3) ? deltaR(muons[4].eta, muons[4].phi, jets[3].eta, jets[3].phi) : -100 ",
                           "dR_Mu5Jet5_wh  :=  ? (muons.size() > 4 && jets.size() > 4) ? deltaR(muons[4].eta, muons[4].phi, jets[4].eta, jets[4].phi) : -100 ",
                           "dR_Mu5Jet6_wh  :=  ? (muons.size() > 4 && jets.size() > 5) ? deltaR(muons[4].eta, muons[4].phi, jets[5].eta, jets[5].phi) : -100 ",
                           "dR_Mu5Jet7_wh  :=  ? (muons.size() > 4 && jets.size() > 6) ? deltaR(muons[4].eta, muons[4].phi, jets[6].eta, jets[6].phi) : -100 ", 
                           "dR_Ele1Jet1_wh  :=  ? (electrons.size() > 0 && jets.size() > 0) ? deltaR(electrons[0].eta, electrons[0].phi, jets[0].eta, jets[0].phi) : -100 ",
                           "dR_Ele1Jet2_wh  :=  ? (electrons.size() > 0 && jets.size() > 1) ? deltaR(electrons[0].eta, electrons[0].phi, jets[1].eta, jets[1].phi) : -100 ",
                           "dR_Ele2Jet1_wh  :=  ? (electrons.size() > 1 && jets.size() > 0) ? deltaR(electrons[1].eta, electrons[1].phi, jets[0].eta, jets[0].phi) : -100 ",
                           "dR_Ele2Jet2_wh  :=  ? (electrons.size() > 1 && jets.size() > 1) ? deltaR(electrons[1].eta, electrons[1].phi, jets[1].eta, jets[1].phi) : -100 ",
                           "dR_Ele1Jet3_wh  :=  ? (electrons.size() > 0 && jets.size() > 2) ? deltaR(electrons[0].eta, electrons[0].phi, jets[2].eta, jets[2].phi) : -100 ",
                           "dR_Ele2Jet3_wh  :=  ? (electrons.size() > 1 && jets.size() > 2) ? deltaR(electrons[1].eta, electrons[1].phi, jets[2].eta, jets[2].phi) : -100 ",
                           "dR_Ele1Jet4_wh  :=  ? (electrons.size() > 0 && jets.size() > 3) ? deltaR(electrons[0].eta, electrons[0].phi, jets[3].eta, jets[3].phi) : -100 ",
                           "dR_Ele2Jet4_wh  :=  ? (electrons.size() > 1 && jets.size() > 3) ? deltaR(electrons[1].eta, electrons[1].phi, jets[3].eta, jets[3].phi) : -100 ",
                           "dR_Ele1Jet5_wh  :=  ? (electrons.size() > 0 && jets.size() > 4) ? deltaR(electrons[0].eta, electrons[0].phi, jets[4].eta, jets[4].phi) : -100 ",
                           "dR_Ele2Jet5_wh  :=  ? (electrons.size() > 1 && jets.size() > 4) ? deltaR(electrons[1].eta, electrons[1].phi, jets[4].eta, jets[4].phi) : -100 ",
                           "dR_Ele1Jet6_wh  :=  ? (electrons.size() > 0 && jets.size() > 5) ? deltaR(electrons[0].eta, electrons[0].phi, jets[5].eta, jets[5].phi) : -100 ",
                           "dR_Ele2Jet6_wh  :=  ? (electrons.size() > 1 && jets.size() > 5) ? deltaR(electrons[1].eta, electrons[1].phi, jets[5].eta, jets[5].phi) : -100 ",
                           "dR_Ele1Jet7_wh  :=  ? (electrons.size() > 0 && jets.size() > 6) ? deltaR(electrons[0].eta, electrons[0].phi, jets[6].eta, jets[6].phi) : -100 ",
                           "dR_Ele2Jet7_wh  :=  ? (electrons.size() > 1 && jets.size() > 6) ? deltaR(electrons[1].eta, electrons[1].phi, jets[6].eta, jets[6].phi) : -100 ",
                           "dR_Ele3Jet1_wh  :=  ? (electrons.size() > 2 && jets.size() > 0) ? deltaR(electrons[2].eta, electrons[2].phi, jets[0].eta, jets[0].phi) : -100 ",
                           "dR_Ele3Jet2_wh  :=  ? (electrons.size() > 2 && jets.size() > 1) ? deltaR(electrons[2].eta, electrons[2].phi, jets[1].eta, jets[1].phi) : -100 ",
                           "dR_Ele3Jet3_wh  :=  ? (electrons.size() > 2 && jets.size() > 2) ? deltaR(electrons[2].eta, electrons[2].phi, jets[2].eta, jets[2].phi) : -100 ",
                           "dR_Ele3Jet4_wh  :=  ? (electrons.size() > 2 && jets.size() > 3) ? deltaR(electrons[2].eta, electrons[2].phi, jets[3].eta, jets[3].phi) : -100 ",
                           "dR_Ele3Jet5_wh  :=  ? (electrons.size() > 2 && jets.size() > 4) ? deltaR(electrons[2].eta, electrons[2].phi, jets[4].eta, jets[4].phi) : -100 ",
                           "dR_Ele3Jet6_wh  :=  ? (electrons.size() > 2 && jets.size() > 5) ? deltaR(electrons[2].eta, electrons[2].phi, jets[5].eta, jets[5].phi) : -100 ",
                           "dR_Ele3Jet7_wh  :=  ? (electrons.size() > 2 && jets.size() > 6) ? deltaR(electrons[2].eta, electrons[2].phi, jets[6].eta, jets[6].phi) : -100 ",  
                           "dR_Ele4Jet1_wh  :=  ? (electrons.size() > 3 && jets.size() > 0) ? deltaR(electrons[3].eta, electrons[3].phi, jets[0].eta, jets[0].phi) : -100 ",
                           "dR_Ele4Jet2_wh  :=  ? (electrons.size() > 3 && jets.size() > 1) ? deltaR(electrons[3].eta, electrons[3].phi, jets[1].eta, jets[1].phi) : -100 ",
                           "dR_Ele4Jet3_wh  :=  ? (electrons.size() > 3 && jets.size() > 2) ? deltaR(electrons[3].eta, electrons[3].phi, jets[2].eta, jets[2].phi) : -100 ",
                           "dR_Ele4Jet4_wh  :=  ? (electrons.size() > 3 && jets.size() > 3) ? deltaR(electrons[3].eta, electrons[3].phi, jets[3].eta, jets[3].phi) : -100 ",
                           "dR_Ele4Jet5_wh  :=  ? (electrons.size() > 3 && jets.size() > 4) ? deltaR(electrons[3].eta, electrons[3].phi, jets[4].eta, jets[4].phi) : -100 ",
                           "dR_Ele4Jet6_wh  :=  ? (electrons.size() > 3 && jets.size() > 5) ? deltaR(electrons[3].eta, electrons[3].phi, jets[5].eta, jets[5].phi) : -100 ",
                           "dR_Ele4Jet7_wh  :=  ? (electrons.size() > 3 && jets.size() > 6) ? deltaR(electrons[3].eta, electrons[3].phi, jets[6].eta, jets[6].phi) : -100 ",  
                           "dR_Ele5Jet1_wh  :=  ? (electrons.size() > 4 && jets.size() > 0) ? deltaR(electrons[4].eta, electrons[4].phi, jets[0].eta, jets[0].phi) : -100 ",
                           "dR_Ele5Jet2_wh  :=  ? (electrons.size() > 4 && jets.size() > 1) ? deltaR(electrons[4].eta, electrons[4].phi, jets[1].eta, jets[1].phi) : -100 ",
                           "dR_Ele5Jet3_wh  :=  ? (electrons.size() > 4 && jets.size() > 2) ? deltaR(electrons[4].eta, electrons[4].phi, jets[2].eta, jets[2].phi) : -100 ",
                           "dR_Ele5Jet4_wh  :=  ? (electrons.size() > 4 && jets.size() > 3) ? deltaR(electrons[4].eta, electrons[4].phi, jets[3].eta, jets[3].phi) : -100 ",
                           "dR_Ele5Jet5_wh  :=  ? (electrons.size() > 4 && jets.size() > 4) ? deltaR(electrons[4].eta, electrons[4].phi, jets[4].eta, jets[4].phi) : -100 ",
                           "dR_Ele5Jet6_wh  :=  ? (electrons.size() > 4 && jets.size() > 5) ? deltaR(electrons[4].eta, electrons[4].phi, jets[5].eta, jets[5].phi) : -100 ",
                           "dR_Ele5Jet7_wh  :=  ? (electrons.size() > 4 && jets.size() > 6) ? deltaR(electrons[4].eta, electrons[4].phi, jets[6].eta, jets[6].phi) : -100 ",                      
                           "dR_Pho1Jet3_wh :=  ? jets.size() > 2 ? deltaR(jets[2].eta, jets[2].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                           "dR_Pho2Jet3_wh :=  ? jets.size() > 2 ? deltaR(jets[2].eta, jets[2].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
                           "dR_Pho1Jet4_wh :=  ? jets.size() > 3 ? deltaR(jets[3].eta, jets[3].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                           "dR_Pho2Jet4_wh :=  ? jets.size() > 3 ? deltaR(jets[3].eta, jets[3].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
                           "dR_Pho1Jet5_wh :=  ? jets.size() > 4 ? deltaR(jets[4].eta, jets[4].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                           "dR_Pho2Jet5_wh :=  ? jets.size() > 4 ? deltaR(jets[4].eta, jets[4].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
                           "dR_Pho1Jet6_wh :=  ? jets.size() > 5 ? deltaR(jets[5].eta, jets[5].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                           "dR_Pho2Jet6_wh :=  ? jets.size() > 5 ? deltaR(jets[5].eta, jets[5].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
                           "dR_Pho1Jet7_wh :=  ? jets.size() > 6 ? deltaR(jets[6].eta, jets[6].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                           "dR_Pho2Jet7_wh :=  ? jets.size() > 6 ? deltaR(jets[6].eta, jets[6].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100"
]

dR_variables_VHLeptonicLoose = ["dR_Pho1Ele1_zh := ? electrons.size() > 0 ? deltaR(electrons[0].eta, electrons[0].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                                "dR_Pho1Ele2_zh := ? electrons.size() > 1 ? deltaR(electrons[1].eta, electrons[1].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                                "dR_Pho2Ele1_zh := ? electrons.size() > 0 ? deltaR(electrons[0].eta, electrons[0].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
                                "dR_Pho1Ele2_zh := ? electrons.size() > 1 ? deltaR(electrons[1].eta, electrons[1].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
                                "dR_Pho1Mu1_zh  := ? muons.size() > 0 ? deltaR(muons[0].eta, muons[0].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                                "dR_Pho1Mu2_zh  := ? muons.size() > 1 ? deltaR(muons[1].eta, muons[1].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                                "dR_Pho2Mu1_zh  := ? muons.size() > 0 ? deltaR(muons[0].eta, muons[0].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
                                "dR_Pho2Mu2_zh  := ? muons.size() > 1 ? deltaR(muons[1].eta, muons[1].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100"
]

dR_variables_ZHLeptonic = ["dR_Pho1Jet1_loose :=  ? jets.size() > 0 ? deltaR(jets[0].eta, jets[0].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                           "dR_Pho1Jet2_loose :=  ? jets.size() > 1 ? deltaR(jets[1].eta, jets[1].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",  
                           "dR_Pho2Jet1_loose :=  ? jets.size() > 0 ? deltaR(jets[0].eta, jets[0].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
                           "dR_Pho2Jet2_loose :=  ? jets.size() > 1 ? deltaR(jets[1].eta, jets[1].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
                           "dR_Pho1Ele1_loose :=  ? electrons.size() > 0 ? deltaR(electrons[0].eta, electrons[0].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                           "dR_Pho1Ele2_loose :=  ? electrons.size() > 1 ? deltaR(electrons[1].eta, electrons[1].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",                           
                           "dR_Pho2Ele1_loose :=  ? electrons.size() > 0 ? deltaR(electrons[0].eta, electrons[0].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",                          
                           "dR_Pho2Ele2_loose :=  ? electrons.size() > 1 ? deltaR(electrons[1].eta, electrons[1].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
                           "dR_Pho1Mu1_loose  :=  ? muons.size() > 0 ? deltaR(muons[0].eta, muons[0].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                           "dR_Pho1Mu2_loose  :=  ? muons.size() > 1 ? deltaR(muons[1].eta, muons[1].phi, diPhoton.leadingPhoton.eta, diPhoton.leadingPhoton.phi) : -100",
                           "dR_Pho2Mu1_loose  :=  ? muons.size() > 0 ? deltaR(muons[0].eta, muons[0].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
                           "dR_Pho2Mu2_loose  :=  ? muons.size() > 1 ? deltaR(muons[1].eta, muons[1].phi, diPhoton.subLeadingPhoton.eta, diPhoton.subLeadingPhoton.phi) : -100",
                           "dR_Mu1Jet1_loose  :=  ? (muons.size() > 0 && jets.size() > 0) ? deltaR(muons[0].eta, muons[0].phi, jets[0].eta, jets[0].phi) : -100 ",
                           "dR_Mu1Jet2_loose  :=  ? (muons.size() > 0 && jets.size() > 1) ? deltaR(muons[0].eta, muons[0].phi, jets[1].eta, jets[1].phi) : -100 ",
                           "dR_Mu2Jet1_loose  :=  ? (muons.size() > 1 && jets.size() > 0) ? deltaR(muons[1].eta, muons[1].phi, jets[0].eta, jets[0].phi) : -100 ",
                           "dR_Mu2Jet2_loose  :=  ? (muons.size() > 1 && jets.size() > 1) ? deltaR(muons[1].eta, muons[1].phi, jets[1].eta, jets[1].phi) : -100 ",
                           "dR_Ele1Jet1_loose  :=  ? (electrons.size() > 0 && jets.size() > 0) ? deltaR(electrons[0].eta, electrons[0].phi, jets[0].eta, jets[0].phi) : -100 ",
                           "dR_Ele1Jet2_loose  :=  ? (electrons.size() > 0 && jets.size() > 1) ? deltaR(electrons[0].eta, electrons[0].phi, jets[1].eta, jets[1].phi) : -100 ",
                           "dR_Ele2Jet1_loose  :=  ? (electrons.size() > 1 && jets.size() > 0) ? deltaR(electrons[1].eta, electrons[1].phi, jets[0].eta, jets[0].phi) : -100 ",
                           "dR_Ele2Jet2_loose  :=  ? (electrons.size() > 1 && jets.size() > 1) ? deltaR(electrons[1].eta, electrons[1].phi, jets[1].eta, jets[1].phi) : -100 "
]




WH_anomalous_dumper_variables = diphoton_variables + leptons_variables + dR_variables_WHLeptonic +jets_variables + custom_vars + Anom_vars




for tag in tagList: 
  tagName=tag[0]
  tagCats=tag[1]
  # remap return value of class-based classifier
  process.tagsDumper.classifierCfg.remap.append( cms.untracked.PSet( src=cms.untracked.string("flashgg%s"%tagName), dst=cms.untracked.string(tagName) ) )
  for systlabel in systlabels:
      if not systlabel in definedSysts:
          # the cut corresponding to the systematics can be defined just once
          cutstring = "hasSyst(\"%s\") "%(systlabel)
          definedSysts.add(systlabel)
      else:
          cutstring = None
      if systlabel == "":
          currentVariables = copy.deepcopy(variablesToUse)
      else:
          if customize.doHTXS:
              currentVariables = copy.deepcopy(systematicVariablesHTXS)
          else:    
              currentVariables = copy.deepcopy(systematicVariables)
      if tagName.upper().count("NOTAG"):
          if customize.doHTXS:
              currentVariables = ["stage0bin[72,9.5,81.5] := tagTruth().HTXSstage0bin"]
          elif customize.doStageOne:
              currentVariables = copy.deepcopy(soc.noTagVariables())
          else:
              currentVariables = []
      isBinnedOnly = (systlabel !=  "")
      is_signal = reduce(lambda y,z: y or z, map(lambda x: customize.processId.count(x), signal_processes))
      if ( customize.doPdfWeights and customize.doSystematics ) and ( (customize.datasetName() and customize.datasetName().count("HToGG")) or customize.processId.count("h_") or customize.processId.count("vbf_") or is_signal ) and (systlabel ==  "") and not (customize.processId.count("bbh_") or customize.processId.count("thw_") or customize.processId.count("thq_")):
          #print "Signal MC central value, so dumping PDF weights"
          dumpPdfWeights = True
          nPdfWeights = 60
          nAlphaSWeights = 2
          nScaleWeights = 9
      else:
          #print "Data, background MC, or non-central value, or no systematics: no PDF weights"
          dumpPdfWeights = False
          nPdfWeights = -1
          nAlphaSWeights = -1
          nScaleWeights = -1

      if systlabel == "":
         if tagName in tag_only_variables.keys():
            currentVariables += tag_only_variables[tagName]

      if tagName == "WHLeptonicTag":#or tagName == "ZHLeptonicTag":# or tagName == "VHMetTag":
           currentVariables += WH_anomalous_dumper_variables+WH_Anom_Vars # if tagname is WHLeptonic, dumps the additional variables...
      elif tagName == "ZHLeptonicTag":
           currentVariables += WH_anomalous_dumper_variables+ZH_Anom_Vars
      cfgTools.addCategory(process.tagsDumper,
                           systlabel,
                           classname=tagName,
                           cutbased=cutstring,
                           subcats=tagCats, 
                           variables=currentVariables,
                           histograms=minimalHistograms,
                           binnedOnly=isBinnedOnly,
                           dumpPdfWeights=dumpPdfWeights,
                           nPdfWeights=nPdfWeights,
                           nAlphaSWeights=nAlphaSWeights,
                           nScaleWeights=nScaleWeights,
                           splitPdfByStage0Bin=customize.doHTXS,
                           splitPdfByStage1Bin=customize.doStageOne,
                           dumpGenWeight=customize.dumpGenWeight
                           )

# Require standard diphoton trigger
filterHLTrigger(process, customize)

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

process.dataRequirements = cms.Sequence()
if customize.processId == "Data":
        process.dataRequirements += process.hltHighLevel

# Split WH and ZH
process.genFilter = cms.Sequence()
if ((customize.processId.count("wh") or customize.processId.count("zh")) and not (customize.processId.count("powheg"))) and not customize.processId.count("wzh") :
    print "enabling vh filter!!!!!"
    process.load("flashgg/Systematics/VHFilter_cfi")
    process.genFilter += process.VHFilter
    process.VHFilter.chooseW = bool(customize.processId.count("wh"))
    process.VHFilter.chooseZ = bool(customize.processId.count("zh"))

#no longer needed, we can pass these samples through the usual STXS classification code now
#if (customize.processId == "th_125" or customize.processId == "bbh_125"):
#    process.load("flashgg/Systematics/CentralHiggsFilter_cfi")
#    process.genFilter += process.CentralHiggsFilter

#pythia8 has an unanticipated EM showering feature, check have two photons from hard scatter
process.penultimateFilter= cms.Sequence()
if customize.processId == "th_125": # for this sample the filter removes also H -> ZG
    process.load("flashgg/Systematics/HardProcessFinalStateFilter_cfi")
#    process.HardProcessFinalStateFilter.debug = True
    process.penultimateFilter += process.HardProcessFinalStateFilter

# Split out prompt-fake or fake-fake
process.finalFilter = cms.Sequence()
if (customize.processId.count("qcd") or customize.processId.count("gjet")) and customize.processId.count("fake"):
    process.load("flashgg/Systematics/PromptFakeFilter_cfi")
    process.finalFilter += process.PromptFakeFilter
    if (customize.processId.count("promptfake")):
        process.PromptFakeFilter.doPromptFake = cms.bool(True)
        process.PromptFakeFilter.doFakeFake =cms.bool(False)
    elif (customize.processId.count("fakefake")):
        process.PromptFakeFilter.doPromptFake =cms.bool(False)
        process.PromptFakeFilter.doFakeFake =cms.bool(True)
    else:
        raise Exception,"Mis-configuration of python for prompt-fake filter"

# Met Filters
process.load('flashgg/Systematics/flashggMetFilters_cfi')

if customize.processId == "Data":
    metFilterSelector = "data"
    filtersInputTag = cms.InputTag("TriggerResults", "", "RECO")
else:
    metFilterSelector = "mc"
    filtersInputTag = cms.InputTag("TriggerResults", "", "PAT")

process.flashggMetFilters.requiredFilterNames = cms.untracked.vstring([filter.encode("ascii") for filter in customize.metaConditions["flashggMetFilters"][metFilterSelector]])
process.flashggMetFilters.filtersInputTag = filtersInputTag

if customize.tthTagsOnly:
    process.p = cms.Path(process.dataRequirements*
                         process.flashggMetFilters*
                         process.genFilter*
                         process.flashggDiPhotons* # needed for 0th vertex from microAOD
                         process.flashggDifferentialPhoIdInputsCorrection*
                         process.flashggDiPhotonSystematics*
                         process.flashggMetSystematics*
                         process.flashggMuonSystematics*process.flashggElectronSystematics*
                         (process.flashggUnpackedJets*process.jetSystematicsSequence)*
                         (process.flashggTagSequence*process.systematicsTagSequences)*
                         process.flashggSystTagMerger*
                         process.penultimateFilter*
                         process.finalFilter*
                         process.tagsDumper)
    # Now, we put the ttH tags back in the sequence with modified systematics workflow
    modifySystematicsWorkflowForttH(process, systlabels, phosystlabels, metsystlabels, jetsystlabels)

else:
    process.p = cms.Path(process.dataRequirements*
                         process.flashggMetFilters*
                         process.genFilter*
                         process.flashggDifferentialPhoIdInputsCorrection*
                         process.flashggDiPhotonSystematics*
                         process.flashggMetSystematics*
                         process.flashggMuonSystematics*process.flashggElectronSystematics*
                         (process.flashggUnpackedJets*process.jetSystematicsSequence)*
                         (process.flashggTagSequence*process.systematicsTagSequences)*
                         process.flashggSystTagMerger*
                         process.penultimateFilter*
                         process.finalFilter*
                         process.tagsDumper)
    if customize.doStageOne: 
        if soc.modifyForttH: soc.modifyWorkflowForttH(systlabels, phosystlabels, metsystlabels, jetsystlabels)

if customize.doBJetRegression:

    bregProducers = []
    doubleHTagProducers = []
    
    from flashgg.Taggers.flashggTags_cff import UnpackedJetCollectionVInputTag
    from flashgg.Taggers.flashggbRegressionProducer_cfi import flashggbRegressionProducer
    recoJetCollections = UnpackedJetCollectionVInputTag
    if customize.metaConditions['bRegression']['useBRegressionJERsf'] :
       bregJERJetsProducers,recoJetCollections = createJetSystematicsForBreg(process , customize)
       process.bregJERJetsProducers = cms.Sequence(reduce(lambda x,y: x+y, bregJERJetsProducers))

    jetsysts = cms.vstring()
    jetnames = cms.vstring()
    for jetsyst in [systlabels[0]]+jetsystlabels:
        jetsysts.append(jetsyst)
    for icoll,coll in enumerate(recoJetCollections):
        jetnames.append(coll.moduleLabel)
    producer = flashggbRegressionProducer.clone(JetSuffixes = jetsysts)
    producer.JetNames = jetnames
    producer.bRegressionWeightfile = cms.untracked.string(str(os.environ["CMSSW_BASE"]+customize.metaConditions['bRegression']['weightFile']))
    producer.y_mean = customize.metaConditions['bRegression']['y_mean']
    producer.y_std = customize.metaConditions['bRegression']['y_std']
    producer.year = cms.untracked.string(str(customize.metaConditions['bRegression']['year']))

    setattr(process,"bRegProducer",producer)
    bregProducers.append(producer)
    process.bregProducers = cms.Sequence(reduce(lambda x,y: x+y, bregProducers))
    if customize.metaConditions['bRegression']['useBRegressionJERsf'] :
       process.p.replace(process.jetSystematicsSequence,process.jetSystematicsSequence*process.bregJERJetsProducers*process.bregProducers)
    else : process.p.replace(process.jetSystematicsSequence,process.jetSystematicsSequence+process.bregProducers)
    

if customize.doDoubleHTag:
    process.p.remove(process.flashggMetFilters)
    hhc.doubleHTagRunSequence(systlabels,jetsystlabels,phosystlabels)
  


if( not hasattr(process,"options") ): process.options = cms.untracked.PSet()
process.options.allowUnscheduled = cms.untracked.bool(True)

print "--- Dumping modules that take diphotons as input: ---"
mns = process.p.moduleNames()
for mn in mns:
    module = getattr(process,mn)
    if hasattr(module,"src") and type(module.src) == type(cms.InputTag("")) and module.src.value().count("DiPhoton"):
        print str(module),module.src
    elif hasattr(module,"DiPhotonTag"):
        print str(module),module.DiPhotonTag
print
printSystematicInfo(process)

### Rerun microAOD sequence on top of microAODs using the parent dataset
if customize.useParentDataset:
    runRivetSequence(process, customize.metaConditions, customize.processId)
    if customize.recalculatePDFWeights and is_signal and not (customize.processId.count("th_") or customize.processId.count("bbh_") or customize.processId.count("thw_") or customize.processId.count("thq_")):
        recalculatePDFWeights(process, customize.metaConditions)

#### BELOW HERE IS MOSTLY DEBUGGING STUFF

#####################################################################
## Memory and timing, n.b. igprof is very complicated to interpret ##
##################################################################### 

#from Validation.Performance.TimeMemoryInfo import customise as TimeMemoryCustomize
#TimeMemoryCustomize(process)
#process.MessageLogger.cerr.threshold = 'WARNING'

#process.load("IgTools.IgProf.IgProfTrigger")
#process.igprof.reportEventInterval     = cms.untracked.int32(250)
#process.igprof.reportToFileAtBeginJob  = cms.untracked.string("|gzip -c>igprof.begin-job.gz")
#process.igprof.reportToFileAtEvent     = cms.untracked.string("|gzip -c>igprof.%I.%E.%L.%R.event.gz")
#process.p += process.igprof

################################
## Dump merged tags to screen ##
################################

if customize.verboseTagDump:
    # crashes right now, dunno why - 02 May 2018
    pass
#    process.load("flashgg/Taggers/flashggTagTester_cfi")
#    process.flashggTagTester.TagSorter = cms.InputTag("flashggSystTagMerger")
#    process.flashggTagTester.ExpectMultiples = cms.untracked.bool(True)
#    process.p += process.flashggTagTester

############################################
## Additional details on tag sorter steps ##
############################################

if customize.verboseTagDump:
    process.flashggTagSorter.Debug = True
    customize.maxEvents = 10
                           
if customize.verboseSystDump:
    turnOnAllSystematicsDebug(process)
    customize.maxEVents = 10

##############
## Dump EDM ##
##############

#process.out = cms.OutputModule("PoolOutputModule", fileName = cms.untracked.string('CustomizeWillChangeThisAnyway.root'),
#                               outputCommands = cms.untracked.vstring('keep *') # dump everything! small tests only!
#                               )
#process.e = cms.EndPath(process.out)

############################
## Dump the output Python ##
############################
#print process.dumpPython()
#processDumpFile = open('processDump.py', 'w')
#print >> processDumpFile, process.dumpPython()
# call the customization
customize(process)
