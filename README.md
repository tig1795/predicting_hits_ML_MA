# Comparative Analysis of Data Sets and Feature Importance in Predicting Hit Songs

This thesis delves into applying machine learning (ML) for predicting song hit potential
within the music industry, analyzing the performance disparities among distinct features
while addressing dataset structuring requisites. It introduces an innovative framework
involving regression-based methodologies for classifying songs into hits and non-hits. Additionally,
two heterogeneous datasets are presented, encompassing audio characteristics,
lyrical content, sentiment analysis outcomes, and emotion categorization. The investigation
highlights the key role of dataset scale and criteria for hit classification. The results
showed that the features popularity and danceability were the most useful in predicting,
emphasizing their importance in classifying hits. Finally, the study highlights the benefits
and ethical complexities of using ML in the music industry.

This repository contains the code used in this master thesis and is structured as follows:

- In the images folder, you will find all the plots used in the Master's thesis.
- In the folder code, you can find the code used in this master thesis. In addition to data creation and exploration, the audio feature generation code can also be found there. In the context of generating the audio features, code from (Heggli, Ole A., Jan Stupacher, and Peter Vuust. 2021. “Diurnal Fluctuations in Musical Preference.” PsyArXiv. March 16. doi:10.31234/osf.io/6e4yw.) was used, among others. In addition, the code for the sentimental analysis, the generation of the emotion labels and the code for the XGBoost algorithm can also be found in this folder.
- The folder data contained all data sets and intermediate states of data sets used.
