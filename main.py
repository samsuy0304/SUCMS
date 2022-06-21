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
#
ROOT.gStyle.SetOptStat(111111)

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


ID_Lw =ROOT.TH1F("ID", "ID",45,-1,8)#, 20, 0.0, 20.0)
pt_Lw =ROOT.TH1F("pt","pt",30,0,300)#, 20, 0.0, 20.0)
eta_Lw =ROOT.TH1F("eta","eta", 30,-3,3)#, 20, 0.0, 20.0)
dxy_Lw =ROOT.TH1F("dxy","dxy", 20,-1,1)#, 20, 0.0, 20.0)
dxyErr_Lw =ROOT.TH1F("dxyErr", "dxyErr", 60,0,0.6 )#, 20, 0.0, 20.0)
dz_Lw =ROOT.TH1F("dz","dz",30,-15,15)#, 20, 0.0, 20.0)
dzErr_Lw =ROOT.TH1F("dzErr","dzErr", 60,0,0.6)#, 20, 0.0, 20.0)
miniPFRelIso_all_Lw =ROOT.TH1F("PF","Pf",150,0,150)#, 20, 0.0, 20.0)
convVeto_Lw =ROOT.TH1F("Veto","Veto",20,0,2)#, 20, 0.0, 20.0)
n_Lw =ROOT.TH1F()#, 20, 0.0, 20.0)

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
    
    for j in range(nLowPtElectron):
        if verbose:
            #print("LowPtElectron {0}: pt = {1:.3f}, eta = {2:.3f}, phi = {3:.3f}, mass = {4:.3f}".format(j, LowPtElectron_pt[j], LowPtElectron_eta[j], LowPtElectron_phi[j], LowPtElectron_mass[j]))
        ID_Lw.Fill(LowPtElectron_ID[j])
        pt_Lw.Fill(LowPtElectron_pt[j])
        eta_Lw.Fill(LowPtElectron_eta[j])
        dxy_Lw.Fill(LowPtElectron_dxy[j])
        dxyErr_Lw.Fill(LowPtElectron_dxyErr[j])
        dz_Lw.Fill(LowPtElectron_dz[j])
        dzErr_Lw.Fill(LowPtElectron_dzErr[j])
        miniPFRelIso_all_Lw.Fill(LowPtElectron_miniPFRelIso_all[j])
        convVeto_Lw.Fill(LowPtElectron_convVeto[j])
        n_Lw.Fill(nLowPtElectron[j])
     
       
    plot(ID_Lw, sample_name, plo, "ID")
    plot(pt_Lw, sample_name, plo, "ptt")
    plot(eta_Lw, sample_name, plo, "eta")
    plot(dxy_Lw, sample_name, plo, "dxy")
    plot(dxyErr_Lw, sample_name, plo, "dxyErr")
    plot(dz_Lw, sample_name, plo, "dz")
    plot(dzErr_Lw, sample_name, plo, "dzErr")
    plot(miniPFRelIso_all_Lw, sample_name, plo, "miniPFRelIso")
    plot(convVeto_Lw, sample_name, plo, "convVeto")
    plot(n_Lw, sample_name, plo, "n_Lw")
     
