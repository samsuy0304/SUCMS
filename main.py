import os
import Root

#########################   Setup ###############################################

# Borrowd from Caleb: https://github.com/ku-cms/LeptonStudies/blob/main/python/makePlots.py
# Make sure ROOT.TFile.Open(fileURL) does not seg fault when $ is in sys.argv (e.g. $ passed in as argument)
ROOT.PyConfig.IgnoreCommandLineOptions = True
# Make plots faster without displaying them
ROOT.gROOT.SetBatch(ROOT.kTRUE)
# Tell ROOT not to be in charge of memory, fix issue of histograms being deleted when ROOT file is closed:
ROOT.TH1.AddDirectory(False)


#Caleb Defined Function

def plot(hist, sample_name, plot_dir, plot_name):
    c = ROOT.TCanvas("c", "c", 800, 800)
    
    # draw
    hist.Draw()

    # save plot
    output_name = "{0}/{1}".format(plot_dir, plot_name)
    c.Update()
    c.SaveAs(output_name + ".pdf")

# Input file
INF = Root.TFile.Open("4153AE9C-1215-A847-8E0A-DEBE98140664.root")

# Name given to tree after using MakeClass
tree_name = "Events"
tree = INF.Get(tree_name)


# The Name that defines what the data is about
sample_name = "SMS-T2-4bd_genMET-80_mStop-500_mLSP-490"

#Number of Events
nEvents = tree.GetEntries()

#Save Plots in
plo = "Pretty_Plots"


ID_Lw = ("h_LowPtElectron_pt", "h_LowPtElectron_pt")#, 20, 0.0, 20.0)
pt_Lw = ("h_LowPtElectron_pt", "h_LowPtElectron_pt")#, 20, 0.0, 20.0)
eta_Lw = ("h_LowPtElectron_pt", "h_LowPtElectron_pt")#, 20, 0.0, 20.0)
dxy_Lw = ("h_LowPtElectron_pt", "h_LowPtElectron_pt")#, 20, 0.0, 20.0)
dxyErr_Lw = ("h_LowPtElectron_pt", "h_LowPtElectron_pt")#, 20, 0.0, 20.0)
dz_Lw = ("h_LowPtElectron_pt", "h_LowPtElectron_pt")#, 20, 0.0, 20.0)
dzErr_Lw = ("h_LowPtElectron_pt", "h_LowPtElectron_pt")#, 20, 0.0, 20.0)
miniPFRelIso_all_Lw = ("h_LowPtElectron_pt", "h_LowPtElectron_pt")#, 20, 0.0, 20.0)
convVeto_Lw = ("h_LowPtElectron_pt", "h_LowPtElectron_pt")#, 20, 0.0, 20.0)
nLowPtElectron = ("h_LowPtElectron_pt", "h_LowPtElectron_pt")#, 20, 0.0, 20.0)

# Sorting Through the Events

for i in range(nEvents): # Using the number of Events for looping
  # MUST ASK CALEB ABOUT THIS SECTION.
  tree.GetEntry(i)
  nLowPtElectron      = tree.nLowPtElectron
  LowPtElectron_ID    = tree.LowPtElectron_ID
  LowPtElectron_pt    = tree.LowPtElectron_pt
  LowPtElectron_eta   = tree.LowPtElectron_eta
  LowPtElectron_dxy   = tree.LowPtElectron_dxy
  LowPtElectron_dxyErr  = tree.LowPtElectron_dxyErr
  LowPtElectron_dz   = tree.LowPtElectron_dz
  LowPtElectron_dzErr  = tree.LowPtElectron_dzErr
  LowPtElectron_miniPFRelIso_all = tree.LowPtElectron_miniPFRelIso_all
  LowPtElectron_convVeto   = tree.LowPtElectron_convVeto
  
  

