import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import sqrt
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import warnings
warnings.filterwarnings('ignore')
#importing data
data=pd.read_csv('amsterdam_listings.csv')
#choosing columns
y = data.price
x = data.drop(['price','name','host_name','last_review','host_id','id'],axis=1)


#dividing data to train and validation
x_train_full, x_valid_full, y_train, y_valid = train_test_split(x, y, random_state=1)

# Select categorical columns
categorical_cols = [cname for cname in x_train_full.columns if 
                    x_train_full[cname].dtype == "object"]

# Select numerical columns
numerical_cols = [cname for cname in x_train_full.columns if 
                  x_train_full[cname].dtype in ['int64', 'float64']]

#retaining these columns
my_cols = categorical_cols + numerical_cols
x_train = x_train_full[my_cols].copy()
x_valid = x_valid_full[my_cols].copy()

# Preprocessing for numerical data
numerical_transformer = SimpleImputer(strategy='mean')
# Preprocessing for categorical data
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])
# Bundle preprocessing for categorical data
preprocessor = ColumnTransformer(transformers =[
    ('num',numerical_transformer,numerical_cols),
    ('cat', categorical_transformer, categorical_cols)])

# create forest model
model = RandomForestRegressor(random_state=1)

# Bundle preprocessing and modeling code in a pipeline
my_pipeline = Pipeline(steps=[('preprocessor',preprocessor),('model',model)])

#train model and give predictions
my_pipeline.fit(x_train, y_train)
predictions = my_pipeline.predict(x_valid)
print(mean_absolute_error(y_valid, predictions),"is the predicted value")


