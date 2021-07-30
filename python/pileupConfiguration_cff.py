import FWCore.ParameterSet.Config as cms

def setPileUpConfiguration(process, options):
  if   options['era'] == "2016": from SimGeneral.MixingModule.mix_2016_25ns_Moriond17MC_PoissonOOTPU_cfi import mix
  elif options['era'] == "2017": from SimGeneral.MixingModule.mix_2017_25ns_WinterMC_PUScenarioV1_PoissonOOTPU_cfi import mix
  elif options['era'] == "2018": from SimGeneral.MixingModule.mix_2018_25ns_JuneProjectionFull18_PoissonOOTPU_cfi import mix
  elif "UL2016" in options['era']: from SimGeneral.MixingModule.mix_2016_25ns_UltraLegacy_PoissonOOTPU_cfi import mix
  elif options['era'] == "UL2017": from SimGeneral.MixingModule.mix_2017_25ns_UltraLegacy_PoissonOOTPU_cfi import mix
  elif options['era'] == "UL2018": from SimGeneral.MixingModule.mix_2018_25ns_UltraLegacy_PoissonOOTPU_cfi import mix

  #### DATA PU DISTRIBUTIONS
  data_pu_distribs = {
          "2016_DATA_xSec69.2mb_postVFP_UL": [4.78e+04,3.37e+05,1.16e+06,1.32e+06,1.72e+06,2.16e+06,2.45e+06,3.59e+06,6.82e+06,1.41e+07,4.13e+07,9.93e+07,1.86e+08,2.9e+08,4.04e+08,5.21e+08,6.26e+08,7.09e+08,7.7e+08,8.14e+08,8.51e+08,8.83e+08,9.07e+08,9.16e+08,9.11e+08,8.95e+08,8.69e+08,8.35e+08,7.92e+08,7.4e+08,6.8e+08,6.13e+08,5.42e+08,4.7e+08,3.98e+08,3.3e+08,2.67e+08,2.1e+08,1.61e+08,1.19e+08,8.49e+07,5.85e+07,3.87e+07,2.46e+07,1.5e+07,8.75e+06,4.9e+06,2.64e+06,1.37e+06,6.87e+05,3.35e+05,1.6e+05,7.6e+04,3.64e+04,1.8e+04,9.3e+03,5.12e+03,2.99e+03,1.84e+03,1.18e+03,765,503,331,217,142,91.5,58.6,37.2,23.4,14.5,8.97,5.47,3.31,1.99,1.18,0.696,0.407,0.236,0.136,0.0775,0.0439,0.0247,0.0138,0.00765,0.00421,0.0023,0.00124,0.00067,0.000357,0.000189,9.96e-05,5.2e-05,2.69e-05,1.38e-05,7.04e-06,3.55e-06,1.78e-06,8.85e-07,4.36e-07],
          "2016_DATA_xSec69.2mb_preVFP_UL": [4.63e+04,4.24e+05,1.21e+06,2.12e+06,4.31e+06,1.36e+07,3.17e+07,5.09e+07,8.45e+07,1.44e+08,2.3e+08,3.37e+08,4.63e+08,6.11e+08,7.78e+08,9.44e+08,1.08e+09,1.17e+09,1.22e+09,1.23e+09,1.22e+09,1.18e+09,1.13e+09,1.07e+09,9.86e+08,8.92e+08,7.9e+08,6.85e+08,5.83e+08,4.88e+08,4.04e+08,3.3e+08,2.66e+08,2.12e+08,1.66e+08,1.28e+08,9.69e+07,7.16e+07,5.17e+07,3.64e+07,2.5e+07,1.68e+07,1.1e+07,7.03e+06,4.4e+06,2.7e+06,1.62e+06,9.49e+05,5.46e+05,3.08e+05,1.71e+05,9.3e+04,4.98e+04,2.63e+04,1.38e+04,7.14e+03,3.7e+03,1.92e+03,1.01e+03,539,293,163,92.4,53.2,30.9,18.1,10.6,6.24,3.66,2.13,1.24,0.715,0.41,0.234,0.132,0.0742,0.0414,0.0229,0.0125,0.0068,0.00365,0.00194,0.00102,0.000534,0.000275,0.00014,7.05e-05,3.51e-05,1.72e-05,8.37e-06,4.01e-06,1.9e-06,8.85e-07,4.08e-07,1.85e-07,8.32e-08,3.68e-08,1.61e-08,6.92e-09],
          "2017_DATA_xSec69.2mb_UL": [2.75e+05,1.06e+06,2.01e+06,3.78e+06,4.09e+06,5.95e+06,6.44e+06,6.81e+06,9.21e+06,2.18e+07,4.37e+07,8.28e+07,1.32e+08,1.9e+08,2.69e+08,3.79e+08,5.27e+08,6.99e+08,8.7e+08,1.03e+09,1.17e+09,1.28e+09,1.37e+09,1.44e+09,1.5e+09,1.55e+09,1.6e+09,1.62e+09,1.63e+09,1.61e+09,1.56e+09,1.5e+09,1.43e+09,1.33e+09,1.24e+09,1.14e+09,1.04e+09,9.47e+08,8.66e+08,7.97e+08,7.44e+08,7.11e+08,6.98e+08,7.06e+08,7.3e+08,7.62e+08,7.91e+08,8.06e+08,7.96e+08,7.56e+08,6.87e+08,5.95e+08,4.91e+08,3.87e+08,2.92e+08,2.12e+08,1.48e+08,1.01e+08,6.67e+07,4.33e+07,2.76e+07,1.74e+07,1.08e+07,6.73e+06,4.17e+06,2.58e+06,1.61e+06,1.01e+06,6.38e+05,4.08e+05,2.64e+05,1.73e+05,1.14e+05,7.57e+04,5.05e+04,3.38e+04,2.27e+04,1.52e+04,1.02e+04,6.77e+03,4.49e+03,2.97e+03,1.95e+03,1.27e+03,823,530,338,214,134,83.4,51.4,31.4,19,11.4,6.73,3.95,2.3,1.32,0.751],
          "2018_DATA_xSec69.2mb_UL": [2.53e+05,7.61e+05,2.91e+06,6.84e+06,1.22e+07,1.89e+07,2.8e+07,4.08e+07,5.77e+07,8.03e+07,1.13e+08,1.58e+08,2.2e+08,3.02e+08,4.04e+08,5.28e+08,6.76e+08,8.46e+08,1.03e+09,1.23e+09,1.41e+09,1.58e+09,1.73e+09,1.84e+09,1.93e+09,2e+09,2.06e+09,2.12e+09,2.17e+09,2.22e+09,2.27e+09,2.31e+09,2.35e+09,2.37e+09,2.38e+09,2.36e+09,2.33e+09,2.27e+09,2.18e+09,2.06e+09,1.91e+09,1.74e+09,1.56e+09,1.36e+09,1.17e+09,9.77e+08,8.01e+08,6.42e+08,5.05e+08,3.89e+08,2.95e+08,2.2e+08,1.62e+08,1.18e+08,8.48e+07,6.06e+07,4.3e+07,3.03e+07,2.13e+07,1.48e+07,1.02e+07,7.02e+06,4.77e+06,3.2e+06,2.13e+06,1.4e+06,9.05e+05,5.79e+05,3.66e+05,2.29e+05,1.42e+05,8.66e+04,5.24e+04,3.14e+04,1.86e+04,1.1e+04,6.37e+03,3.67e+03,2.09e+03,1.18e+03,656,361,196,105,55.3,28.7,14.7,7.41,3.67,1.79,0.858,0.404,0.187,0.0852,0.0381,0.0167,0.00722,0.00306,0.00128],
   }

  if   options['era'] == "UL2016preVFP": data_pu_distribution = data_pu_distribs['2016_DATA_xSec69.2mb_preVFP_UL']
  elif options['era'] == "UL2016postVFP": data_pu_distribution = data_pu_distribs['2016_DATA_xSec69.2mb_postVFP_UL']
  elif '2017' in options['era']: data_pu_distribution = data_pu_distribs['2017_DATA_xSec69.2mb_UL']
  elif '2018' in options['era']: data_pu_distribution = data_pu_distribs['2018_DATA_xSec69.2mb_UL']

  process.pileupReweightingProducer = cms.EDProducer("PileupWeightProducer",
                                  pileupInfoTag = cms.InputTag("slimmedAddPileupInfo"),
                                  PileupMC      = cms.vdouble(mix.input.nbPileupEvents.probValue),
                                  PileupData    = cms.vdouble(data_pu_distribution),
                                  )
  if options['useAOD']: process.pileupReweightingProducer.pileupInfoTag = "addPileupInfo"

  process.mc_sequence = cms.Sequence()
  if options['isMC'] : process.mc_sequence = cms.Sequence( process.pileupReweightingProducer )
