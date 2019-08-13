from libPython.tnpClassUtils import tnpSample

### qll stat
#myinputDir = '/data1/EGM_TnP/TnPTree/Dalmin/HN/Moriond17_GainSwitch_newTnP_v3_test/'
myinputDir_leg1 = '/data1/EGM_TnP/TnPTree/Dalmin/HN/Moriond17_GainSwitch_newTnP_v3_leg1/'
myinputDir_leg2 = '/data1/EGM_TnP/TnPTree/Dalmin/HN/Moriond17_GainSwitch_newTnP_v3_leg2/'
myinputDir = '/data7/Users/jhkim/Moriond17_GainSwitch_newTnP_v6/'
myinputDirv2 = '/data7/Users/jhkim/Moriond17_GainSwitch_newTnP_v6/'

DZfilter_2016 = {
    ### MiniAOD TnP for IDs scale factors
    'DY_amcatnlo_Winter17' : tnpSample('DY_amcatnlo_Winter17',
                                       myinputDirv2 + 'DYJets.root',
                                       isMC = True, nEvts = 28968252 ),

    'data_Run2016B' : tnpSample('data_Run2016B' , myinputDirv2 + 'periodB_ver2.root' , lumi = 5.788 ),
    'data_Run2016C' : tnpSample('data_Run2016C' , myinputDirv2 + 'periodC.root' , lumi = 2.573 ),
    'data_Run2016D' : tnpSample('data_Run2016D' , myinputDirv2 + 'periodD.root' , lumi = 4.248 ),
    'data_Run2016E' : tnpSample('data_Run2016E' , myinputDirv2 + 'periodE.root' , lumi = 4.009 ),
    'data_Run2016F' : tnpSample('data_Run2016F' , myinputDirv2 + 'periodF.root' , lumi = 3.102 ),
    'data_Run2016G' : tnpSample('data_Run2016G' , myinputDirv2 + 'periodG.root' , lumi = 7.540 ),
    'data_Run2016H' : tnpSample('data_Run2016H' , myinputDirv2 + 'periodH.root' , lumi = 8.606  ),
    }


Moriond17_80X = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph_Winter17' : tnpSample('DY_madgraph_Winter17', 
                                       myinputDir + 'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_DYToLL_madgraph_Moriond17.root',
                                       isMC = True, nEvts = 49144274 ),
    'DY_amcatnlo_Winter17' : tnpSample('DY_amcatnlo_Winter17', 
                                       myinputDir + 'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_DYToLL_mcAtNLO_Moriond17.root',
                                       isMC = True, nEvts = 28968252 ),

    'data_Run2016B' : tnpSample('data_Run2016B' , myinputDir + 'data/SingleElectron/TnPTree_SingleElectron_2016rereco_RunB.root' , lumi = 5.788 ),
    'data_Run2016C' : tnpSample('data_Run2016C' , myinputDir + 'data/SingleElectron/TnPTree_SingleElectron_2016rereco_RunC.root' , lumi = 2.573 ),
    'data_Run2016D' : tnpSample('data_Run2016D' , myinputDir + 'data/SingleElectron/TnPTree_SingleElectron_2016rereco_RunD.root' , lumi = 4.248 ),
    'data_Run2016E' : tnpSample('data_Run2016E' , myinputDir + 'data/SingleElectron/TnPTree_SingleElectron_2016rereco_RunE.root' , lumi = 4.009 ),
    'data_Run2016F' : tnpSample('data_Run2016F' , myinputDir + 'data/SingleElectron/TnPTree_SingleElectron_2016rereco_RunF.root' , lumi = 3.102 ),
    'data_Run2016G' : tnpSample('data_Run2016G' , myinputDir + 'data/SingleElectron/TnPTree_SingleElectron_2016rereco_RunG.root' , lumi = 7.540 ),
    'data_Run2016H' : tnpSample('data_Run2016H' , myinputDir + 'data/SingleElectron/TnPTree_SingleElectron_2016prompt_RunH.root' , lumi = 8.606 ),
    }

