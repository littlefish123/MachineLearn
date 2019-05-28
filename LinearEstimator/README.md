Purpose
=======
Build a Binary Classification by using Tensorflow Estimator to predict whether
a person earns more than 50000 per year (LABEL) based on the census data which contains
person's age, education, marital status and occupation (FEATURE).

Model
=====
Logistic Regression Model


Approch 1
=========
For small dataset, simply slice the dataset by using pandas.DataFrame function.

Approach 2
==========
For larger datasets should stream data from disk and input_fn() using
tf.decode_csv and tf.data.TextLineDataset.

When building a tf.estimator model, the input data is specified by using an input function (or input_fn).
This builder function returns a tf.data.Dataset of batches of (features-dict, label) pairs. 
The input builder function returns the following pair:

features: A dict from feature names to Tensors or SparseTensors containing batches of features.
labels: A Tensor containing batches of labels.


Example 1
=========
Using AGE (numeric) as feature input layer
Train & Evaluate Model
Accuracy : 78%

Example 2
=========
Using multiple numeric fields - EDUCATION,CAPTIAL GAIN,CAPTIAL LOSS,Hours per week as input layer
Train & Evaluate Model
Accuracy : 78%

Example 3
=========
Use AGE & RELATIONSHIP(Categorical column) to be input layer
Train & Evaluate Model
Accuracy : 74%

Example 4
=========
if we don't know the set of possible values in advance, use the categorical_column_with_hash_bucket instead.
Use OCCUPATION (Categorial Column with Hash Bucket)
Train & Evaluate Model
Accuracy : 83%

More direct relationship by using occupation with salary income than using
AGE + RElATIONSHIP

Example 5
=========
Derived Feature Columns
 Learn the fine-grained correlation between income and each age group separately, we can leverage bucketization. Bucketization is a process of dividing the entire range of a continuous feature into a set of consecutive buckets, and then converting the original numerical feature into a bucket ID (as a categorical feature) depending on which bucket that value falls into.
 
Define a bucketized_column over age as:
age_buckets = tf.feature_column.bucketized_column(
    age, boundaries=[18, 25, 30, 35, 40, 45, 50, 55, 60, 65])
	
Example 6
=========
Learn complex relationships with crossed column
The correlation between education and the label (earning > 50,000 dollars) may be different for different occupations

education_x_occupation = tf.feature_column.crossed_column(
    ['education', 'occupation'], hash_bucket_size=1000)
	
base_columns = [
    education, marital_status, relationship, workclass, occupation,
    age_buckets,
]

crossed_columns = [
    tf.feature_column.crossed_column(
        ['education', 'occupation'], hash_bucket_size=1000),
    tf.feature_column.crossed_column(
        [age_buckets, 'education', 'occupation'], hash_bucket_size=1000),
]

Train & Evaluate Model

Accuracy : 83%


Add L1 Regularization to improve Overfitting issue

Accuracy : 84%


Add L2 Regularization to improve Overfitting issue

Accuracy : 84%


Plot Weight Distribution Graph to compare Base Model, L1 Regularization and L2 Regularization Weight Distribution


