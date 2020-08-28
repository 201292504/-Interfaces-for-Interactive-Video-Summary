# -Interfaces-for-Interactive-Video-Summary

### Installation

1. Download the trained weights of the models.
------------------------------------------------------------------------------------------
if not os.path.exists('data/vgg19.pkl'):
    !wget -P ./data/ https://data.vision.ee.ethz.ch/arunv/qv_summary_codes/vgg19.tar.gz -nc
    !tar -xzvf ./data/vgg19.tar.gz -C ./data/ --skip-old-files
    !rm ./data/vgg19.tar.gz
!wget -P ./data/ https://data.vision.ee.ethz.ch/arunv/qv_summary_codes/CNNmodel.npz -nc
!wget -P ./data/ https://data.vision.ee.ethz.ch/arunv/qv_summary_codes/LSTMmodel.npz -nc
'''
Warning: The model below is of 10G. This is complete version. May take some time to download and unzip. 
For a smaller model, comment this and use the commented model further below.
'''
# !wget -P ./data/ https://data.vision.ee.ethz.ch/arunv/qv_summary_codes/word2vecmodel.tar.gz -nc
# !mkdir ./data/word2vec
!wget -P ./data/word2vec/ https://data.vision.ee.ethz.ch/arunv/qv_summary_codes/GoogleNews-vectors-negative300.bin -nc
------------------------------------------------------------------------------------------
2. Install the requirements with `pip install -r requirements.txt`
3. Run `python setup.py install --user` to install the package __qvsumm__.
4. Download Django3 in the website.


### Getting Started

1. Run 'python2 testmodel.py' in /videoSummary/.
2. Run 'python3 manage.py runserver' in /videoSummary/video-query-website/
