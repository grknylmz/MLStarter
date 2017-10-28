import pandas as pd
#from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import tensorflow as tf


url = "../resources/export.csv"
names = ['CLIENT', 'GUID', 'OBJECT_ID', 'PROCESS_TYPE', 'POSTING_DATE', 'DESCRIPTION', 'DESCR_LANGUAGE',
        'LOGICAL_SYSTEM', 'CRM_RELEASE', 'SCENARIO','TEMPLATE_TYPE', 'CREATED_AT', 'CREATED_BY', 'CHANGED_AT',
         'CHANGED_BY', 'HEAD_CHANGED_AT', 'ORDERADM_H_DUMMY', 'ZZAFLD000000', 'ZZAFLD000003',
         'ZZPARENT_LOC_ID', 'ZZUNIQUE', 'ZZAFLD000005', 'ZZAFLD00000E', 'ZZAFLD00001H', 'ZZREZERV_AMACI',
         'ZZNET_DEGER', 'INPUT_CHANNEL', 'BTX_CLASS', 'AUTH_SCOPE', 'COMP_TX_HEADER', 'OBJECT_TYPE',
         'ARCHIVING_FLAG', 'DESCRIPTION_UC', 'OBJECT_ID_OK', 'VERIFY_DATE', 'CRM_CHANGED_AT', 'POSTPROCESS_AT']
data = pd.read_csv(url, sep=",", names=names)
label_names = data['target_names']
labels = data['target']
feature_names = data['feature_names']
features = data['data']

train, test, train_labels, test_labels = train_test_split(features,
                                                          labels,
                                                          test_size=0.33,
                                                          random_state=42)

