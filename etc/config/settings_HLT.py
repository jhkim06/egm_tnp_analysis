#############################################################
########## General settings
#############################################################
## -- Test mva cut value in endcap for HNEleID -- ##
HNEleID_without_HNMVA = '( el_pt > 10 && abs(el_sc_eta) < 2.5 && el_reliso03 < 0.08 && abs(el_dxy) < 0.01 && abs(el_dz) < 0.04 && el_3charge == 1 && el_passConversionVeto == 1 && el_dxysig < 4 )'
HNMVA = '( ( abs(el_sc_eta) < 0.8 && el_mva > 0.9 ) || ( 0.8 < abs(el_sc_eta) && abs(el_sc_eta) < 1.479 && el_mva > 0.825 ) || ( 1.479 < abs(el_sc_eta) && el_mva > 0.500 ) )' 
HNEleID = HNEleID_without_HNMVA + ' && ' + HNMVA

# flag to be Tested
flags = {
    'passingHNEleID'    : HNEleID,
    'passingVeto' : '(passingVeto == 1)',
    'passingLoose' : '(passingLoose == 1)',
    'passingMedium' : '(passingMedium == 1)',
    'passingTight' : '(passingTight == 1)',
    'passingVeto80X' : '(passingVeto80X == 1)',
    'passingLoose80X' : '(passingLoose80X == 1)',
    'passingMedium80X' : '(passingMedium80X == 1)',
    'passingTight80X' : '(passingTight80X == 1)',
    'passingMVA80Xwp80' : '(passingMVA80Xwp80 == 1)',
    'passingMVA80Xwp90' : '(passingMVA80Xwp90 == 1)',
    'passingReco' : '(passingRECO == 1)',
    #'passingHLTleg1' : '(passingHLTEle23Ele12leg1 == 1) && (passingL1seed == 1)',
    'passingHLTleg1' : '(passingHLTEle23Ele12leg1 == 1)',
    'passingHLTleg2' : '(passingHLTEle23Ele12leg2 == 1)' 
   }

baseOutDir = 'results/Moriond17/tnpEleTrig' # JH

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
#import etc.inputs.tnpSampleDef as tnpSamples
import etc.inputs.tnpSampleDef as tnpSamples
#tnpTreeDir = 'GsfElectronToEleID'

tnpTreeDir = 'tnpEleTrig'

samplesDef = {
    'data'   : tnpSamples.Moriond17_80X['data_Run2016H'].clone(),
    'mcNom'  : tnpSamples.Moriond17_80X['DY_madgraph_Winter17'].clone(),
    'mcAlt'  : None,
#    'mcAlt'  : tnpSamples.Moriond17_80X['DY_amcatnlo_Winter17'].clone(),
#    'mcAlt'  : tnpSamples.Moriond17_80X['DYee_powheg_Winter17'].clone(),
#    'tagSel' : tnpSamples.Moriond17_80X['DY_madgraph_Winter17'].clone(),
    'tagSel' : None,
    'dataToCompare': None,
}
## can add data sample easily
#samplesDef['data'].add_sample( tnpSamples.Moriond17_80X['data_Run2016G'] )
#samplesDef['data'].add_sample( tnpSamples.Moriond17_80X['data_Run2016F'] )
#samplesDef['data'].add_sample( tnpSamples.Moriond17_80X['data_Run2016E'] )
#samplesDef['data'].add_sample( tnpSamples.Moriond17_80X['data_Run2016D'] )
#samplesDef['data'].add_sample( tnpSamples.Moriond17_80X['data_Run2016C'] )
#samplesDef['data'].add_sample( tnpSamples.Moriond17_80X['data_Run2016B'] )

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
samplesDef['data' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_tnpTree(tnpTreeDir)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_tnpTree(tnpTreeDir)
## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_tnpTree(tnpTreeDir)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_tnpTree(tnpTreeDir)

if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
if not samplesDef['tagSel'] is None:
    samplesDef['tagSel'].rename('mcAltSel_DY_madgraph')
 #   samplesDef['tagSel'].set_cut('tag_Ele_pt > 27  && tag_Ele_nonTrigMVA80X > 0.95')
    samplesDef['tagSel'].set_cut('tag_Ele_pt > 33  && tag_Ele_nonTrigMVA > 0.90')

## set MC weight, simple way (use tree weight) 
#weightName = 'totWeight'
#weightName = 'weight'
#if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)

## set MC weight, can use several pileup rw for different data taking periods
#weightName = 'weights_2016_runGH.totWeight'
weightName = 'weights_2016_runAll.totWeight'
hltPSName = 'test'

if not samplesDef['data' ] is None:  samplesDef['data' ].set_hltPS(hltPSName)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('/home/jhkim/pu/DY_madgraph_Winter17_ele.pu.puTree.root')
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('/home/jhkim/pu/DY_amcatnlo_Winter17_ele.pu.puTree.root')
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_puTree('/home/jhkim/pu/DY_madgraph_Winter17_ele.pu.puTree.root')


#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
   #{ 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5,-2.0,-1.566,-1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5] },
   { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, 2.5] },
   { 'var' : 'el_pt' , 'type': 'float', 'bins': [10,15,20,25,30,40,50,90,150,500] },
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
#cutBase   = 'tag_Ele_pt > 30 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0' # it is default!
#cutBase   = 'tag_Ele_pt > 40 && abs(tag_sc_eta) < 2.17 && probe_Ele_q*tag_Ele_q < 0'
## -- DM -- ##
cutBase   = 'tag_Ele_pt > 30 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0 && (passingMedium80X == 1) && (abs(el_sc_eta) < 1.442 || abs(el_sc_eta) > 1.566) '

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
additionalCuts = { 
    0 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    1 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    #2 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    #3 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    #4 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    #5 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    #6 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    #7 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    #8 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    #9 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    #10 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    #11 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    #12 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    #13 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    #14 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    #15 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    #16 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    #17 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    #18 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    #19 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45'
}

