"""
@package tweet_features
Convert tweet to feature vector.

These routines help convert arbitrary tweets in to feature vectors.

"""
import numpy


# search patterns for features
testFeatures = \
    [('hasAddict',     (' addict',)), \
     ('hasAwesome',    ('awesome',)), \
     ('hasBroken',     ('broke',)), \
     ('hasBad',        (' bad',)), \
     ('hasBug',        (' bug',)), \
     ('hasCant',       ('cant','can\'t')), \
     ('hasCrash',      ('crash',)), \
     ('hasCool',       ('cool',)), \
     ('hasDifficult',  ('difficult',)), \
     ('hasDisaster',   ('disaster',)), \
     ('hasDown',       (' down',)), \
     ('hasDont',       ('dont','don\'t','do not','does not','doesn\'t')), \
     ('hasEasy',       (' easy',)), \
     ('hasExclaim',    ('!',)), \
     ('hasExcite',     (' excite',)), \
     ('hasExpense',    ('expense','expensive')), \
     ('hasFail',       (' fail',)), \
     ('hasFast',       (' fast',)), \
     ('hasFix',        (' fix',)), \
     ('hasFree',       (' free',)), \
     ('hasFrowny',     (':(', '):')), \
     ('hasFuck',       ('fuck',)), \
     ('hasGood',       ('good','great')), \
     ('hasHappy',      (' happy',' happi')), \
     ('hasHate',       ('hate',)), \
     ('hasHeart',      ('heart', '<3')), \
     ('hasIssue',      (' issue',)), \
     ('hasIncredible', ('incredible',)), \
     ('hasInterest',   ('interest',)), \
     ('hasLike',       (' like',)), \
     ('hasLol',        (' lol',)), \
     ('hasLove',       ('love','loving')), \
     ('hasLose',       (' lose',)), \
     ('hasNeat',       ('neat',)), \
     ('hasNever',      (' never',)), \
     ('hasNice',       (' nice',)), \
     ('hasPoor',       ('poor',)), \
     ('hasPerfect',    ('perfect',)), \
     ('hasPlease',     ('please',)), \
     ('hasSerious',    ('serious',)), \
     ('hasShit',       ('shit',)), \
     ('hasSlow',       (' slow',)), \
     ('hasSmiley',     (':)', ':D', '(:')), \
     ('hasSuck',       ('suck',)), \
     ('hasTerrible',   ('terrible',)), \
     ('hasThanks',     ('thank',)), \
     ('hasTrouble',    ('trouble',)), \
     ('hasUnhappy',    ('unhapp',)), \
     ('hasWin',        (' win ','winner','winning')), \
     ('hasWinky',      (';)',)), \
     ('hasWow',        ('wow','omg')) ]


def make_tweet_dict( txt ):#创建一个字典，字典的用法具体可看http://sebug.net/paper/python/ch09s04.html
    """ 
    Extract tweet feature vector as dictionary. 
    """
    txtLow = ' ' + txt.lower() + ' '

    # result storage
    fvec = {}

    # search for each feature
    for test in testFeatures:

        key = test[0]#testFeatures的第一列元素，hasAddict，hasaweson...

        fvec[key] = False;#先把fvec[key]初始化为false
        for tstr in test[1]:
            fvec[key] = fvec[key] or (txtLow.find(tstr) != -1)#如果我的推文含有testFeatures里的
			#关键字，如“awesome”“hate”，那么对应序号上会变为true，表示字典上相应序号上命中

    return fvec
#返回的结果类似于{'hasUnhappy': False, 'hasExclaim': False, 'hasSmiley': False, 'hasHappy': False, 'hasLose': False, 
#'hasExpense': False, 'hasFail': False, 'hasWin': False, 'hasShit': False, 'hasIssue': False, 'hasCant': False, 
#'hasPlease': False, 'hasInterest': False, 'hasNeat': False, 'hasSuck': False, 'hasWinky': False, 'hasFrowny': False,
# 'hasWow': False, 'hasTerrible': False, 'hasFuck': False, 'hasLove': False, 'hasDont': False, 'hasBad': False, 
#'hasBug': False, 'hasDifficult': False, 'hasCool': False, 'hasFree': False, 'hasHate': True, 'hasDown': False, 
#'hasLike': False, 'hasAddict': False, 'hasHeart': False, 'hasNever': False, 'hasBroken': False, 'hasFix': False,
# 'hasSlow': False, 'hasPoor': False, 'hasDisaster': False, 'hasAwesome': True, 'hasLol': False, 'hasFast': False, 
#'hasIncredible': False, 'hasExcite': False, 'hasSerious': False, 'hasThanks': False, 'hasTrouble': False, 'hasCrash': False,
# 'hasNice': False, 'hasPerfect': False, 'hasGood': False, 'hasEasy': False}

