"""
@package sentiment
Twitter sentiment analysis.

This code performs sentiment analysis on Tweets.

A custom feature extractor looks for key words and emoticons.  These are fed in
to a naive Bayes classifier to assign a label of 'positive', 'negative', or
'neutral'.  Optionally, a principle components transform (PCT) is used to lessen
the influence of covariant features.

"""
import csv, random
import nltk
import tweet_features, tweet_pca


# read all tweets and labels
fp = open( 'sentiment.csv', 'rb' )
reader = csv.reader( fp, delimiter=',', quotechar='"', escapechar='\\' )
tweets = []
for row in reader:
    tweets.append( [row[3], row[4]] );#�����tweets���list���渽������Ԫ��
	#�����ĺͽ��


# treat neutral and irrelevant the same
for t in tweets:
    if t[1] == 'irrelevant':#t[1]�����ĵ�label���ǡ�positive���ػ��ǡ�negtive��
        t[1] = 'neutral'#���������ǰ�irrelevant��neutralһ��ͬ�ʳɡ�neutral��


# split in to training and test sets
random.shuffle( tweets );

fvecs = [(tweet_features.make_tweet_dict(t),s) for (t,s) in tweets]
#��ÿһ��tweet�ĵ�һ��Ԫ����tweet_features.make_tweet_dict����󣬺͵ڶ�
#��Ԫ��һ�����fvecs�б�
v_train = fvecs[:2500]#ʹ��ǰ2500����Ϊѵ����
v_test  = fvecs[2500:]#ʹ��ʣ�����Ϊ���Լ�


# train classifier
classifier = nltk.NaiveBayesClassifier.train(v_train);#�����ǿ�ʼ�����ѵ������ѵ��������
#classifier = nltk.classify.maxent.train_maxent_classifier_with_gis(v_train);


# classify and dump results for interpretation
print '\nAccuracy %f\n' % nltk.classify.accuracy(classifier, v_test)#�鿴������׼ȷ��
#print classifier.show_most_informative_features(200)


# build confusion matrix over test set
test_truth   = [s for (t,s) in v_test]#�鿴���Լ������ÿ��tweet�����Ľ������postive�أ�����neg��
test_predict = [classifier.classify(t) for (t,s) in v_test]#�ҵ����Լ���Ĺ����Ե����ģ���ѵ���õķ�����
#��Ԥ�����

print 'Confusion Matrix'
print nltk.ConfusionMatrix( test_truth, test_predict )#����������������б���nltk���������
#�����������
