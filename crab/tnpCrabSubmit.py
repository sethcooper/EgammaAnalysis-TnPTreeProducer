#!/bin/env python
import os
try:
    from CRABClient.UserUtilities import config
except ImportError:
    print
    print(
        "ERROR: Could not load CRABClient.UserUtilities.  Please source the crab3 setup:"
    )
    print("source /cvmfs/cms.cern.ch/crab3/crab.sh")
    exit(-1)
try:
    cmsswBaseDir = os.environ["CMSSW_BASE"]
except KeyError as e:
    print("Could not find CMSSW_BASE env var; have you set up the CMSSW environment?")
    exit(-1)

from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException
from multiprocessing import Process

#
# Example script to submit TnPTreeProducer to crab
#
submitVersion = "2021-07-30test"  # add some date here
doL1matching = False

defaultArgs = ["doEleID=True", "doPhoID=False", "doTrigger=True"]
mainOutputDir = "/store/user/scooper/LQ/TnP/%s" % (submitVersion)

# Logging the current version of TnpTreeProducer here, such that you can find back what the actual code looked like when you were submitting
# os.system("mkdir -p /eos/cms/%s" % mainOutputDir)
# os.system("(git log -n 1;git diff) &> /eos/cms/%s/git.log" % mainOutputDir)


#
# Common CRAB settings
#
config = config()

config.General.requestName = ""
config.General.transferLogs = False
config.General.workArea = "crab_%s" % submitVersion

config.JobType.pluginName = "Analysis"
config.JobType.psetName = "../python/TnPTreeProducer_cfg.py"
config.JobType.sendExternalFolder = True
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = ""
config.Data.inputDBS = "global"
config.Data.publication = False
# config.Data.allowNonValidInputDataset = True
# config.Site.storageSite = "T2_CH_CERN"
config.Site.storageSite = "T2_US_Florida"


#
# Certified lumis for the different eras
#   (seems the JSON for UL2017 is slightly different from rereco 2017, it's not documented anywhere though)
#
def getLumiMask(era):
    if era == "2016":
        return "https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"
    elif era == "2017":
        return "https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt"
    elif era == "2018":
        return "https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/13TeV/PromptReco/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt"
    elif "UL2016" in era:
        return "https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions16/13TeV/Legacy_2016/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt"
    elif era == "UL2017":
        return "https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions17/13TeV/Legacy_2017/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt"
    elif era == "UL2018":
        return "https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt"


#
# Submit command
#
def submit(config, requestName, sample, era, json, extraParam=[]):
    isMC = "SIM" in sample
    config.General.requestName = "%s_%s" % (era, requestName)
    config.Data.inputDataset = sample
    config.Data.outLFNDirBase = "%s/%s/%s/" % (
        mainOutputDir,
        era,
        "mc" if isMC else "data",
    )
    config.Data.splitting = "FileBased" if isMC else "LumiBased"
    config.Data.lumiMask = None if isMC else json
    config.Data.unitsPerJob = 5 if isMC else 25
    config.JobType.pyCfgParams = (
        defaultArgs
        + ["isMC=True" if isMC else "isMC=False", "era=%s" % era]
        + extraParam
    )

    print config
    try:
        crabCommand("submit", config=config)
    except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
    except ClientException as cle:
        print "Failed submitting task: %s" % (cle)
    print
    print


#
# Wrapping the submit command
# In case of doL1matching=True, vary the L1Threshold and use sub-json
#
def submitWrapper(requestName, sample, era, extraParam=[]):
    if doL1matching:
        from getLeg1ThresholdForDoubleEle import getLeg1ThresholdForDoubleEle

        for leg1Threshold, json in getLeg1ThresholdForDoubleEle(era):
            print "Submitting for leg 1 threshold %s" % (leg1Threshold)
            p = Process(
                target=submit,
                args=(
                    config,
                    "%s_leg1Threshold%s" % (requestName, leg1Threshold),
                    sample,
                    era,
                    json,
                    extraParam + ["L1Threshold=%s" % leg1Threshold],
                ),
            )
            p.start()
            p.join()
    else:
        p = Process(
            target=submit,
            args=(config, requestName, sample, era, getLumiMask(era), extraParam),
        )
        p.start()
        p.join()


#
# List of samples to submit, with eras
# Here the default data/MC for UL and rereco are given (taken based on the release environment)
# If you would switch to AOD, don't forget to add 'isAOD=True' to the defaultArgs!
#
# era = "UL2017"
# submitWrapper(
#     "Run2017B", "FIXME", era
# )
# submitWrapper(
#     "Run2017C", "FIXME", era
# )
# submitWrapper(
#     "Run2017D", "FIXME", era
# )
# submitWrapper(
#     "Run2017E", "FIXME", era
# )
# submitWrapper(
#     "Run2017F", "FIXME", era
# )

# submitWrapper(
#     "DY_NLO",
#     "FIXME",
#     era,
# )
# submitWrapper(
#     "DY_LO",
#     "FIXME",
#     era,
# )

# era = "UL2018"
# submitWrapper("Run2018A", "/EGamma/Run2018A-UL2018_MiniAODv2-v1/MINIAOD", era)
# submitWrapper("Run2018B", "/EGamma/Run2018B-UL2018_MiniAODv2-v1/MINIAOD", era)
# submitWrapper("Run2018C", "/EGamma/Run2018C-UL2018_MiniAODv2-v1/MINIAOD", era)
# submitWrapper("Run2018D", "/EGamma/Run2018D-UL2018_MiniAODv2-v1/MINIAOD", era)

# submitWrapper(
#     "DY_NLO",
#     "FIXME",
#     era,
# )
# submitWrapper(
#     "DY_LO",
#     "FIXME",
#     era,
# )

# test
era = "UL2018"
# /EGamma/Run2018*-UL2018_MiniAODv2-*/MINIAOD
submitWrapper("Run2018A", "/EGamma/Run2018A-UL2018_MiniAODv2-v1/MINIAOD", era)
# MC
submitWrapper(
    "DY_LO",
    "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM",
    era,
)
