The dataset source is from kaggle
https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance/data

1. Here i use pipelines to make the code more stuructural
2. to find good K i use grid, first i try 1 - 200, then the graph slowly stable at 60+, then i make again 60 - 90 and i decide to take 69 based on the graph
3. In this project i use train, valid and test, so i can trial and error to get best K
4. after done modelling i use joblib to convert into .pkl so i can use it on .py
