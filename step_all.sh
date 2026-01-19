echo Check if TTY
if [ "`tty`" != "not a tty" ]; then
  echo "YOU SHOULD NOT RUN THIS IN INTERACTIVE, IT DELETES YOUR LOCAL FILES"
else

echo "ENV..................................."
env 
echo "VOMS"
voms-proxy-info -all
echo "CMSSW BASE, python path, pwd"
echo $CMSSW_BASE 
echo $PYTHON_PATH
echo $PWD 

echo Found Proxy in: $X509_USER_PROXY
# cmsRun -j FrameworkJobReport.xml step1_GEN_SIM.py
# cmsRun -j FrameworkJobReport.xml step2_DIGI_L1_DIGI2RAW_HLT.py
cmsRun -j FrameworkJobReport.xml step3_RAW2DIGI_L1Reco_RECO_PAT_DQM.py
cmsRun -j FrameworkJobReport.xml step4_HARVESTING.py
fi
