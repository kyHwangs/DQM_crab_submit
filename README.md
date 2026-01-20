new
```
source /cvmfs/cms.cern.ch/cmsset_default.sh

cmsrel CMSSW_16_0_0_pre4
cd CMSSW_16_0_0_pre4/src

cmsenv

git cms-addpkg DQMOffline/Trigger
git cms-addpkg DQMOffline/Configuration

git remote add kygit https://github.com/SeoYJang/cmssw.git
git fetch kygit
git cherry-pick 53d1e08
git clone https://github.com/kyHwangs/DQM_crab_submit.git

scram b -j8

cd DQM_crab_submit
voms-proxy-init -voms cms -rfc  -valid 192:00
source /cvmfs/cms.cern.ch/common/crab-setup.sh

crab submit -c crab_Run398390.py
```



old
```
source /cvmfs/cms.cern.ch/cmsset_default.sh

cmsrel CMSSW_16_0_0_pre4
cd CMSSW_16_0_0_pre4/src

cmsenv

git cms-addpkg DQMOffline/Trigger
git cms-addpkg DQMOffline/Configuration

git remote add seoy https://github.com/SeoYJang/cmssw.git
git fetch seoy
git cherry-pick 48835c3
git clone https://github.com/kyHwangs/DQM_crab_submit.git

scram b -j8

cd DQM_crab_submit
voms-proxy-init -voms cms -rfc  -valid 192:00
source /cvmfs/cms.cern.ch/common/crab-setup.sh

crab submit -c crab_Run398390.py
```