#### or remove any additional cut (default)
#additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [

    ### myBinNom02

#    "meanP[0.0,-5.0,5.0]","sigmaP[0.15,0.,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
#    "acmsP[0.,0.,0.]","betaP[0.,0.,0.]","gammaP[0., 0., 0.]","peakP[90.0]",
#    "acmsF[50.,40.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ### default
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",

    ## bin1
#    "meanP[0.0,-5.0,5.0]","sigmaP[1.2]",
#    "meanF[0.0,-5.0,5.0]","sigmaF[1.2]",
#    "acmsP[100.,40.,150.]","betaP[1.1,0.00001,1.3]","gammaP[0.1,-2,5]","peakP[90.0]",
#    "acmsF[60.,30.,100.]","betaF[0.05,0.001,0.08]","gammaF[0.1,-2,2]","peakF[90.0]",

    ## bin3
#    "meanP[0.0,-3.0,3.0]","sigmaP[0.8]",
#    "meanF[0.0,-3.0,3.0]","sigmaF[1.5]",
#    "acmsP[60.,30.,80.]","betaP[0.05,0.001,0.18]","gammaP[0.1,-2,2]","peakP[90.0]",
#    "acmsF[80.,10.,100.]","betaF[0.05,0.001,0.08]","gammaF[0.1,-2,2]","peakF[90.0]",

    ## bin4
#    "meanP[0.0,-3.0,3.0]","sigmaP[0.7]",
#    "meanF[0.0,-3.0,3.0]","sigmaF[1.0]",
#    "acmsP[60.,30.,80.]","betaP[0.05,0.001,0.18]","gammaP[0.05,-2,2]","peakP[90.0]",
#    "acmsF[50.,40.,80.]","betaF[0.05,0.001,0.08]","gammaF[0.05,-2,2]","peakF[90.0]",

    ## bin5
#    "meanP[0.0,-3.0,3.0]","sigmaP[0.7]",
#    "meanF[0.0,-3.0,3.0]","sigmaF[1.5]",
#    "acmsP[60.,30.,80.]","betaP[0.05,0.001,0.18]","gammaP[0.1,-2,2]","peakP[90.0]",
#    "acmsF[80.,10.,100.]","betaF[0.05,0.001,0.08]","gammaF[0.1,-2,2]","peakF[90.0]",

    ## bin6
#    "meanP[0.0,-3.0,3.0]","sigmaP[0.5]",
#    "meanF[0.0,-3.0,3.0]","sigmaF[1.0]",
#    "acmsP[80.,30.,100.]","betaP[0.05,0.001,0.18]","gammaP[0.1,-2,2]","peakP[90.0]",
#    "acmsF[80.,10.,100.]","betaF[0.05,0.001,0.08]","gammaF[0.1,-2,2]","peakF[90.0]",


    ## bin9
#    "meanP[0.0,-5.0,5.0]","sigmaP[1.2]",
#    "meanF[0.0,-5.0,5.0]","sigmaF[0.5]",
#    "acmsP[60.,40.,100.]","betaP[0.05,0.001,0.08]","gammaP[0.1,-2,2]","peakP[90.0]",
#    "acmsF[60.,40.,100.]","betaF[0.05,0.001,0.08]","gammaF[0.1,-2,2]","peakF[90.0]",

    ## bin11
#    "meanP[0.0,-3.0,3.0]","sigmaP[1.0]",
#    "meanF[0.0,-3.0,3.0]","sigmaF[1.0]",
#    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1,-2,2]","peakP[90.0]",
#    "acmsF[60.,50.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1,-2,2]","peakF[90.0]",

    ## bin21
