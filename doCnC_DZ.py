import os

legs = ['leg1']
fittings = ['--checkBins', '--createBins', '--createHists --isPassOverTotal --flagForTotal nonDZPath', '--doCutCount --isPassOverTotal ']
#fittings = ['--checkBins', '--createBins', '--createHists --isPassOverTotal --flagForTotal nonDZPath', '--doCutCount --isPassOverTotal --onlyDoPlot --plotX nvtx ']
#fittings = ['--doCutCount --isPassOverTotal --onlyDoPlot --plotX nvtx ']


for value in fittings:
    os.system('python tnpEGM_fitter.py etc/config/settings_DZ.py --flag DZPath' + ' ' + value)
    #os.system('python tnpEGM_fitter.py etc/config/settings_DZ_runDenpendent.py --flag DZPath' + ' ' + value)
