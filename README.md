# LD_Trust_social_netw
Exam of Learning Dynamics 2020: Measuring  behavioral trust in social networks (Adali et al.)
https://ieeexplore.ieee.org/document/5484757

Folder organisation : 
  - Infos : 
    contains the article, the extended version, the abbreviations used both in the articles and the code and installation informations
  - Dataset :
    contains the code used to process the data given as input (TODO). For now it only contains a class for building random inputs.
  - Trust_analysis :
    contains the code for building the trust networks based on one of the input in dataset
  - Results : 
    contains the results of Conversational trust and Propagational trust on the Twitter and the Enron dataset, contains random and scale-free networks
    
Files:
  - Dataset:
      - get_tweets.py : python file to retreive tweets from Belgium (50km around Brussels)
      - tweeter_data.csv : Twitter dataset
      - tweeter_data_narrow.csv : another Twitter dataset with a more restricted place (not used in the article)
      - Enron.csv : Enron e-mail dataset
      - data_to_input.py : python class to transform the .csv file to a set of 3-tuples (sender, receiver, time) 
   - Trust analysis:
      - Conversational_Trust.py : python class for making the conversational trust graph
      - Propagation_Trust.py: python class for making the propagational trust graph
      - data_to_input.py: python class for converting the Twitter/Enron dataset to a set of tuples (sender, receiver, time) needed for the algorithms
      - primary_analysis.txt : Count of the number of interactions between people in the Twitter dataset -> first approach to the trust graph
   - Results:
      - Analysis_results.py : python class for analysing the results of the algorithms
      - Synthetic_netw.py : python class for making random/scale-free networks in order to input them to the algorithms
      - conversational_trust_enron/twitter : pickle file of the results of conversational trust
      - propagational_trust_enron/twitter : pickle file of the results of propagational trust
      - enron/twitter_50_randoms/scale_free : pickle file of 50 graphs with the same number of nodes and or edges as our datasets
            twitter_50_randoms is a file too big to put on the github, you can send an email to c.hendrickx.bbb@gmail.com and I will kindly provide it to you ;)
      
    



