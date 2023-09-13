$mallet_dir = "put the path to the MALLET directory here"
$data_loc = "put the path to the 'tweets.mallet' file here"

cd $mallet_dir

.\bin\mallet train-classifier --input $data_loc --trainer DecisionTree --trainer NaiveBayes --trainer MaxEnt --training-portion .7 --cross-validation 4