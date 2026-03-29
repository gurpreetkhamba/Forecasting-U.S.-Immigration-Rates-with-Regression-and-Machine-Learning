# Forecasting U.S. Immigration Rates with Regression and Machine Learning
## TLDR: 
In this project I forecast annual U.S immigration counts using historical immigration data and economic indicators. The best model was a lagged regression model which beat the best baseline (a LOCF baseline) by 3.3% 

## Description: 
Immigration flows are influenced by economic, social, and geopolitical factors, and past trends are highly informative of future movements. In this project, I used historical U.S. immigration data spanning 2003–2023, along with GDP and unemployment rate indicators, to forecast immigration levels for each country. I created three models to compare against two baselines. Workflow included data preparation, modeling approaches and an evaluation. The best performing model (lagged regression model) used historical data and an economic indicator to achieve an RMSE of 0.2835, on a target variable ranging from 0 to 1. The machine learning model was able to achieve an RMSE of 0.4212. 

## Libraries & Tools:
R: tidyverse, ggplot2, stats (Linear Modeling, randomForest, ANOVA)

Python: Playwright
