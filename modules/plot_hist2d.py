"""
    Nice plots for hyper-parameter tunning
    Requires python 2.7 and ROOT 6.10/08
"""

from __future__ import division

from ROOT import gROOT, TCanvas, TH2F

gROOT.SetBatch(True)

timing = [21.526516, 38.697022, 21.801782, 18.44195, 39.922742, 32.731565, 42.106807,
          50.200812, 23.214379, 10.198113, 9.88649, 9.957186, 23.863473, 28.228622,
          28.804091, 16.237075, 4.056886, 8.267317, 4.250014, 4.070573, 5.335695,
          9.338416, 4.359317, 4.29553, 2.295932, 2.353202, 2.299685, 2.371533,
          2.456108, 2.527569, 3.646254, 3.140338, 0.967866, 0.894383, 0.962015,
          0.899259, 1.096401, 0.988191, 1.046669, 1.037391, 0.714606, 0.768995,
          0.708612, 0.769892, 0.79048, 0.851255, 0.916281, 0.786869, 0.617785,
          0.549758, 0.608248, 0.547591, 0.683419, 0.617111, 0.617212, 0.683746]

train_accuracy = [0.50338739, 0.70441216, 0.71192712, 0.71796185, 0.72075152, 0.72507828, 0.71562767,
                  0.72729862, 0.50338739, 0.70686024, 0.71004838, 0.71841729, 0.7229718, 0.72240251,
                  0.7202391, 0.72815257, 0.68869913, 0.70737261, 0.71101624, 0.71932822, 0.72086537,
                  0.72445202, 0.7230857, 0.72536296, 0.68932539, 0.70691717, 0.71278107, 0.71870196,
                  0.72576147, 0.7240535, 0.72553372, 0.72667235, 0.68488473, 0.70577854, 0.70868206,
                  0.71579844, 0.72359806, 0.72422433, 0.72467977, 0.72376883, 0.68209505, 0.70270425,
                  0.7077142, 0.71414745, 0.71813267, 0.7254768, 0.72177625, 0.7191574, 0.65231997,
                  0.67065185, 0.67930543, 0.69587249, 0.69735271, 0.68926841, 0.69735271, 0.70515227]

test_accuracy = [0.50962943, 0.70049143, 0.70753086, 0.71377343, 0.71642983, 0.71948469, 0.71058571,
                 0.72121131, 0.50962943, 0.70328063, 0.70846063, 0.71603137, 0.71868771, 0.71629697,
                 0.71709388, 0.72134411, 0.6854828, 0.7042104, 0.70739806, 0.7151016, 0.71297652,
                 0.71735954, 0.71895337, 0.71842211, 0.6854828, 0.70301503, 0.7095232, 0.71603137,
                 0.717758, 0.72068006, 0.7178908, 0.72001594, 0.68309206, 0.70062423, 0.70580423,
                 0.71337497, 0.71603137, 0.71550006, 0.71842211, 0.71895337, 0.67884183, 0.6987648,
                 0.70460886, 0.71443748, 0.71018726, 0.71656263, 0.71828926, 0.7176252, 0.64749634,
                 0.6667552, 0.67884183, 0.69185817, 0.69424891, 0.68627971, 0.69770223, 0.70009297]

xl = [[1], [2], [5], [10], [5, 5], [10, 5], [5, 10], [10, 10]]

yl = [1, 2, 5, 10, 50, 100, 1000]

nx = len(xl)
ny = len(yl)

c1 = TCanvas('c1', 'c1', 1400, 800)

h0 = TH2F('h0', 'Accuracy Score (training)', nx, 0, nx, ny, 0, ny)

h0.SetStats(0)
h0.SetMarkerSize(1.8)
h0.SetMarkerColor(2)
h0.GetXaxis().SetTitle('number of hidden units per layer')
h0.GetYaxis().SetTitle('batch size')
h0.GetXaxis().CenterTitle()
h0.GetYaxis().CenterTitle()

h1 = h0.Clone('h1')
h1.SetTitle('Accuracy Score (test)')

h2 = h0.Clone('h2')
h2.SetTitle('Training Time (seconds)')

for j in xrange(ny):
    for i in xrange(nx):
        w = train_accuracy[j*nx+i]
        z = test_accuracy[j*nx+i]
        t = timing[j*nx+i]
        h0.Fill(str(xl[i]), str(yl[j]), round(w, 3))
        h1.Fill(str(xl[i]), str(yl[j]), round(z, 3))
        h2.Fill(str(xl[i]), str(yl[j]), round(t, 1))

h0.Draw('colz')
h0.Draw('text same')
c1.SaveAs('trainaccuracy.png')

h1.Draw('colz')
h1.Draw('text same')
c1.SaveAs('testaccuracy.png')

h2.Draw('colz')
h2.Draw('text same')
c1.SaveAs('traintime.png')