Moriond17_80X_HN_leg1 = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph_Winter17' : tnpSample('DY_madgraph_Winter17', 
                                       myinputDir_leg1 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_DYToLL_madgraph_Moriond17.root',
                                       isMC = True, nEvts = 49144274 ),
    'DY_amcatnlo_Winter17' : tnpSample('DY_amcatnlo_Winter17', 
                                       myinputDir_leg1 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_DYToLL_mcAtNLO_Moriond17.root',
                                       isMC = True, nEvts = 28968252 ),

    'data_Run2016B' : tnpSample('data_Run2016B' , myinputDir_leg1 + 'data/TnPTree_SingleElectron_2016rereco_RunB.root' , lumi = 5.788 ),
    'data_Run2016C' : tnpSample('data_Run2016C' , myinputDir_leg1 + 'data/TnPTree_SingleElectron_2016rereco_RunC.root' , lumi = 2.573 ),
    'data_Run2016D' : tnpSample('data_Run2016D' , myinputDir_leg1 + 'data/TnPTree_SingleElectron_2016rereco_RunD.root' , lumi = 4.248 ),
    'data_Run2016E' : tnpSample('data_Run2016E' , myinputDir_leg1 + 'data/TnPTree_SingleElectron_2016rereco_RunE.root' , lumi = 4.009 ),
    'data_Run2016F' : tnpSample('data_Run2016F' , myinputDir_leg1 + 'data/TnPTree_SingleElectron_2016rereco_RunF.root' , lumi = 3.102 ),
    'data_Run2016G' : tnpSample('data_Run2016G' , myinputDir_leg1 + 'data/TnPTree_SingleElectron_2016rereco_RunG.root' , lumi = 7.540 ),
    'data_Run2016H' : tnpSample('data_Run2016H' , myinputDir_leg1 + 'data/TnPTree_SingleElectron_2016prompt_RunH.root' , lumi = 8.606 ),
    }

Moriond17_80X_HN_leg2 = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph_Winter17' : tnpSample('DY_madgraph_Winter17', 
                                       myinputDir_leg2 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_DYToLL_madgraph_Moriond17.root',
                                       isMC = True, nEvts = 49144274 ),
    'DY_amcatnlo_Winter17' : tnpSample('DY_amcatnlo_Winter17', 
                                       myinputDir_leg2 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_DYToLL_mcAtNLO_Moriond17.root',
                                       isMC = True, nEvts = 28968252 ),

    'data_Run2016B' : tnpSample('data_Run2016B' , myinputDir_leg2 + 'data/TnPTree_SingleElectron_2016rereco_RunB.root' , lumi = 5.788 ),
    'data_Run2016C' : tnpSample('data_Run2016C' , myinputDir_leg2 + 'data/TnPTree_SingleElectron_2016rereco_RunC.root' , lumi = 2.573 ),
    'data_Run2016D' : tnpSample('data_Run2016D' , myinputDir_leg2 + 'data/TnPTree_SingleElectron_2016rereco_RunD.root' , lumi = 4.248 ),
    'data_Run2016E' : tnpSample('data_Run2016E' , myinputDir_leg2 + 'data/TnPTree_SingleElectron_2016rereco_RunE.root' , lumi = 4.009 ),
    'data_Run2016F' : tnpSample('data_Run2016F' , myinputDir_leg2 + 'data/TnPTree_SingleElectron_2016rereco_RunF.root' , lumi = 3.102 ),
    'data_Run2016G' : tnpSample('data_Run2016G' , myinputDir_leg2 + 'data/TnPTree_SingleElectron_2016rereco_RunG.root' , lumi = 7.540 ),
    'data_Run2016H' : tnpSample('data_Run2016H' , myinputDir_leg2 + 'data/TnPTree_SingleElectron_2016prompt_RunH.root' , lumi = 8.606 ),
    }