#    "meanP[0.0,-5.0,5.0]","sigmaP[1.2]",
#    "meanF[0.0,-5.0,5.0]","sigmaF[0.5]",
#    "acmsP[60.,40.,100.]","betaP[0.05,0.001,0.08]","gammaP[0.1,-2,2]","peakP[90.0]",
#    "acmsF[60.,40.,100.]","betaF[0.05,0.001,0.08]","gammaF[0.1,-2,2]","peakF[90.0]",

    ## bin46
#    "meanP[0.0,-5.0,5.0]","sigmaP[0.75]",
#    "meanF[0.0,-5.0,5.0]","sigmaF[1.5]",
#    "acmsP[60.,40.,120.]","betaP[0.05,0.001,0.08]","gammaP[0.1,-2,2]","peakP[90.0]",
#    "acmsF[60.,40.,100.]","betaF[0.05,0.001,0.08]","gammaF[0.1,-2,2]","peakF[90.0]",


    ## bin53
#    "meanP[0.0,-5.0,5.0]","sigmaP[0.7]",
#    "meanF[0.0,-5.0,5.0]","sigmaF[1.0]",
#    "acmsP[60.,40.,100.]","betaP[0.05,0.001,0.08]","gammaP[0.1,-2,2]","peakP[90.0]",
#    "acmsF[60.,40.,100.]","betaF[0.05,0.001,0.08]","gammaF[0.1,-2,2]","peakF[90.0]",

    ## bin54
#    "meanP[0.0,-5.0,5.0]","sigmaP[0.6]",
#    "meanF[0.0,-5.0,5.0]","sigmaF[1.0]",
#    "acmsP[60.,40.,120.]","betaP[0.05,0.001,0.08]","gammaP[0.1,-2,2]","peakP[90.0]",
#    "acmsF[60.,40.,100.]","betaF[0.05,0.001,0.08]","gammaF[0.1,-2,2]","peakF[90.0]",

    ## bin59
#    "meanP[0.0,-5.0,5.0]","sigmaP[1.0]",
#    "meanF[0.0,-5.0,5.0]","sigmaF[1.0]",
#    "acmsP[60.,40.,120.]","betaP[0.05,0.001,0.12]","gammaP[0.1,-2,2]","peakP[90.0]",
#    "acmsF[60.,40.,100.]","betaF[0.05,0.001,0.08]","gammaF[0.1,-2,2]","peakF[90.0]",

    ]

tnpParAltSigFit = [
    ### default in Arun's setting
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ### MC bin15
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.7]","alphaP[2,0.5,3.5]" ,'nP[9,-5,25]',"sigmaP_2[1.2,0.5,6.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.2,0.7,15.0]","alphaF[2.1,0.3,3.5]",'nF[10,-5,25]',"sigmaF_2[1.7,0.5,6.0]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,100.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ### MC bin20
#    "meanP[-0.0,-3.0,3.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.0,0.5,2.5]","sosP[0.5,0.01,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[1.7,0.5,5.]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,100.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ### MC bin21 bin29 bin33? bin34 bin35? bin36? bin38
#    "meanP[-0.0,-3.0,3.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,1.0,2.0]","sosP[0.5,0.01,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.,1.5,2.5]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,100.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ### MC bin24 bin25 bin26 bin31
#    "meanP[-0.0,-3.0,3.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.0,0.5,2.5]","sosP[0.5,0.01,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[1.2,0.5,2.]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,100.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ### MC bin28
#    "meanP[-0.0,-3.0,3.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.0,0.5,2.5]","sosP[0.5,0.01,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.3,0.5,2.]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,100.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ### MC bin29 bin33
#    "meanP[-0.0,-3.0,3.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.0,0.5,2.5]","sosP[0.5,0.01,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,2.]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,100.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",


    ### MC bin30
#    "meanP[-0.0,-3.0,3.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.0,0.5,2.5]","sosP[0.5,0.01,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.1,0.5,2.]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,100.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ### bin3 bin5 
#    "meanP[-0.0,-3.0,3.0]","sigmaP[0.8,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.0,0.5,6.0]","sosP[0.5,0.01,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,100.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ### bin4 bin9 bin20 bin24
#    "meanP[-0.0,-3.0,3.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[0.5,0.01,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,100.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ### bin21 bin23
#    "meanP[-0.0,-3.0,3.0]","sigmaP[1,0.7,2.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.0,0.5,5.0]","sosP[0.5,0.01,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,4.0]","alphaF[2.0,1.2,3.0]",'nF[3,-5,5]',"sigmaF_2[1.0,0.5,1.5]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,80.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[70.,50.,80.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ### bin28##FIXME this doesn't work
#    "meanP[-0.0,-3.0,3.0]","sigmaP[1,0.7,2.0]","alphaP[2.0,1.2,3.0]" ,'nP[3,-5,5]',"sigmaP_2[1.0,0.5,3.0]","sosP[0.5,0.01,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.5]","alphaF[2.0,1.2,3.0]",'nF[3,-5,5]',"sigmaF_2[0.5]","sosF[1,0.5,2.0]",
#    "acmsP[60.,50.,100.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",


    ### bin25
