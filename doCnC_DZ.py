import os

legs = ['leg1']
#fittings = ['--checkBins', '--createBins', '--createHists --isPassOverTotal --flagForTotal nonDZPath', '--doCutCount --isPassOverTotal']
fittings = ['--doCutCount --isPassOverTotal']


for value in fittings:
    os.system('python tnpEGM_fitter.py etc/config/settings_DZ.py --flag DZPath' + ' ' + value)
