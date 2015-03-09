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
    tweets.append( [row[3], row[4]] );#向这个tweets这个list里面附加两个元素
	#，推文和结果


# treat neutral and irrelevant the same
for t in tweets:
    if t[1] == 'irrelevant':#t[1]即推文的label，是“positive”呢还是“negtive”
        t[1] = 'neutral'#这里做的是把irrelevant和neutral一视同仁成“neutral”


# split in to training and test sets
random.shuffle( tweets );

fvecs = [(tweet_features.make_tweet_dict(t),s) for (t,s) in tweets]
#将每一条tweet的第一个元素做tweet_features.make_tweet_dict处理后，和第二
#个元素一起加入fvecs列表
v_train = fvecs[:2500]#使用前2500条作为训练集
v_test  = fvecs[2500:]#使用剩余的作为测试集


# train classifier
classifier = nltk.NaiveBayesClassifier.train(v_train);#用我们开始定义的训练集来训练分类器
#classifier = nltk.classify.maxent.train_maxent_classifier_with_gis(v_train);


# classify and dump results for interpretation
print '\nAccuracy %f\n' % nltk.classify.accuracy(classifier, v_test)#查看分类器准确度
#print classifier.show_most_informative_features(200)


# build confusion matrix over test set
test_truth   = [s for (t,s) in v_test]#查看测试集里面的每个tweet真正的结果，是postive呢？还是neg？
test_predict = [classifier.classify(t) for (t,s) in v_test]#找到测试集里的供测试的推文，用训练好的分类器
#来预估结果

print 'Confusion Matrix'
print nltk.ConfusionMatrix( test_truth, test_predict )#将上面算出的两个列表传给nltk的这个函数
#计算混淆矩阵