#    "meanP[-0.0,-3.0,3.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.0,0.5,6.0]","sosP[0.5,0.01,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[1.0,0.5,6.0]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,100.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ### bin26
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.2,0.7,6.0]","alphaP[2,0.5,3.5]" ,'nP[9,-5,25]',"sigmaP_2[1.2,0.5,6.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.2,0.7,15.0]","alphaF[2.1,0.3,3.5]",'nF[10,-5,25]',"sigmaF_2[1.7,0.5,6.0]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ### bin26
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.7]","alphaP[2,0.5,3.5]" ,'nP[9,-5,25]',"sigmaP_2[1.2,0.5,6.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.2,0.7,15.0]","alphaF[2.1,0.3,3.5]",'nF[10,-5,25]',"sigmaF_2[1.7,0.5,6.0]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,100.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",


    ### bin29 bin30 
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.2,0.7,6.0]","alphaP[2,0.5,3.5]" ,'nP[9,-5,25]',"sigmaP_2[1.2,0.5,6.0]","sosP[1,0.5,5.0]",
#    "meanF[-2.0,-5.0,5.0]","sigmaF[0.1,0.1,0.5]","alphaF[2.1,0.3,3.5]",'nF[5,-25,25]',"sigmaF_2[0.7,0.5,1.2]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",


    ### MC bin30
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.2,0.7,6.0]","alphaP[2,0.5,3.5]" ,'nP[9,-5,25]',"sigmaP_2[1.2,0.5,6.0]","sosP[1,0.5,5.0]",
#    "meanF[-2.0,-5.0,5.0]","sigmaF[0.5,0.1,1.5]","alphaF[2.1,0.3,3.5]",'nF[5,-25,25]',"sigmaF_2[1.2,0.5,3.0]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",


    ### bin31 test
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[-1.5,-3,-0.5]" ,'nP[1,-5,5]',"sigmaP_2[0.6]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.5,0.7,15.0]","alphaF[-1.5,-3,-0.5]",'nF[1,-5,5]',"sigmaF_2[0.6]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,120.]","betaP[0.04,0.01,0.08]","gammaP[0.1, 0.001, 1]","peakP[90.0]",
#    "acmsF[40.,30.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ### bin33 bin34
#    "meanP[-0.0,-3.0,3.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.0,0.5,6.0]","sosP[0.5,0.01,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.5]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[0.5]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,100.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[70.,50.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",

    ### bin36 bin46
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[-1.5,-3,-0.5]" ,'nP[1,-5,5]',"sigmaP_2[0.6]","sosP[1,0.1,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.5,0.7,15.0]","alphaF[-1.5,-3,-0.5]",'nF[1,-5,5]',"sigmaF_2[0.6]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,120.]","betaP[0.04,0.01,0.08]","gammaP[0.1, 0.001, 1]","peakP[90.0]",
#    "acmsF[40.,30.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",


    ### bin38
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1.2,0.7,6.0]","alphaP[2,0.5,3.5]" ,'nP[9,-5,25]',"sigmaP_2[1.2,0.5,6.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.2,0.7,15.0]","alphaF[2.1,0.3,3.5]",'nF[10,-5,25]',"sigmaF_2[1.7,0.5,6.0]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[70.,50.,100.]","betaF[0.08,0.01,0.10]","gammaF[0.2, 0.005, 1]","peakF[90.0]",


    ]
     
tnpParAltBkgFit = [
    #default
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "alphaP[0.,-5.,5.]",
    "alphaF[0.,-5.,5.]",

     #bin01
#    "meanP[-0.0,-3.0,3.0]","sigmaP[1.0]",
#    "meanF[-0.0,-3.0,3.0]","sigmaF[1.1]",
#    "alphaP[0.,-5.,5.]",
#    "alphaF[0.,-5.,5.]",

     #bin01
#    "meanP[-0.0,-3.0,3.0]","sigmaP[0.9]",
#    "meanF[-0.0,-3.0,3.0]","sigmaF[1.1]",
#    "alphaP[0.,-5.,5.]",
#    "alphaF[0.,-5.,5.]",


     #bin09
#    "meanP[-0.0,-3.0,3.0]","sigmaP[1.5]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.5]",
#    "alphaP[0.,-5.,5.]",
#    "alphaF[0.,-5.,5.]",


    ]
        
